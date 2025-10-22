# 星辰大海 future

## AI 的未来

AI 是什么？

当你看到这里的时候，意味着你的西二 AI 考核之旅已经接近尾声。强烈建议你去读一下 [ShaddockNH3 关于 AI 学习路线的思考](https://shaddocknh3.github.io/p/%E6%9C%89%E5%85%B3ai%E5%AD%A6%E4%B9%A0%E8%B7%AF%E7%BA%BF%E7%9A%84%E6%80%9D%E8%80%83/)，这也是考核如何设计以及改革的核心。

学到这里，相信你已经对 AI 有了初步的了解，也大致知道了 AI 是什么。

在你踏上这段旅程之初，这或许只是一个模糊的概念，一堆由代码、数学和人工智能这个时髦词汇构成的集合。而现在，当你历经了从 Python 基础到手动实现反向传播，再到驾驭现代神经网络的全部洗礼后，你已经有资格用自己的代码和理解，去书写这个问题的答案。

**总而言之，这个文件夹内的所有内容不是考核内容的一部分，而是你此后漫长学习生涯的开篇。**

恭喜你，你已经出色地完成了所有结构化的训练任务。但这并不意味着学习的结束。恰恰相反，你才刚刚抵达新世界的港口，拿到了属于你自己的船票。真正的 AI 之旅，现在才刚刚开始。

AI 领域的发展速度超乎想象，每隔几个月甚至几周，都可能有颠覆性的论文或模型诞生。昨日的 SOTA（State-of-the-Art），可能在明天就成为历史。这种飞速的迭代，既是挑战，也是机遇。它意味着，**持续学习、阅读文献、探索前沿，将不再是加分项，而是每一位 AI 从业者的生存法则。**

本章的目的，就是为你绘制一幅通往当前 AI 前沿领域的航海图，并为你提供追逐前沿的方法论。从现在起，你不再是课程的学生，而是 AI 领域的探索者。

你的新手保护期已经结束，前方的星辰大海充满了未知与挑战，但也蕴藏着无限的宝藏与可能。你手中已经握有最坚实的船舵（基础知识）和最精确的罗盘（学习能力）。

请保持好奇，保持谦逊，永远不要停止学习的脚步。

祝你，也祝我们，在这场波澜壮阔的AI革命中，都能找到属于自己的航线，看到最美的风景。

## 未来可能的学习路线

本路线为 [ShaddockNH3](https://github.com/ShaddockNH3) 自行设计的，如有纰漏请提 issue

task1：Python 基础（含一定 OOP 思想）

task2：爬虫（基本业务可能会碰到的所有情况）

task3：数据分析工具（NumPy、Pandas、Matplotlib）

task4：机器学习（KNN、SVM、Softmax、两层神经网络，以及与深度学习机理不同的决策树、随机森林、XGBoost 等）

task5：深度学习入门（反向传播、批/层归一化、CNN、PyTorch）

task6：深度学习深入

LLM：词嵌入、机器翻译、Transformer

CV：RNN、Transformer、GAN、SSL、LSTM

task7：

LLM：Hugging Face 生态（包括 pipeline、预训练）、LangChain 框架

CV：timm、OpenCV、Albumentations、OpenMMLab

task8：

LLM 应用：高级 RAG 与 Agent、模型微调、LoRA

LLM 论文：BERT -> GPT-2/3 -> LoRA -> RAG -> ReAct (Agent)

CV 应用：YOLO/Faster R-CNN

CV 论文：AlexNet -> ResNet -> R-CNN -> YOLO

task9：

LLM 应用：LLM 部署与运维 (MLOps / LLMOps)、vLLM 推理、流式传输、容器

LLM 论文：RLHF -> DPO -> HELM

CV 应用：CV 部署与运维 (MLOps)、ONNX/TensorRT 加速、实时应用、容器

CV 论文：3D Vision -> Stable Diffusion -> DiT (Transformer & Diffusion, the core of sora)

task10：AI 安全与伦理、Embodied AI/Robotics、多模态（Gemini 系列）、World Models（JEPA 框架等）、自己的理解

| 阶段 (Phase)                                                                                                              | 学习内容 (Learning Content)                              | 目标 (Goal)                                                                                                          | 预期时长 (Duration) |
| :---------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------------- |
| **[高级生态](task7.md)**                                         | AI生态工具链 (Hugging Face, LangChain, OpenMMLab, OpenCV) | **掌握工业界的核心魔法杖**。告别底层复现，转向高效开发。熟练驾驭Hugging Face、LangChain（LLM）与OpenMMLab、timm（CV）等SOTA生态，具备快速构建、训练和迭代复杂AI应用的能力。   | -             |
| **[应用与科研](task8.md)** | 高级应用与论文阅读 (Advanced RAG, Agent, YOLO, 论文复现)          | **分化**分化专精：成为解决者与思考者。深入LLM（高级RAG, Agent）与CV（YOLO系列, R-CNN）的SOTA应用。同时，系统性阅读顶会论文，培养独立科研能力，实现从使用者到贡献者的转变。 | -             |
| **[部署与前沿](task9.md)**                                        | 模型部署与前沿探索 (MLOps, vLLM, TensorRT, Sora, 3D Vision)   | 终极试**终极试炼：让AI落地并触碰未来**。掌握MLOps/LLMOps，学会使用vLLM、TensorRT、ONNX将模型部署到生产环境。同时，追踪Sora、3D视觉等最前沿研究，保持对技术浪潮的绝对敏锐。      | -             |
| **[视野与责任](task10.md)**                                       | AI安全、伦理与多模态                                          | **成为负责任的AI引领者**。超越技术本身，深入探讨AI安全、对齐与伦理问题。全面理解多模态（Multi-modal）的未来趋势，构建完整、深刻、富有责任感的AI世界观，为**为科技赋予温度**。          | -             |
