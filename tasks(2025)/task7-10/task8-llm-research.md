# Task 8：LLM-Research

## 学习目的

你已经在 Task 7 中初步接触了 Hugging Face 和 LangChain 生态，这些是当今大语言模型应用的标准工具。然而，仅仅掌握工具的使用并不足以深入理解大语言模型技术的本质。

本阶段的学习目标是理解现代大语言模型技术的演进脉络，通过研读经典论文，掌握核心思想的演化过程。

- **追本溯源，构建知识体系**：通过阅读奠基性论文，理解现代大语言模型技术的发展历程
- **理解技术演进规律**：当前的高级技术都是在前人工作基础上的创新。LoRA 是对 BERT 微调范式的改进；RAG 是对 GPT 知识局限的补充；Agent 则是对 GPT 的 ICL 能力的应用
- **建立系统性思维**：完成本阶段学习后，你将建立清晰的概念框架。面对新的技术（如 DPO、Mamba）时，能够快速定位其在技术谱系中的位置，理解其解决的问题和继承的思想

## 学习内容

本阶段将通过研读现代大语言模型领域的核心论文，理解技术演进的内在逻辑。

### 预训练-微调范式

**BERT**：理解双向 Transformer、Masked Language Model（MLM）以及其如何定义了 Pre-train、Fine-tune 这个范式。这是所有微调思想的起点。

### 生成与涌现能力

**GPT-2/3**：深入理解自回归生成模型的潜力，以及当模型规模跨越某个阈值后，上下文学习（In-Context Learning、ICL）和 Few-Shot 能力的涌现。这是所有 Agent 能够思考和理解指令的根本前提。

### 参数高效微调

**LoRA**：针对 GPT-3 这样大规模模型无法全量微调的问题，学习 LoRA 如何通过低秩适应的数学技巧，实现了参数高效微调（PEFT）。这是对 BERT 微调范式在大模型时代的改进。

### 检索增强生成

**RAG**：针对 GPT-3 知识会过时和产生幻觉的问题，学习 RAG 如何将参数化知识（模型记忆）与非参数化知识（外部数据库）结合起来。这是解决幻觉问题的核心工程思想。

### 推理与行动

**ReAct（Agent）**：学习 ReAct 框架如何利用 GPT-3 强大的 ICL 能力，让模型学会 Reason（思考）和 Act（行动）的交错循环，从而将聊天模型转变为能使用工具、解决问题的智能代理。

## 推荐教程

本阶段的学习资料为奠基性论文，建议至少阅读论文的摘要（Abstract）、引言（Introduction）和结论（Conclusion）部分。

- **BERT**: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" (Devlin et al., 2018) [搜索论文](https://www.google.com/search?q=BERT:+Pre-training+of+Deep+Bidirectional+Transformers+for+Language+Understanding+paper)
- **GPT-3**: "Language Models are Few-Shot Learners" (Brown et al., 2020) [搜索论文](https://www.google.com/search?q=Language+Models+are+Few-Shot+Learners+GPT-3+paper)
- **LoRA**: "LoRA: Low-Rank Adaptation of Large Language Models" (Hu et al., 2021) [搜索论文](https://www.google.com/search?q=LoRA:+Low-Rank+Adaptation+of+Large+Language+Models+paper)
- **RAG**: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al., 2020) [搜索论文](https://www.google.com/search?q=Retrieval-Augmented+Generation+for+Knowledge-Intensive+NLP+Tasks+paper)
- **ReAct**: "ReAct: Synergizing Reasoning and Acting in Language Models" (Yao et al., 2022) [搜索论文](https://www.google.com/search?q=ReAct:+Synergizing+Reasoning+and+Acting+in+Language+Models+paper)

## 作业

### 论文研读报告

1. **提交形式**

以 Markdown 或 Jupyter Notebook 形式提交分析报告

2. **核心内容**

通过研读上述 5 篇（或更多）论文，回答以下核心问题：

- **BERT -> LoRA**
  - BERT 确立的 Pre-train、Fine-tune 范式是什么
  - 为什么当 GPT-3 出现后，BERT 的全量微调范式会失效
  - LoRA 是如何继承了微调思想，又如何革新了它以适应大模型时代的

- **GPT -> RAG**
  - GPT-3 强大的生成能力背后，暴露了哪些缺陷（如幻觉、知识过时）
  - RAG 是如何通过检索来补充这些缺陷的。它的核心思想（参数化 vs 非参数化知识）是什么

- **GPT -> ReAct**
  - GPT-3 论文中揭示的涌现能力是什么（提示：ICL / Few-Shot）
  - ReAct 框架是如何利用这种能力，让模型从一个回答者转变为一个执行者的
