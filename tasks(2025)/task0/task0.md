# Task 0 计算机基础知识

本文档汇总了进行 AI 学习所需掌握的计算机基础知识。你不需要一开始就全部掌握，而是在遇到相关问题时，再回来查阅对应的章节。

## 前置准备

### 账号与工具准备

在开始学习之前，你需要完成以下准备工作：

1. 注册 Google 账号，并配置科学上网工具
2. 注册 [GitHub](https://github.com/) 账号
3. 注册一个非 QQ 的邮箱（推荐网易邮箱或 Gmail）用于接收学术通知

> 如果在科学上网方面遇到困难，可以私聊寻求帮助。

## 文档编写

### Markdown 语法

Markdown 是一种轻量级标记语言，广泛应用于技术文档编写。你将使用 Markdown 格式完成作业文档和项目说明。

* 学习资源：[Markdown 基础语法](https://markdown.com.cn/basic-syntax/)

### 编程规范

良好的编程习惯从命名开始。掌握规范的变量命名方式，将让你的代码更易读、更易维护。

* 常用命名规范：
  * 驼峰命名法（camelCase）：适用于变量和函数名
  * 帕斯卡命名法（PascalCase）：适用于类名
  * 下划线命名法（snake_case）：Python 推荐使用

## 版本控制

### Git 基础

Git 是目前最流行的分布式版本控制系统。掌握 Git 是每个开发者的必备技能。

* 推荐教程：
  * [collection-ai 仓库](https://github.com/west2-online-reserve/collection-ai)：包含 Git 使用和西二作业提交教程
  * [Git 工作流和核心原理 | GitHub 基本操作 | VS Code 里使用 Git 和关联 GitHub](https://www.bilibili.com/video/BV1r3411F7kn/?share_source=copy_web&vd_source=31019e44b62a4369d4eab7afea0fcfdf)

### GitHub 使用

GitHub 是基于 Git 的代码托管平台。你需要学会：

* 创建和管理仓库
* 提交代码（commit & push）
* 提交 Pull Request（PR）
* 查看和解决 Issue

* 推荐教程：
  * [Git 工作流详解](https://www.bilibili.com/video/BV19e4y1q7JJ/?spm_id_from=333.337.search-card.all.click)

## 开发环境

### Python 虚拟环境

虚拟环境是 Python 开发中用于隔离项目依赖的重要工具。不同项目可能需要不同版本的库，使用虚拟环境可以避免版本冲突。

* 常用工具：
  * Conda/Miniconda：功能强大，适合科学计算
  * venv：Python 内置，轻量简洁
  * pyenv：适合管理多个 Python 版本

> 详细的环境配置方法将在 Task 1 中介绍。

### 集成开发环境（IDE）

选择合适的开发工具能显著提升编程效率。

* 推荐工具：
  * [PyCharm](https://www.jetbrains.com.cn/pycharm/)：功能强大的 Python IDE
  * [VS Code](https://code.visualstudio.com/)：轻量级且扩展丰富

> IDE 的详细配置和使用方法将在 Task 1 中详细介绍。

## 系统操作

### 终端与命令行

终端（Terminal）是与计算机交互的重要方式。掌握基本的命令行操作将让你的工作更加高效。

* 需要掌握的概念：
  * 绝对路径与相对路径
  * 常用命令：`cd`、`ls`/`dir`、`pwd`、`mkdir`、`rm`
  * 环境变量的概念

### 文件管理

理解文件系统的组织结构，掌握文件的创建、移动、复制和删除操作。

* Windows：文件资源管理器
* macOS：Finder
* Linux：命令行操作为主

#### 项目文件夹组织

良好的文件管理习惯能让你的学习和工作更加高效。建议采用以下方式组织你的项目：

* 为每个项目单独创建一个文件夹，例如：
  ```
  ~/Projects/
  ├── task1-python-basics/
  ├── task2-web-crawler/
  ├── task3-data-analysis/
  └── my-personal-project/
  ```

* 在项目文件夹内保持清晰的结构：
  ```
  task1-python-basics/
  ├── README.md          # 项目说明文档
  ├── requirements.txt   # 依赖列表
  ├── src/              # 源代码目录
  │   └── main.py
  ├── data/             # 数据文件目录
  ├── tests/            # 测试文件目录
  └── docs/             # 文档目录
  ```

* 命名规范：
  * 使用小写字母和连字符（kebab-case）或下划线（snake_case）
  * 避免使用空格和特殊字符
  * 使用有意义的名称，便于日后查找

> 养成良好的文件组织习惯，能让你在项目数量增多时依然保持清晰的思路。

### Linux 基础

虽然不是必需，但掌握 Linux 基础对于深度学习和服务器开发很有帮助。

* 学习方式：
  * Windows 用户：安装 WSL（Windows Subsystem for Linux）或使用虚拟机（VirtualBox、VMware）
  * macOS 用户：macOS 本身基于 Unix 系统，终端操作与 Linux 类似，通常不需要额外安装虚拟机
  * Linux 用户：已具备原生环境

## 学习方法

### 高效提问

作为一名计算机学习者，学会如何高效提问是一项重要技能。

* 推荐阅读：[提问的智慧](https://github.com/tangx/Stop-Ask-Questions-The-Stupid-Ways/blob/master/README.md)

* 提问时应包含的信息：
  1. 你想做什么？（你的目标）
  2. 你尝试了什么？（贴上你的关键代码）
  3. 你遇到了什么问题？（贴上完整的报错信息）
  4. 你觉得可能的原因是什么？（展现你的思考过程）

### 使用搜索引擎

遇到问题时，首先应该尝试使用搜索引擎（Google、Bing）自行解决。这不仅能培养独立解决问题的能力，也能帮助你更快地成长。

* 搜索技巧：
  * 使用英文关键词通常能获得更好的结果
  * 添加 `site:stackoverflow.com` 限定在特定网站搜索
  * 搜索完整的错误信息

### 使用 AI 辅助工具

不限制使用 ChatGPT、Gemini 等大语言模型工具，但你需要注意：

1. 确保你理解 AI 生成内容的每一个细节
2. 不要盲目复制粘贴，要理解代码的工作原理
3. 在使用 AI 生成的代码时，建议添加注释标注来源（如 `# reference from ChatGPT`）

---

## 使用说明

本文档是一个索引性质的知识清单。建议你：

1. 首次阅读时，快速浏览各个章节，了解大致内容
2. 在实际学习过程中遇到相关问题时，再回来详细查阅对应章节
3. 逐步掌握这些基础知识，它们将伴随你整个编程生涯
