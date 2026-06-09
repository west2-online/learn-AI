from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Generic, TypeVar

from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field as PydanticField
from sqlmodel import Field, Session, SQLModel, create_engine, select

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'todo.sqlite3'}"
engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})


class TodoState(str, Enum):
    TODO = "todo"
    DONE = "done"


class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True, min_length=1, max_length=120)
    description: str = Field(default="", max_length=1000)
    tag: str = Field(default="学习", index=True, max_length=30)
    state: TodoState = Field(default=TodoState.TODO, index=True)
    is_deleted: bool = Field(default=False, index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), index=True)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class TodoCreate(BaseModel):
    title: str = PydanticField(min_length=1, max_length=120)
    description: str = PydanticField(default="", max_length=1000)
    tag: str = PydanticField(default="学习", min_length=1, max_length=30)


class TodoUpdateTag(BaseModel):
    tag: str = PydanticField(min_length=1, max_length=30)


class TodoRead(BaseModel):
    id: int
    title: str
    description: str
    tag: str
    state: TodoState
    created_at: datetime
    updated_at: datetime


T = TypeVar("T")


class Page(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int
    page_size: int


class ApiResponse(BaseModel, Generic[T]):
    code: int = 0
    message: str = "success"
    data: T | None = None


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def get_active_todo(todo_id: int, session: Session) -> Todo:
    todo = session.get(Todo, todo_id)
    if todo is None or todo.is_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo


def to_read(todo: Todo) -> TodoRead:
    return TodoRead(
        id=todo.id or 0,
        title=todo.title,
        description=todo.description,
        tag=todo.tag,
        state=todo.state,
        created_at=todo.created_at,
        updated_at=todo.updated_at,
    )


def paged_todos(statement, page: int, page_size: int, session: Session) -> Page[TodoRead]:
    all_items = list(session.exec(statement).all())
    start = (page - 1) * page_size
    end = start + page_size
    return Page(
        items=[to_read(todo) for todo in all_items[start:end]],
        total=len(all_items),
        page=page,
        page_size=page_size,
    )


app = FastAPI(
    title="Memo Codex 5.5 TODO API",
    description="FastAPI + SQLite TODO LIST，支持增删改查、分页、标签和逻辑删除。",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(BASE_DIR / "frontend" / "index.html")


app.mount("/static", StaticFiles(directory=BASE_DIR / "frontend"), name="static")


@app.get("/api/health", response_model=ApiResponse[dict[str, str]], tags=["system"])
def health() -> ApiResponse[dict[str, str]]:
    return ApiResponse(data={"status": "ok"})


@app.post("/api/todos", response_model=ApiResponse[TodoRead], status_code=status.HTTP_201_CREATED, tags=["todos"])
def create_todo(payload: TodoCreate, session: Session = Depends(get_session)) -> ApiResponse[TodoRead]:
    todo = Todo(title=payload.title.strip(), description=payload.description.strip(), tag=payload.tag.strip())
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return ApiResponse(message="created", data=to_read(todo))


@app.get("/api/todos", response_model=ApiResponse[Page[TodoRead]], tags=["todos"])
def list_todos(
    state: TodoState | None = Query(default=None, description="todo=待办，done=已完成，不传则全部"),
    keyword: str | None = Query(default=None, description="按标题或描述关键字查询"),
    tag: str | None = Query(default=None, description="按标签筛选"),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
    session: Session = Depends(get_session),
) -> ApiResponse[Page[TodoRead]]:
    statement = select(Todo).where(Todo.is_deleted == False)  # noqa: E712
    if state is not None:
        statement = statement.where(Todo.state == state)
    if keyword:
        text = f"%{keyword.strip()}%"
        statement = statement.where((Todo.title.like(text)) | (Todo.description.like(text)))
    if tag:
        statement = statement.where(Todo.tag == tag.strip())
    statement = statement.order_by(Todo.created_at.desc(), Todo.id.desc())
    return ApiResponse(data=paged_todos(statement, page, page_size, session))


@app.get("/api/todos/{todo_id}", response_model=ApiResponse[TodoRead], tags=["todos"])
def get_todo(todo_id: int, session: Session = Depends(get_session)) -> ApiResponse[TodoRead]:
    return ApiResponse(data=to_read(get_active_todo(todo_id, session)))


@app.patch("/api/todos/{todo_id}/complete", response_model=ApiResponse[TodoRead], tags=["todos"])
def complete_todo(todo_id: int, session: Session = Depends(get_session)) -> ApiResponse[TodoRead]:
    todo = get_active_todo(todo_id, session)
    todo.state = TodoState.DONE
    todo.updated_at = now_utc()
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return ApiResponse(message="marked as done", data=to_read(todo))


@app.patch("/api/todos/complete", response_model=ApiResponse[dict[str, int]], tags=["todos"])
def complete_all_todos(session: Session = Depends(get_session)) -> ApiResponse[dict[str, int]]:
    todos = list(session.exec(select(Todo).where(Todo.is_deleted == False, Todo.state == TodoState.TODO)).all())  # noqa: E712
    for todo in todos:
        todo.state = TodoState.DONE
        todo.updated_at = now_utc()
        session.add(todo)
    session.commit()
    return ApiResponse(message="all todo items marked as done", data={"affected": len(todos)})


@app.patch("/api/todos/{todo_id}/reopen", response_model=ApiResponse[TodoRead], tags=["todos"])
def reopen_todo(todo_id: int, session: Session = Depends(get_session)) -> ApiResponse[TodoRead]:
    todo = get_active_todo(todo_id, session)
    todo.state = TodoState.TODO
    todo.updated_at = now_utc()
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return ApiResponse(message="marked as todo", data=to_read(todo))


@app.patch("/api/todos/reopen", response_model=ApiResponse[dict[str, int]], tags=["todos"])
def reopen_all_done_todos(session: Session = Depends(get_session)) -> ApiResponse[dict[str, int]]:
    todos = list(session.exec(select(Todo).where(Todo.is_deleted == False, Todo.state == TodoState.DONE)).all())  # noqa: E712
    for todo in todos:
        todo.state = TodoState.TODO
        todo.updated_at = now_utc()
        session.add(todo)
    session.commit()
    return ApiResponse(message="all done items marked as todo", data={"affected": len(todos)})


@app.patch("/api/todos/{todo_id}/tag", response_model=ApiResponse[TodoRead], tags=["todos"])
def update_todo_tag(todo_id: int, payload: TodoUpdateTag, session: Session = Depends(get_session)) -> ApiResponse[TodoRead]:
    todo = get_active_todo(todo_id, session)
    todo.tag = payload.tag.strip()
    todo.updated_at = now_utc()
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return ApiResponse(message="tag updated", data=to_read(todo))


@app.delete("/api/todos/{todo_id}", response_model=ApiResponse[TodoRead], tags=["todos"])
def delete_todo(todo_id: int, session: Session = Depends(get_session)) -> ApiResponse[TodoRead]:
    todo = get_active_todo(todo_id, session)
    todo.is_deleted = True
    todo.updated_at = now_utc()
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return ApiResponse(message="deleted logically", data=to_read(todo))


@app.delete("/api/todos", response_model=ApiResponse[dict[str, int]], tags=["todos"])
def delete_todos(
    state: TodoState | None = Query(default=None, description="todo=删除所有待办，done=删除所有已完成，不传则删除所有"),
    session: Session = Depends(get_session),
) -> ApiResponse[dict[str, int]]:
    statement = select(Todo).where(Todo.is_deleted == False)  # noqa: E712
    if state is not None:
        statement = statement.where(Todo.state == state)
    todos = list(session.exec(statement).all())
    for todo in todos:
        todo.is_deleted = True
        todo.updated_at = now_utc()
        session.add(todo)
    session.commit()
    return ApiResponse(message="deleted logically", data={"affected": len(todos)})
