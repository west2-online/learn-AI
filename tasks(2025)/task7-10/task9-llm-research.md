# Task 9：LLM-Research

## 学习内容

本阶段将聚焦于对齐与评估这两大前沿核心，理解它们如何塑造了我们今天所用的 LLM。

- 经典对齐范式
  - `RLHF（InstructGPT）`：深入理解 `RLHF`（基于人类反馈的强化学习）的三阶段流程：
    1. SFT（监督微调）：教会模型模仿人类高质量的回答
    2. Reward Modeling（RM）：教会一个奖励模型去理解人类的偏好（哪个回答更好？）
    3. RL（PPO）：用强化学习让主模型在奖励模型的打分下，优化输出质量
- 现代对齐范式
  - `DPO`：理解 `RLHF` 流程（尤其是第三阶段 PPO）的复杂性与不稳定性。学习 `DPO`（直接偏好优化）是如何巧妙地绕过训练一个单独的奖励模型和复杂的强化学习这两步，用一个简单的分类损失函数直接在偏好数据上进行优化的
- 整体性评估
  - `HELM`：理解为什么 BERT 时代的 `GLUE` / `SuperGLUE` 基准已经不足以评估现代 LLM。学习 `HELM`（整体性评估）的核心思想：
    1. Holistic（整体性）：不再只看准确率，而是同时评估 7 个指标（准确性、校准度、鲁棒性、公平性、偏见、毒性等）
    2. Scenarios（广覆盖）：不再是几个小任务，而是覆盖 42 个不同的场景
    3. Standardization（标准化）：用统一的方法去测试所有模型（包括开放和闭源的）

## 推荐教程

这是定义 AI 对齐与评估时代的论文，它们决定了我们今天使用的 ChatGPT 和 Llama 3 为什么是安全的和有用的。

- [RLHF]："Training language models to follow instructions with human feedback"（Ouyang et al., 2022 - *InstructGPT 论文*）
  - [点击搜索论文（Google Search）](https://www.google.com/search?q=Training+language+models+to+follow+instructions+with+human+feedback+paper)
- [DPO]："Direct Preference Optimization: Your Language Model is Secretly a Reward Model"（Rafailov et al., 2023）
  - [点击搜索论文（Google Search）](https://www.google.com/search?q=Direct+Preference+Optimization:+Your+Language+Model+is+Secretly+a+Reward+Model+paper)
- [HELM]："Holistic Evaluation of Language Models"（Liang et al., 2022）
  - [点击搜索论文（Google Search）](https://www.google.com/search?q=HELM:+Holistic+Evaluation+of+Language+Models+paper)

## 作业

你的任务是撰写一份阐明对齐与评估技术演进的思想报告。

### 作业要求

1. 提交形式：
   - 一份 Markdown 报告（或 Jupyter Notebook），清晰地阐述你的分析
2. 核心内容：
   - 你需要串联阅读上述 3 篇论文，并回答以下几个核心问题：
   - [为何需要 RLHF？]
     - 在 `RLHF` 论文出现之前，像 `GPT-3`（Task 8 论文）这样的预训练模型存在哪些严重的未对齐问题？
     - `RLHF` 的三阶段流程（SFT、RM、PPO）各自是为了解决什么问题？
   - [为何需要 DPO？]
     - `RLHF` 既然如此成功（诞生了 ChatGPT），为什么研究者还要发明 `DPO`？`RLHF`（尤其是 PPO 阶段）有哪些公认的困难和缺陷？
     - `DPO` 最重要的洞察是什么？（提示：它如何绕过了 RM 和 RL）
   - [为何需要 HELM？]
     - 为什么我们不能用 Task 8 里的 `BERT` 时代的基准（如 GLUE）来评估 `GPT-3` 或 `InstructGPT`？
     - `HELM` 强调的 Holistic（整体性）具体体现在哪些方面？（提示：多指标、多场景）
   - [综合思考]
     - 你认为对齐（Alignment - RLHF/DPO）和评估（Evaluation - HELM）之间是什么关系？
     - 如果我们只有强大的对齐技术，却没有公正的评估；或者反过来，我们只有公正的评估，却没有有效的对齐技术，这两种情况分别会导致什么后果？
