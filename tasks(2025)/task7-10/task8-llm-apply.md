# Task 8：LLM-Apply

## **学习目的：从拼接到全链路应用**

你已经在 Task 7 中成功驾驭了 Hugging Face 和 LangChain 这些强大的生态工具。你不再是一个对 LLM 应用一无所知的门外汉，而是已经亲手构建了属于自己的对话原型和文本工具。

然而，真正的挑战才刚刚开始。Task 7 的原型，如同未开刃的宝剑，虽然锋利，却缺少灵魂与深度。它们依赖模型的通用知识，无法回答专业领域的问题（RAG 的雏形）；它们只能被动地响应，无法主动地思考与行动（Agent 的雏形）。

**Task 8，正是你从工匠向宗师蜕变，为你宝剑开刃的时刻！**

此阶段的学习目的在于：

* **深入 RAG 与 Agent 的心脏**：你将不再停留在概念认知和简单调用上。本轮，你将深入探索 **高级 RAG** 的奥秘，学习如何通过混合检索、重排序（Reranking）等技术大幅提升知识检索的精准度；你将深入 **高级 Agent** 的世界，学习如何设计复杂的思考链（Reasoning）和自主规划，让你的 Agent 真正活起来。
* **掌握数据->微调->应用的全链路**：这是本轮最核心的挑战！你将亲手打通一个 LLM 应用的完整生命周期：从 **Task 2** 的爬虫技能出发，**自主爬取**特定领域的数据；运用 **Task 7** 的微调技术（`PEFT/LoRA`），为模型注入独特的**人设**；最后，将你微调过的模型，与你构建的高级 RAG 知识库、高级 Agent 框架**完美融合**。
* **从单一功能到系统工程的跨越**：你不再是构建零散的脚本，而是要完成一完整的项目。这个项目将是一个复杂的系统工程，它要求你像一名真正的AI架构师一样思考，如何让数据流、模型、工具链协同工作，最终交付一个真正强大、智能、且能解决特定领域问题的专家级应用。

完成本轮试炼，你将不再是调包侠，而是真正具备了构建一个复杂、智能、且真正有用的 LLM 应用的综合能力！

---

## 学习内容：高级LLM开发

本阶段将聚焦于将 Task 7 的基础组件，升级和融合成一个复杂、完整的项目。

* **模型微调（Model Fine-tuning）实战**

  * **数据准备与清洗**：学习如何为你爬取的数据（Task 2 成果）或特定任务（如风格、人设），构建高质量的微调数据集（如 `jsonl` 格式的对话数据）。
  * **`PEFT/LoRA` 深入实践**：深入 `SFTTrainer`（from `trl`）的使用，理解 `LoRA` / `QLoRA` 的关键参数（如 `r`、`lora_alpha`、`target_modules`），并完成一次完整的模型微调训练。
  * **模型评估与合并**：学习如何（至少在主观上）评估微调后的模型效果，并掌握如何将 LoRA 权重与基础模型合并（merge），以方便后续部署。
* **高级检索增强生成（Advanced RAG）**

  * **数据注入流水线（Ingestion Pipeline）**：构建一个自动化的数据处理流程：`爬虫（Task 2）-> 清洗 -> 智能切分（RecursiveCharacterTextSplitter）-> 嵌入（Embedding）-> 存入向量数据库（Chroma/FAISS）`。
  * **高级检索策略（Advanced Retrieval）**：

    * 了解并尝试**混合检索（Hybrid Search）**：结合 `BM25`（稀疏检索）与向量（稠密检索）的优势，提高召回率。
    * 了解**查询转换（Query Transformations）**：如 `HyDE`（用 LLM 生成假设性文档再检索）、`Multi-Query`（让 LLM 把一个复杂问题拆成多个子问题）。
  * **重排序（Re-ranking）**：学习 RAG 的关键优化步骤。使用更小、更快的 `Cross-Encoder`（交叉编码器）模型，对召回的粗糙文档进行二次精排，大幅提升最终答案的精准度。
