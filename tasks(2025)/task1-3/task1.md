# Task 1 Python 基础与面向对象

## 学习目的

如今，Python 是构建人工智能应用的首选语言之一。因此，熟练掌握其语法是开启 AI 之旅的必备基础。

需要注意的是，不建议将主要精力投入到 [Python 后端](https://github.com/west2-online/learn-python)开发上。Python 后端虽然开发效率高，适合快速原型验证和中小型项目，但在高并发场景下性能表现不如 [Golang](https://github.com/west2-online/learn-go) 和 [Java](https://github.com/west2-online/learn-java)，且在企业级应用和就业市场中竞争力相对较弱。

Python 也有前端框架(如 Streamlit)，适合快速搭建数据展示和 AI 演示应用，但功能和生态远不如 JavaScript 生态系统完善。因此，若要从事专业的 [前端开发](https://github.com/west2-online/learn-frontend)，建议学习主流前端技术栈。

## 学习内容

Python 基础语法、认识生成式 AI

## 疑问解答

- 是否需要好的显卡？

学习人工智能有一个好的显卡会有一定帮助，但并非刚需，你完全可以使用 [Colab](https://colab.research.google.com/) 或者 GPU 云服务器来进行机器学习代码的编写和运行。

- 英语的学习？

学习人工智能，英语是必要的，可以使用插件「沉浸式翻译」或大语言模型辅助。

- 浏览器的使用？

请使用 Edge 或 Chrome，它们对各类开发工具和现代网页技术的兼容性最好，能为你减少很多不必要的麻烦。

- 大语言模型的使用？

不限制大语言模型的使用，但你需要对大语言模型生成的内容做到足够了解，并且确保可以复现。

<details style="display:inline-block; margin-bottom: -5px;"><summary>（...）</summary>

如果有能力，建议使用 Gemini 系列或者 ChatGPT 等国外 AI；如果是国内的 AI，也请使用 DeepSeek 或腾讯元宝（DeepSeek 版）。不要使用豆包

</details>

## 考核内容

### 1. 配置环境

- 科学上网工具的使用以及谷歌账号的注册

前者实在找不到的私聊群主，后者自行研究（taobao）

- 安装 IDE 集成开发环境

初学者可以选择使用 [PyCharm](https://www.jetbrains.com.cn/pycharm/)，可以[申请学生免费许可证](https://blog.jetbrains.com/zh-hans/blog/2022/08/24/2022-jetbrains-student-program/)以使用专业版。

个人更建议使用 [VSCode](https://code.visualstudio.com/)（主要是 PyCharm 的 Jupyter Notebook 太过难用，建议初学者可以多使用 Jupyter 来编写程序）。

- 安装 Conda 环境/学习 Python 虚拟环境的配置

使用 [miniconda](https://docs.anaconda.com/miniconda/) 来管理环境，它轻量且功能强大。

当然如果你不喜欢 Conda 这样会污染命令窗口，使用 pyenv 或 venv 管理环境也都是可以的，初学者一定要注意这个问题，从一开始就养成好的习惯。

> 关于虚拟环境，等你某一天环境炸了，自然会来研究

### 2. 推荐教程

- Python 基础：

1. Crossin 编程教室 [Python 入门指南](https://python666.cn/cls/lesson/list/)
2. Python - 100 天从新手到大师的前 10 节课 [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days)
3. Python 官方文档 [3.12.12 Documentation](https://docs.python.org/zh-cn/3.12/)
4. 菜鸟教程 [Python3 教程](https://www.runoob.com/python3/python3-tutorial.html)
5. 廖雪峰的官方教程 [Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
6. B 站上有大量的入门基础课程，大家可以自行探索，找到适合自己的是最好的。
7. 如果你想要系统的学习的话，强烈推荐来自 UCB 的神课 [CS61A](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/Python/CS61A/)（课程难度较大，建议可以先选择一个更为友好的入门编程课程入门，需要学习相关学习资料的群里有压缩包）。

> 对于教程，不需要全部都看，只需要挑选几个自己喜欢的，边学边写。

> 推荐使用 Python 3.12 版本，人工智能主流框架一般更新的没那么快

- 生成式 AI 认识：

[李宏毅 2024 B 站](https://www.bilibili.com/video/BV1BJ4m1e7g8/?spm_id_from=333.337.search-card.all.click&vd_source=e3594664d709db7578f4b2e76329df18)

[李宏毅 2024 YouTube](https://www.youtube.com/watch?v=AVIKFXLCPY8&t=1s)

[李宏毅 2025 YouTube](https://www.youtube.com/watch?v=VuQUF1VVX40&list=PLJV_el3uVTsMMGi5kbnKP5DrDHZpTX0jT&index=1&t=10s)

[李宏毅生成式人工智能教程课本](https://github.com/datawhalechina/leegenai-tutorial/releases)

> 注意，生成式 AI 导论可不要求该课程的作业，2025 油管上的课程还在持续更新中，课本其实就是上课的话整理出来的，是先有的课才有的课本。

### 3. 完成作业

关于本次的任务，你需要完成以下内容——

- 两份文档，帮助你将学到的 Python 和对生成式 AI 的理解，系统地记录下来
- 完成作业一
- 从作业二、三、四中选择一项完成，可以根据自己的情况和偏好来自由选择

如果对于作业一上来感觉很懵逼的，可以写一部分作业零来帮助自己熟悉和巩固，作业零是不必要的。

本轮作业二、三、四不要求实现得多完美，这一轮考核主要是要你的输出，只要有写出来点什么东西即可。考核给的时间很长，截止至 11 月中旬，请尽可能完善你的项目。

作业难度：作业零 ≈ 作业一 << 作业二 < 作业三 ≈ 作业四

#### 文档 1

当你初步掌握 Python 基础的知识学习后，请将以下知识点的理解，整理成一份你自己的笔记（推荐使用 Markdown 或 Jupyter Notebook）。

- 基础容器：List（列表）、Dict（字典）的使用技巧
- 函数：Lambda 匿名函数、Decorator 装饰器
- 面向对象：Class（类）与 Magic Methods（魔法方法），以及 OOP（面向对象编程）的思想
- 文本处理：re 正则表达式
- 代码格式：列表推导式、Type Hint（类型注释）
- 进阶技巧：generator 生成器（yield 关键字）

#### 文档 2

在完成生成式 AI 的认识后，你需要以文档形式讲述大语言模型的整个训练流程。（不需要精确的表达与数学公式，只需大致讲解自己的理解即可）

#### 作业零 OI

请使用 Python 完成下列任务

1. 洛谷 P1001：https://www.luogu.com.cn/problem/P1001

2. 洛谷 P1046：https://www.luogu.com.cn/problem/P1046

3. 洛谷 P5737：https://www.luogu.com.cn/problem/P5737

4. AtCoder ARC017A：https://www.luogu.com.cn/problem/AT_arc017_1

5. Python 后端[作业 1](https://github.com/west2-online/learn-python/blob/main/docs/1-%E5%9F%BA%E7%A1%80%E8%AF%AD%E6%B3%95.md)

#### 作业一 娜比娅偷吃事件

某日，在前往 ShaddockNH3 办公室的路上，重樱的神子大人**长门**意外地发现，一个塞壬人形「娜比娅」正鬼鬼祟祟地躲在角落里偷吃军粮！

「汝，竟敢在余之港区放肆！」

为了维护港区的和平（和食物！），长门决定亲自出手，给这个不懂礼数的闯入者一点教训！

你的任务，就是为长门大人编写战斗的核心逻辑，帮助她赶跑偷吃的娜比娅！

请下载 [Nabia_Snack_Incident](https://github.com/ShaddockNH3/learn-AI/releases/download/task1/Nabia_Snack_Incident/Nabia_Snack_Incident.rar)，解压后阅读 `README.md`，根据指引完成8个函数的编写。

这份作业并不难，只涉及到 `if`、`else`、`while`，所以请不要看 `Nabia_Snack_Incident` 下的 `answer.py`。

#### 作业二 校园·if恋

[Tomori Nao](https://github.com/TomoriNaoiy) 是一个死宅，他憎恨所有的现充，但是弱小的他无法改变一切。但是，偶然一天他发现了一个名为 Python 的东西，于是，一个神奇的想法在他脑海里面浮现......

**他要在Python的世界里面，掌控一切！**

你需要完成一个由他臆想出来的 gal 世界，通过阅读 [Campus_IF_Love_Story.md](Campus_IF_Love/Campus_IF_Love_Story.md)，完成 [Campus_IF_Love.py](Campus_IF_Love/Campus_IF_Love.py) 文件里面的待完成函数。其中包括：对话函数、好感度函数、玩家操作等等。

如果你实在无法理解

**「一个死宅到底是怎么想的啊！」**

那么你可以点开 [Campus_IF_Love/README](Campus_IF_Love/README.md) 来窥视他梦境的一角...

#### 作业三 宝可梦对战

[JadeMelody](https://github.com/JadeMelody) 是一个 cool guy，他最近沉迷上了宝可梦游戏。可是有一天他的 Switch 坏掉了，为了在等待维修的过程中还能玩宝可梦游戏，他向你提出了以下的程序设计要求——

你将要实现一个基于命令行游玩的宝可梦对战游戏，玩家和电脑可以各自选择 3 名宝可梦（电脑随机选择）组成队伍，游戏开始时从 3 个宝可梦中选择一个出战，每个宝可梦拥有以下特性：

1. HP：此宝可梦的血量，当宝可梦的剩余 HP 小于等于 0 时，该宝可梦会【昏厥】
2. 属性：宝可梦的属性会影响属性和抗性，相同属性的宝可梦会有一个相同的属性被动，宝可梦的属性会影响造成和受到的伤害
3. 攻击力：决定其对其他宝可梦的伤害
4. 防御力：来自其他宝可梦的伤害需要减去防御力的数值
5. 闪避率：在战斗中成功躲闪开敌人攻击的概率

| 属性 | 克制 | 被克制 | 属性被动                             |
| ---- | ---- | ------ | ------------------------------------ |
| 草   | 水   | 火     | 每回合回复 10% 最大 HP 值            |
| 火   | 草   | 水     | 每次造成伤害，叠加 10% 攻击力，最多 4 层 |
| 水   | 火   | 电     | 受到伤害时，有 50% 的几率减免 30% 的伤害 |
| 电   | 水   | 草     | 当成功躲闪时，可以立即使用一次技能   |
| ···  | ···  | ···    | ···（你还可以自行设计）              |

被克制的宝可梦受到来自克制的宝可梦的伤害翻倍，被克制的宝可梦对克制的宝可梦造成的伤害减半

6. 招式：即技能，用来攻击对手的宝可梦，或者给对手的宝可梦附加各种各样的「效果」

这是 JadeMelody 设计的 4 个宝可梦：

1. **皮卡丘（PikaChu）**

![皮卡丘](./阶段1.assets/BE1707F2-C858-4085-8A9C-1C282825D0D1.jpeg)

**HP**：80 **攻击力**：35 **防御力**：5 **属性**：电 **躲闪率**：30%

**十万伏特（Thunderbolt）：** 对敌人造成 1.4 倍攻击力的电属性伤害，并有 10% 概率使敌人麻痹

**电光一闪（Quick Attack）：** 对敌人造成 1.0 倍攻击力的快速攻击（快速攻击有几率触发第二次攻击），10% 概率触发第二次

2. **妙蛙种子（Bulbasaur）**

![妙蛙种子](./阶段1.assets/3A370008-CF12-4404-B088-634C466404AA.jpeg)

**HP**：100 **攻击力**：35 **防御力**：10 **属性**：草 **躲闪率**：10%

**种子炸弹（Seed Bomb）：** 妙蛙种子发射一颗种子，爆炸后对敌方造成草属性伤害。若击中目标，目标有 15% 几率陷入「中毒」状态，每回合损失 10% 生命值

**寄生种子（Parasitic Seeds）：** 妙蛙种子向对手播种，每回合吸取对手 10% 的最大生命值并恢复自己，效果持续 3 回合

3. **杰尼龟（Squirtle）**

![杰尼龟](./阶段1.assets/D9506539-335B-4856-9768-27203069DE8C.jpeg)

**HP**：80 **攻击力**：25 **防御力**：20 **属性**：水 **躲闪率**：20%

**水枪（Aqua Jet）：** 杰尼龟喷射出一股强力的水流，对敌方造成 140% 水属性伤害

**护盾（Shield）：** 杰尼龟使用水流形成保护盾，减少下一回合受到的伤害 50%

4. **小火龙（Charmander）**

![小火龙](./阶段1.assets/A46CDBFA-F132-4DC0-BCCE-4506CB07B905.jpeg)

**HP**：80 **攻击力**：35 **防御力**：15 **属性**：火 **躲闪率**：10%

**火花（Ember）：** 小火龙发射出一团小火焰，对敌人造成 100% 火属性伤害，并有 10% 的几率使目标陷入「烧伤」状态（每回合受到 10 额外伤害，持续 2 回合）

**蓄能爆炎（Flame Charge）：** 小火龙召唤出强大的火焰，对敌人造成 300% 火属性伤害，并有 80% 的几率使敌人陷入「烧伤」状态，这个技能需要 1 个回合的蓄力，并且在面对该技能时敌法闪避率增加 20%

你仍需要再设计至少一个宝可梦，如果你对 JadeMelody 设计的宝可梦不满意，feel free 去修改他们。

你需要实现类似这样命令行输出用于游玩该游戏：

```log
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

对于 JadeMelody 设计的玩法不满意，同样 feel free 去修改他们

要尽可能避免代码重复，可以创建一个 Pokemon 的基类，一个属性类像 WaterPokemon 继承自它，再有一个宝可梦继承自属性类。

完成后写一个 README.md 文件介绍玩法，一同上传 GitHub。

> 在[示例代码](./Pokemon_Example) 文件夹中有示例代码（已经实现了一个宝可梦，你们只需要在 JadeMelody 的基础上添加更多内容就可以）（阅读代码也是一个需要大家多多锻炼的技能），可以发挥自己的创造力去实现更多的功能做得 fancy 一点，到时候再写一个 Markdown 文档可以放在你的 GitHub 仓库下。

> JadeMelody 的代码里面依旧有许多不足的地方，可以多多完善，当然也可以自行从零开始设计（在面向对象程序设计中每个人都会有不一样的思路，而每个思路都会有可取的地方，大家也可以在群里多多交流）。

> 可参考 ShaddockNH3 去年考核写的[完整代码](https://github.com/ShaddockNH3/west2-online-ai-2024-test/blob/master/pokemon_impact.py)，但是他的代码显然有很大的优化空间，比如说没有分包（其实是因为当时分包了会报错）、大量的代码复用，以及一些取巧的实践方式。

#### 作业四 好玩的东西

猫娘是一种软乎乎的、可爱的生物，美中不足的是，她们有的时候会哈气。这个时候只有一种办法安抚她们，那就是奉上一个完整的 py 项目。

你的任务是自行设计一个结构完整、功能清晰的小项目，需要运用到类（Class）、魔法方法（Magic Methods）等面向对象的思想，并合理地拆分为多个文件。

#### Bonus

完成 CS61A 的学习，完成相应的作业和 lab，不要畏惧全英文的学习，你完全可以使用各类翻译软件帮助你学习，包括 GPT。

CS61A 是一门大学级别的计算机科学导论课，它将带你深入探索编程的本质，如递归、高阶函数、数据抽象和解释器设计等。这门课的挑战性极高，但若能坚持学完，你的编程内功和计算机思维将获得质的飞跃，如果能啃下这门课，那么你的编程水平将会超过绝大多数毕业生。

## 作业要求

1. 不要抄袭
2. 遇到不会可以多使用搜索引擎，实在没有找到解决方法可以来群里提问，作为一个CSer学习提问的方式也非常重要，强烈建议阅读[Stop-Ask-Questions-The-Stupid-Ways](https://github.com/tangx/Stop-Ask-Questions-The-Stupid-Ways/blob/master/README.md)这篇文章
3. 不限制使用ChatGPT等大语言模型工具，但你需要确保你了解模型生成的内容的每一个细节，最好你可以在使用大语言模型生成的代码部分注释上"reference from ChatGPT"这样的内容
3. 不限制使用 ChatGPT 等大语言模型工具，但你需要确保你了解模型生成的内容的每一个细节，最好你可以在使用大语言模型生成的代码部分注释上「reference from ChatGPT」这样的内容
4. 你还需要学习基本的 Git 的使用，所有考核都采用 Git 的方式进行上传
5. 作业内容可能会进行更新，请保持关注

## 作业提交方式

1. 你需要学习 GitHub 的使用，创建一个你自己的仓库用来存放你的代码实现
2. 接着你需要学习如何使用 Git 进行 PR 操作，在 [solutions](https://github.com/west2-online-reserve/collection-ai) 中进行操作

## 相关教程：

[https://github.com/west2-online-reserve/collection-ai](https://github.com/west2-online-reserve/collection-ai) 里面有 Git 使用和西二作业提交教程

[Git 工作流和核心原理 | GitHub 基本操作 | VS Code 里使用 Git 和关联 GitHub](https://www.bilibili.com/video/BV1r3411F7kn/?share_source=copy_web&vd_source=31019e44b62a4369d4eab7afea0fcfdf)
