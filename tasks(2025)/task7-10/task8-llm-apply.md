# Task 8：LLM-Apply

## 学习目的

在 Task 7 中，你已经掌握了 Hugging Face 和 LangChain 等大语言模型生态工具的基本使用方法，能够构建对话原型和文本处理工具。

然而，基础原型仍存在明显局限。这些原型依赖模型的通用知识，无法回答专业领域的问题；只能被动响应，缺乏主动思考与执行能力。

本阶段的学习目标包括：

- **深入理解 RAG 与 Agent 技术**：系统学习高级 RAG 技术，掌握混合检索、重排序（Reranking）等方法以提升知识检索精准度；深入学习高级 Agent 技术，掌握复杂推理链（Reasoning）和自主规划的设计方法
- **掌握完整的模型开发流程**：学习从数据收集、模型微调到应用部署的全流程开发方法。利用 Task 2 的数据获取技能，自主收集特定领域的数据；运用 Task 7 的微调技术（`PEFT/LoRA`），为模型注入特定能力；最后，将微调后的模型与高级 RAG 知识库、高级 Agent 框架整合
- **构建完整的智能系统**：从编写独立脚本转向构建系统化的智能应用。学习如何让数据流、模型、工具链协同工作，最终交付一个能够解决特定领域问题的专家级应用

完成本阶段学习后，你将具备构建复杂、智能且实用的大语言模型应用的综合能力。

## 学习内容

### 模型微调

- **数据准备与清洗**：学习如何为爬取的数据（Task 2）或特定任务（如风格、人设），构建高质量的微调数据集（如 `jsonl` 格式的对话数据）
- **PEFT/LoRA 实践**：深入学习 `SFTTrainer`（from `trl`）的使用，理解 `LoRA` / `QLoRA` 的关键参数（如 `r`、`lora_alpha`、`target_modules`），并完成一次完整的模型微调训练
- **模型评估与合并**：学习如何评估微调后的模型效果，并掌握如何将 LoRA 权重与基础模型合并（merge），以方便后续部署

### 高级检索增强生成（Advanced RAG）

- **数据处理流水线（Ingestion Pipeline）**：构建自动化的数据处理流程：`爬虫（Task 2）-> 清洗 -> 智能切分（RecursiveCharacterTextSplitter）-> 嵌入（Embedding）-> 存入向量数据库（Chroma/FAISS）`
- **高级检索策略（Advanced Retrieval）**：
  - 学习并实践混合检索（Hybrid Search）：结合 `BM25`（稀疏检索）与向量（稠密检索）的优势，提高召回率
  - 学习查询转换（Query Transformations）：如 `HyDE`（用 LLM 生成假设性文档再检索）、`Multi-Query`（让 LLM 把一个复杂问题拆成多个子问题）
- **重排序（Re-ranking）**：学习 RAG 的关键优化步骤。使用更小、更快的 `Cross-Encoder`（交叉编码器）模型，对召回的文档进行二次精排，提升最终答案的精准度

### 高级智能代理（Advanced Agent）

- **自定义工具（Custom Tools）**：学习如何将构建的高级 RAG 链封装成强大的 `Tool`，供 Agent 调用
- **复杂规划与推理（Planning & Reasoning）**：
  - 深入理解 `ReAct` 框架（Agent 思考与行动的逻辑）
  - 掌握 `create_react_agent` 或 `create_openai_tools_agent` 等现代 Agent 构造器，学习如何构建、调试和管理一个拥有多个自定义工具（如 RAG 工具、网页搜索工具、计算器工具）的 `AgentExecutor`
- **Function Calling（工具调用）**：深入理解现代 LLM（如 OpenAI、Zhipu、Moonshot）的 `Function Calling` / `Tool Using` 能力，以及 LangChain 是如何抽象和利用这一能力的

## 推荐教程

### 模型微调

