# AI Conversation - Memo Codex 5.5

> [!TIP]
> 本文件用于满足作业中“附带你与 AI 的对话链接或导出完整的对话 Markdown 文件”的要求。当前环境是 Codex CLI Agent，本文件记录本次生成项目时的主要对话与执行过程。若提交平台支持完整会话导出，建议同时附上完整导出文件。

## 用户提示词

用户要求：

- 在 `tasks(2026)/foundation` 下创建 `Memo-Codex5.5`
- 完成作业 3：Vibe Coding TODO LIST
- 后端使用 FastAPI，操作数据表
- 前端使用 Vue3
- 实现增、改、查、删 API
- 删除必须是逻辑删除
- 查、改操作不能影响或返回已逻辑删除的数据
- 路径尽量 RESTful，返回 JSON
- 编写 README 部署文档
- 编写 API 测试脚本并确保可跑通
- Windows 开发环境，所有东西只存在当前文件夹
- 注意 Git 上传规范，不要上传虚拟环境、数据库、缓存等垃圾文件
- 不需要完成课后思考文档

## AI 执行摘要

AI 使用 Codex CLI Agent 形式完成任务，主要步骤：

1. 检查仓库结构和 `.gitignore`
2. 在 `tasks(2026)/foundation/Memo-Codex5.5` 创建独立项目
3. 编写 `.gitignore`，避免上传 `.venv/`、数据库、缓存、`node_modules/` 等文件
4. 编写 `requirements.txt`
5. 编写 `backend/main.py`
   - 使用 FastAPI
   - 使用 SQLModel + SQLite
   - 定义 TODO 数据表
   - 实现增删改查 API
   - 统一 JSON 返回格式
   - 支持分页、关键字、状态、标签筛选
   - 删除使用 `is_deleted` 逻辑删除
6. 编写 `frontend/index.html`
   - 使用 Vue3 CDN
   - 实现新增、查询、分页、完成/待办切换、标签修改、逻辑删除
7. 编写 `tests/api_test.py`
   - 使用 Python requests 调用所有核心 API
   - 验证分页、关键字、标签、id 查询、批量修改、逻辑删除
8. 编写 `README.md`
   - Windows 部署步骤
   - API 文档
   - 测试脚本运行方法
   - Git 上传规范

## 使用的 AI 形式

- AI：OpenAI Codex CLI Agent
- 形式：本地命令行 Agent
- 特点：可以读取和修改当前仓库文件，可以执行命令验证项目，不需要用户手动复制代码

## 关键提示词策略

本次提示词重点约束：

- 项目必须创建在指定文件夹，避免影响大环境
- Windows 环境优先
- 后端、前端、README、测试脚本一次性完整交付
- 删除使用逻辑删除，不允许真正删除数据
- 查、改、删必须排除已逻辑删除数据
- API 路径需要语义清晰并尽量 RESTful
- Git 提交前必须避免上传虚拟环境、数据库、缓存等垃圾文件

## 过程中的修正

在生成过程中，AI 主动做了以下防错设计：

- 使用项目内 `.venv`，不安装到全局 Python
- SQLite 数据库放在项目根目录，并加入 `.gitignore`
- 前端使用 Vue3 CDN，避免创建 `node_modules` 和额外构建产物
- 后端挂载静态前端页面，运行一个 FastAPI 服务即可同时访问前后端
- 所有批量改动和查询都添加 `is_deleted == False` 过滤
- API 测试最后会验证逻辑删除后的 id 查询返回 404，标签查询不再返回被删除事项

## 提交说明

提交作业时建议包含：

- `Memo-Codex5.5/backend/main.py`
- `Memo-Codex5.5/frontend/index.html`
- `Memo-Codex5.5/tests/api_test.py`
- `Memo-Codex5.5/requirements.txt`
- `Memo-Codex5.5/README.md`
- `Memo-Codex5.5/AI_CONVERSATION.md`
- `Memo-Codex5.5/.gitignore`

不要提交：

- `.venv/`
- `todo.sqlite3`
- `__pycache__/`
- `node_modules/`
- `.env`
