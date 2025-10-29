# Task 7：LLM

## 学习目的：从理解原理到高效实践（Learning Objectives: From Understanding to Efficient Practice）

祝贺你已经成功完成了深度学习前沿内容的学习，亲手掌握并理解了诸如 Transformer 这样具有重要影响的核心技术。你现在已经能够深刻理解这些大型语言模型（LLM）的底层运作机制，甚至可以从零开始实现它们的结构。

然而，真正的能力，并非仅仅在于理解算法的构成，更在于如何有效地运用这些算法，去解决现实世界中复杂的问题。当你需要快速实现一个强大的语言模型应用时，你会选择从头开始实现每一个组件，还是会直接使用那些由众多研究者共同开发、包含了大量优化技术的**成熟框架**呢？

**Task 7，正是你从理论学习向 LLM 高效开发转变的关键阶段！**

此阶段的学习目的在于：

* **掌握业界最强生态系统，提升效率**：你将从纯粹的底层实现转向掌握由全球 AI 社区共同构建的、工业界最先进的 LLM 工具——以 **Hugging Face** 和 **LangChain** 为代表的工具链。学习如何高效地加载、调用、微调和组合这些强大的模型与框架，让你的开发效率实现显著提升。
* **掌握基础语言技术，实现核心功能**：你将不仅仅停留在调用 LLM API 的层面。你将学习如何灵活运用 LLM 的核心能力，通过有效的提示工程（Prompt Engineering）和简单的链式（Chains）组合，实现文本生成、智能问答、内容摘要等基础而强大的语言智能功能。
* **奠定 LLM 实战基础，指引未来方向**：通过本阶段的学习与实践，你将建立起扎实的 LLM 应用开发能力，清楚地了解从模型选择、数据准备、基础微调策略到应用原型设计的全链路。这不仅是技能的扩展，更是你未来在 LLM 领域进行更高级部署、前沿科研探索及商业化应用的坚实基础。你将从一个学习者，成长为一名能够真正创造和推动语言智能发展的开发者！

---

## 学习内容：LLM 技术的工具生态系统（Learning Content: LLM Technology Ecosystem）

本阶段将聚焦于 LLM 领域最核心、最实用的应用开发工具与技术，助你从理论走向实践。

* **Hugging Face 生态工具链的深度探索：你的"模型军械库"**

  * **`transformers` 库**：

    * 深入学习如何加载和使用各种预训练的 LLM 模型（如 Llama、Mistral、Gemma、GLM 等）及其配套的 Tokenizer。
    * 进行文本生成、情感分析、问答、翻译等基础任务的推理实践。
    * 模型结构认知：理解不同 LLM 模型的特点、优势及适用场景。
  * **`pipeline` 模块**：

    * 学习如何利用 `pipeline` 快速构建和部署各类 NLP 任务，大幅简化开发流程。
  * **`datasets` 库**：

    * 掌握高效加载、处理、转换和管理大规模文本数据集的方法，为模型微调准备高质量数据。
  * **`peft` / `LoRA` (Low-Rank Adaptation) 等高效微调技术**：

    * 学习如何在计算资源有限的情况下，对大型 LLM 进行高效、低成本的微调，使其适应特定任务或领域。
* **LangChain 框架与应用：你的“智能流程编排平台”**

  * **核心模块理解**：深入学习 LangChain 的基础构建块，包括 `Prompt Templates` (提示模板)、`LLMs` (模型接口)、`Chains` (链式调用) 和 `Memory` (记忆管理)。

    * **重点实践**：如何设计高效的 `Prompt Templates`，并将多个提示和LLM调用连接成一个简单的 `Chain`。
  * **基础概念认知**：初步了解**检索增强生成 (RAG)** 和 **Agent** 的基本概念，知道它们是解决 LLM 局限性的强大思路。
  * **工具使用 (Tool Use) 初探**：简单了解工具（Function Calling）的概念，知道如何让 LLM 能够调用外部功能，但暂不要求实现复杂 Agent。

- --

## 推荐教程：通往LLM世界的权威指引

