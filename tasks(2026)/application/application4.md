# Application 4 - Agent

> [!NOTE]
> 预计耗时：60 天

## 学习目的

从 Application 1 开始，我们逐渐理解了当下 AI 应用的方方面面，从作业 1 的视觉和语音应用，再到作业 2 和作业 3 的大模型应用。

在作业 3 中，我们要求你使用 LangChain 去搭建一个 RAG demo 与虚拟伴侣，其目的是为了熟悉 LangChain 和 RAG 这两项技术，这在本次作业中将会发挥巨大的作用。

本次作业聚焦于 Agent，或者更准确的说，聚焦于 Harness 。Agent 的本质是 LLM + Harness。而 Harness 的构建是一项值得去研究的课题，经过前面和接下来的学习，我们希望你拥有设计 Harness 架构的能力并能够将你的想法落地去完成一项自由发挥的大作品。

## 学习内容

- Agent

## 作业

### 作业 1 - Agent Learning

#### Potato Code

Claude Code 是 Anthropic 公司推出的一款面向开发者的智能编程助手，在一次“意外”中被迫开源。

[learn-claude-code](https://github.com/shareAI-lab/learn-claude-code/blob/main/README-zh.md) 是一个学习 Claude Code 的项目，旨在从 0 构建自己的 Agent。

你需要学习 learn-claude-code 的 s01 到 s04。

#### Potato Code Pro

Potato Code 的能力明显不足以满足天才程序员的 Coding 需求了，所以我们需要一个更加强大的智能编程助手，Potato Code Pro！

你需要学习 learn-claude-code 的 s05 到 s11。

#### Potato Code Ultra

在和低调的黑客笑面佛战斗 500 回合后，天才程序员的 Potato Code Pro 终于被斩于马下。

一刻都没有为 Potato Code Pro 的死亡哀悼，立刻赶到战场的是 Potato Code Ultra！

你需要学习 learn-claude-code 的 s12 到 s20。

#### 学习要求

- 学习 learn-claude-code 的 s01 到 s20 的内容。
- learn-claude-code 出于教学目的，其代码是采用单脚本形式，在实际工程中并不能这样做，因此你需要思考如何拆分各模块使其代码的更便于维护。
- 我们并不要求你去跟着教程实现一个 claude-code demo，而是希望你去理解现代 agent 架构的构建思路。

### 作业 2 - 好玩的东西 Plus

你知道的，猫娘是一种软乎乎的、可爱的生物，但她们太久没有收到好玩的东西了。

于是她们对你发起了哈气，并化身脊背龙形态。

你的任务是自行设计并完成一个有关 Agent 的项目来安抚她们，该项目可以综合考核内你学到的一切东西进行设计。在最后的答辩中，你需要详细介绍一下你设计的好玩的东西。

你需要自己亲自动脑思考，根据你的所学设计一个 Agent 架构，无论架构优秀与否，我们都希望你能够大胆将其落地。

我们并不对细节进行要求，你可以用任何语言，任何框架，任何技术栈去实现它。我们更在意的是你在大作品中的思考，例如你遇到了什么问题，最后你又是如何解决的。

但鉴于我们前面学习的内容，我们更推荐你使用 Python + LangChain / LangGraph

当然，既然你已经有能力学到这里了，应该知道一个合格的项目是不能像上面的学习版教程一样把所有代码都塞到一个文件里的。

你可能需要一个 idea，但 idea 不是那么容易就有的。

所以以下有几个思路供你参考：

#### 多 Agent 协同长篇小说创作

底线要求：

1. 多 Agent 协同要求在这个项目中需要有多个 Agent 共同工作，而不是单个 Agent 的工作
2. 实现对设定一致性的约束

#### Agent 游戏陪玩

底线要求：

1. Agent 需具备多模态功能，能够获取实时游戏信息
2. 实时聊天陪伴，高光操作赞美，战后安慰、评价等

#### 多 Agent 狼人杀博弈

底线要求：

1. 具备语音功能，即在发言阶段实时聊天。
2. 至少实现预言家、女巫、狼人与平民四种角色，且有 1 个预言家，1 个女巫，2 个狼人，2 个平民。神（即预言家、女巫）获胜条件为投票出所有狼人，狼人获胜条件为杀死所有神或平明（即屠边）。
3. 在 2 的基础上，可进入 x 名玩家与 y 名 agent，其中 x 与 y 为正整数，且 x+y=6。
4. 如果你精通狼人杀规则，可以在 2 与 3 的基础上进行扩展。

#### Bonus

实际业务中用到的 Agent 是非常复杂的，需要更加深入的去学习 Agent 相关技术以及一些更深入的概念，而针对这些，我们提供了一些资料供你参考。这部分并不做任何要求。

1. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) 目前所有 Agent 框架祖师爷级的论文。

2. [CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society](https://arxiv.org/abs/2303.17760)

3. [AutoGen](https://github.com/microsoft/autogen) 2 和 3 都是关于多智能体的相关资料

4. [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)

5. [mem0](https://github.com/mem0ai/mem0) 一个有关于上下文工程的项目。
