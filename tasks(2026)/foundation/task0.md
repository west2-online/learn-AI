# Task 0 - 环境搭建

> 预计耗时：7 天

## 学习目的

在一切开始之前，你应该学会一些计算机的基本素养，例如配环境。

以及一些作为 CSer 最基本的技能。

## 学习内容

- 基本的计算机操作
- 基本的环境配置
- Python 语法基础

## 学习要求

本轮考核的目的在于熟悉作为 CSer 最基本的工作环境，以及跑通最基本的几个 Python 程序。

## 作业

### 作业 1 - 环境搭建与基本工具的使用

你应该参考推荐教程与参考资料中的内容（后文均略），在你的电脑上搭建好 Python 的开发环境。

在完成本次作业后，你应该注意并使用正确的浏览器，学会基本的文件管理，学会使用基本的截图工具，自由访问需要的网站等。

### 作业 2 - Git 基础使用

创建一个 GitHub 账号，并且创建一个名为 `learn-ai-username` 的仓库（其中 `username` 替换为你的 GitHub 用户名，或者你也可以自行命名）。

在这个仓库中，你需要提交一个 `crazy-day.md` 文件，使用 Markdown 语法撰写一篇文章，内容自拟，要求至少包含以下元素：

- 多级标题
- 图片插入
- 链接插入
- 代码块
- 表格

你的 Markdown 文档需要通过 Markdown Lint 的基本检查。

### 作业 3 - Hello World

在你的 Python 环境中，编写一个简单的 Python 程序，输出 "Hello, World!"。

### 作业 4 - OI

使用 Python 完成下列任务：

1. 洛谷 P1001：<https://www.luogu.com.cn/problem/P1001>

2. 洛谷 P1046：<https://www.luogu.com.cn/problem/P1046>

3. 洛谷 P5737：<https://www.luogu.com.cn/problem/P5737>

4. AtCoder ARC017A：<https://www.luogu.com.cn/problem/AT_arc017_1>

### Bonus - 简单的 Python 程序

#### 比较基础的 Python 程序

1. 输入三个整数 x、y、z，请尝试用多种方式把这三个数由大到小输出
2. 输出九九乘法表
3. 输入⼀个字符串，判断字符串中是否含有 "ol" 这个⼦串，若有把所有的 "ol" 替换为 "fzu"，最后把字符串倒序输出
4. 输入⼀个列表（list），列表中含有字符串和整数，删除其中的字符串元素，然后把剩下的整数升序排序，输出列表
5. 创建一个字典（dict），为字典添加几个键为学号，值为姓名元素，删除学号尾号为偶数的元素，输出字典
6. 创建一个函数，这个函数可以统计一个只有数字的列表中各个数字出现的次数，通过字典方式返回
7. 设计⼀个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量。具有的 公有成员函数是：初始化商品信息的构造函数 __init__，显示商品信息的函数display，计算已售出 商品价值 income，修改商品信息的函数 setdata
8. 尝试用所学的知识写一个斗地主随机发牌程序，将每个人的发牌以及多的三张牌的结果分别输出到 player1.txt，player2.txt，player3.txt，others.txt 四个文件中，可以不要求牌的花色

#### 相对进阶的 Python 程序

1. 实现一个装饰器，在开始执行函数时输出该函数名称， 并在结束时输出函数的开始时间和结束时间以及运行时间
2. 用所学的知识写一个斗地主随机发牌程序，将每个人的发牌以及多的三张牌的结果分别按照从大到小的顺序输出到 player1.txt，player2.txt，player3.txt，others.txt 四个文件中
3. 写一个列表推导式，生成一个 5*10 的矩阵，矩阵内的所有值为 1，再写一个列表推导式，把这个矩阵转置
4. 了解类的魔术方法（Magic Method）。创建类 MyZoo，实现以下功能：
    - 具有字典 `animals`，动物名称作为 key，动物数量作为 value
    - 实例化对象的时候，输出 "My Zoo!"
    - 创建对象的时候可以输入字典进行初始化，若无字典传入，则初始化 `animals` 为空字典

    ```python
    myzoooo = MyZoo({"pig":5,'dog':6}) 
    myzoooo = MyZoo() 
    ```

    - print(myzoooo) 输出 动物名称和数量
    - 比较两个对象是否相等时，只要动物种类一样，就判断相等：

        ```python
        输入：
        myzoooo1 = MyZoo({'pig':1})
        myzoooo2 = MyZoo({'pig':5})
        print(myzoooo1 == myzoooo2)
        输出：
        My Zoo!
        My Zoo!
        True
        ```

    - len(myzoooo) 输出所有动物总数
