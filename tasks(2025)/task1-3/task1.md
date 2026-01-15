# Task 1 Python 基础与面向对象

## 学习目的

如今，Python 是构建人工智能应用的首选语言之一。因此，熟练掌握其语法是开启 AI 之旅的必备基础。

需要注意的是，不建议将主要精力投入到 [Python 后端](https://github.com/west2-online/learn-python)开发上。Python 后端虽然开发效率高，适合快速原型验证和中小型项目，但在高并发场景下性能表现不如 [Golang](https://github.com/west2-online/learn-go) 和 [Java](https://github.com/west2-online/learn-java)，且在企业级应用和就业市场中竞争力相对较弱。

Python 也有前端框架(如 Streamlit)，适合快速搭建数据展示和 AI 演示应用，但功能和生态远不如 JavaScript 生态系统完善。因此，若要从事专业的 [前端开发](https://github.com/west2-online/learn-frontend)，建议学习主流前端技术栈。

## 学习内容

- 基本的环境配置
- Python 基础语法
- 认识生成式 AI

## 学习要求

本轮考核的目的在于熟悉作为 CSer 最基本的工作环境，语言只是载体。

结束本轮的学习后，你应该掌握最基本的 Git 使用、基础的 Python 语法以及一定的 OOP 思想，为日后 AI 的学习打下扎实的基础。

### 疑问解答

- 是否需要好的显卡？

学习人工智能有一个好的显卡会有一定帮助，但并非刚需，你完全可以使用 [Colab](https://colab.research.google.com/) 或者 GPU 云服务器来进行机器学习代码的编写和运行。

- 英语的学习？

学习人工智能，英语是必要的，可以使用插件「沉浸式翻译」或大语言模型辅助。

- 浏览器的使用？

请使用 Edge 或 Chrome，它们对各类开发工具和现代网页技术的兼容性最好，能为你减少很多不必要的麻烦。

- 大语言模型的使用？

不限制大语言模型的使用，但你需要对大语言模型生成的内容做到足够了解，并且确保可以复现。

如果有能力，建议使用 Gemini，ChatGPT 等，也请至少使用腾讯元宝（DeepSeek 版）、千问、智谱、DeepSeek。

请不要使用豆包。

## 推荐教程

### 安装 Python

访问 [Python 官方网站](https://www.python.org/downloads/) 下载并安装 Python 3 版本。

下载的时候请选择 Add Python 3.x to PATH 选项以便在命令行中使用 Python。

> 对于 Python 的版本，我的建议是固定使用 Python 3.12.3 版本，这是目前很多主流 AI 框架支持的比较新的版本，也是 Ubuntu 24.04 LTS 默认支持的版本。
>
> 对于 Python 3.13 乃至 Python 3.14，很多 AI 框架还没有支持。
>
> Python 属于是一个对版本变化非常敏感的语言，很多东西你只要改了一个小版本号，然后代码就全炸了。

### 环境配置

- 科学上网工具的使用以及谷歌账号的注册

前者实在找不到的私聊群主，后者自行研究（taobao or xianyu）。

- 安装 IDE 集成开发环境

初学者可以选择使用 [PyCharm](https://www.jetbrains.com.cn/pycharm/)，可以[申请学生免费许可证](https://blog.jetbrains.com/zh-hans/blog/2022/08/24/2022-jetbrains-student-program/)以使用专业版。

个人更建议使用 [VSCode](https://code.visualstudio.com/)（主要是 PyCharm 的 Jupyter Notebook 太过难用，建议初学者可以多使用 Jupyter 来编写程序）。

> 在下载 VSCode 后，请下载 Python 插件以获得更好的 Python 支持

- 安装 Conda 环境 / 学习 Python 虚拟环境的配置

使用 [miniconda](https://docs.anaconda.com/miniconda/) 来管理环境，它轻量且功能强大。

如果你不喜欢 Conda 这样会污染命令窗口，使用 pyenv 或 venv 管理环境也都是可以的。

此外，使用 `poetry` 或 `uv` 等工具来自动管理项目依赖和虚拟环境，能够提升项目的可维护性和可移植性。

初学者一定要注意这个问题，从一开始就养成好的习惯。

> 关于虚拟环境，你现在可以在全局里跑。
>
> 等你哪一天环境炸了，自然会来研究。

### Python 基础

1. Crossin 编程教室 [Python 入门指南](https://python666.cn/cls/lesson/list/)
2. Python - 100 天从新手到大师的前 10 节课 [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days)
3. Python 官方文档 [3.12.12 Documentation](https://docs.python.org/zh-cn/3.12/)
4. 菜鸟教程 [Python3 教程](https://www.runoob.com/python3/python3-tutorial.html)
5. 廖雪峰的官方教程 [Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
6. B 站上有大量的入门基础课程，大家可以自行探索，找到适合自己的是最好的。
7. 如果你想要系统的学习的话，强烈推荐来自 UCB 的神课 [CS61A](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/Python/CS61A/)（课程难度较大，建议可以先选择一个更为友好的入门编程课程入门，需要学习相关学习资料的群里有压缩包）。

> 对于教程，不需要全部都看，只需要挑选几个自己喜欢的，边学边写。

### 生成式 AI 认识

[李宏毅 2024 B 站](https://www.bilibili.com/video/BV1BJ4m1e7g8/?spm_id_from=333.337.search-card.all.click&vd_source=e3594664d709db7578f4b2e76329df18)

[李宏毅 2024 YouTube](https://www.youtube.com/watch?v=AVIKFXLCPY8&t=1s)

[李宏毅 2025 YouTube](https://www.youtube.com/watch?v=VuQUF1VVX40&list=PLJV_el3uVTsMMGi5kbnKP5DrDHZpTX0jT&index=1&t=10s)

[李宏毅生成式人工智能教程课本](https://github.com/datawhalechina/leegenai-tutorial/releases)

> 注意：生成式 AI 导论不要求完成课程作业。YouTube 上的 2025 版课程仍在持续更新，教程课本是根据 2024 年春季学期课程整理而成。
>
> 2025 年秋季版课程在前几讲就引入了较为复杂的概念，与 2024 年春季版相比难度提升较多，内容变化也较大。建议初学者优先学习 2024 年春季版课程或直接阅读教程课本，无需观看 2025 年秋季版。
>
> 学习生成式 AI 导论时，无需看完所有课程或课本，只需根据作业文档 2 的要求，针对性地学习相关内容即可。

### Markdown 基础

Markdown 是一种轻量级标记语言，排版语法简洁，让人们更多地关注内容本身而非排版。它使用易读易写的纯文本格式编写文档，可与 HTML 混编，可导出 HTML、PDF 以及本身的 .md 格式的文件。因简洁、高效、易读、易写，Markdown 被大量使用，如 Github、Wikipedia、简书等。

在线体验一下 [Markdown 在线编辑器](https://markdown.com.cn/editor/)。

对于未来的文档作业，我们要求你使用 Markdown 或者 Jupyter Notebook 来编写。

Markdown 语法并不复杂，建议初学者只需掌握基本语法即可，如标题、列表、加粗、斜体、链接、代码块等。进阶语法如脚注、任务列表等可根据需要学习。

[Markdown 基本语法学习](https://markdown.com.cn/basic-syntax/)

> 你可以直接在 Vscode 里编写 Markdown 文件，然后使用快捷键 `Ctrl+Shift+V` 进行预览。建议下载 Markdown 格式检查插件。
>
> 需要注意的是，Github 不完全是 Markdown 标准，建议下载 GitHub Markdown Preview 插件以获得更好的兼容性。

### 代码风格

#### PEP 8 规范

- [PEP 8 -- Style Guide for Python Code](https://peps.python.org/pep-0008/)

在一开始学习的时候，我们不强制你使用 PEP 8 规范，但是建议你养成良好的代码风格习惯。

#### Main 函数编写与 Vscode 直接运行

虽然 python 是可以直接运行脚本的语言，但是建议都写一个 main 函数简单封装一下。

Vscode 等集成开发环境右上角有一个运行按钮，建议搞明白这个是什么之后再使用一键运行的按钮。

否则请开一个终端，使用：

```bash
python your_script.py
```

#### 代码格式化

手写的代码经常黏黏糊糊一大坨，写起来方便，但是阅读起来就很痛苦，而好的代码风格能大大提升代码的可读性和可维护性。

推荐使用 black formatter(vs code) <https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter>

默认快捷键 `Alt+Shift+F` 进行代码格式化，推荐打开 `保存时自动格式化`

链接：<vscode://settings/editor.formatOnSave>

### Git 教程以及规范

#### Git 相关教程

Git入门：<https://west2-online.feishu.cn/wiki/Lsz9w3CiGinXzgkevtmceHZknrf>

Github 如何 fork 以及 pr（如何交作业）：<https://west2-online.feishu.cn/wiki/Zvqow0CUxig3iWkWQgBcHp4AnHe>

Git 使用和西二作业提交教程：<https://github.com/west2-online-reserve/collection-ai>

Git 工作流和核心原理 | GitHub 基本操作 | VS Code 里使用 Git 和关联 GitHub：<https://www.bilibili.com/video/BV1r3411F7kn/?share_source=copy_web&vd_source=31019e44b62a4369d4eab7afea0fcfdf>

Git 工作流：<https://www.bilibili.com/video/BV19e4y1q7JJ/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3>

#### Git 规范

- 妥善使用 .gitignore

一些对于项目无用的，如 `__pycache__` 文件夹，`.vscode` 文件夹等不需要提交到 Git 仓库。

可以通过 `.gitignore` 文件忽略这些文件夹。

- 不要上传大文件到 GitHub

Github 建议大小不要超过 50MB，超过 100MB 的文件是无法上传的。另外，二进制文件不适合上传到 github 上，建议使用云盘进行存储，然后把链接放在 github 上。

例如图片就是二进制存储的，所以你一旦进行了修改，Github 不会删掉这个旧版本的图片，而是会把新的图片和旧的图片都存储下来，导致仓库体积暴涨。

旧图藏在了历史版本里，肉眼是看不到的。

所以，不要把你的大文件直接上传到 Github 上。

例如训练前的数据，训练好的模型文件，你爬虫爬到的东西，请使用 .gitignore 忽略掉。

- Commit 信息规范

对于这部分，刚开始可以相对随意一些，等你熟悉了 Git 的使用之后，再来规范这部分内容。

```bash
git commit -m "feat: add xxx feature"
git commit -m "fix: fix xxx bug"
git commit -m "docs: update xxx doc"
git commit -m "style: format xxx code"
git commit -m "refactor: refactor xxx code"
git commit -m "test: add xxx test"
git commit -m "chore: update xxx config"
```

## 作业

关于本次的任务，你需要完成以下内容——

- 两份文档，帮助你将学到的 Python 和对生成式 AI 的理解，系统地记录下来
- 完成作业一
- 从作业二、三、四中选择一项完成，可以根据自己的情况和偏好来自由选择

如果对于作业一上来感觉很懵逼的，可以写一部分作业零来帮助自己熟悉和巩固，作业零是不必要的。

本轮作业二、三、四不要求实现得多完美，这一轮考核主要是要你的输出，只要有写出来点什么东西即可。考核给的时间很长，截止至 11 月中旬，请尽可能完善你的项目。

作业难度：作业零 ≈ 作业一 << 作业二 < 作业三 ≈ 作业四

### 文档 1

当你初步掌握 Python 基础的知识学习后，请将以下知识点的理解，整理成一份你自己的笔记（使用 Markdown 或 Jupyter Notebook）。

- 基础容器：List（列表）、Dict（字典）的使用技巧
- 函数：Lambda 匿名函数、Decorator 装饰器
- 面向对象：Class（类）与 Magic Methods（魔法方法），以及 OOP（面向对象编程）的思想
- 文本处理：re 正则表达式
- 代码格式：列表推导式、Type Hint（类型注释）
- 进阶技巧：generator 生成器（yield 关键字）

### 文档 2

在完成生成式 AI 的认识后，你需要以文档形式讲述大语言模型的整个训练流程。

> 本文档**不要求精确的数学公式和理论表达**，只需用你自己的话，简要描述生成式 AI 的三个核心训练阶段：
>
> 1. 自监督学习（Pre-training）
> 2. 监督式学习（Supervised Fine-tuning）
> 3. 人类反馈强化学习（RLHF）

### 作业 0： OI

请使用 Python 完成下列任务

1. 洛谷 P1001：<https://www.luogu.com.cn/problem/P1001>

2. 洛谷 P1046：<https://www.luogu.com.cn/problem/P1046>

3. 洛谷 P5737：<https://www.luogu.com.cn/problem/P5737>

4. AtCoder ARC017A：<https://www.luogu.com.cn/problem/AT_arc017_1>

5. Python 后端[作业 1](https://github.com/west2-online/learn-python/blob/main/docs/1-%E5%9F%BA%E7%A1%80%E8%AF%AD%E6%B3%95.md)

### 作业 1：娜比娅偷吃事件

某日，在前往 ShaddockNH3 办公室的路上，重樱的神子大人**长门**意外地发现，一个塞壬人形「娜比娅」正鬼鬼祟祟地躲在角落里偷吃军粮！

「汝，竟敢在余之港区放肆！」

为了维护港区的和平（和食物！），长门决定亲自出手，给这个不懂礼数的闯入者一点教训！

你的任务，就是为长门大人编写战斗的核心逻辑，帮助她赶跑偷吃的娜比娅！

请下载 [Nabia_Snack_Incident](https://github.com/ShaddockNH3/learn-AI/releases/download/task1/Nabia_Snack_Incident/Nabia_Snack_Incident.rar)，解压后阅读 `README.md`，根据指引完成8个函数的编写。

这份作业并不难，只涉及到 `if`、`else`、`while`，所以请不要看 `Nabia_Snack_Incident` 下的 `answer.py`。

> 在写这份作业的时候，请思考 pass 的作用并且删除之。

### 作业 2：校园·if恋

[Tomori Nao](https://github.com/TomoriNaoiy) 是一个死宅，他憎恨所有的现充，但是弱小的他无法改变一切。但是，偶然一天他发现了一个名为 Python 的东西，于是，一个神奇的想法在他脑海里面浮现......

**他要在Python的世界里面，掌控一切！**

你需要完成一个由他臆想出来的 gal 世界，通过阅读 [Campus_IF_Love_Story.md](Campus_IF_Love/Campus_IF_Love_Story.md)，完成 [Campus_IF_Love.py](Campus_IF_Love/Campus_IF_Love.py) 文件里面的待完成函数。其中包括：对话函数、好感度函数、玩家操作等等。

如果你实在无法理解

「一个死宅到底是怎么想的啊！」

那么你可以点开 [Campus_IF_Love/README](Campus_IF_Love/README.md) 来窥视他梦境的一角...

### 作业3：宝可梦对战

[JadeMelody](https://github.com/JadeMelody) 是一个 cool guy，他最近沉迷上了宝可梦游戏。可是有一天他的 Switch 坏掉了，为了在等待维修的过程中还能玩宝可梦游戏，他向你提出了以下的程序设计要求——

你将要实现一个基于命令行游玩的宝可梦对战游戏，玩家和电脑可以各自选择 3 名宝可梦（电脑随机选择）组成队伍，游戏开始时从 3 个宝可梦中选择一个出战，每个宝可梦拥有以下特性：

1. HP：此宝可梦的血量，当宝可梦的剩余 HP 小于等于 0 时，该宝可梦会【昏厥】
2. 属性：宝可梦的属性会影响属性和抗性，相同属性的宝可梦会有一个相同的属性被动，宝可梦的属性会影响造成和受到的伤害
3. 攻击力：决定其对其他宝可梦的伤害
4. 防御力：来自其他宝可梦的伤害需要减去防御力的数值
5. 闪避率：在战斗中成功躲闪开敌人攻击的概率

| 属性 | 克制 | 被克制 | 属性被动                                 |
| ---- | ---- | ------ | ---------------------------------------- |
| 草   | 水   | 火     | 每回合回复 10% 最大 HP 值                |
| 火   | 草   | 水     | 每次造成伤害,叠加 10% 攻击力,最多 4 层   |
| 水   | 火   | 电     | 受到伤害时,有 50% 的几率减免 30% 的伤害  |
| 电   | 水   | 草     | 当成功躲闪时,可以立即使用一次技能        |
| ···  | ···  | ···    | ···                                      |

被克制的宝可梦受到来自克制的宝可梦的伤害翻倍，被克制的宝可梦对克制的宝可梦造成的伤害减半。
6. 招式：即技能，用来攻击对手的宝可梦，或者给对手的宝可梦附加各种各样的「效果」

这是 JadeMelody 设计的 4 个宝可梦：

1. **皮卡丘（PikaChu）**

![皮卡丘](./task1-3.assets/BE1707F2-C858-4085-8A9C-1C282825D0D1.jpeg)

**HP**：80 **攻击力**：35 **防御力**：5 **属性**：电 **躲闪率**：30%

**十万伏特（Thunderbolt）：** 对敌人造成 1.4 倍攻击力的电属性伤害，并有 10% 概率使敌人麻痹

**电光一闪（Quick Attack）：** 对敌人造成 1.0 倍攻击力的快速攻击（快速攻击有几率触发第二次攻击），10% 概率触发第二次
2. **妙蛙种子（Bulbasaur）**

![妙蛙种子](./task1-3.assets/3A370008-CF12-4404-B088-634C466404AA.jpeg)

**HP**：100 **攻击力**：35 **防御力**：10 **属性**：草 **躲闪率**：10%

**种子炸弹（Seed Bomb）：** 妙蛙种子发射一颗种子，爆炸后对敌方造成草属性伤害。若击中目标，目标有 15% 几率陷入「中毒」状态，每回合损失 10% 生命值

**寄生种子（Parasitic Seeds）：** 妙蛙种子向对手播种，每回合吸取对手 10% 的最大生命值并恢复自己，效果持续 3 回合
3. **杰尼龟（Squirtle）**

![杰尼龟](./task1-3.assets/D9506539-335B-4856-9768-27203069DE8C.jpeg)

**HP**：80 **攻击力**：25 **防御力**：20 **属性**：水 **躲闪率**：20%

**水枪（Aqua Jet）：** 杰尼龟喷射出一股强力的水流，对敌方造成 140% 水属性伤害

**护盾（Shield）：** 杰尼龟使用水流形成保护盾，减少下一回合受到的伤害 50%
4. **小火龙（Charmander）**

![小火龙](./task1-3.assets/A46CDBFA-F132-4DC0-BCCE-4506CB07B905.jpeg)

**HP**：80 **攻击力**：35 **防御力**：15 **属性**：火 **躲闪率**：10%

**火花（Ember）：** 小火龙发射出一团小火焰，对敌人造成 100% 火属性伤害，并有 10% 的几率使目标陷入「烧伤」状态（每回合受到 10 额外伤害，持续 2 回合）

**蓄能爆炎（Flame Charge）：** 小火龙召唤出强大的火焰，对敌人造成 300% 火属性伤害，并有 80% 的几率使敌人陷入「烧伤」状态，这个技能需要 1 个回合的蓄力，并且在面对该技能时敌法闪避率增加 20%

你仍需要再设计至少一个宝可梦，如果你对 JadeMelody 设计的宝可梦不满意，feel free 去修改他们。

你需要实现类似这样命令行输出用于游玩该游戏：

```bash
请选择 3 个宝可梦用于组成你的队伍：
1. 皮卡丘（电属性） 2. 妙蛙种子（草属性） 3. 杰尼龟（水属性） 4. 小火龙（火属性）
输入数字选择你的宝可梦：1 2 4

请选择你的宝可梦：
1. 小火龙（火属性） 2. 杰尼龟（水属性） 3. 妙蛙种子（草属性）
输入数字选择你的宝可梦：1
你选择了 小火龙！
电脑选择了 杰尼龟！

你的 小火龙 的技能：
1. 火花
2. 蓄能爆炎
选择一个技能进行攻击：1
小火龙 使用了 火焰喷射！
杰尼龟 受到了 30 点伤害！剩余 HP：70

杰尼龟 使用了 水枪！
小火龙 受到了 25 点伤害！剩余 HP：75
```

如果对于 JadeMelody 设计的玩法不满意，feel free 修改他们。

要尽可能避免代码重复，可以创建一个 Pokemon 的基类，一个属性类像 WaterPokemon 继承自它，再有一个宝可梦继承自属性类。

完成后写一个 README.md 文件介绍玩法，一同上传 GitHub。

> 在[示例代码](./Pokemon_Example) 文件夹中有示例代码（已经实现了一个宝可梦，你们只需要在 JadeMelody 的基础上添加更多内容就可以）（阅读代码也是一个需要大家多多锻炼的技能），可以发挥自己的创造力去实现更多的功能做得 fancy 一点，到时候再写一个 Markdown 文档可以放在你的 GitHub 仓库下。
>
> JadeMelody 的代码里面依旧有许多不足的地方，可以多多完善，当然也可以自行从零开始设计（在面向对象程序设计中每个人都会有不一样的思路，而每个思路都会有可取的地方，大家也可以在群里多多交流）。
>
> 可参考 ShaddockNH3 考核写的[完整代码](https://github.com/ShaddockNH3/west2-online-ai-2024-test/blob/master/pokemon_impact.py)，但是他的代码显然有很大的优化空间，比如说没有分包（其实是因为当时分包了会报错）、大量的代码复用，以及一些取巧的实践方式。

### 作业4：好玩的东西

猫娘是一种软乎乎的、可爱的生物，美中不足的是，她们有的时候会哈气。这个时候只有一种办法安抚她们，那就是奉上一个完整的 py 项目。

你的任务是自行设计一个结构完整、功能清晰的小项目，需要运用到类（Class）、魔法方法（Magic Methods）等面向对象的思想，并合理地拆分为多个文件。

### Bonus

完成 CS61A 的学习，完成相应的作业和 lab，不要畏惧全英文的学习，你完全可以使用各类翻译软件帮助你学习，包括 GPT。

CS61A 是一门大学级别的计算机科学导论课，它将带你深入探索编程的本质，如递归、高阶函数、数据抽象和解释器设计等。这门课的挑战性极高，但若能坚持学完，你的编程内功和计算机思维将获得质的飞跃，如果能啃下这门课，那么你的编程水平将会超过绝大多数毕业生。

## 作业要求

1. 不要抄袭
2. 遇到不会可以多使用搜索引擎，实在没有找到解决方法可以来群里提问，作为一个CSer学习提问的方式也非常重要，强烈建议阅读[Stop-Ask-Questions-The-Stupid-Ways](https://github.com/tangx/Stop-Ask-Questions-The-Stupid-Ways/blob/master/README.md)这篇文章
3. 不限制使用 ChatGPT 等大语言模型工具，但你需要确保你了解模型生成的内容的每一个细节，最好你可以在使用大语言模型生成的代码部分注释上「reference from ChatGPT」这样的内容
4. 你还需要学习基本的 Git 的使用，所有考核都采用 Git 的方式进行上传
5. 作业内容可能会进行更新，请保持关注

## 作业提交方式

1. 你需要学习 GitHub 的使用，创建一个你自己的仓库用来存放你的代码实现
2. 接着你需要学习如何使用 Git 进行 PR 操作，在 [solutions](https://github.com/west2-online-reserve/collection-ai) 中进行操作
