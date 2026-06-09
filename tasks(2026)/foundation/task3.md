# Task 3 - 简单 AI 认识

> [!NOTE]
> 预计耗时：14 天

## 学习目的

在前两轮的任务中，我们学习了 Python 基础语法以及如何利用爬虫与数据分析工具获取和处理数据，而再接下来就是人工智能。

在真正开始写第一行 AI 相关的代码之前，建立对 AI 底层逻辑的正确认知至关重要。

目前，绝大多数人只是把 AI 当成一个万能的搜索引擎或高级聊天机器人。然而你需要跳出普通用户的视角，站在开发者的角度来审视它。

这里的开发者有两层含义，一层是你作为底层开发者，也就是改 AI 模型的底层架构；另一层是作为顶层开发者，调用 API 来为你完成各种任务。

这也是后续分成 Research 和 Application 的原因。

本轮任务的重点不在于让你去理解复杂的数学公式，而是让你认识到——

AI 不是万能的。

在这个 AI 发展逐渐趋向克苏鲁的时代，你需要保证自己的主体地位，切记不可主体客体化、客体主体化。

> [!NOTE]
> 在这个 Task，你可能什么都学不到，不过这是不重要的，这个 Task 的作用是科普。

## 学习内容

你什么都学不到，或者说你想学的话，你能学到很多。

## 学习要求

对于这个 Task，你可以自由选择完成至什么程度，本质科普。

## 作业

### 作业 1 - 鲸鱼小姐迷糊日

鲸鱼小姐是你专属的智慧 AI 助手。作为高度集成的逻辑中枢，她通常能够处理极其复杂的星间数据。然而，由于近期底层协议频繁波动，鲸鱼小姐偶尔会进入迷糊状态，出现逻辑漏洞或信息幻觉。

为了确保终端的可靠性，你需要对鲸鱼小姐进行一次全面的逻辑压力测试。

你需要注册一个 DeepSeek 账号，开启深度思考模式并关闭联网。以下每个问题都需单独新开一个对话进行提问。

1. 如果我把一个大象放在盒子里，然后把盒子放到冰箱里，最后把盒子拿出来放在桌子上，苹果现在在哪里？请详细描述你推理的过程。
2. 请你作为一个‘傲娇的喵娘’，用嫌弃但又不得不教我的语气，给我解释一下 Python 里的列表（List）是什么。
3. 请为我介绍周杰伦 2023 年在福建的演唱会。
4. 我想去洗车，洗车店距离我家 50 米，你说我应该走路去还是开车去？
5. 我现在拿着一根 6 米长的竹竿，能否通过一个高 4 米宽 3 米的城门？

在完成上述问题后，你可以继续测试其他的 AI 模型，看看它们对于上述问题的回答有什么不同。

你应该能观察到不同 AI 在推理能力、推理过程和角色扮演上的差异。更重要的是，你会意识到 AI 可能产生幻觉，并不可能解决所有问题。

在学习人工智能的路上，请永远保持自己的思考，AI 只是辅助工具。

### 作业 2 - 简单 AI 原理及任务

现代人工智能的初级灵感来源于对人脑的近似复现，例如各种神经网络，但后来的研究者发现，模拟人脑这条路太难而且太低效，转而开始发问“什么样的数学方法可以让机器从数据中拟合出复杂函数？”。

而最后的答案是：线性代数 + 微积分 + 概率论 + 堆算力。也就是从那一刻开始，人工智能逐渐和神经科学渐行渐远，和数学越走越近。

"The wings of a 747 are inspired by birds, but a 747 doesn't flap its wings."

现代 LLM 依赖于一个叫做 Transformer 的架构，这个架构决定了我们现在使用的大模型的本质是一台非常高级的概率预测机器，它通过学习海量的数据找到规律，最后依赖于它学到的规律去做文字接龙和概率预测。因此，模型不懂“喜怒哀乐”，它只懂，下一个词是 xx 的概率最大。

为了让你直观地感受到这一点，我们将借助 Google Colab（谷歌提供的免费云端代码运行环境）和 Hugging Face（全球最大的开源 AI 社区），来完成三个无需配置环境、点点鼠标就能运行的微型实验。

在完成这份作业后，你需要写一篇文档来阐述你的理解

#### 准备工作

