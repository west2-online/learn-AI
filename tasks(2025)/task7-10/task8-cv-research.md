# Task 8：CV-Research

## **学习目的：从调包到洞察**

你已经在 Task 7 中初步接触了 `OpenCV`, `timm` 和 `OpenMMLab` 生态，它们是当今 CV 应用的标准套件。然而，你是否曾想过：

* 为什么 `AlexNet` 的出现，被称作CV界的宇宙大爆炸？
* 为什么 `ResNet` 能堆到152层还不会退化，它解决了什么根本问题？
* `R-CNN` 和 `YOLO`，同为目标检测，它们在设计哲学上到底有何天壤之别？

此阶段的学习目的，是让你**开始理解思想**。你将沿着 `AlexNet -> ResNet -> R-CNN -> YOLO` 这条黄金族谱，进行一次思想考古。

* **追本溯源，构筑你的思想族谱**：你将亲身回到那些神话诞生的时刻，阅读那些定义了现代深度视觉范式的奠基之作。
* **理解演化而非突变**：你将洞察到，今天我们所用的一切SOTA模型，都不是凭空出现的。`ResNet` 是对 `AlexNet` 深度瓶颈的伟大突破；而 `R-CNN` 和 `YOLO` 则是站在 `ResNet` 这样的巨人骨架上，对检测任务提出的两种截然不同的解法。
* **从调包侠到思想布道者**：完成本轮试炼，你将拥有一个清晰的概念地图。当你再次面对新的CV技术（如 ViT, DETR, NeRF）时，你将不再是盲目跟风，而是能迅速定位它在整个族谱中的位置，理解它解决了什么以及继承了什么。

这是成为一名真正AI架构师和研究者的必经之路。

---

## 学习内容：CV黄金时代的思想族谱

本阶段将聚焦于串联起现代 CV 应用背后的核心论文，理解它们之间的传承与革新。

* **深度力量的觉醒 (The Big Bang)**

  * **`AlexNet`**: 理解它为何能在 2012 年断层式地赢得 ImageNet 竞赛。学习它如何**首次成功地将深度卷积网络(CNN)应用于大规模图像分类**，以及 `ReLU` 激活函数、`GPU` 并行训练等工程技巧的开创性使用。
* **深度瓶颈的突破 (The Backbone)**

  * **`ResNet`**: 洞察在 `AlexNet` 之后，网络越堆越深时遇到的梯度消失和网络退化(Degradation)的绝境。学习 `ResNet` 是如何通过**残差连接(Skip Connection)**的精妙设计，**彻底解决了深度的诅咒**，让训练成百上千层的网络成为可能，并成为了后续所有CV任务的标准骨架。
