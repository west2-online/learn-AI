# Application 1 - AI 应用认知

> [!NOTE]
> 预计耗时：14 天

## 学习目的

首先需要说明，这里的应用指的是极为顶层的 AI 应用开发，几乎不涉及底层算法实现。手搓 CNN 训练图片识别模型这类工作不属于应用，而属于算法实现。

因此应用指的是工程化地使用 AI，把 AI 作为业务链条中的一环。比如 Application 2 的 task 1，是调用大语言模型完成情感分析任务，而不是传统地训练一个情感分析器。

打一个通俗易懂的链条：

数学 -> Numpy 手算反向传播 -> Pytorch 自动推导反向传播 -> Transformer 库（Hugging Face 集成 Pytorch / TensorFlow，屏蔽底层细节，抽象出 Pipeline 的概念） -> Langchain / Dify 模块化集成（轻松调用工具） -> LLM API 屏蔽所有底层细节 -> AI 应用（调用 API 完成任务、聊天机器人、Agent 调用 API）-> harness

Application 的目的是要你站在最顶层的视角向下看，并且向下只最多接触到 Hugging Face。

从这里不难看出，AI 应用主要学习的是怎么使用 AI，而不是 AI 的底层原理。所以如果你选择了应用方向，你不只是学习 AI 调用，还需要学习后端、运维等方面的知识。

当前的 AI 应用开发主要围绕大语言模型展开。未来可能会有更多 AI 模型出现，应用开发形态也会更加多样化。

当然正如 [Task 4](../foundation/task4.md) 导引部分提到的一样，作为一个 211 的本科生，如果只拥有高级应用能力，会在就业市场上很吃亏。

所以建议学习这部分的前提是你已经掌握了一门其他语言，或者将来会去学习其他语言。

本轮作业将从传统机器学习与深度学习开始，带你认识 AI 应用。

$\color{red}{\text{再次强调，进行这部分内容前请你清晰的知道你现在在做什么。}}$

$\color{red}{\text{否则不仅晦涩难懂，而且还没什么用。}}$

## 学习内容

- 简单底层理解
- 机器学习与深度学习
- YOLO

## 作业

