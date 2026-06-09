# Application 1 - 简单 AI 应用

> [!NOTE]
> 预计耗时：30 天

## 学习目的

首先需要说明，这里的应用指的是极为顶层的 AI 应用开发，几乎不涉及底层算法实现。手搓 CNN 训练图片识别模型这类工作不属于应用，而属于算法实现。

因此应用指的是工程化地使用 AI，把 AI 作为业务链条中的一环。比如本次作业 1，是调用大语言模型完成情感分析任务，而不是传统地训练一个情感分析器。

打一个通俗易懂的链条：

数学 -> Numpy 手算反向传播 -> Pytorch 自动推导反向传播 -> Transformer 库（Hugging Face 集成 Pytorch / TensorFlow，屏蔽底层细节，抽象出 Pipeline 的概念） -> Langchain / Dify 模块化集成（轻松调用工具） -> LLM API 屏蔽所有底层细节 -> AI 应用（调用 API 完成任务、聊天机器人、Agent 调用 API）

Application 的目的是要你站在最顶层的视角向下看，并且向下只最多接触到 Hugging Face。

从这里不难看出，AI 应用主要学习的是怎么使用 AI，而不是 AI 的底层原理。所以如果你选择了应用方向，你不只是学习 AI 调用，还需要学习后端、运维等方面的知识。

当前的 AI 应用开发主要围绕大语言模型展开。未来可能会有更多 AI 模型出现，应用开发形态也会更加多样化。

当然正如 [Task 4](../foundation/task4.md) 导引部分提到的一样，作为一个 211 的本科生，如果只拥有高级应用能力，会在就业市场上很吃亏。

所以建议学习这部分的前提是你已经掌握了一门其他语言，或者将来会去学习其他语言。

## 学习内容

- 简单底层理解
- 简单 API 调用（Open AI 格式）
- 简单 MCP
- 简单 Agent

## 作业

### 文档 1

大部分现代人工智能库已经提供了非常多高度封装的方法供开发者去调用，这些方法很好的屏蔽了底层的细节，使得开发者不用反复纠结于晦涩的数学公式推导，将精力放在实际的产品开发中。

但反复的实践已经证明了，只会调库其实是远远不够的，掌握部分底层相关的知识可以更好的帮助我们进行 AI 应用开发。

因此，本次的任务要求你阅读以下几份资料：