* **两阶段检测范式的确立 (The Two-Stage)**

  * **`R-CNN`**: 学习它是如何开创性地将分类问题拓展到检测问题。理解其**先提议、后分类(Propose then Classify)的两阶段核心思想好的，主人！( ´ ▽ ` )ﾉ

完全没问题！您已经为CV的科研路线定下了 `AlexNet -> ResNet -> R-CNN -> YOLO` 这条神话族谱！

Cai酱这就来模仿您给的 `Task 8: LLM-Research` 范本，为您撰写一份平行的 `Task 8: CV-Research` 考核文档，喵~

---

# Task 8：CV-Research

## **学习目的：从调包到洞察**

你已经在 Task 7 中初步接触了 `OpenCV`, `timm` 和 `OpenMMLab` 生态，它们是当今 CV 应用的标准套件。然而，你是否曾想过：

* 为什么 `AlexNet` 的出现，被称作CV界的宇宙大爆炸？
* 为什么 `ResNet` 能堆到152层还不会退化，它解决了什么根本问题？
* `R-CNN` 和 `YOLO`，同为目标检测，它们在设计哲学上到底有何天壤之别？

如果你在应用路线上感到知其然，而不知其所以然，那么 **Task 8 的科研路线，就是为你铸魂的时刻！**

此阶段的学习目的，是让你**停止追逐SOTA，开始理解思想**。你将沿着 `AlexNet -> ResNet -> R-CNN -> YOLO` 这条黄金族谱，进行一次思想考古。

* **追本溯源，构筑你的思想族谱**：你将亲身回到那些神话诞生的时刻，阅读那些定义了现代深度视觉范式的奠基之作。
* **理解演化而非突变**：你将洞察到，今天我们所用的一切SOTA模型，都不是凭空出现的。`ResNet` 是对 `AlexNet` 深度瓶颈的伟大突破；而 `R-CNN` 和 `YOLO` 则是站在 `ResNet` 这样的巨人骨架上，对检测任务提出的两种截然不同的解法。
* **从调包侠到思想布道者**：完成本轮试炼，你将拥有一个清晰的概念地图。当你再次面对新的CV技术（如 ViT, DETR, NeRF）时，你将不再是盲目跟风，而是能迅速定位它在整个族谱中的位置，理解它解决了什么以及继承了什么。

这是成为一名真正AI架构师和研究者的必经之路。

---

## 学习内容：CV黄金时代的思想族谱

本阶段将聚焦于串联起现代 CV 应用背后的核心论文，理解它们之间的传承与革新。

* **深度力量的觉醒 (The Big Bang)**

  * **`AlexNet`**: 理解它为何能在 2012 年断层式地赢得 ImageNet 竞赛。学习它如何**首次成功地将深度卷积网络(CNN)应用于大规模图像分类**，以及 `ReLU` 激活函数、`GPU` 并行训练等工程技巧的开创性使用。
* **深度瓶颈的突破 (The Backbone)**

  * **`ResNet`**: 洞察在 `AlexNet` 之后，网络越堆越深时遇到的梯度消失和网络退化(Degradation)的绝境。学习 `ResNet` 是如何通过**残差连接(Skip Connection)**的精妙设计，**彻底解决了深度的诅咒**，让训练成百上千层的网络成为可能，并成为了后续所有CV任务的标准骨架。
* **两阶段检测范式的确立 (The Two-Stage)**

  * **`R-CNN`**: 学习它是如何开创性地将分类问题拓展到检测问题。理解其**先提议、后分类(Propose then Classify)的两阶段核心思想**——即先用传统方法（如 Selective Search）找出可能有物体的区域(Region)，再对每个区域用CNN（如 `AlexNet`）去识别。
* **一阶段检测革命 (The One-Stage)**

  * **`YOLO`**: 学习 `YOLO (You Only Look Once)` 是如何**彻底颠覆** `R-CNN` 体系的。理解其**一步到位的端到端哲学**——它将检测视为一个**单一的回归问题**，直接在全图上预测框和类别，从而实现了**前所未有的实时检测速度**。

---

## 推荐教程：神话的原文 (The Papers)

本阶段的教程不再是文档或博客，而是那些定义了时代的原始论文。请至少阅读它们的摘要(Abstract)、引言(Introduction)和结论(Conclusion)。

* **[AlexNet]**: **"ImageNet Classification with Deep Convolutional Neural Networks"** (Krizhevsky et al., 2012)

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=ImageNet+Classification+with+Deep+Convolutional+Neural+Networks+paper)
* **[ResNet]**: **"Deep Residual Learning for Image Recognition"** (He et al., 2015)

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=Deep+Residual+Learning+for+Image+Recognition+paper)
* **[R-CNN]**: **"Rich feature hierarchies for accurate object detection and semantic segmentation"** (Girshick et al., 2014)

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=Rich+feature+hierarchies+for+accurate+object+detection+and+semantic+segmentation+paper)
* **[YOLO]**: **"You Only Look Once: Unified, Real-Time Object Detection"** (Redmon et al., 2016)

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=You+Only+Look+Once:+Unified,+Real-Time+Object+Detection+paper)

---

## 作业：撰写你的CV思想族谱报告 (A-la-One Report)

在应用路线的同学在配置 `mmdetection` 跑通 `YOLO` 项目时，你的任务是构建一个All-in-One Insight——一份阐明你所有见解的**思想族谱报告**。

### **作业要求**

1. **提交形式**：

   * 一份 Markdown 报告（或 Jupyter Notebook），清晰地阐述你的分析。
2. **核心内容：连接思想的脉络**：

   * 你需要**串联**阅读上述 4 篇（或更多）论文，并回答以下几个**核心问题**：
   * **[AlexNet -> ResNet]**

     * `AlexNet` 证明了深是好的，但为什么在它之后，人们无法简单地堆叠出更深的网络？（即网络退化问题是什么？）
     * `ResNet` 的残差块是如何从**根本上**解决这个问题的？
   * **[ResNet -> R-CNN / YOLO]**

     * 为什么一个强大的分类网络（如 `ResNet`）是 `R-CNN` 和 `YOLO` 成功的**先决条件**？（即Backbone的意义是什么？）
   * **[R-CNN vs. YOLO]**

     * 请用你自己的话，描述 `R-CNN`（两阶段）和 `YOLO`（一阶段）在**核心设计哲学**上的**最大区别**。
     * 这个哲学区别是如何直接导致了它们俩最著名的性能权衡（Trade-off）的？（提示：一个准而慢，一个快但（早期）没那么准）
——即先用传统方法（如 Selective Search）找出可能有物体的区域(Region)，再对每个区域用CNN（如 `AlexNet`）去识别。
* **一阶段检测革命 (The One-Stage)**

  * **`YOLO`**: 学习 `YOLO (You Only Look Once)` 是如何**彻底颠覆** `R-CNN` 体系的。理解其**一步到位的端到端哲学**——它将检测视为一个**单一的回归问题**，直接在全图上预测框和类别，从而实现了**前所未有的实时检测速度**。

---

## 推荐教程：神话的原文 (The Papers)

本阶段的教程不再是文档或博客，而是那些定义了时代的原始论文。请至少阅读它们的摘要(Abstract)、引言(Introduction)和结论(Conclusion)。

* **[AlexNet]**: **"ImageNet Classification with Deep Convolutional Neural Networks"** (Krizhevsky et al., 2012)

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=ImageNet+Classification+with+Deep+Convolutional+Neural+Networks+paper)
* **[ResNet]**: **"Deep Residual Learning for Image Recognition"** (He et al., 2015)

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=Deep+Residual+Learning+for+Image+Recognition+paper)
* **[R-CNN]**: **"Rich feature hierarchies for accurate object detection and semantic segmentation"** (Girshick et al., 2014)

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=Rich+feature+hierarchies+for+accurate+object+detection+and+semantic+segmentation+paper)
* **[YOLO]**: **"You Only Look Once: Unified, Real-Time Object Detection"** (Redmon et al., 2016)

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=You+Only+Look+Once:+Unified,+Real-Time+Object+Detection+paper)

---

## 作业：撰写你的CV思想族谱报告 (A-la-One Report)

你的任务是构建一个All-in-One Insight——一份阐明你所有见解的**思想族谱报告**。

### **作业要求**

1. **提交形式**：

   * 一份 Markdown 报告（或 Jupyter Notebook），清晰地阐述你的分析。
2. **核心内容：连接思想的脉络**：

   * 你需要**串联**阅读上述 4 篇（或更多）论文，并回答以下几个**核心问题**：
   * **[AlexNet -> ResNet]**

     * `AlexNet` 证明了深是好的，但为什么在它之后，人们无法简单地堆叠出更深的网络？（即网络退化问题是什么？）
     * `ResNet` 的残差块是如何从**根本上**解决这个问题的？
   * **[ResNet -> R-CNN / YOLO]**

     * 为什么一个强大的分类网络（如 `ResNet`）是 `R-CNN` 和 `YOLO` 成功的**先决条件**？（即Backbone的意义是什么？）
   * **[R-CNN vs. YOLO]**

     * 请用你自己的话，描述 `R-CNN`（两阶段）和 `YOLO`（一阶段）在**核心设计哲学**上的**最大区别**。
     * 这个哲学区别是如何直接导致了它们俩最著名的性能权衡（Trade-off）的？（提示：一个准而慢，一个快但（早期）没那么准）
