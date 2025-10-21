# Task 9：The Summit

## 学习目的：从**原型**到**成品**，从**已知**到**未来**

你已经征服了 Task 8。

* **如果你写了task8-apply**：你亲手打造了一个功能强大、逻辑复杂的**魔法原型**（一个高级RAG Agent，或一个SOTA的CV检测模型）。它在你的本地机器/开发 环境里里运行得完美无缺... 但它能承受一千个、一万个用户的同时访问吗？它能在生产环境上做到瞬时响应、坚如磐石吗？
* **如果你研究了task8-research**：你已经追溯了那些**古代神话**（BERT, ResNet...）。你理解了我们**为何**站在这里... 但你是否听到了来自**未来**的呼唤？那些正在被书写的**新神话**（DPO, Sora, NeRF），你是否敢于去直面它们、解构它们？

**Task 9，就是你从过去走到现在的实战。**

* **【应用 (The Path of Application)】**

  * **使命**：**部署 (Deployment)** 与 **运维 (Operations)**。你的使命不再是**让它跑通**，而是**让它跑得又快、又稳、又能服务万千用户**。你将成为连接**算法**与**现实**的最后一道桥梁，执掌AI在生产环境中的命脉。
  * **战场**：

    * **(LLM 应用)**：你将深入 **MLOps / LLMOps** 的核心。你的敌人是**延迟**和**成本**。你的武器是 `vLLM` (极致吞吐量), `FastAPI` (标准API), `Docker/容器化` (环境隔离), `流式传输` (用户体验), 以及 `Triton` (NVIDIA推理服务)。
    * **(CV 应用)**：你将成为**性能优化大师**。你的战场是**边缘设备**和**云端GPU**。你的武器是 `TensorRT / ONNX` (模型加速), `OpenVINO` (Intel平台), `Triton Inference Server` (工业级部署), 以及 `MLOps` 流水线 (CI/CD)。
  * **核心**：**性能、稳定、可扩展性 (Performance, Reliability, Scalability)。**

* **【论文 (The Path of Research)】**

  * **使命**：**预言 (Foreseeing)**。你的使命不再是**理解过去**，而是**解构现在，洞察未来**。你将站在时间的最前沿，去触碰那些刚刚诞生、甚至还未被完全理解的**新魔法**。
  * **战场**：

    * **(LLM)**：你将深入AI的**灵魂**——**对齐 (Alignment)**。你将直面 `RLHF` 的复杂与 `DPO` 的精妙。你将学习如何**衡量**灵魂—— `HELM` 等**整体性评估**基准。
    * **(CV)**：你将从**看懂2D**跃迁到**创造3D**。你将探索**神经渲染** (`NeRF`) 的奥秘，解构**生成模型** (`Stable Diffusion`, `DiT/Sora`) 如何凭空创造世界。
  * **核心**：**前沿论文、批判性思维、未来趋势 (Bleeding-Edge, Critical Thinking, Future Trends)。**

---

## 学习内容：

[task9-llm-apply](task9-llm-apply.md)

[task9-llm-research](task9-llm-research.md)

[task9-cv-apply](task9-cv-apply.md)

[task9-cv-research](task9-cv-research.md)
