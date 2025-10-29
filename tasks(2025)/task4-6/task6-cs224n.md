# Task 6

## 学习目的（Learning Objectives）

祝贺你坚持到这里。你已经完成了前期的系统学习：在 Task 4 中，你实现了反向传播算法；在 Task 5 中，你使用模块化的方法构建了现代卷积神经网络的架构。你不再仅是调用 API 的使用者，而是真正理解神经网络内部运作机制的开发者。

现在，欢迎来到 NLP 学习阶段的开始，也是基础学习阶段的重要总结。

在本阶段的学习中，我们将从相对基础的文本分类、序列标注任务扩展到更广阔、更深入的自然语言**理解（Understanding）**与**生成（Generation）**领域。你将学习语言是如何被赋予数学形式的，机器是如何解析复杂句法结构的，以及如何实现不同语言之间的翻译。

本次任务将是你从理解经典模型到接触前沿研究的过渡。完成它，意味着你将具备初步阅读 NLP 顶级会议论文、理解并实现复杂语言系统的核心能力。

## 学习内容（Learning Content）

本阶段你将接触到一系列定义了现代 NLP 研究方向的重要模型与方法：

* **词的向量表示（Word Embeddings）**：学习 `word2vec` 的原理，理解计算机如何通过向量运算捕捉词语间的语义关系。
* **句法结构分析（Syntactic Parsing）**：学习并实现一个基于神经网络的**依存句法分析器（Dependency Parser）**，让模型理解句子的结构。
* **序列到序列模型（Sequence-to-Sequence Models）**：构建一个带**注意力机制（Attention）**的**神经机器翻译（Neural Machine Translation, NMT）**系统，体验模型在翻译时的注意力分配。
* **Transformer 架构（Transformer Architecture）**：深入理解驱动了当今大语言模型发展的核心——**自注意力机制（Self-Attention）**，并亲手实现其关键组件。

## 学习要求（Learning Requirements）

与前几次作业相比，本阶段任务对**数学基础、理论深度和代码实现精度**的要求达到了最高水平。

1. **深入理论学习**：CS224n 以其理论深度著称。你需要花费大量时间消化课程笔记，彻底理解反向传播在 RNN（BPTT）、Attention 和 Transformer 中的推导细节。
2. **代码精确实现**：本次作业中的很多模块（如 NMT 的 `forward` 和 `backward`）对代码的精确度要求极高，一个微小的索引错误或维度不匹配都可能导致整个系统出错。
3. **系统级整合与调试**：你需要将编码器、解码器、注意力模块等多个复杂组件准确地组合起来。调试这样一个庞大的系统极具挑战，你需要更有耐心，并学会如何设计单元测试来验证每个模块的正确性。

## 作业（Assignment）

**核心任务：完成 [CS224n 四大编程作业](https://web.stanford.edu/class/cs224n/)**

本次考核由四个核心模块构成，它们将引领你逐步掌握 NLP 领域的核心技术。

### **第一部分：词向量的探索与应用（Assignment 1）**

在这一部分，你将深入学习词语在向量空间中的表示方法。你需要：

* 理解 `word2vec` 模型（CBOW 和 Skip-Gram）背后的核心思想。
* 使用 `gensim` 等工具进行实践，并完成基于词向量的语义类比测试（如「king - man + woman ≈ queen」），直观感受词向量的效果。

### **第二部分：神经网络与依存句法分析（Assignment 2）**

在理解了词的表示后，你将开始让机器理解句子的结构。你需要：

* 实现一个基于神经网络的依存句法分析器。
* 深刻理解模型是如何通过分析句子中词语之间的修饰与被修饰关系，来形成对整个句子结构的语法树表示的。

### **第三部分：神经机器翻译（Assignment 3）**

这是最具挑战性的任务之一！你将构建一个能将一种语言翻译成另一种语言的系统。你需要：

* 实现一个带有注意力机制（Attention）的编码器-解码器（Encoder-Decoder）模型。
* 在训练过程中，你将能观察到模型在生成每一个目标语言单词时，它的注意力是如何在源语言句子的不同部分上动态分配的。

### **第四部分：探索 Transformer（Assignment 4）**

在体验了 RNN 处理序列的模式后，你将接触到当今 AI 领域的主流方法——Transformer。你需要：

* 学习并亲手实现自注意力机制（Self-Attention）和多头注意力（Multi-Head Attention）的核心计算过程。
* 通过构建一个简化的 Transformer 模型，你将彻底理解它为何能并行处理序列，并成为 GPT 等所有大语言模型的基础架构。

---

## ⭐ 重要提示 ⭐

* **关于最终项目（Final Project）**：为了让大家能将精力完全集中在对核心知识的编码实现上，本次考核**无需完成** CS224n 的最终项目（Final Project）
* **关于翻译与学习资料**：在学习过程中，如果遇到困难，可以参考：

  * **[ShaddockNH3/CS224N-Nyan-Book](https://github.com/ShaddockNH3/CS224N-Nyan-Book)**
  * 这是本人的学习仓库，你可以在这里找到课程 PPT 的翻译、论文精读笔记等学习资料，尤其是环境配置（cs224n 的环境配置没有 cs231n 配置那么方便）。仓库下放着本人的实现代码，这部分请不要看。

> 建议选择 LLM 路线的同学先完成 cs224n 的前三个 assignment，然后再去完成 cs231n

### **作业参考资料**

0. [cs224n](https://www.bilibili.com/video/BV1vQMBz6EvP/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)，能够理解 ppt 和论文的可以不用看视频
1. [跟李沐学AI 词向量（word2vec）【动手学深度学习v2】](https://www.bilibili.com/video/BV1sY4y1572C/)
2. [跟李沐学AI 注意力机制【动手学深度学习v2】](https://www.bilibili.com/video/BV1ui4y1j783/)
3. [跟李沐学AI Transformer论文逐段精读【论文精读】](https://www.bilibili.com/video/BV1pu411o7BE/)
4. [【Transformer 其实是个简单到令人困惑的模型【白话DeepSeek-06】】](https://www.bilibili.com/video/BV1C3dqYxE3q/)
5. [台大李宏毅老师 机器学习2021（Self-Attention和Transformer部分）](https://www.bilibili.com/video/BV1JA411X76s?p=65)

### **作业要求**

1. **严禁抄袭**。这是你的重要学习成果，请用一份独立完成的作业为这一阶段的学习画上句号，这既是对知识的尊重，也是对自己的负责。
2. **善用工具**。遇到问题时，首先尝试通过搜索引擎、官方文档和 AI 助手解决。如果仍然无法解决，欢迎在群里进行有深度的、描述清晰的提问。
3. **拥抱 AI，但保持思考**。不限制使用 ChatGPT 等大语言模型工具辅助学习和 Debug，但你必须确保能完全理解模型生成的每一行代码的含义。
4. **规范化提交**。所有作业均需通过 Git 提交到你个人的 GitHub 仓库中。

## 作业提交方式（Submission Method）

1. 你需要学习 GitHub 的使用，创建一个你自己的仓库用来存放你的代码实现
2. 接着你需要学习如何使用 Git 进行 PR 操作，在 [solutions](https://github.com/west2-online-reserve/collection-ai) 中进行操作
