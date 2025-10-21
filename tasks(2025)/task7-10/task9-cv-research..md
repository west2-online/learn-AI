# Task 9：CV-Research

## **学习目的：从理解到创造与模拟**

你在 Task 8 中，已经完成了对CV经典神话的考古。你亲眼见证了 `AlexNet` 如何点燃深度的星星之火，`ResNet` 如何铸造深度的通天塔，以及 `R-CNN` 与 `YOLO` 如何开辟了感知的（两阶段与一阶段）两大王朝。

你已经深刻理解了AI是如何看见世界的。然而，就在感知的巅峰之上，一个全新的纪元已经拉开了序幕——**生成 (Generation)**。

**Task 9，是你从世界的观察者蜕变为世界的创造者的进阶试炼！**

此阶段的学习目的，是让你从解构过去转向洞察未来。你将不再满足于识别图像，而是要开始生成乃至模拟一个全新的世界：

* **跃迁维度 (2D -> 3D)**：你将探索 `NeRF (3D Vision)` 的奥秘，学习AI是如何仅凭几张2D照片，就在大脑中**重构**出一个完整、逼真的3D世界。
* **掌握创世 (Generation)**：你将深入 `Stable Diffusion` (Latent Diffusion) 的潜空间，理解它是如何用惊人的效率**创造**出照片级的2D图像，引爆了AIGC的革命。
* **预见模拟 (Simulation)**：你将解构 `DiT (Diffusion Transformer)` 这一 `Sora` 的核心架构，理解当生成(Diffusion)与序列王者(Transformer)结合时，AI是如何获得了**模拟物理、创造动态视频**的恐怖潜力。

完成本轮，你将不再是感知魔法的学徒，而是手握创世权柄的先驱，真正站在了CV领域未来十年的浪潮之巅。

---

## 学习内容：CV创世的三大基石

本阶段将聚焦于串联起生成式CV背后的核心论文，理解它们如何共同构筑了世界模拟器的未来。

* **重构3D世界 (3D Vision)**

  * **`NeRF`**: 学习神经辐射场 (Neural Radiance Fields) 的核心思想。理解它如何使用一个简单的MLP神经网络，去记忆一个连续的3D场景，从而实现从**任意新视角**渲染出照片级图像的惊人效果。
* **精通2D创世 (Generative Revolution)**

  * **`Stable Diffusion (LDM)`**: 学习潜在扩散模型 (Latent Diffusion Models) 为何能引爆AIGC。理解它最天才的创新点：**在潜空间(Latent Space)中进行扩散**，而不是在昂贵的像素空间，从而**极大降低了计算成本**，让高分辨率图像生成变得触手可及。
* **模拟动态世界 (The "Sora" Engine)**

  * **`DiT`**: 学习扩散型Transformer (Diffusion Transformer) 的架构革新。理解它为何**用 `Transformer` 取代了 `Stable Diffusion` 中的 `U-Net`**。`Transformer` 无与伦比的**可扩展性 (Scalability)**，正是 `Sora` 能够处理海量视频数据、学习复杂时空动态和物理规律的**秘密武器**。

---

## 推荐教程：新神话的原文 (The Papers)

这是定义生成式AI时代的论文，它们是 `Sora` 和未来世界模型的基石。

* **[3D Vision]**: **"NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis"** (Mildenhall et al., 2020)

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=NeRF:+Representing+Scenes+as+Neural+Radiance+Fields+for+View+Synthesis+paper)
* **[Stable Diffusion]**: **"High-Resolution Image Synthesis with Latent Diffusion Models"** (Rombach et al., 2022)

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=High-Resolution+Image+Synthesis+with+Latent+Diffusion+Models+paper)
* **[DiT]**: **"Scalable Diffusion Models with Transformers"** (Peebles & Xie, 2023)

  * [点击搜索论文 (Google Search)](https://www.google.com/search?q=Scalable+Diffusion+Models+with+Transformers+paper)

---

## 作业：撰写你的CV创世思想报告 (A-la-One Report)

你的任务是深入未来，撰写一份阐明创世原理的**思想演进报告**。

### **作业要求**

1. **提交形式**：

   * 一份 Markdown 报告（或 Jupyter Notebook），清晰地阐述你的分析。
2. **核心内容：连接思想的脉络**：

   * 你需要**串联**阅读上述 3 篇论文，并回答以下几个**核心问题**：
   * **[关于 NeRF]**

     * `NeRF` 是如何实现无中生有地渲染出新视角的？它与传统的3D建模（如三角网格, Meshes）在**核心原理**上有什么根本不同？
   * **[关于 Stable Diffusion]**

     * `Stable Diffusion` (LDM) 论文中提到的在潜空间(Latent Space)中扩散是它最大的贡献。请解释，为什么这一小步会成为AIGC的一大步？
   * **[关于 DiT]**

     * `DiT` 论文的核心是将 `U-Net` 替换为 `Transformer`。`Transformer` 架构（相比 `U-Net`）到底有什么**关键优势**，使得它更适合用于像 `Sora` 这样的大规模视频生成任务？
   * **[综合思考：从重构到模拟]**

     * 请用你自己的话，描述 `NeRF` (3D重构)、`Stable Diffusion` (2D生成) 和 `DiT` (可扩展生成架构) 这三者，是如何一步步铺路，最终共同指向了 `Sora` 这样的世界模拟器的？
