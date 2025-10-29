# Task 6

## 学习目的（Learning Objectives）

祝贺你坚持到这里。你已经完成了前期的系统学习：在 Task 4 中，你实现了反向传播算法；在 Task 5 中，你使用模块化的方法构建了现代卷积神经网络的架构。你不再仅是调用 API 的使用者，而是真正理解神经网络内部运作机制的开发者。

现在，欢迎来到 CS231n 系列的最后阶段，也是基础学习阶段的重要总结。

在本阶段的学习中，我们将从单一的**判别式（Discriminative）**图像分类任务扩展到更广阔的领域。你将学习如何让模型**生成（Generate）**全新的数据，如何让模型结合视觉与语言进行**多模态处理（Multimodal Processing）**，以及如何在没有人工标注的情况下进行**自监督学习（Self-Supervised Learning）**。

本次任务将是你从理解经典模型到接触前沿研究的过渡。完成它，意味着你将具备初步阅读顶级会议论文、理解并实现复杂 AI 系统的核心能力。

## 学习内容（Learning Content）

本阶段你将接触到一系列定义了现代 AI 研究方向的重要模型与方法：

* **序列模型（Sequence Models）**：循环神经网络（Recurrent Neural Network, RNN）与长短期记忆网络（Long Short-Term Memory, LSTM），及其在图文生成任务中的应用。
* **注意力机制与 Transformer（Attention Mechanism and Transformer）**：理解驱动了当今大语言模型发展的核心——自注意力机制（Self-Attention），并将其应用于计算机视觉任务。
* **生成式模型（Generative Models）**：学习并实现生成对抗网络（Generative Adversarial Networks, GANs），训练一个能生成逼真图像的模型。
* **自监督学习（Self-Supervised Learning）**：学习前沿的自监督学习方法（SimCLR），了解如何在没有标签的数据上训练强大的表征模型。

## 学习要求（Learning Requirements）

与前两次作业相比，本阶段任务在代码实现上的工作量可能有所减少，但对**概念理解和系统整合能力**的要求达到了最高水平。

1. **跨领域思维**：你需要将 Task 5 中训练的 CNN 作为特征提取器（Feature Extractor），与本阶段学习的 RNN/Transformer 等序列处理器（Sequence Processor）结合起来，共同完成图文生成这一多模态任务。
2. **理解前沿方法**：GAN 的博弈论思想、Transformer 的自注意力机制、SimCLR 的对比学习范式，这些都是近十年来 AI 领域的重大突破。你需要花费大量时间阅读课程笔记，甚至尝试阅读相关的经典论文（如「Attention Is All You Need」），才能真正理解其核心思想。
3. **系统级调试**：你将要构建的是一个包含多个复杂组件的系统，调试的难度会显著上升。你需要更有耐心，并学会如何分模块进行测试和验证。

## 作业（Assignment）

**核心任务：完成 [CS231n Assignment 3](https://cs231n.github.io/assignments2025/assignment3/)**

本次考核包含多个模块，你可以根据自己的兴趣和精力选择完成的深度。

### 第一部分：图文生成 - RNN / LSTM

在这一部分，你将构建一个能够为图片生成文字描述的模型。它会接收一张图片，并生成一段描述图片内容的文字。你需要：

* 使用一个预训练好的 CNN 模型来提取图像的特征向量。
* 实现一个基于**循环神经网络（RNN）**的解码器，它会接收图像特征，并逐词生成描述语句。
* 为了解决 RNN 的长期依赖问题，你将进一步实现一个基于长短期记忆网络（LSTM）的解码器，并观察其性能提升。

### 第二部分：图文生成 - Transformer

在体验了 RNN 处理序列的模式后，你将接触到当今 AI 领域的主流方法——Transformer。你需要：

* 学习并实现**自注意力机制（Self-Attention）**和**多头注意力（Multi-Head Attention）**。
* 将 RNN 解码器替换为一个基于 **Transformer** 的解码器，再次完成图文生成任务，并与 LSTM 的结果进行比较。

### 第三部分：图像生成 - 生成对抗网络（GANs）

在这一部分，你将从理解内容转向创造内容。你将实现一个 GAN，从随机噪声中生成逼真的手写数字图像。你需要：

* 分别实现一个生成器（Generator）**和一个**判别器（Discriminator）网络。
* 理解并实现 GAN 的交替训练过程，在生成器和判别器的对抗与博弈中，让模型学会生成越来越真实的图像。

### 第四部分：自监督学习 - SimCLR

这是为学有余力的同学准备的前沿探索任务。你将接触到一种强大的无监督学习方法，它使得在海量无标签数据上预训练模型成为可能。你需要：

* 理解对比学习（Contrastive Learning）的核心思想。
* 实现 SimCLR 的关键组件，如数据增强、投影头和 NT-Xent 损失函数。

### 作业参考资料

1. [跟李沐学AI 54 循环神经网络 RNN【动手学深度学习v2】](https://www.bilibili.com/video/BV1D64y1z7CA/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)

2. [跟李沐学AI 57 长短期记忆网络（LSTM）【动手学深度学习v2】](https://www.bilibili.com/video/BV1JU4y1H7PC?spm_id_from=333.788.recommend_more_video.4&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)

3. [跟李沐学AI GAN论文逐段精读【论文精读】](https://www.bilibili.com/video/BV1rb4y187vD/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)

4. [跟着李沐学AI Transformer论文逐段精读【论文精读】](https://www.bilibili.com/video/BV1pu411o7BE/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)

5. [自监督式学习](https://www.bilibili.com/video/BV1m3411p7wD?spm_id_from=333.788.videopod.episodes&vd_source=0272bb7dd0d8d9302c55fc082442b9e3&p=46)

6. [【Transformer 其实是个简单到令人困惑的模型【白话DeepSeek-06】](https://www.bilibili.com/video/BV1C3dqYxE3q/?share_source=copy_web&vd_source=3fbbb3c2ad24817002f9c39fad247a3b)

7. [68 Transformer【动手学深度学习v2】](https://www.bilibili.com/video/BV1Kq4y1H7FL/?p=2&share_source=copy_web&vd_source=3fbbb3c2ad24817002f9c39fad247a3b)

---

## 作业要求（Assignment Requirements）

1. **严禁抄袭**。这是你的重要学习成果，请用一份独立完成的作业为这一阶段的学习画上句号。
2. **善用工具**。遇到问题时，首先尝试通过搜索引擎、官方文档和 AI 助手解决。如果仍然无法解决，欢迎在群里进行有深度的提问。
3. **拥抱 AI，但保持思考**。不限制使用 ChatGPT 等大语言模型工具，但你必须确保能完全理解模型生成的每一行代码。
4. **规范化提交**。所有作业均需通过 Git 提交到你个人的 GitHub 仓库中。

## 作业提交方式（Submission Method）

1. 你需要学习 GitHub 的使用，创建一个你自己的仓库用来存放你的代码实现
2. 接着你需要学习如何使用 Git 进行 PR 操作，在 [solutions](https://github.com/west2-online-reserve/collection-ai) 中进行操作
