# Task 8：LLM-Research

## **学习目的：从调用到洞察**

你已经在 Task 7 中初步接触了 Hugging Face 和 LangChain 生态，它们是当今 LLM 应用的标准套件。然而，你是否曾想过：

* 为什么 `LoRA` 会成为微调的标配？它解决了什么根本问题？
* 为什么 `RAG` 是一个如此天才的设计？它诞生于怎样的历史局限？
* 为什么 `Agent` 能思考和行动？它依赖于大模型怎样的涌现能力？

如果你在应用路线上感到知其然，而不知其所以然，那么 **Task 8 的科研路线，就是为你铸魂的时刻！**

此阶段的学习目的，是让你**停止追逐工具，开始理解思想**。你将沿着 `BERT -> GPT -> LoRA -> RAG -> ReAct` 这条黄金族谱，进行一次思想考古。

* **追本溯源，构筑你的思想族谱**：你将亲身回到那些神话诞生的时刻，阅读那些定义了现代 LLM 范式的奠基之作。
* **理解演化而非突变**：你将洞察到，今天我们所用的一切高级技巧，都不是凭空出现的。LoRA 是对 BERT 微调范式的精妙改良；RAG 是对 GPT 知识局限的完美补完；Agent 则是对 GPT 的 ICL 能力的极致挖掘。
* **从工具使用者到思想布道者**：完成本轮试炼，你将拥有一个清晰的概念地图。当你再次面对新的技术（如 DPO、Mamba）时，你将不再是盲目跟风，而是能迅速定位它在整个族谱中的位置，理解它解决了什么以及继承了什么。

这是成为一名真正 AI 架构师和研究者的必经之路。

---

## 学习内容：LLM 黄金时代的思想族谱

本阶段将聚焦于串联起现代 LLM 应用背后的核心论文，理解它们之间的传承与革新。

* **预训练-微调范式的确立（The Paradigm）**

  * **`BERT`**：理解双向 Transformer、Masked Language Model（MLM）以及它如何**定义了 Pre-train、Fine-tune 这个黄金范式**。这是所有微调思想的起点。
* **生成与涌现的奇点（The Singularity）**

  * **`GPT-2/3`**：洞察自回归生成模型的潜力，以及当模型规模跨越某个阈值后，**上下文学习（In-Context Learning、ICL）** 和 Few-Shot 能力的惊人**涌现**。这是所有 Agent 能够思考和听懂指令的根本前提。
* **大象的轻盈舞蹈（The Adaptation）**

  * **`LoRA`**：针对 GPT-3 这样大到无法微调的困境，学习 LoRA 是如何通过低秩适应的精妙数学技巧，实现了**参数高效微调（PEFT）**。这是对 BERT 微调范式在大模型时代的伟大继承。
* **大脑与书架的结合（The Augmentation）**

  * **`RAG`**：针对 GPT-3 知识会过时和会瞎编的致命缺陷，学习 RAG 是如何开创性地将参数化知识（模型记忆）与非参数化知识（外挂数据库）结合起来的。这是**解决幻觉问题的核心工程思想**。
* **思想到行动的飞跃（The Action）**

  * **`ReAct（Agent）`**：学习 ReAct 框架是如何**巧妙地利用 GPT-3 强大的 ICL 能力**，让模型学会 Reason（思考）和 Act（行动）的交错循环，从而将一个聊天模型转变为一个能使用工具、解决问题的智能代理。

---

## 推荐教程：神话的原文（The Papers）

本阶段的教程不再是文档或博客，而是那些定义了时代的原始论文。请至少阅读它们的摘要（Abstract）、引言（Introduction）和结论（Conclusion）。

* **[BERT]**：**BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding**（Devlin et al.、2018）

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=BERT:+Pre-training+of+Deep+Bidirectional+Transformers+for+Language+Understanding+paper)
* **[GPT-3]**：**Language Models are Few-Shot Learners**（Brown et al.、2020）

  * [点击搜索论文（Google Search）](https://www.google.com/search?q=Language+Models+are+Few-Shot+Learners+GPT-3+paper)
* **[LoRA]**：**LoRA: Low-Rank Adaptation of Large Language Models**（Hu et al.、2021）

  * [点击搜索论文（Google Search）](https://www.google.com/search?q=LoRA:+Low-Rank+Adaptation+of+Large+Language+Models+paper)
* **[RAG]**：**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**（Lewis et al.、2020）

  * [点击搜索论文（Google Search）](https://www.google.com/search?q=Retrieval-Augmented+Generation+for+Knowledge-Intensive+NLP+Tasks+paper)
* **[ReAct]**：**ReAct: Synergizing Reasoning and Acting in Language Models**（Yao et al.、2022）

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=ReAct:+Synergizing+Reasoning+and+Acting+in+Language+Models+paper)

---

## 作业：撰写你的 LLM 思想族谱报告（A-la-One Report）

你的任务是构建一个 All-in-One Insight——一份阐明你所有见解的**思想族谱报告**。

### **作业要求**

1. **提交形式**：

   * 一份 Markdown 报告（或 Jupyter Notebook），清晰地阐述你的分析。
2. **核心内容：连接思想的脉络**：

   * 你需要**串联**阅读上述 5 篇（或更多）论文，并回答以下几个**核心问题**：
   * **[BERT -> LoRA]**

     * BERT 确立的 Pre-train、Fine-tune 范式是什么？
     * 为什么当 GPT-3 出现后，BERT 的全量微调范式会失效？
     * LoRA 是如何继承了微调思想，又如何革新了它以适应大模型时代的？
   * **[GPT -> RAG]**

     * GPT-3 强大的生成能力背后，暴露了哪些致命缺陷（如幻觉、知识过时）？
     * RAG 是如何通过检索来**修补**这些缺陷的？它的核心思想（参数化 vs 非参数化知识）是什么？
   * **[GPT -> ReAct]**

     * GPT-3 论文中揭示的，最令人震惊的涌现能力是什么？（提示：ICL / Few-Shot）
     * ReAct 框架是如何**利用**这种能力，让模型从一个回答者转变为一个执行者的？
