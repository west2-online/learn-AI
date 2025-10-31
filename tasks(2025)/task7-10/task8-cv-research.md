# Task 8：CV-Research

## 学习目的

你已经在 Task 7 中初步接触了 `OpenCV`、`timm` 和 `OpenMMLab` 生态，这些是当今计算机视觉应用的标准工具。然而，仅仅掌握工具的使用并不足以深入理解计算机视觉技术的本质。

本阶段的学习目标是理解现代计算机视觉技术的演进脉络，通过研读经典论文，掌握核心思想的演化过程。

- **追本溯源，构建知识体系**：通过阅读奠基性论文，理解现代深度视觉技术的发展历程
- **理解技术演进规律**：当前的 SOTA 模型都是在前人工作基础上的创新。`ResNet` 解决了 `AlexNet` 面临的深度瓶颈问题；`R-CNN` 和 `YOLO` 则基于强大的分类网络（如 `ResNet`），针对检测任务提出了两种不同的解决方案
- **建立系统性思维**：完成本阶段学习后，你将建立清晰的概念框架。面对新的计算机视觉技术（如 ViT、DETR、NeRF）时，能够快速定位其在技术谱系中的位置，理解其解决的问题和继承的思想

## 学习内容

本阶段将通过研读现代计算机视觉领域的核心论文，理解技术演进的内在逻辑。

### 深度卷积网络的突破

**AlexNet**：理解其在 2012 年 ImageNet 竞赛中取得突破性成功的原因。学习其如何首次成功地将深度卷积网络（CNN）应用于大规模图像分类，以及 `ReLU` 激活函数、`GPU` 并行训练等工程技术的应用。

### 网络深度的突破

**ResNet**：深入理解网络加深过程中遇到的梯度消失和网络退化（Degradation）问题。学习 `ResNet` 如何通过残差连接（Skip Connection）解决深度网络训练的难题，使得训练成百上千层的网络成为可能，并成为后续计算机视觉任务的标准骨干网络。

### 两阶段检测范式

**R-CNN**：学习其如何将分类问题拓展到检测问题。理解其先提议、后分类（Propose then Classify）的两阶段核心思想——先使用传统方法（如 Selective Search）提取可能包含物体的区域（Region），再对每个区域使用 CNN（如 `AlexNet`）进行分类。

### 一阶段检测革命

**YOLO**：学习 `YOLO (You Only Look Once)` 如何突破 `R-CNN` 的两阶段范式。理解其端到端的设计思想——将检测视为单一的回归问题，直接在全图上预测框和类别，从而实现实时检测。

## 推荐教程

本阶段的学习资料为奠基性论文，建议至少阅读论文的摘要（Abstract）、引言（Introduction）和结论（Conclusion）部分。

- **AlexNet**: "ImageNet Classification with Deep Convolutional Neural Networks" (Krizhevsky et al., 2012) [搜索论文](https://www.google.com/search?q=ImageNet+Classification+with+Deep+Convolutional+Neural+Networks+paper)
- **ResNet**: "Deep Residual Learning for Image Recognition" (He et al., 2015) [搜索论文](https://www.google.com/search?q=Deep+Residual+Learning+for+Image+Recognition+paper)
- **R-CNN**: "Rich feature hierarchies for accurate object detection and semantic segmentation" (Girshick et al., 2014) [搜索论文](https://www.google.com/search?q=Rich+feature+hierarchies+for+accurate+object+detection+and+semantic+segmentation+paper)
- **YOLO**: "You Only Look Once: Unified, Real-Time Object Detection" (Redmon et al., 2016) [搜索论文](https://www.google.com/search?q=You+Only+Look+Once:+Unified,+Real-Time+Object+Detection+paper)

## 作业

### 论文研读报告

1. **提交形式**

以 Markdown 或 Jupyter Notebook 形式提交分析报告

2. **核心内容**

通过研读上述 4 篇（或更多）论文，回答以下核心问题：

- **AlexNet -> ResNet**
  - `AlexNet` 证明了深度网络的有效性，但为什么在其之后，简单地堆叠更深的网络会遇到困难（即网络退化问题的本质是什么）
  - `ResNet` 的残差块如何从根本上解决这个问题

- **ResNet -> R-CNN / YOLO**
  - 为什么强大的分类网络（如 `ResNet`）是 `R-CNN` 和 `YOLO` 成功的前提条件（即 Backbone 的意义）

- **R-CNN vs. YOLO**
  - 描述 `R-CNN`（两阶段）和 `YOLO`（一阶段）在核心设计思想上的主要区别
  - 这种设计差异如何导致了它们在性能上的权衡（Trade-off）
