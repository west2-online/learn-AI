# Task 9：LLM-Research

## **学习目的：从强大到可控与可知**

你在 Task 8 中，已经见证了那些创世神话—— `BERT` 如何定义了范式，`GPT` 如何带来了涌现。你得到了一个无比**强大**的魔法引擎。

然而，一个只懂续写文本、无法控制的引擎，是危险的。它可能会说谎、会伤人、会答非所问。它拥有智力，却没有灵魂。

**Task 9，就是为这个强大的引擎注入灵魂并校准罗盘的终极试炼！**

此阶段的学习目的，是让你从模型的使用者一跃成为灵魂的工程师和公正的裁决者：

* **理解对齐（Alignment）的圣杯**:你将深入探索 AI 领域最核心的议题——对齐。你将学习经典的 `RLHF` 是如何通过一个复杂的三阶段流程（SFT -> RM -> PPO），将一个原始的 GPT-3 驯化成乐于助人、人畜无害的 InstructGPT（ChatGPT 的前身）的。
* **掌握对齐的进化**：你将见证思想的演进。在理解了 `RLHF` 的强大与复杂之后，你将学习 `DPO` 是如何用一个惊艳的、更简单、更稳定的直接优化框架，来**革新** `RLHF` 的。
* **铸造标尺（Evaluation）**：有了驯化的方法还不够，你怎么知道谁驯化得更好？你将学习 `HELM` 这种整体性评估框架，是如何**取代**那些过时的小考场（如 GLUE），成为衡量一个现代大模型综合素质（准确性、公平性、鲁棒性、偏见等）的魔法竞技场的。

完成本轮，你将真正理解 AI 安全与对齐的深刻含义，这正是 LLM 科研皇冠上的明珠。

---

## 学习内容：灵魂的注入与标尺的铸造

本阶段将聚焦于对齐与评估这两大前沿核心,理解它们如何塑造了我们今天所用的 LLM。

* **经典对齐范式（The Classic）**

  * **`RLHF（InstructGPT）`**：深入理解 `RLHF`（基于人类反馈的强化学习）著名的**三阶段流程**：

    1. **SFT（监督微调）**：教会模型模仿人类高质量的回答。
    2. **Reward Modeling（RM）**：教会一个裁判模型去理解人类的偏好（哪个回答更好？）。
    3. **RL（PPO）**：用强化学习去钻空子，让主模型在裁判的打分下，刷出最高分。
* **现代对齐范式（The Evolution）**

  * **`DPO`**：理解 `RLHF` 流程（尤其是第三阶段 PPO）的**复杂性与不稳定性**。学习 `DPO`（直接偏好优化）是如何巧妙地**绕过**训练一个单独的奖励模型和复杂的强化学习这两步，用一个简单的分类损失函数**直接在偏好数据上**进行优化的。
* **公正的标尺（The Benchmark）**

  * **`HELM`**：理解为什么 BERT 时代的 `GLUE` / `SuperGLUE` 基准已经**完全不足以**评估现代 LLM。学习 `HELM`（整体性评估）的**核心思想**：

    1. **Holistic（整体性）**：不再只看准确率，而是同时评估**7 个指标**（准确性、校准度、鲁棒性、公平性、偏见、毒性等）。
    2. **Scenarios（广覆盖）**：不再是几个小任务，而是覆盖**42 个**不同的场景。
    3. **Standardization（标准化）**：用统一的方法去测试所有模型（包括开放和闭源的）。

---

## 推荐教程：原文（The Papers）

这是定义 AI 对齐与评估时代的论文，它们决定了我们今天使用的 ChatGPT 和 Llama 3 为什么是安全的和有用的。

* **[RLHF]**：**"Training language models to follow instructions with human feedback"**（Ouyang et al.、2022 - *InstructGPT 论文*）

  * [点击搜索论文（Google Search）](https://www.google.com/search?q=Training+language+models+to+follow+instructions+with+human+feedback+paper)
* **[DPO]**：**"Direct Preference Optimization: Your Language Model is Secretly a Reward Model"**（Rafailov et al.、2023）

  * [点击搜索论文（Google Search）](https://www.google.com/search?q=Direct+Preference+Optimization:+Your+Language+Model+is+Secretly+a+Reward+Model+paper)
* **[HELM]**：**"Holistic Evaluation of Language Models"**（Liang et al.、2022）

  * [点击搜索论文（Google Search）](https://www.google.com/search?q=HELM:+Holistic+Evaluation+of+Language+Models+paper)

---

## 作业：撰写你的 LLM 对齐与评估思想报告

你的任务是撰写一份阐明价值观与标尺的**思想演进报告**。

### **作业要求**

1. **提交形式**：

   * 一份 Markdown 报告（或 Jupyter Notebook），清晰地阐述你的分析。
2. **核心内容：连接思想的脉络**：

   * 你需要**串联**阅读上述 3 篇论文，并回答以下几个**核心问题**：
   * **[为何需要 RLHF？]**

     * 在 `RLHF` 论文出现之前，像 `GPT-3`（Task 8 论文）这样的预训练模型存在哪些严重的未对齐问题？
     * `RLHF` 的三阶段流程（SFT、RM、PPO）**各自**是为了解决什么问题？
   * **[为何需要 DPO？]**

     * `RLHF` 既然如此成功（诞生了 ChatGPT），为什么研究者还要发明 `DPO`？`RLHF`（尤其是 PPO 阶段）有哪些公认的**困难和缺陷**？
     * `DPO` 最天才的洞察是什么？（提示：它如何绕过了 RM 和 RL）
   * **[为何需要 HELM？]**

     * 为什么我们不能用 Task 8 里的 `BERT` 时代的基准（如 GLUE）来评估 `GPT-3` 或 `InstructGPT`？
     * `HELM` 强调的 Holistic（整体性）**具体**体现在哪些方面？（提示：多指标、多场景）。
   * **[综合思考]**

     * 你认为对齐（Alignment - RLHF/DPO）和评估（Evaluation - HELM）之间是什么关系？
     * 如果我们只有强大的对齐技术，却没有公正的评估；或者反过来，我们只有公正的评估，却没有有效的对齐技术... 这两种情况分别会导致什么后果？