1. [Andrej Karpathy《Let's build GPT: from scratch, in code, spelled out.》](https://www.bilibili.com/video/BV1K4LPzLEoA/)

2. [nanoGPT](https://github.com/karpathy/nanoGPT)

3. [Schariac125 简单科普博客：自顶向下——可能要懂的底层原理简单讲解](https://schariac125.online/2026/05/31/%E8%87%AA%E9%A1%B6%E5%90%91%E4%B8%8B/)

4. （Bonus）论文 [Attention Is All You Need](https://arxiv.org/abs/1706.03762) 及其讲解视频 [Transformer 论文逐段精读【论文精读】跟李沐学 AI](https://www.bilibili.com/video/BV1pu411o7BE/?spm_id_from=333.337.search-card.all.click)

完成上述任务后，你需要写一篇文档来阐述你的理解。

> [!NOTE]
> 如果你对 Pytorch 感兴趣的话，以下是推荐你可以去阅读和完成的资料和任务，这些并不做强制性要求。
>
>1. [Pytorch 官方文档](https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
>
>2. [pytorch-deep-learning](https://github.com/mrdbourke/pytorch-deep-learning)
>
>3. 基于 mnist 数据集的 CNN 图像分类任务（资料太多了，自己找去吧）
>
>4. [Cassava Leaf Disease Classification](https://www.kaggle.com/competitions/cassava-leaf-disease-classification/overview)
>
>5. [Global Wheat Detection](https://www.kaggle.com/competitions/global-wheat-detection)
>
> 一般而言并不建议初学者一上来就去阅读 Pytorch 官方文档，你可以从 pytorch-deep-learning 项目开始做起一步步学会使用 Pytorch。

### 文档 2

阅读 [停止用 Windows 工作](https://zhuanlan.zhihu.com/p/2024527609388627701?share_code=14xesITQCN5Vm&utm_psn=2045213199549609466)。

### 作业 1 - 橘雪莉妙妙屋

橘雪莉是《魔法少女的魔女审判》中的登场角色。自称侦探的少女，笑容满面，性格奔放，对有意思的事情会毫不犹豫扑上去。

现在她潜入了一个 QQ 群，想要分析群成员的情绪，判断群友当前的状态。

分析某个群友的 x 条信息后（x 可由你定义，也可由 AI 自行判断），她要发送表情包来回应这个群友的状态。

如果群友是开心的，那么她就发送标签为“开心”的表情包；如果群友是难过的，那么她就发送标签为“难过”的表情包。

恰好，智谱在开源方面有很大贡献。她拜托你访问 [智谱 AI 开放平台](https://open.bigmodel.cn/) 官网，注册账号并申请密钥（密钥不可泄露，你也不想你的 token 被橘雪莉吃掉吧），然后调用 GLM 4.0 完成这个任务：

对 x 句话（或表情、图片）进行分析后，输出一个心情标签，并根据该标签从已打好标签的表情包中随机发送。

你需要阅读 GLM 4.0 文档，仅调用 API，并通过提示词完成句子的情感分析。情感类别限制为“开心”“难过”“愤怒”“中性”。

需要注意的是，GLM 的输出只能是你定义的词汇之一。如果输出了其他内容，说明你的提示词设计不合理，需要进行修改。

#### 作业要求 - 作业 1

- 使用具有视觉能力的模型完成文本和表情包的分析。
- 设计合理的提示词，确保模型输出符合预期的情感标签。
- 使用 openai 模块调用 GLM API。
- 务必使用 .gitignore 文件保护你的密钥，避免泄露。
- （Bonus）使用 uv 管理项目依赖和运行环境。

> [!NOTE]
> 你可以自由使用喜欢的 API，不一定非要使用 GLM，但是请确保你使用的 API 具有视觉能力。

### 作业 2 - 自动调课

众所周知，福大放假会发调课通知，但课表却从不跟着改。每次一调休，课表上的安排全乱了，非常糟糕。

我们强大的课表 APP 福 uu 可以对课表使用调课规则，但是调课通知不是结构化的，无法直接输入到福 uu 中。LLM 具有强大的文本泛化能力，福 uu 的开发者们想到了一个办法，就是让 LLM 来解析调课通知，将调课通知转换成结构化的调课规则。

现在你需要实现一个调课通知解析器，将你在 [Foundation Task 2](../foundation/task2.md) 中爬取并单独提取的调课通知 csv 内所有的通知转换成结构化的调课规则。

调课规则的格式如下：

```json
[
  {
    "from_date": "2026-01-02",  // 原定上课日期
    "to_date": "2026-01-04"     // 调课后上课日期
  },
  {
    "from_date": "2026-01-03",
    "to_date": ""               // 空表示不上课
  }
]
```

#### 参考资料 - 作业 2

[宝硕博客：LLM 工程化在福 uu 中的落地实践 —— 假期调课的智能解析](https://blog.baoshuo.ren/post/fzuhelper-llm-as-function/)

#### 作业要求 - 作业 2

- 设计合理的提示词，确保模型能够正确解析调课通知。
- 使用 openai 模块调用 API，选择合适的模型。
- 必须使用 uv 管理项目依赖和运行环境。
- 校验模型输出的调课规则是否符合预期格式。
- 使用在之前任务爬取的教务通知验证你的解析器，确保它能够正确解析调课通知。

### 作业 3 - Potato Code

Claude Code 是 Anthropic 公司推出的一款面向开发者的智能编程助手，在一次“意外”中被迫开源。

[learn-claude-code](https://github.com/shareAI-lab/learn-claude-code/blob/main/README-zh.md) 是一个学习 Claude Code 的项目，旨在从 0 构建自己的 Agent。

你需要学习 learn-claude-code 的 s01 到 s04，完成一个简单的 Agent。

#### 作业要求 - 作业 3

- 学习 learn-claude-code 的 s01 到 s04 的内容。
- 你需要自己编写一个简单的 Agent，并且覆盖 s01 到 s04 中的所有功能。
- 使用 anthropic 模块调用 API，选择合适的模型。
- 你需要有清晰的项目结构，而不是像 learn-claude-code 的单脚本应用。
- 必须使用 uv 管理项目依赖和运行环境。