5. 写一个正则表达式，用于验证用户密码，长度在 6~18 之间，只能包含英文和数字

## 推荐教程与参考资料

### 疑难解答以及一些基本认知

#### 是否需要好的显卡

学习人工智能有一个好的显卡会有一定帮助，但并非刚需，你完全可以使用 [Colab](https://colab.research.google.com/) 或者 GPU 云服务器来进行机器学习代码的编写和运行。

#### 英语的学习

学习人工智能，英语是必要的，可以使用插件「沉浸式翻译」或大语言模型辅助。

#### 浏览器的使用

请使用 Edge 或 Chrome，它们对各类开发工具和现代网页技术的兼容性最好，能为你减少很多不必要的麻烦。

#### 截图工具的使用

Windows 用户可以使用 `Win + Shift + S` 快捷键调出截图工具，Mac 用户可以使用 `Command + Shift + 4` 快捷键进行截图。

实在不会截图请使用 QQ 截图，快捷键通常是 `Ctrl + Alt + A`，不可以使用手机拍照。

#### 如何卸载

Windows 用户可以通过「控制面板」中的「程序和功能」来卸载软件，Mac 用户可以将应用程序拖动到废纸篓中进行卸载。

需要注意的是，不可以直接删除安装目录来卸载软件，这样可能会留下残余文件和注册表项，导致系统不稳定或占用磁盘空间。

#### 如何提问

你需要在提问之前仔细思考自己这个问题是否合理。提问需要附上源码，错误信息，错误截图，复现步骤等相关信息，不接受任何无图的提问。

#### 大语言模型的使用

不限制大语言模型的使用，但你需要对大语言模型生成的内容做到足够了解，并且确保可以复现。

如果有能力，建议使用 Gemini，ChatGPT 等，也请至少使用腾讯元宝（DeepSeek 版）、千问、智谱、DeepSeek。

请不要使用豆包。

### 魔法工具

你需要自行寻找科学上网工具并且注册谷歌账号。

前者实在找不到的私聊群主，后者自行研究（taobao or xianyu）。

### 安装 Python

访问 [Python 官方网站](https://www.python.org/downloads/) 下载并安装 Python 3 版本。

下载的时候请选择 Add Python 3.x to PATH 选项以便在命令行中使用 Python。如果你没有做这一步，最简单的方法是卸载后重新下载。

> 对于 Python 的版本，我的建议是固定使用 Python 3.12.3 版本，这是目前很多主流 AI 框架支持的比较新的版本，也是 Ubuntu 24.04 LTS 默认支持的版本。
>
> 对于 Python 3.13 乃至 Python 3.14，很多 AI 框架还不支持。
>
> Python 属于是一个对版本变化非常敏感的语言，很多东西你只要改了一个小版本号，然后代码就全炸了。
>
> 这里贴出 Python 3.12.3 的下载链接：
>
> <https://www.python.org/downloads/release/python-3123/>

### 安装 IDE 集成开发环境

初学者可以选择使用 [PyCharm](https://www.jetbrains.com.cn/pycharm/)，可以 [申请学生免费许可证](https://blog.jetbrains.com/zh-hans/blog/2022/08/24/2022-jetbrains-student-program/) 以使用专业版。

个人更建议使用 [VS Code](https://code.visualstudio.com/)（主要是 PyCharm 的 Jupyter Notebook 太过难用，建议初学者可以多使用 Jupyter 来编写程序）。

> 在下载 VS Code 后，请下载 Python 插件以获得更好的 Python 支持

### Python 虚拟环境的配置

在未来的学习中，由于不同项目可能会依赖不同版本的库，因此建议使用虚拟环境来隔离项目的依赖，避免版本冲突。

最简单的方法是使用 `venv`，这是 Python 内置的虚拟环境工具，可以通过以下命令创建和激活虚拟环境：

```bash
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate  # Windows
```

当然，更推荐使用 `uv`，这是一个更现代的 Python 虚拟环境管理工具，提供了更简洁的命令和更好的性能，最重要的是它支持并发安装依赖，极大地提升了安装速度。

你也可以使用 [miniconda](https://docs.anaconda.com/miniconda/) 来管理环境，它轻量且功能强大。

但是 Conda 会污染命令窗口，因此这里不作首选推荐。

初学者一定要注意环境相关的问题，从一开始就养成好的习惯。

> 关于虚拟环境，你现在可以在全局里跑。
>
> 等你哪一天环境炸了，自然会来研究。

### 清华源

在中国大陆访问 Python 官方的 PyPI 镜像可能会比较慢，因此建议使用清华大学提供的 PyPI 镜像源来加速包的下载。你可以通过以下命令临时使用清华源：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

如果你想永久使用清华源，可以在你的用户目录下创建一个名为 `pip` 的文件夹，并在其中创建一个名为 `pip.ini` 的文件，内容如下：

```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

这样配置后，你就可以直接使用 `pip install some-package` 来安装包了，速度会快很多。

### Markdown 基础

Markdown 是一种轻量级标记语言，排版语法简洁。它使用易读易写的纯文本格式编写文档，可与 HTML 混编，也可导出 HTML、PDF 以及 .md 文件。因简洁、高效、易读、易写，Markdown 被大量使用，如 GitHub、Wikipedia 等。

在线体验一下 [Markdown 在线编辑器](https://markdown.com.cn/editor/)。

对于未来的文档作业，我们要求你使用 Markdown 或者 Jupyter Notebook 来编写。

Markdown 语法并不复杂，建议初学者只需掌握基本语法即可，如标题、列表、加粗、斜体、链接、代码块等。进阶语法如脚注、任务列表等可根据需要学习。

[Markdown 基本语法学习](https://markdown.com.cn/basic-syntax/)

[Markdown 规范检查](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

> 你可以直接在 VS Code 里编写 Markdown 文件，然后使用快捷键 `Ctrl+Shift+V` 进行预览。
>
> 需要注意的是，GitHub 并不完全遵循 Markdown 标准，建议下载 GitHub Markdown Preview 插件以获得更好的兼容性。

### Python 基础

1. Crossin 编程教室 [Python 入门指南](https://python666.cn/cls/lesson/list/)
2. Python - 100 天从新手到大师的前 10 节课 [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days)
3. Python 官方文档 [3.12.12 Documentation](https://docs.python.org/zh-cn/3.12/)
4. 菜鸟教程 [Python3 教程](https://www.runoob.com/python3/python3-tutorial.html)
5. 廖雪峰的官方教程 [Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
6. B 站上有大量的入门基础课程，大家可以自行探索，找到适合自己的是最好的。

> 对于教程，不需要全部都看，只需要挑选几个自己喜欢的，边学边写。

### 代码风格

#### PEP 8 规范

[PEP 8 -- Style Guide for Python Code](https://peps.python.org/pep-0008/)

在一开始学习的时候，我们不强制你使用 PEP 8 规范，但是建议你养成良好的代码风格习惯。

#### Main 函数编写与 VS Code 直接运行

虽然 Python 可以直接运行脚本，但还是建议写一个 main 函数做简单封装。

VS Code 等集成开发环境右上角有一个运行按钮，建议搞明白这个是什么之后再使用一键运行的按钮。

否则请开一个终端，使用：

```bash
python your_script.py
```

#### 代码格式化

手写的代码经常黏黏糊糊一大坨，写起来方便，但是阅读起来就很痛苦，而好的代码风格能大大提升代码的可读性和可维护性。

推荐使用 black formatter(vs code) <https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter>

默认快捷键 `Alt+Shift+F` 进行代码格式化，推荐打开 `保存时自动格式化`

链接：<vscode://settings/editor.formatOnSave>