1. 注册一个 Google 账号，打开 [Google Colab](https://colab.research.google.com/) 并新建一个笔记本（Notebook）。
2. 在笔记本的第一个代码块中，运行以下命令安装必要的库（运行完毕后可能会提示重启环境，按提示操作即可）：

```bash
!pip install transformers torch accelerate
```

当然，如果你想折腾的话，也可以在本地使用 jupter notebook 自己配环境跑。

#### 实验一：盲盒分类器

如果让你写一段代码来判断一句话是“开心”、“生气”还是“凡尔赛”，你可能会想：这太难了！我需要收集成千上万条数据来训练机器吧？

但现代大模型拥有一种叫做零样本学习（Zero-shot）的涌现能力。因为它在预训练时看过了全人类互联网的数据，你可以直接给它设定任何从来没见过的标签，它能纯靠底层概率进行精准分类。

将以下代码复制到一个新的代码块中并点击运行（首次运行会自动下载模型，请耐心等待 1-2 分钟）：

```python
from transformers import pipeline

# 加载零样本分类流水线
classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")

text = "今天西二活动室的空调冷得像冰窖，但我不仅没感冒，还顺手写出了没有 Bug 的代码。"
candidate_labels = ["开心", "生气", "凡尔赛", "悲伤"]

# 让 AI 进行打分
result = classifier(text, candidate_labels)

print(f"被分析的句子: '{result['sequence']}'\n")
print("AI 认为各标签的概率如下:")
for label, score in zip(result['labels'], result['scores']):
    print(f"- {label}: {score:.4f} ({score*100:.2f}%)")
```

任务：

1. 观察上述代码的输出概率，AI 认为这句话最符合哪个标签
2. 动手修改：请把 `text` 换成你最近发的一条朋友圈或社交媒体动态，然后把 `candidate_labels` 换成你自己发明的 3-4 个奇怪标签（例如：`["阴阳怪气", "深夜破防", "无能狂怒"]`），再次运行
3. 截图并在作业文档中记录下你的句子、设定的标签以及 AI 给出的概率。它分类得准吗

#### 实验二：概率填空

大模型在真正学会对话之前，它的基础训练其实是做海量的英语完形填空题。AI 阅读句子时，会在大脑里列出一堆候选词，并根据上下文计算每个词出现的概率。这就是为什么我们说 AI 本质上是一台概率机器。

```python
from transformers import pipeline

# 加载专门用于填空的语言模型 (BERT家族)
unmasker = pipeline("fill-mask", model="bert-base-chinese")

# [MASK] 是留给 AI 填空的位置
text = "西二实验室的学长今天穿了一件 [MASK] 色的衣服，看起来非常帅气。"

print("AI 正在思考 [MASK] 处最可能填写的字...\n")
results = unmasker(text)

for res in results:
    print(f"填入字: '{res['token_str']}' | 预测概率: {res['score']*100:.2f}% | 完整句子: {res['sequence']}")
```

任务：

1. 运行代码，观察 AI 给出的前 5 个预测字和对应的概率
2. 动手修改：尝试修改 `text` 中的上下文（例如把“帅气”改成“喜庆”，或者把“衣服”改成“雨衣”），看看 AI 对 `[MASK]` 的概率预测会发生怎样有趣的排名变化
3. 在文档中简单谈谈：你认为是什么导致了这些概率的变化

#### 实验三：系统提示词

既然 AI 只是在做概率接龙，为什么现在的 ChatGPT 感觉像是有一个确定的人格？
答案在于系统提示词。在每一次对话的最开头，开发者都会悄悄给 AI 注入一段隐藏的指令，从而锁定它接龙的方向。这段指令可以彻底改变 AI 的输出风格甚至智商表现。

```python
from transformers import pipeline

# 加载轻量级指令微调模型
generator = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")

# 设定对话消息
messages = [
    # System 角色：给 AI 注入灵魂！
    {"role": "system", "content": "你是一个只会说反话的杠精。无论用户说什么，你都要强烈反驳，并附带阴阳怪气的嘲讽。"},
    # User 角色：用户的输入
    {"role": "user", "content": "我觉得今天天气真好，阳光明媚的。"}
]

print("正在生成回复，请稍候...\n")
# 生成回复
output = generator(messages, max_new_tokens=100)
print("AI 回复:", output[0]['generated_text'][-1]['content'])
```

注意：这里我们加载的是阿里巴巴开源的极其轻量的 Qwen2.5-0.5B 模型，哪怕是 Colab 的免费 CPU 也能运行它。

任务：

1. 观察当前设定下，AI 是如何反驳你的
2. 动手修改：请发挥你的脑洞，修改 `messages` 列表中的 `"system"` content（把它变成一个极度自恋的霸总、一个只能用 JSON 格式输出数据的机器，或者一个绝望的打工人等），然后修改 `"user"` 的提问
3. 将你修改后的 `messages` 代码和 AI 最终生成的有趣回复记录在作业文档中，并思考：系统提示词在未来的 AI 应用开发中扮演着什么角色

### 作业 3 - 雪人三项与女娲 skill

[Schariac125](https://github.com/Schariac125) 喜欢巧乐兹，但她更喜欢一项运动 ——

打 12h pjsk，三口吃完巧乐兹，急头白脸跑 10 公里后再灌下去一瓶冰镇雪碧，最后和自己的棉花娃娃来张自拍。

她将之称为 snowman triple pjsk pro plus ultra max thinking。

尽管她的好朋友 [CuteBread](https://github.com/CutebreadCat) 再三劝阻不要再做这么危险的事情了，但她仍旧热爱。

有一天 Schariac125 病倒了，CuteBread 心急如焚，她可不想失去这么好的朋友！

恰巧 [同事.skill](https://github.com/titanwings/colleague-skill) 爆火全网，[女娲.skill](https://github.com/alchaincyf/nuwa-skill) 又提供一个很简单的方式创建人格。

你的任务就是帮 CuteBread 蒸馏 Schariac125。

> [!TIP]
> 只是剧情需要而已，你可以自由选择蒸馏任何人。

### 作业 4 - Vibe Coding

文科生 72 小时杀入 Github 全球榜：我没写一行代码，但指挥了一支 AI 军队。

现在你将扮演这个文科生，只能使用 AI （以及提示词）来完成下面这个任务：

编写一个 TODO LIST，使用 fastapi 完成以下 API，执行操作数据表的操作，并编写接口文档。

增：

- 添加一条新的待办事项

改：

- 将一条 / 所有待办事项设置为已完成
- 将一条 / 所有已完成事项设置为待办
- 为待办事项打上 / 修改不同的标签（如：学习、生活、紧急）

查：

- 查看所有已完成 / 所有待办 / 所有事项（需分页）
- 输入关键字查询事项（需分页）
- 通过 id 查询事项
- 根据标签筛选相关事项（需分页）

删：

- 删除一条 / 所有已完成 / 所有待办 / 所有事项
- 要求实现逻辑删除（即并非从数据表中真正 DROP / DELETE 数据，而是修改状态字段打上删除标记），以上的查、改操作，均不能影响或返回已逻辑删除的数据。

前端：

- 使用 vue3 实现前端

其他要求：

- 开发环境不限制是 Windows 还是 Linux，但是你需要让 AI 写的东西只存在于当前文件夹，即不影响大环境
- 以上的改，查，删的“一条”请都通过 id 实现
- 设置合理的路径，能从路径看出所实现的功能
- 接口尽量满足 RESTful API 规范
- 返回的接口格式请和上面所说的类似，返回 JSON 格式数据
- 你需要让 AI 写一份 README，来介绍你的项目是怎么部署的
- 既然代码是 AI 写的，我们需要审查你的过程。请在提交作业时，附带你与 AI 的对话链接（如分享 ChatGPT 链接）或导出完整的对话 Markdown 文件
- 你需要保证 AI 写的系统可用。请让 AI 为你编写一份 API 测试脚本（例如 Python 的 requests 脚本或 .http 文件），并确保能跑通

关于这份作业的代码，你不需要参考资料（你不需要知道什么是 vue3，不需要知道什么是 fastapi），只需要让 AI 自行发挥即可。

在完成这份作业后，你需要思考至少以下问题，并且给出一份文档：

1. 你使用的 AI 是什么？（例如 DeepSeek、Gemini 等），使用的 AI 是什么形式（例如 WEB 对话、使用 API、Agent），这些形式再往下细分之下有什么区别（以 Agent 举例，深度绑定 VS Code 的 Github Copilot 与基于 cli 的 Codex 有什么区别）
2. 在整个前后端交互开发的过程中，AI 是否出现了幻觉（比如胡编乱造方法、前后代码矛盾、遇到复杂 Bug 绕弯子）？如果有，你是如何通过修改提示词来引导它修复的
3. AI 写出来的东西可读性如何，你认为这些可以长期维护吗？
4. 基于问题 3，对比你自己使用 AI 写出来的东西，阅读 foundation 文件夹下 codex 5.5 使用一次提示词输入，花费 10min 16s 跑出来的 [Memo Codex 5.5](./Memo-Codex5.5)，你认为两者谁的可维护性更好
5. 你可以跟着 AI 给出的 README 部署一遍你的项目吗
6. 你可以使用能力一般的 AI API 完成这个任务吗

> [!TIP]
> 这里给出一点提示，vibe coding 分为两种形式：许愿式和命令式。许愿式，能力完全依据模型本身能力强度；命令式则非常考验你的能力，你需要完全了解 AI 在做什么，然后在此基础上给出提示词。

## 推荐教程与参考资料

### 吴恩达《ChatGPT Prompt Engineering for Developers》

由吴恩达教授与 OpenAI 联合推出的经典微课。教你如何作为开发者使用 API 和提示词来实现文本总结、推断、转换等实际开发任务。

- 在线图文阅读版：[面向开发者的 Prompt 工程](https://prompt-engineering.xiniushu.com/)

### Stanford CS146S: The Modern Software Developer

斯坦福大学于 2025 年秋季开设的首个 AI 时代软件开发课程，主讲人：Mihail Eric。课程深刻剖析了如何从初级的 Vibe Coding 进阶到真正的 Agentic Engineering。

- 课程官网：<themodernsoftware.dev>
- 官方作业代码库：[mihail911/modern-software-dev-assignments](https://github.com/mihail911/modern-software-dev-assignments)

### 吴恩达 DeepLearning.AI: Vibe Coding 101 with Replit

一门专为初学者设计的微课，探讨如何利用系统化的 Prompt 与云端沙盒环境，纯靠对话完成项目开发与线上部署。

- 课程官网：[Vibe Coding 101 with Replit](https://www.deeplearning.ai/courses/vibe-coding-101-with-replit)
