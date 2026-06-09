# Memo Codex 5.5 - TODO LIST

这是作业 3 的 Vibe Coding 成品：一个使用 FastAPI + SQLite + Vue3 实现的 TODO LIST。项目所有文件都在当前 `Memo-Codex5.5` 文件夹内，运行时只会在本文件夹生成本地虚拟环境和 `todo.sqlite3` 数据库，不污染全局环境。

## 功能清单

- 新增待办事项
- 将一条 / 所有待办事项设置为已完成
- 将一条 / 所有已完成事项设置为待办
- 为待办事项打上 / 修改标签，例如：学习、生活、紧急
- 查看所有事项、所有待办、所有已完成事项，支持分页
- 输入关键字查询事项，支持分页
- 通过 id 查询事项
- 根据标签筛选事项，支持分页
- 删除一条 / 所有已完成 / 所有待办 / 所有事项
- 删除使用逻辑删除：只修改 `is_deleted` 标记，不真正从数据表删除数据
- 已逻辑删除的数据不会被查询、修改、批量操作影响
- Vue3 前端页面可直接操作所有核心功能
- FastAPI 自动接口文档：`/docs`

## 项目结构

```text
Memo-Codex5.5/
├─ backend/
│  └─ main.py              # FastAPI 后端与 SQLite 数据模型
├─ frontend/
│  └─ index.html           # Vue3 单页前端
├─ tests/
│  └─ api_test.py          # requests API 自动测试脚本
├─ .gitignore              # 避免上传数据库、虚拟环境、node_modules 等垃圾文件
├─ requirements.txt        # Python 依赖
└─ README.md               # 部署与接口说明
```

## Windows 部署步骤

请在 PowerShell 中进入本项目目录：

```powershell
cd "tasks(2026)\foundation\Memo-Codex5.5"
```

创建只属于当前文件夹的 Python 虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

如果 PowerShell 阻止激活脚本，可临时执行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

安装依赖：

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

启动后端服务：

```powershell
uvicorn backend.main:app --reload
```

打开浏览器访问：

- 前端页面：<http://127.0.0.1:8000/>
- Swagger 接口文档：<http://127.0.0.1:8000/docs>
- ReDoc 接口文档：<http://127.0.0.1:8000/redoc>

## API 测试脚本

保持后端服务正在运行，另开一个 PowerShell 窗口进入项目目录并激活虚拟环境：

```powershell
cd "tasks(2026)\foundation\Memo-Codex5.5"
.\.venv\Scripts\Activate.ps1
python tests\api_test.py
```

看到以下输出即代表测试通过：

```text
All API tests passed.
```

也可以指定服务地址：

```powershell
python tests\api_test.py http://127.0.0.1:8000
```

## 接口约定

统一返回 JSON：

```json
{
  "code": 0,
  "message": "success",
  "data": {}
}
```

分页返回格式：

```json
{
  "items": [],
  "total": 0,
  "page": 1,
  "page_size": 10
}
```

## API 列表

### 系统

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/api/health` | 健康检查 |

### 增

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| POST | `/api/todos` | 添加一条新的待办事项 |

请求体示例：

```json
{
  "title": "完成 AI 作业",
  "description": "实现 FastAPI + Vue3 TODO LIST",
  "tag": "学习"
}
```

### 改

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| PATCH | `/api/todos/{todo_id}/complete` | 将一条事项设置为已完成 |
| PATCH | `/api/todos/complete` | 将所有待办事项设置为已完成 |
| PATCH | `/api/todos/{todo_id}/reopen` | 将一条已完成事项设置为待办 |
| PATCH | `/api/todos/reopen` | 将所有已完成事项设置为待办 |
| PATCH | `/api/todos/{todo_id}/tag` | 为一条事项打上 / 修改标签 |

修改标签请求体示例：

```json
{
  "tag": "紧急"
}
```

### 查

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/api/todos?page=1&page_size=10` | 查看所有事项，分页 |
| GET | `/api/todos?state=todo&page=1&page_size=10` | 查看所有待办事项，分页 |
| GET | `/api/todos?state=done&page=1&page_size=10` | 查看所有已完成事项，分页 |
| GET | `/api/todos?keyword=作业&page=1&page_size=10` | 输入关键字查询事项，分页 |
| GET | `/api/todos/{todo_id}` | 通过 id 查询事项 |
| GET | `/api/todos?tag=学习&page=1&page_size=10` | 根据标签筛选事项，分页 |

查询参数可组合，例如：

```text
/api/todos?state=todo&keyword=AI&tag=学习&page=1&page_size=5
```

### 删

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| DELETE | `/api/todos/{todo_id}` | 逻辑删除一条事项 |
| DELETE | `/api/todos?state=done` | 逻辑删除所有已完成事项 |
| DELETE | `/api/todos?state=todo` | 逻辑删除所有待办事项 |
| DELETE | `/api/todos` | 逻辑删除所有事项 |

## 数据表说明

SQLite 数据库文件为 `todo.sqlite3`，自动在项目根目录生成。主要字段：

| 字段 | 说明 |
| --- | --- |
| `id` | 主键 id |
| `title` | 标题 |
| `description` | 描述 |
| `tag` | 标签 |
| `state` | 状态：`todo` 或 `done` |
| `is_deleted` | 逻辑删除标记 |
| `created_at` | 创建时间 |
| `updated_at` | 更新时间 |

后端所有查询、修改、批量操作都会先过滤 `is_deleted = false`，因此已逻辑删除的数据不会被返回或再次影响。

## Git 上传规范

本项目的 `.gitignore` 已忽略以下不应上传的内容：

- `.venv/`：本地虚拟环境
- `todo.sqlite3`、`*.db`：本地数据库
- `__pycache__/`、`*.pyc`：Python 缓存
- `node_modules/`、`dist/`：前端依赖或构建产物
- `.env`：本地环境变量
- `.DS_Store`、`.idea/`、`.vscode/`：系统或编辑器文件

提交前建议检查：

```powershell
git status
```

确认不要把虚拟环境、数据库、缓存、编辑器配置等“史”传上去。

## AI 对话记录说明

作业要求提交与 AI 的对话链接或完整 Markdown 导出。本项目提供 `AI_CONVERSATION.md` 作为本次 Codex CLI Agent 生成过程的对话记录摘要与关键提示词记录。若平台支持导出完整聊天记录，也可以同时提交平台导出的完整 Markdown。
