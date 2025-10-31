# 未来发展方向

## AI 的未来

AI 是什么？

当你看到这里的时候，意味着你的西二 AI 考核已经接近尾声。强烈建议你阅读 [ShaddockNH3 关于 AI 学习路线的思考](https://shaddocknh3.github.io/p/%E6%9C%89%E5%85%B3ai%E5%AD%A6%E4%B9%A0%E8%B7%AF%E7%BA%BF%E7%9A%84%E6%80%9D%E8%80%83/)，这也是考核设计以及改革的核心思想。

学到这里，相信你已经对 AI 有了初步的了解，也大致知道了 AI 是什么。

在开始学习之初，这或许只是一个模糊的概念，一个由代码、数学和人工智能这个术语构成的集合。而现在，当你完成了从 Python 基础到手动实现反向传播，再到掌握现代神经网络的全部学习后，你已经有能力用自己的代码和理解，去回答这个问题。

**本文件夹内的所有内容不是考核内容的一部分，而是你此后持续学习的开始。**

祝贺你已经出色地完成了所有结构化的训练任务。但这并不意味着学习的结束。恰恰相反，你才刚刚进入新的学习阶段，获得了继续深入学习的基础。真正的 AI 学习，现在才刚刚开始。

AI 领域的发展速度超乎想象，每隔几个月甚至几周，都可能有突破性的论文或模型发布。昨日的最先进技术（State-of-the-Art, SOTA），可能在明天就被超越。这种快速的迭代，既是挑战，也是机遇。它意味着，**持续学习、阅读文献、探索前沿，将不再是可选项，而是每一位 AI 从业者的必备能力。**

本章的目的，就是为你提供一个通往当前 AI 前沿领域的学习路线，并为你提供追踪前沿的方法论。从现在起，你不再是课程的学生，而是 AI 领域的学习者。

你的基础学习阶段已经结束，前方的学习道路充满了未知与挑战，但也蕴藏着无限的可能。你已经掌握了扎实的基础知识和有效的学习能力。

请保持好奇心，保持谦逊态度，永远不要停止学习的步伐。

祝你，也祝我们，在这场 AI 技术发展中，都能找到属于自己的发展方向，获得最好的学习成果。

## 未来可能的学习路线

本路线为 [ShaddockNH3](https://github.com/ShaddockNH3) 自行设计的，如有问题请提 issue

**Task 1**：Python 基础（含一定面向对象编程（OOP）思想）

**Task 2**：爬虫（基本业务可能会遇到的所有情况）

**Task 3**：数据分析工具（NumPy、Pandas、Matplotlib）

**Task 4**：机器学习（KNN、SVM、Softmax、两层神经网络，以及与深度学习机理不同的决策树、随机森林、XGBoost 等）

**Task 5**：深度学习入门（反向传播、批/层归一化、CNN、PyTorch）

**Task 6**：深度学习深入

- LLM：词嵌入、机器翻译、Transformer
- CV：RNN、Transformer、GAN、SSL、LSTM

**Task 7**：

- LLM：Hugging Face 生态（包括 pipeline、预训练）、LangChain 框架
- CV：timm、OpenCV、Albumentations、OpenMMLab

**Task 8**：

- LLM 应用：高级 RAG 与 Agent、模型微调、LoRA
- LLM 论文：BERT -> GPT-2/3 -> LoRA -> RAG -> ReAct（Agent）
- CV 应用：YOLO/Faster R-CNN
- CV 论文：AlexNet -> ResNet -> R-CNN -> YOLO

**Task 9**：

- LLM 应用：LLM 部署与运维（MLOps / LLMOps）、vLLM 推理、流式传输、容器
- LLM 论文：RLHF -> DPO -> HELM
- CV 应用：CV 部署与运维（MLOps）、ONNX/TensorRT 加速、实时应用、容器
- CV 论文：3D Vision -> Stable Diffusion -> DiT（Transformer & Diffusion, the core of sora）

**Task 10**：AI 安全与伦理、具身智能（Embodied AI）/机器人、多模态（Gemini 系列）、世界模型（World Models，JEPA 框架等）、自己的理解

| 阶段（Phase） | 学习内容（Learning Content） | 目标（Goal） | 预期时长（Duration） |
| :--- | :--- | :--- | :--- |
| **[高级生态](task7.md)** | AI 生态工具链（Hugging Face, LangChain, OpenMMLab, OpenCV） | **掌握工业界的核心工具**。从底层实现转向高效开发。熟练使用 Hugging Face、LangChain（LLM）与 OpenMMLab、timm（CV）等最先进生态系统，具备快速构建、训练和迭代复杂 AI 应用的能力。 | 45 天 |
| **[应用与科研](task8.md)** | 高级应用与论文阅读（Advanced RAG, Agent, YOLO, 论文复现） | **方向分化与专业深化**：成为实践者与研究者。深入 LLM（高级 RAG, Agent）与 CV（YOLO 系列, R-CNN）的最先进应用。同时，系统性阅读顶级会议论文，培养独立科研能力，实现从使用者到贡献者的转变。 | 90 天 |
| **[部署与前沿](task9.md)** | 模型部署与前沿探索（MLOps, vLLM, TensorRT, Sora, 3D Vision） | **系统部署与前沿追踪**：让 AI 落地并追踪未来。掌握 MLOps/LLMOps，学会使用 vLLM、TensorRT、ONNX 将模型部署到生产环境。同时，追踪 Sora、3D 视觉等最前沿研究，保持对技术发展的持续关注。 | 75 天 |
| **[视野与责任](task10.md)** | AI 安全、伦理与多模态 | **成为负责任的 AI 开发者**。超越技术本身，深入探讨 AI 安全、对齐与伦理问题。全面理解多模态（Multi-modal）的未来趋势，构建完整、深刻、富有责任感的 AI 世界观，为技术赋予社会价值。 | 30 天 |