- [Hugging Face `trl` 库文档](https://www.google.com/search?q=%5Bhttps://huggingface.co/docs/trl/index%5D%28https://huggingface.co/docs/trl/index%29)
- [Hugging Face `peft` 库文档](https://www.google.com/search?q=%5Bhttps://huggingface.co/docs/peft/index%5D%28https://huggingface.co/docs/peft/index%29)
- [B 站/知乎搜索 LoRA 微调实战](https://www.google.com/search?q=LoRA+%E5%BE%AE%E8%B0%83%E5%AE%9E%E6%88%98)

### 高级 RAG

- [LangChain - RAG 官方文档](https://www.google.com/search?q=https://python.langchain.com/docs/use_cases/question_answering/)
- [LlamaIndex 官方文档](https://www.llamaindex.ai/)
- [B 站/知乎搜索 LangChain Reranking 或混合检索](https://www.google.com/search?q=LangChain+Reranking+%E6%95%99%E7%A8%8B)

### 高级 Agent

- [LangChain - Agents 官方文档](https://python.langchain.com/docs/modules/agents/)
- [OpenAI Function Calling 文档](https://platform.openai.com/docs/guides/function-calling)
- [B 站搜索 LangChain Agent 自定义工具](https://www.google.com/search?q=LangChain+Agent+%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B7%A5%E5%85%B7)

## 作业

本阶段的考核重点是项目完整性和技术融合能力。你需要将 task1-7 学到的技能整合成一个完整的应用项目。

### 作业 1：数据与模型准备

1. **爬取数据**

选择一个知识密集的领域（例如：游戏 Wiki 网站、编程语言的官方文档、动漫百科全书、专业领域知识网站等），使用 `requests` + `bs4/xpath` 或 `selenium` 或 `api` 爬取相关内容，并存为本地文件（如 .txt 或 .md）

2. **模型微调**

对一个基础模型（如 Qwen-7B、Llama3-8B-Instruct、Mistral-7B-Instruct、Gemma-7B-Instruct 等）进行 `LoRA` 微调。微调数据可以自己构建对话数据集（`jsonl` 格式），或使用现有的人设数据集，让模型拥有独特的说话风格

### 作业 2：高级 RAG 知识库构建

1. **构建知识库**

将阶段一爬取的所有文档进行清洗、切分（推荐使用 `RecursiveCharacterTextSplitter`）、嵌入（使用开源嵌入模型），并存入本地的向量数据库（如 `ChromaDB` 或 `FAISS`）

2. **实现高级 RAG 链**

构建一个 RAG 问答链，并在简单检索的基础上至少实现以下一项优化：

- **优化 A（Reranking）**：在检索（Retrieve）后，使用一个 `Cross-Encoder` 模型（如 `bge-reranker-base`）进行重排序，只把最相关的 Top-K 个文档交给 LLM
- **优化 B（Hybrid Search）**：实现 `BM25` + 向量嵌入的混合检索
- **优化 C（Query Transform）**：实现 `Multi-Query Retriever` 或 `HyDE`

### 作业 3：Agent 的构建与整合

1. **创建自定义工具（Tools）**

创建并注册至少 3 个工具：

- **工具 1（核心）：领域知识库（Custom Tool）**：将阶段二构建的高级 RAG 链封装成一个 LangChain `Tool`。当 Agent 需要回答关于爬取领域的内部知识时，它应该调用这个工具
- **工具 2（扩展）：实时网络搜索引擎（Built-in Tool）**：集成一个 LangChain 的内置工具，如 `SerperAPIWrapper` 或 `DuckGoSearchRun`。当 Agent 发现领域知识库无法回答时，它应该调用这个工具
- **工具 3（功能）：计算器或 Python REPL（Built-in Tool）**：集成 `PythonREPLTool` 或 `LLMMathChain`。当 Agent 需要进行数学计算时，它应该调用这个工具

2. **构建并运行 Agent**

使用 LangChain 的 `AgentExecutor`（推荐 `create_react_agent` 或 `create_openai_tools_agent`），将阶段一微调过的模型（如果没做微调，就用基础模型）和阶段三创建的 3 个工具整合起来

### 作业 4：报告与演示

1. 以 **Jupyter Notebook** 或 Markdown 形式提交代码和分析报告

2. 报告中需详细说明：

- 项目设计、爬虫目标网站和数据处理流程
- 微调思路、数据集和微调后的效果对比（如果进行了微调）
- 高级 RAG 实现了哪种优化，效果如何
- Agent 的设计方案，每个工具的作用是什么

3. 最终演示：

展示至少 2 个复杂的查询示例，这些示例需要能清晰地展示出 Agent 自主思考、规划、并调用了多个不同工具（如先查 RAG，再查网络，最后计算）的全过程。请务必打开 `verbose=True` 或 `return_intermediate_steps=True` 来展示 Agent 的思考链条