* **高级智能代理（Advanced Agent）**

  * **自定义工具（Custom Tools）**：**重中之重**！你将不再使用 LangChain 的内置玩具工具，而是要学会如何把你构建的 **高级 RAG 链** 本身，封装成一个强大的 `Tool`，供 Agent 调用。
  * **复杂规划与推理（Planning & Reasoning）**：

    * 深入理解 `ReAct` 框架（Agent 思考与行动的逻辑）。
    * 掌握 `create_react_agent` 或 `create_openai_tools_agent` 等现代 Agent 构造器，学习如何构建、调试和管理一个拥有**多个自定义工具**（如 RAG 工具、网页搜索工具、计算器工具）的 `AgentExecutor`。
  * **Function Calling（工具调用）**：深入理解现代 LLM（如 OpenAI、Zhipu、Moonshot）的 `Function Calling` / `Tool Using` 能力，以及 LangChain 是如何抽象和利用这一能力的。

---

## 推荐教程：

* **模型微调（Fine-tuning）**

  * [Hugging Face `trl` 库文档](https://www.google.com/search?q=%5Bhttps://huggingface.co/docs/trl/index%5D%28https://huggingface.co/docs/trl/index%29)（SFTTrainer 的权威指南）
  * [Hugging Face `peft` 库文档](https://www.google.com/search?q=%5Bhttps://huggingface.co/docs/peft/index%5D%28https://huggingface.co/docs/peft/index%29)（LoRA 的权威指南）
  * [B 站/知乎搜索 LoRA 微调实战](https://www.google.com/search?q=LoRA+%E5%BE%AE%E8%B0%83%E5%AE%9E%E6%88%98)（寻找端到端的项目教程）
* **高级 RAG（Advanced RAG）**

  * [LangChain - RAG 官方文档](https://www.google.com/search?q=https://python.langchain.com/docs/use_cases/question_answering/)（深入阅读 `Retrieval` 和 `Chains` 部分）
  * [LlamaIndex 官方文档](https://www.llamaindex.ai/)（LlamaIndex 在 RAG 方面做得非常深入，可以作为交叉参考和灵感来源）
  * [B 站/知乎搜索 LangChain Reranking 或混合检索](https://www.google.com/search?q=LangChain+Reranking+%E6%95%99%E7%A8%8B)
* **高级 Agent（Advanced Agent）**
  * [LangChain - Agents 官方文档](https://python.langchain.com/docs/modules/agents/)（**必读**，尤其是 `Agent Executor` 和 `Custom tools` 部分）

  * [OpenAI Function Calling 文档](https://platform.openai.com/docs/guides/function-calling)（理解 Agent 调用工具的底层原理）
  * [B 站搜索 LangChain Agent 自定义工具](https://www.google.com/search?q=LangChain+Agent+%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B7%A5%E5%85%B7)

---

## 作业：构建你的领域专家智能代理（All-in-One Project）

本轮作业的重点是 **项目完整性** 和 **技术融合**。你需要将 task1-7 学到的技能整合成一个单一的、强大的应用。我们将不再提供多个小作业，而是只提供一个综合性的大项目。

比如说你喜欢一个游戏的剧情（以原神为例），并且是胡桃厨，你可以先收集和创造胡桃的对话，对模型进行微调（LoRA/QLoRA），使之拥有胡桃的人格。然后将你收集到的原神剧情文本转换为向量库，设计agent流进行回答等。

你可以先使用1.5b的小模型测试。

### **作业要求（All-in-One）**

#### **阶段一：数据与模型准备（爬虫 + 微调）**

1. **爬取数据**

   * 请自行选择**一个你感兴趣的、知识密集的领域**（例如：一个游戏的 Wiki 网站、一个编程语言的官方文档、某个动漫的百科全书、你专业领域的某个知识网站等）。
   * 使用 `requests` + `bs4/xpath` 或 `selenium` 或 `api`，爬取你需要的内容，并存为本地文件（如 .txt 或 .md）。
2. **模型微调**

   * 为了让你的 Agent 更有灵魂，请对一个基础模型（如 Qwen-7B、Llama3-8B-Instruct、Mistral-7B-Instruct、Gemma-7B-Instruct 等）进行 `LoRA` 微调。
   * 微调数据：你可以自己构建一个小的对话数据集（`jsonl` 格式），或者在网上找到一个人设数据集（如傲娇助手、学术专家等），让你的模型拥有独特的说话风格。

#### **阶段二：高级 RAG 知识库构建（Task 8 技能）**

1. **构建知识库**

   * 将你在【阶段一】爬取的所有文档，进行**清洗、切分**（推荐使用 `RecursiveCharacterTextSplitter`）、**嵌入**（使用开源嵌入模型），并存入一个本地的向量数据库（如 `ChromaDB` 或 `FAISS`）。
2. **实现高级 RAG 链**

   * 构建一个 RAG 问答链。
   * **【高级要求】**：为了提升 RAG 的质量，你必须在简单检索的基础上，至少实现以下一项优化：

     * **优化 A（Reranking）**：在检索（Retrieve）后，使用一个 `Cross-Encoder` 模型（如 `bge-reranker-base`）进行重排序，只把最相关的 Top-K 个文档交给 LLM。
     * **优化 B（Hybrid Search）**：实现 `BM25` + 向量嵌入的混合检索。
     * **优化 C（Query Transform）**：实现 `Multi-Query Retriever` 或 `HyDE`。

#### **阶段三：Agent 的构建与整合**

1. **创建自定义工具（Tools）**

   * 这是本作业的**核心**！你必须创建并注册至少 **3 个**工具：
   * **工具 1（核心）：`领域知识库`（Custom Tool）**
     * **将你在【阶段二】构建的高级 RAG 链封装成一个 LangChain `Tool`**。当 Agent 需要回答关于你爬取领域的内部知识时，它应该调用这个工具。
   * **工具 2（扩展）：`实时网络搜索引擎`（Built-in Tool）**

     * 集成一个 LangChain 的内置工具，如 `SerperAPIWrapper`（需要申请免费 Key）或 `DuckGoSearchRun`。当 Agent 发现领域知识库无法回答（比如问最新的新闻）时，它应该调用这个工具。
   * **工具 3（功能）：`计算器` 或 `Python REPL`（Built-in Tool）**

     * 集成 `PythonREPLTool` 或 `LLMMathChain`。当 Agent 需要进行数学计算时（比如合成 3 个 A 需要多少 B），它应该调用这个工具。
2. **构建并运行 Agent**

   * 使用 LangChain 的 `AgentExecutor`（推荐 `create_react_agent` 或 `create_openai_tools_agent` 体系），将你在【阶段一】**微调过的模型**（如果没做微调，就用基础模型）和你在【阶段三】**创建的 3 个工具**整合起来。
   * **启动你的 Agent！**

#### **阶段四：报告与演示**

1. 以 **Jupyter Notebook** 或 Markdown 形式提交你的代码和分析报告。
2. 在报告中，请详细说明：

   * 你的项目设计、爬虫目标网站和数据处理流程。
   * （如果做了）你的微调思路、数据集和微调后的效果对比。
   * 你的高级 RAG实现了哪种优化，效果如何。
   * 你的 Agent 是如何设计的，每个工具的作用是什么。
3. **【最终演示】**：

   * 请在报告中，**必须**展示至少 **2 个** 复杂的查询示例，这两个示例需要能清晰地展示出你的 Agent **自主思考、规划、并调用了多个不同工具（如先查 RAG，再查网络，最后计算）** 的全过程。请务必打开 `verbose=True` 或 `return_intermediate_steps=True` 来展示 Agent 的思考链条！
