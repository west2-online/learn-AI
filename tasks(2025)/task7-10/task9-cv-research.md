# Task 9：CV-Research

## 学习内容

本阶段将聚焦于生成式 CV 背后的核心论文，理解它们如何共同构建了世界模拟器的基础。

- 重构 3D 世界（3D Vision）
  - `NeRF`：学习神经辐射场（Neural Radiance Fields）的核心思想。理解它如何使用一个 MLP 神经网络，去表示一个连续的 3D 场景，从而实现从任意新视角渲染出照片级图像的效果
- 精通 2D 生成（Generative Revolution）
  - `Stable Diffusion（LDM）`：学习潜在扩散模型（Latent Diffusion Models）在 AIGC 中的作用。理解它的核心创新点：在潜空间（Latent Space）中进行扩散，而不是在昂贵的像素空间，从而极大降低了计算成本，让高分辨率图像生成变得可行
- 模拟动态世界（The "Sora" Engine）
  - `DiT`：学习扩散型 Transformer（Diffusion Transformer）的架构革新。理解它为何用 `Transformer` 取代了 `Stable Diffusion` 中的 `U-Net`。`Transformer` 无与伦比的可扩展性（Scalability），正是 `Sora` 能够处理海量视频数据、学习复杂时空动态和物理规律的关键因素

## 推荐教程

这是定义生成式 AI 时代的论文，它们是 `Sora` 和未来世界模型的基石。

- [3D Vision]："NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis"（Mildenhall et al., 2020）
  - [点击搜索论文（Google Search）](https://www.google.com/search?q=NeRF:+Representing+Scenes+as+Neural+Radiance+Fields+for+View+Synthesis+paper)
- [Stable Diffusion]："High-Resolution Image Synthesis with Latent Diffusion Models"（Rombach et al., 2022）
  - [点击搜索论文（Google Search）](https://www.google.com/search?q=High-Resolution+Image+Synthesis+with+Latent+Diffusion+Models+paper)
- [DiT]："Scalable Diffusion Models with Transformers"（Peebles & Xie, 2023）
  - [点击搜索论文（Google Search）](https://www.google.com/search?q=Scalable+Diffusion+Models+with+Transformers+paper)

## 作业

你的任务是深入阅读相关论文，撰写一份阐明生成原理的思想演进报告。

### 作业要求

1. 提交形式：
   - 一份 Markdown 报告（或 Jupyter Notebook），清晰地阐述你的分析
2. 核心内容：
   - 你需要串联阅读上述 3 篇论文，并回答以下几个核心问题：
   - [关于 NeRF]
     - `NeRF` 是如何实现从新视角渲染的？它与传统的 3D 建模（如三角网格、Meshes）在核心原理上有什么根本不同？
   - [关于 Stable Diffusion]
     - `Stable Diffusion`（LDM）论文中提到的在潜空间（Latent Space）中扩散是它的重要贡献。请解释，为什么这一技术对 AIGC 的发展如此重要？
   - [关于 DiT]
     - `DiT` 论文的核心是将 `U-Net` 替换为 `Transformer`。`Transformer` 架构（相比 `U-Net`）到底有什么关键优势，使得它更适合用于像 `Sora` 这样的大规模视频生成任务？
   - [综合思考：从重构到模拟]
     - 请用你自己的话，描述 `NeRF`（3D 重构）、`Stable Diffusion`（2D 生成）和 `DiT`（可扩展生成架构）这三者，是如何一步步发展，最终共同指向了 `Sora` 这样的世界模拟器的？
