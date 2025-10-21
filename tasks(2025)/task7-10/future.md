# 星辰大海 future

## AI的未来

AI是什么？

当你看到这里的时候，意味着你的西二AI考核之旅已经接近尾声。强烈建议你去读一下[ShaddockNH3关于AI学习路线的思考](https://shaddocknh3.github.io/p/%E6%9C%89%E5%85%B3ai%E5%AD%A6%E4%B9%A0%E8%B7%AF%E7%BA%BF%E7%9A%84%E6%80%9D%E8%80%83/)，这也是考核如何设计以及改革的核心。

学到这里，相信你已经对AI有了初步的了解，也大致知道了AI是什么。

在你踏上这段旅程之初，这或许只是一个模糊的概念，一堆由代码、数学和人工智能这个时髦词汇构成的集合。而现在，当你历经了从Python基础到手动实现反向传播，再到驾驭现代神经网络的全部洗礼后，你已经有资格用自己的代码和理解，去书写这个问题的答案。

**总而言之，这个文件夹内的所有内容不是考核内容的一部分，而是你此后漫长学习生涯的开篇。**

恭喜你，你已经出色地完成了所有结构化的训练任务。但这并不意味着学习的结束。恰恰相反，你才刚刚抵达新世界的港口，拿到了属于你自己的船票。真正的AI之旅，现在才刚刚开始。

AI领域的发展速度超乎想象，每隔几个月甚至几周，都可能有颠覆性的论文或模型诞生。昨日的SOTA（State-of-the-Art），可能在明天就成为历史。这种飞速的迭代，既是挑战，也是机遇。它意味着，**持续学习、阅读文献、探索前沿，将不再是加分项，而是每一位AI从业者的生存法则。**

本章的目的，就是为你绘制一幅通往当前AI前沿领域的航海图，并为你提供追逐前沿的方法论。从现在起，你不再是课程的学生，而是AI领域的探索者。

你的新手保护期已经结束，前方的星辰大海充满了未知与挑战，但也蕴藏着无限的宝藏与可能。你手中已经握有最坚实的船舵（基础知识）和最精确的罗盘（学习能力）。

请保持好奇，保持谦逊，永远不要停止学习的脚步。

祝你，也祝我们，在这场波澜壮阔的AI革命中，都能找到属于自己的航线，看到最美的风景。

## 未来可能的学习路线

本路线为[ShaddockNH3](https://github.com/ShaddockNH3)自行设计的，如有纰漏请提issue

task1：py基础（含一定oop思想）

task2：爬虫（基本业务可能会碰到的所有情况）

task3：数据分析工具（numpy，pandas，matplotlib）

task4：机器学习（knn，svm，softmax，两层神经网络，以及与深度学习机理不同的决策树，随机森林，xgboost等）

task5：深度学习入门（反向传播，批/层归一化，cnn，pytorch）

task6：深度学习深入

llm：词嵌入，机器翻译，transformer

cv：rnn，transformer，gan，ssl，ltsm

task7：

llm：hugging face生态（包括pipline，预训练），langchain框架

cv：timm，opencv，Albumentations，OpenMMLab

task8：

llm应用：高级rag与agent，模型微调，lora

llm论文：BERT -> gpt2/3 -> LoRA -> RAG -> ReAct(Agent)

cv应用：YOLO/Faster，R-CNN

cv论文：AlexNet ->  ResNet -> R-CNN -> YOLO

task9：

llm应用：LLM部署与运维 (MLOps / LLMOps)，vllm推理，流式传输，容器

llm论文：RLHF -> DPO -> HELM

cv应用：CV部署与运维 (MLOps)，ONNX/TensorRT加速，实时应用，容器

cv论文：3D Vision -> Stable Diffusion -> DiT(Transformer&Diffusion, the core of sora)

task10：AI安全与伦理，Embodied AI/Robotics，多模态（Gemini系列），World Models（JEPA框架等），自己的理解

| 阶段 (Phase)                                                                                                              | 学习内容 (Learning Content)                              | 目标 (Goal)                                                                                                          | 预期时长 (Duration) |
| :---------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------------- |
| **[高级生态](task7.md)**                                         | AI生态工具链 (Hugging Face, LangChain, OpenMMLab, OpenCV) | **掌握工业界的核心魔法杖**。告别底层复现，转向高效开发。熟练驾驭Hugging Face、LangChain（LLM）与OpenMMLab、timm（CV）等SOTA生态，具备快速构建、训练和迭代复杂AI应用的能力。   | -             |
| **[应用与科研](task8.md)** | 高级应用与论文阅读 (Advanced RAG, Agent, YOLO, 论文复现)          | **分化**分化专精：成为解决者与思考者。深入LLM（高级RAG, Agent）与CV（YOLO系列, R-CNN）的SOTA应用。同时，系统性阅读顶会论文，培养独立科研能力，实现从使用者到贡献者的转变。 | -             |
| **[部署与前沿](task9.md)**                                        | 模型部署与前沿探索 (MLOps, vLLM, TensorRT, Sora, 3D Vision)   | 终极试**终极试炼：让AI落地并触碰未来**。掌握MLOps/LLMOps，学会使用vLLM、TensorRT、ONNX将模型部署到生产环境。同时，追踪Sora、3D视觉等最前沿研究，保持对技术浪潮的绝对敏锐。      | -             |
| **[视野与责任](task10.md)**                                       | AI安全、伦理与多模态                                          | **成为负责任的AI引领者**。超越技术本身，深入探讨AI安全、对齐与伦理问题。全面理解多模态（Multi-modal）的未来趋势，构建完整、深刻、富有责任感的AI世界观，为**为科技赋予温度**。          | -             |
