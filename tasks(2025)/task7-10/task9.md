# Task 9

## 学习目的

你已经完成了 Task 8 的学习。

- **如果你完成了 task8-apply**：你构建了一个功能强大、逻辑复杂的应用原型（一个高级 RAG Agent，或一个 SOTA 的 CV 检测模型）。它在本地开发环境里运行良好，但是否能承受大量用户的同时访问？能否在生产环境上做到高效响应和稳定运行？
- **如果你完成了 task8-research**：你已经研读了那些奠基性论文（BERT、ResNet 等），理解了我们为何站在这里。但你是否关注到正在被书写的新技术（DPO、Sora、NeRF）？

Task 9 是你从理论到实践的进阶阶段。

### 应用路线（Apply）

- **核心目标**：部署（Deployment）与运维（Operations）。你的目标不再是让系统运行，而是让它运行得高效、稳定，能够服务大量用户
- **学习方向**：
  - **LLM 应用**：深入学习 MLOps / LLMOps 的核心技术。你将面对延迟和成本的挑战，使用 `vLLM`（高吞吐量）、`FastAPI`（API 标准化）、`Docker/容器化`（环境隔离）、`流式传输`（用户体验优化），以及 `Triton`（NVIDIA 推理服务）等工具
  - **CV 应用**：学习性能优化技术。你的学习重点是边缘设备和云端 GPU 的部署，使用 `TensorRT / ONNX`（模型加速）、`OpenVINO`（Intel 平台）、`Triton Inference Server`（工业级部署），以及 `MLOps` 流水线（CI/CD）
- **关键词**：性能、稳定性、可扩展性（Performance, Reliability, Scalability）

### 研究路线（Research）

- **核心目标**：前沿探索。你的目标不再是理解过去，而是解读现在，洞察未来。你将学习那些刚刚诞生、甚至还未被完全理解的新技术
- **学习方向**：
  - **LLM**：深入学习 AI 对齐（Alignment）技术。你将研究 `RLHF` 和 `DPO` 的原理，学习如何使用 `HELM` 等整体性评估基准衡量模型能力
  - **CV**：从 2D 理解跃迁到 3D 创造。你将探索神经渲染（`NeRF`）的原理，研究生成模型（`Stable Diffusion`、`DiT/Sora`）如何生成图像和视频
- **关键词**：前沿论文、批判性思维、未来趋势（Bleeding-Edge, Critical Thinking, Future Trends）

## 学习内容

[task9-llm-apply](task9-llm-apply.md)

[task9-llm-research](task9-llm-research.md)

[task9-cv-apply](task9-cv-apply.md)

[task9-cv-research](task9-cv-research.md)