我们鼓励你在 Application 方向的相关作业中使用 MacOS / Linux 系统进行学习。但如果硬件条件实在有限，Windows 系统的 WSL2 依旧是一个不错的选择，相关配置教程可以参考[安装教程](https://learn.microsoft.com/zh-cn/windows/wsl/install)。

### 文档 1

大部分现代人工智能库已经提供了非常多高度封装的方法供开发者去调用，这些方法很好的屏蔽了底层的细节，使得开发者不用反复纠结于晦涩的数学公式推导，将精力放在实际的产品开发中。

但反复的实践已经证明了，只会调库其实是远远不够的，掌握部分底层相关的知识可以更好的帮助我们进行 AI 应用开发。

因此，本次的任务要求你阅读以下几份资料：

1. [Andrej Karpathy《Let's build GPT: from scratch, in code, spelled out.》](https://www.bilibili.com/video/BV1K4LPzLEoA/)

2. [nanoGPT](https://github.com/karpathy/nanoGPT)

3. [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)

4. [Schariac125 简单科普博客：自顶向下——可能要懂的底层原理简单讲解](https://schariac125.online/2026/05/31/%E8%87%AA%E9%A1%B6%E5%90%91%E4%B8%8B/)

5. （Bonus）论文 [Attention Is All You Need](https://arxiv.org/abs/1706.03762) 及其讲解视频 [Transformer 论文逐段精读【论文精读】跟李沐学 AI](https://www.bilibili.com/video/BV1pu411o7BE/?spm_id_from=333.337.search-card.all.click)

完成上述任务后，你需要写一篇文档来阐述你的理解。

> [!NOTE]
> 如果你对 Pytorch 感兴趣的话，以下是推荐你可以去阅读和完成的资料和任务，这些并不做强制性要求。
>
>1. [Pytorch 官方文档](https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
>
>2. [pytorch-deep-learning](https://github.com/mrdbourke/pytorch-deep-learning)
>
>3. 基于 mnist 数据集的 CNN 图像分类任务（资料太多了，自己找去吧）
>
>4. [Cassava Leaf Disease Classification](https://www.kaggle.com/competitions/cassava-leaf-disease-classification/overview)
>
>5. [Global Wheat Detection](https://www.kaggle.com/competitions/global-wheat-detection)
>
> 一般而言并不建议初学者一上来就去阅读 Pytorch 官方文档，你可以从 pytorch-deep-learning 项目开始做起一步步学会使用 Pytorch。

### 作业 1 - 机器学习与深度学习

LLM 的底层实现基于深度学习神经网络，深度学习的前身是机器学习。

数学建模竞赛通常涉及大量的数据处理和分析任务，近年来，深度学习方法在数学建模中的应用越来越广泛，成为解决复杂问题的有力工具。

但本次任务的重点并不是完整的数学建模，而是通过数学建模对机器学习和深度学习相关内容进行学习并且学会使用 [scikit-learn](https://scikit-learn.org/stable/) 等工具。

但我们希望你的眼光能够不止局限于 [scikit-learn](https://scikit-learn.org/stable/) 里封装好的机器学习方法，而应放眼深度学习领域，了解一些基本的深度学习知识。

本次你需要完成的任务是完成 2025 电工杯数学建模的第 2 题。数据集在参考资料中已有给出。

提示：本题的最优解是一个深度学习网络方法。

#### 基本方法

- SVM
- XGBoost
- Random Forest
- CNN
- RNN
- Transformer
- LSTM

对于这部分内容，你可以翻阅 [scikit-learn](https://scikit-learn.org/stable/) 官网来学习。

#### 下载题目

你可以从官网下载题目，参考下面两条链接：

1. [2025 电工杯下载链接](https://new.saikr.com/vse/EECMCM2025?type=notice&id=31337)
2. [2025 电工杯压缩包密码](https://new.saikr.com/vse/EECMCM2025?type=notice&id=31338)

#### 作业要求

- 请勿抄袭
- 不对大模型的使用做出限制，我们希望你能够借助大模型提升自己的知识面，但请不要直接对大模型说“帮我解决这个问题”
- 使用 uv 对你的虚拟环境进行管理
- 对于 “基本方法” 里的所有方法，你需要至少挑选 3 个（其中包含你认为的最优解）对比分析
- 你需要对原始数据进行一些处理
- 完成作业后请撰写一份文档阐述 “基本方法” 内所有方法的大致原理，“对比分析” 中你的理解与遇到的问题。请不要让大模型直接生成你的文档

#### 参考资料 - 作业 1

1. [2017 Sky Images and Photovoltaic Power Generation Dataset for Short-term Solar Forecasting (Stanford Raw)](https://purl.stanford.edu/sm043zf7254)

### 作业 2 - YOLO 的基本使用

[ShaddockNH3](https://github.com/ShaddockNH3) 是忠实的 PVZ 玩家，不过她的技术实在太差了。

直到某天她碰到 [柠檬味氨水](https://github.com/weijianxian) 对着某款枪战游戏框框画画。

“鬼！”

于是她找到了技术力差的解决方案。

YOLO 是计算机视觉领域最具代表性的单阶段目标检测算法系列，它的作用是提供一个简单的 API 来识别特定的物体。

本次任务并不会太难，目的是介绍 AI 应用领域并非只有 LLM，在视觉领域也有广泛的应用。

你需要借助 YOLO 实现一个自拟的项目，最终效果是自动化完成某些单机游戏的自动化操作。

如果你没有 idea，你可以做一个自动通关 PVZ 1-10 关的脚本。

#### 作业要求 - 作业 2

- 请不要只是做一个识别 YOLO 模型中已经包含的模型的 demo。

#### 参考资料 - 作业 2

1. [YOLO 快速使用](https://docs.ultralytics.com/zh)
2. [PVZ 原版下载](http://jspvz.com/ResDownload/1_PC_E.htm#v1.0.0.1051)
3. [PVZ 修改器](http://jspvz.com/ResDownload/Modifier.htm#v1.9)

### 作业 3 - 现代 LLM 思想

在现代的框架下，调用大语言模型只需要挑很少量的参数，例如 Temperature、Top-K、Top-P 等等，而不需要关心模型的底层实现细节。

Hugging Face 是一个友好的开源社区，在上面你可以找到绝大多数的开源模型及其参数。

尽管我们做的是上层应用，但仍应理解现代 LLM 应用是如何基于 Pipeline 这一概念构建的。

阅读 Hugging Face 官方文档教学，了解现代的 LLM 架构（例如 Pipeline），了解 Transformer 的基本原理。

1. [PyTorch 文档](https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
2. [Hugging Face 课程](https://huggingface.co/learn/llm-course/zh-CN)
3. [Transformers 文档](https://huggingface.co/docs/transformers/v5.9.0/zh/index)

在完成上述任务后，你应该写一份文档来阐述你的理解，并且做到可以完成类似 Foundation 3 作业 2 中的代码即可。
