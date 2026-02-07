# Task 7：RAG 与 Agent

## 学习内容

* Hugging Face 生态工具链
  * `transformers` 库：
    * 深入学习如何加载和使用各种预训练的 LLM 模型（如 Llama、Mistral、Gemma、GLM 等）及其配套的 Tokenizer。
    * 进行文本生成、情感分析、问答、翻译等基础任务的推理实践。
    * 模型结构认知：理解不同 LLM 模型的特点、优势及适用场景。
  * `pipeline` 模块：
    * 学习如何利用 `pipeline` 快速构建和部署各类 NLP 任务，大幅简化开发流程。
  * `datasets` 库：
    * 掌握高效加载、处理、转换和管理大规模文本数据集的方法，为模型微调准备高质量数据。
  * `peft` / `LoRA` (Low-Rank Adaptation) 等高效微调技术：
    * 学习如何在计算资源有限的情况下，对大型 LLM 进行高效、低成本的微调，使其适应特定任务或领域。
* LangChain 框架与应用
  * 核心模块理解：深入学习 LangChain 的基础构建块，包括 `Prompt Templates` (提示模板)、`LLMs` (模型接口)、`Chains` (链式调用) 和 `Memory` (记忆管理)。
    * 重点实践：如何设计高效的 `Prompt Templates`，并将多个提示和LLM调用连接成一个简单的 `Chain`。
  * 基础概念认知：初步了解检索增强生成 (RAG) 和 Agent 的基本概念，知道它们是解决 LLM 局限性的强大思路。
  * 工具使用 (Tool Use) 初探：简单了解工具（Function Calling）的概念，知道如何让 LLM 能够调用外部功能，但暂不要求实现复杂 Agent。

## 推荐教程

* Hugging Face 官方文档与教程
  * [Hugging Face Transformers 官方文档](https://huggingface.co/docs/transformers/index)
  * [Hugging Face Course (推荐从 NLP 模块开始)](https://huggingface.co/course/chapter1/1)
* LangChain 官方文档
  * [LangChain Python Docs](https://python.langchain.com/docs/get_started/introduction)
  * [LangChain Expressions Language (LCEL) 教程](https://python.langchain.com/docs/expression_language/) (非常推荐，它是 LangChain 的未来)
* Kaggle Learn 相关课程
  * [Kaggle Learn - Natural Language Processing](https://www.google.com/search?q=https://www.kaggle.com/learn/natural-language-processing) (基础)
  * 关注 Kaggle 上关于 LLM 的入门级竞赛 Notebooks，学习基础的实战技巧。
* 知名博客与社区
  * 订阅 LLM 相关的技术博客（如 Hugging Face Blog, LlamaIndex Blog 等），保持对最新技术的关注。
* B 站相关视频教程
  * 搜索 Hugging Face 和 LangChain 相关的入门视频，观看实操演示。

## 作业

本轮作业的重点在于实战运用 Hugging Face 和 LangChain 的核心功能，构建一些基础的语言智能应用原型。我们不要求你从零开始训练一个大型语言模型，也不要求你实现复杂的 RAG 和 Agent 系统，而是期望你能够熟练运用现有的生态工具和框架，实现核心的语言处理功能。本轮考核将延续 “can run is ok” 的原则，鼓励你大胆尝试，让你的程序先跑起来，实现核心功能。

### 作业 1：智能文本处理工具集 (基于 Hugging Face)

你的是利用 Hugging Face 的 `transformers` 库和 `pipeline` 模块，构建一个智能文本处理工具集。

#### 作业 1 - 要求

1. 文本生成器：
   * 加载一个开源的文本生成 LLM 模型（例如 Llama2-7B-Chat、Mistral-7B-Instruct 等，可通过 Hugging Face 加载）。
   * 实现一个简单的文本生成功能，用户输入一个开头（prompt），模型能生成一段连贯的文本。
   * 尝试调整生成参数（如 `max_new_tokens`、`temperature`、`top_k`、`top_p`），观察它们对生成结果的影响。
2. 文本摘要/翻译器：
   * 选择一个你感兴趣的 NLP 任务，例如：
     * 文本摘要：加载一个预训练的摘要模型（如 `bart-large-cnn`、`t5-small`），对一段长文本进行概括。
     * 机器翻译：加载一个预训练的翻译模型（如 `Helsinki-NLP/opus-mt-en-zh`），实现英汉互译。
   * 使用 `pipeline` 模块简化任务的实现。
3. 报告与思考：
   * 以 Jupyter Notebook 或 Markdown 形式提交你的代码和分析报告。
   * 报告中请说明你选择的模型、任务实现思路，并展示几个不同任务的运行示例及结果。
   * 思考并记录你在使用 Hugging Face `pipeline` 和 `transformers` 过程中遇到的便利之处，以及对不同模型表现的初步体会。

### 作业 2：智能对话片段模拟器（基于 LangChain）

你的任务是利用 LangChain 的 `Prompt Templates`、`LLMs` 和 `Memory` 模块，构建一个能进行简单记忆的对话片段模拟器。

#### 作业 2 - 要求

1. 基础对话链：
   * 使用 LangChain 加载一个开源的 LLM 模型。
   * 设计一个 `Prompt Template`，用于引导模型的对话风格或角色设定（例如：让模型扮演一个友善的助手）。
   * 构建一个简单的 `LLMChain`，实现用户与模型的单轮对话。
2. 加入记忆功能：
   * 将 `ConversationBufferMemory` 或其他简单的 `Memory` 模块集成到你的对话链中。
   * 让模型能够记住过去几轮的对话历史，并在新的回复中体现出这种记忆。
   * （选做）尝试调整记忆的长度，观察对对话连贯性的影响。
3. 任务演示与分析：
   * 以 Jupyter Notebook 或 Markdown 形式提交你的代码和分析报告。
   * 报告中请详细描述你设计的 `Prompt Template`、如何集成 `Memory`，并展示多轮对话的详细交互过程（突出记忆效果）。
   * 分析加入记忆后的对话与无记忆对话的区别，指出其优点和局限性。