* **Hugging Face 官方文档与教程**

  * [Hugging Face Transformers 官方文档](https://huggingface.co/docs/transformers/index)
  * [Hugging Face Course (推荐从 NLP 模块开始)](https://huggingface.co/course/chapter1/1)
* **LangChain 官方文档**

  * [LangChain Python Docs](https://python.langchain.com/docs/get_started/introduction)
  * [LangChain Expressions Language (LCEL) 教程](https://python.langchain.com/docs/expression_language/) (非常推荐，它是 LangChain 的未来)
* **B站系列教程 (中文，易于理解)**

  * 搜索 “李宏毅 LLM” 或 “吴恩达 LLM” 相关课程。
  * 搜索 “Hugging Face 教程” 或 “LangChain 教程”，选择最新、评价高的进行学习。
* **实战平台 Kaggle**

  * [Kaggle Learn - Natural Language Processing](https://www.google.com/search?q=https://www.kaggle.com/learn/natural-language-processing) (基础)
  * 关注 Kaggle 上关于 LLM 的入门级竞赛 Notebooks，学习基础的实战技巧。
* **知名博客与社区**

  * 订阅 LLM 相关的技术博客（如 Hugging Face Blog, LlamaIndex Blog 等），保持对最新技术的关注。

- --

## 作业：专属智能助手原型

本轮作业的重点在于**实战运用 Hugging Face 和 LangChain 的核心功能**，构建一些基础的语言智能应用原型。我们不要求你从零开始训练一个大型语言模型，也不要求你实现复杂的 RAG 和 Agent 系统，而是期望你能够熟练运用现有的生态工具和框架，实现核心的语言处理功能。本轮考核将延续“can run is ok”的原则，鼓励你大胆尝试，让你的程序先跑起来，实现核心功能。

### **作业1：智能文本处理工具集 (基于 Hugging Face)**

你的是利用 Hugging Face 的 `transformers` 库和 `pipeline` 模块，构建一个智能文本处理工具集。

#### **要求**

1. **文本生成器**：

   * 加载一个开源的文本生成 LLM 模型（例如 Llama2-7B-Chat、Mistral-7B-Instruct 等，可通过 Hugging Face 加载）。
   * 实现一个简单的文本生成功能，用户输入一个开头（prompt），模型能生成一段连贯的文本。
   * 尝试调整生成参数（如 `max_new_tokens`、`temperature`、`top_k`、`top_p`），观察它们对生成结果的影响。
2. **文本摘要/翻译器**：

   * 选择一个你感兴趣的 NLP 任务，例如：

     * **文本摘要**：加载一个预训练的摘要模型（如 `bart-large-cnn`、`t5-small`），对一段长文本进行概括。
     * **机器翻译**：加载一个预训练的翻译模型（如 `Helsinki-NLP/opus-mt-en-zh`），实现英汉互译。
   * 使用 `pipeline` 模块简化任务的实现。
3. **报告与思考**：

   * 以 **Jupyter Notebook** 或 Markdown 形式提交你的代码和分析报告。
   * 报告中请说明你选择的模型、任务实现思路，并展示几个不同任务的运行示例及结果。
   * 思考并记录你在使用 Hugging Face `pipeline` 和 `transformers` 过程中遇到的便利之处，以及对不同模型表现的初步体会。

### **作业2：智能对话片段模拟器（基于 LangChain）**

你的任务是利用 LangChain 的 `Prompt Templates`、`LLMs` 和 `Memory` 模块，构建一个能进行简单记忆的对话片段模拟器。

#### **要求**

1. **基础对话链**：

   * 使用 LangChain 加载一个开源的 LLM 模型。
   * 设计一个 `Prompt Template`，用于引导模型的对话风格或角色设定（例如：让模型扮演一个友善的助手）。
   * 构建一个简单的 `LLMChain`，实现用户与模型的单轮对话。
2. **加入记忆功能**：

   * 将 `ConversationBufferMemory` 或其他简单的 `Memory` 模块集成到你的对话链中。
   * 让模型能够记住过去几轮的对话历史，并在新的回复中体现出这种记忆。
   * （选做，学有余力）尝试调整记忆的长度，观察对对话连贯性的影响。
3. **任务演示与分析**：

   * 以 **Jupyter Notebook** 或 Markdown 形式提交你的代码和分析报告。
   * 报告中请详细描述你设计的 `Prompt Template`、如何集成 `Memory`，并展示多轮对话的详细交互过程（突出记忆效果）。
   * 分析加入记忆后的对话与无记忆对话的区别，指出其优点和局限性。
