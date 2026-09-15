# Markdown 维护规范

本文档用于统一本仓库 Markdown 文档的写作、检查与提交流程。维护者在提交文档改动前，应先阅读本文档并运行检查脚本。

## 适用范围

默认适用于以下文档：

- `README.md`
- `tasks(2026)` 目录下的 Markdown 文件

`pre-tasks` 是历史归档内容，默认不纳入新规范检查。如需检查历史文档，可在脚本后追加路径。

## 检查方式

Windows PowerShell 5：

```powershell
.\scripts\check-markdown.ps1
```

跨平台 Node.js：

```shell
node scripts/check-markdown.mjs
```

macOS / Linux shell：

```shell
sh scripts/check-markdown.sh
```

检查指定文件或目录：

```powershell
.\scripts\check-markdown.ps1 README.md "tasks(2026)\application"
```

```shell
node scripts/check-markdown.mjs README.md 'tasks(2026)/application'
```

脚本会执行两类检查：

- markdownlint：使用仓库根目录的 `.markdownlint.json`。
- Apple 中文排版规范：检查中英文、中文数字、数字单位和中文标点。

## 基础 Markdown 规范

提交前必须通过 Markdown 检查。常见要求：

- 标题层级连续，不跳级。
- 列表、引用、代码块前后保留必要空行。
- 表格分隔行与内容列风格一致，避免 `MD060`。
- 代码块尽量标注语言，例如 `powershell`、`python`、`markdown`。
- 链接优先使用明确文本，不使用裸露的长 URL；必要时可用尖括号包裹 URL。

## Apple 中文排版规范

### 中英文之间增加空格

```txt
√ 小红书 App 在苹果 iOS 应用商店将官方英文名称统一改写为全小写的 “rednote”。
x 小红书App在苹果iOS应用商店将官方英文名称统一改为全小写的“rednote”
```

### 中文与数字之间增加空格

```txt
√ 可预约开启 6 小时后，苹果 iPhone 17 系列新品预约总量突破 200 万。
x 可预约开启6小时后，苹果 iPhone 17 系列新品预约总量突破200万。
```

### 数字与单位之间无需增加空格

```txt
√ iPhone 17 标准版起步内存为 8GB，存储容量均从 256GB 起步。
x iPhone 17 标准版起步内存为 8 GB，存储容量均从 256 GB 起步。
```

### 中文语境使用全角标点

中文语境下使用全角标点（，。！？：；）。英文 / 代码语境下使用半角标点。当中文句子被英文词汇打断时，如果标点承担中文句子的停顿，仍使用中文全角标点。

```txt
√ 打开你的 iPhone，然后点击“设置”。
x 打开你的 iPhone, 然后点击“设置”.
```

### 代码与命令

- 行内代码使用反引号，例如 `uv run python main.py`。
- 代码块、命令、URL 内部不强制套用中文排版规则。
- 中文解释中的工具名仍按中英混排规则加空格，例如“使用 `uv` 创建虚拟环境”。

## Windows PowerShell 5 注意事项

维护脚本以 Windows PowerShell 5 为兼容目标：

- 不使用 `utf8NoBOM` 作为 `Set-Content -Encoding` 参数。
- 写入 UTF-8 文件时优先使用 .NET：`System.Text.UTF8Encoding($false)`。
- 不依赖 Bash、GNU sed 或 Linux-only 工具。
- 如需运行 Node 工具，请先确认 `node` 和 `npm` 可用。

## Git 工作流

推荐所有维护者按以下流程提交文档：

1. 从主分支同步最新代码。

   ```powershell
   git checkout main
   git pull --ff-only
   ```

2. 创建功能分支。

   ```powershell
   git checkout -b docs/update-markdown-style
   ```

3. 修改文档后检查工作区。

   ```powershell
   git status --short
   ```

4. 运行 Markdown 检查。

   ```powershell
   .\scripts\check-markdown.ps1
   ```

5. 查看差异，确认没有误改无关文件。

   ```powershell
   git diff -- README.md "tasks(2026)" docs scripts .markdownlint.json
   ```

6. 暂存并提交。

   ```powershell
   git add README.md "tasks(2026)" docs scripts .markdownlint.json
   git commit -m "docs: update markdown style checks"
   ```

7. 推送分支并发起 Pull Request。

   ```powershell
   git push -u origin docs/update-markdown-style
   ```

## 维护者自查清单

- 已运行 `.\scripts\check-markdown.ps1` 或 `node scripts/check-markdown.mjs` 且结果通过。
- 没有把密钥、Token、个人配置提交进仓库。
- 没有误改 `pre-tasks` 等历史归档内容。
- 中文、英文、数字和标点符合本文档规范。
- 表格在编辑器中没有 markdownlint 报错。
