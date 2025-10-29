# Task 9：CV Apply

## 学习目的

你已经在 Task 8 中成功训练出了一个高性能、高精度的计算机视觉模型。它是一个出色的原型（Prototype），成功验证了你的技术构想。

然而，在工业界的实际应用中，原型和产品（Product）之间存在显著差距。一个只能在本地 GPU 上运行、一次只能处理一张图片、响应缓慢且未经优化的原型，无法在现实世界中创造价值。

Task 9 是你将原型转化为工业级系统的关键阶段。

本阶段的学习目标包括：

- **掌握服务化核心技术**：学习如何将 Task 8 的 Python 代码重构并封装成标准化的、高性能的 Web API（如 `FastAPI` 或 `gRPC`），使模型能被任何客户端调用
- **掌握性能优化技术**：学习使用业界顶尖的 CV 推理加速引擎。通过将 PyTorch 模型转换为 `ONNX` 格式，并进一步用 `TensorRT` 编译，将模型的推理速度（FPS）提升数倍乃至数十倍
- **掌握容器化技术**：学习使用 **Docker** 将复杂的应用（包括所有依赖、模型、加速引擎、配置）打包成标准、轻量、可移植的容器，实现在任何地方一键运行，尤其是在带 NVIDIA GPU 的环境中
- **掌握监控与运维基础**：学习使用 **Prometheus** 和 **Grafana** 为 GPU 服务构建监控系统。学习如何度量服务的健康状况（如 FPS、延迟、GPU 利用率），这是实现运维的第一步
- **掌握工程化思维**：学习使用 `Streamlit` 等工具构建独立的前端 UI，并使用 `Docker Compose` 编排后端 API 服务、前端 UI 服务乃至监控服务，构建多服务协同的复杂应用系统

完成本阶段学习后，你将具备将 CV 创意转化为可部署、可扩展、高性能、高可用、可观测的生产级服务的能力。

## 学习内容

### Web API 框架

- **FastAPI（推荐）**：学习这个现代、高性能的 Python Web 框架
  - 掌握如何定义路由（`@app.post`）和文件上传（`UploadFile`）
  - 学习如何处理图像数据（`BytesIO`、`Pillow`、`NumPy`）并返回 JSON 结果或处理后的图像
- **gRPC / Protobuf（更推荐）**：学习 Google 的高性能 RPC 框架
  - 学习如何编写 `.proto` 文件来定义服务和图像消息（`bytes`）

### 高性能推理引擎

- **ONNX（Open Neural Network Exchange）**：学习这个开放的模型交换格式
  - 学习如何使用 `torch.onnx.export` 将 PyTorch 模型（`.pth`）转换为 `ONNX` 格式（`.onnx`）
- **TensorRT（NVIDIA 推荐）**：学习 NVIDIA 的推理优化器
  - 学习如何使用 `trtexec`（命令行工具）或 `TensorRT Python API` 将 `.onnx` 模型编译成高度优化的 `.engine` 文件
  - 学习如何使用 `onnxruntime-gpu` 或 `TensorRT runtime` 来加载并运行优化后的模型

### 服务运维与监控

- **Prometheus & Grafana**：学习监控系统的构建
- **指标暴露（Metrics Exposing）**：学习 `prometheus-fastapi-instrumentator` 库
- **自定义指标（Custom Metrics）**：学习如何使用 `prometheus-client` 库，手动创建并更新自定义指标，例如 `inference_fps`（每秒推理帧数）或 `gpu_utilization`（GPU 利用率，可通过 `pynvml` 库获取）

### 前端原型工具

- **Streamlit（推荐）**：学习这个简单的 Python 前端框架
  - 学习 `st.file_uploader` 来构建图像上传界面
  - 学习如何在 Streamlit 客户端中调用（`requests`）FastAPI 后端，并展示返回的检测结果（画框）

### 容器化与编排

- **Docker**：
  - 学习如何为 `FastAPI` + `TensorRT` 应用编写 `Dockerfile`
  - 理解如何构建能调用 NVIDIA GPU 的 Docker 镜像（如使用 `nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04` 作为基础镜像）并安装 `TensorRT`
- **Docker Compose**：学习如何使用它来编排所有服务

- --

## 推荐教程

- **API**
  - [FastAPI 官方文档](https://fastapi.tiangolo.com/zh/)（中文版，重点参考 `Request Files` 章节）
- **高性能推理**
  - [PyTorch to ONNX 官方教程](https://pytorch.org/tutorials/advanced/super_resolution_with_onnxruntime.html)
  - [TensorRT 官方文档（Python API）](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#python_api)
  - [B站/知乎搜索 PyTorch 转 TensorRT 实战](https://www.google.com/search?q=pytorch+tensorrt+tutorial)
- **运维与监控**
  - [Prometheus 官方文档](https://prometheus.io/docs/introduction/overview/)
  - [Grafana 官方文档](https://grafana.com/docs/grafana/latest/getting-started/)
  - [prometheus-client（Python 库）](https://github.com/prometheus/client_python)（学习自定义指标）
- **前端与容器化**
  - [Streamlit 官方文档](https://docs.streamlit.io/en/stable/)（重点参考 `File Uploader` 章节）
  - [NVIDIA Container Toolkit（Docker GPU 支持）](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)（必读）
  - [Docker Compose 官方教程](https://docs.docker.com/compose/gettingstarted/)

## 作业

本轮作业重点为服务化、容器化、高性能和可观测性。你需要将 Task 8 的 All-in-One 项目进行全面重构，转化为现代化的多服务协同云原生应用。

### 作业 1：服务化升级（API、ONNX、TensorRT）

**目标**：将 Task 8 的模型封装为高性能、可度量的 API。

1. **代码重构**：将 Task 8 的 Jupyter Notebook 代码彻底重构为 `.py` 模块
2. **模型转换**：
   - **核心要求**：将你在 Task 8 训练好的 PyTorch 模型（`.pth`）导出为 ONNX 格式（`.onnx`）
   - **高级要求**：使用 `trtexec` 或 Python API，将 `.onnx` 模型进一步编译为 TensorRT engine（`.engine`）
3. **构建 API（FastAPI/gRPC）**：
   - 创建一个 `main.py` 并使用 `FastAPI` 构建一个 `/detect` 路由，该路由接收上传的图片
   - **核心要求**：在这个路由的背后，必须使用 `onnxruntime-gpu` 或 `TensorRT runtime` 来加载并运行你转换后的模型进行推理，而不是 PyTorch
4. **暴露监控指标**：
   - 使用 `prometheus-fastapi-instrumentator` 库，为你的 FastAPI 应用自动添加 `/metrics` 接口
   - **高级要求**：使用 `prometheus-client` 库，手动创建并暴露至少 2 个自定义指标：
     - `inference_latency_seconds`（推理延迟）
     - `images_processed_total`（已处理图片总数）

### 作业 2：容器化与编排（Docker & UI）

**目标**：为你的服务构建一个同时支持"静态上传"和"实时视频流"的前端 UI，并使用 Docker Compose 将其与后端打包成一个完整的应用系统。

1. **构建客户端 UI（`Streamlit`）**：

   * 创建一个独立的 `app.py`（例如放在 `frontend/` 目录）。
   * **核心要求 1（静态模式）**：使用 `st.file_uploader` 构建一个**文件上传**界面。这个界面必须通过 `requests` **调用**你在 `作业 1` 中构建的后端 API，并将返回的画好框的图片展示出来。
   * **核心要求 2（实时模式）**：使用 `streamlit-webrtc` 库，为你的前端应用增加一个**实时摄像头检测**功能。用户点击按钮后，应用应该能：

     1. 启动用户的摄像头。
     2. 实时捕获视频帧。
     3. 将视频帧持续不断地发送给你的后端 API
     4. 接收后端返回的结果，并将检测框实时地绘制在视频画面上返回给用户
2. **为后端编写 `Dockerfile`**：
   - **核心要求**：在作业 1 的目录（`backend/`）下，编写一个 `Dockerfile`
   - 这个 `Dockerfile` 必须使用 `nvidia/cuda` 相关的镜像作为基础，并能正确安装 `TensorRT`、`CUDA` 依赖和你的 Python 库
3. **使用 `Docker Compose` 编排**：
   - 在项目根目录，编写一个 `docker-compose.yml`
   - **核心要求**：这个文件必须定义至少两个服务：`backend` 和 `frontend`
   - 你需要正确配置 `backend` 服务的 `deploy.resources.reservations.devices` 字段，以确保容器可以访问到主机的 NVIDIA GPU

### 作业 3：监控仪表盘

**目标**：为你的应用构建完整的监控系统。

1. **编写 `prometheus.yml`**：
   - 创建一个 `prometheus.yml` 配置文件，并定义抓取目标，指向你的 `backend:8000/metrics` 接口
2. **升级 `docker-compose.yml`**：
   - 在作业 2 的基础上，再添加两个服务：`prometheus` 和 `grafana`
   - 现在，当你运行 `docker compose up --build` 时，你应该能同时启动 4 个服务
3. **构建监控仪表盘**：
   - 启动后，访问 `http://localhost:3000`（Grafana）
   - 手动完成：添加 Prometheus 数据源，并创建一个新的 Dashboard
   - **核心要求**：在你的 Dashboard 上，必须创建至少 4 个 Panel（图表），展示以下关键指标：
     - **API QPS**（每秒请求数，来自 FastAPI）
     - **API 延迟**（p99 延迟，来自 FastAPI）
     - **自定义指标：平均推理延迟**（来自你手动暴露的 `inference_latency_seconds`）
     - **系统级：GPU 利用率**（需要额外部署 `dcgm-exporter`，作为加分项/选做，或用 `pynvml` 在代码中暴露）

### 作业 4：报告与演示

1. 以 Markdown 或 Jupyter Notebook 形式提交你的报告，并附上你的项目结构和所有代码、配置文件
2. 在报告中，请详细说明：
   - 你是如何将 `.pth` 成功转换为 `.onnx` 乃至 `.engine` 的？对比一下转换前后的模型推理速度
   - 你是如何编写一个支持 GPU 的 `Dockerfile` 的？
   - 你的 `docker-compose.yml` 是如何协同四个服务（`frontend`、`backend`、`prometheus`、`grafana`）并分配 GPU 资源的？
   - **新增核心**：你是如何实现"实时视频流"检测的？请描述你的前端（`streamlit-webrtc`）和后端（`FastAPI`）是如何协作来处理视频流的
3. **最终演示**：
   - 你需要清晰地展示：你只需要在命令行中运行 `docker compose up --build`，你的应用（包含 UI 和 API）就能一键启动
   - 你需要截图你在浏览器（`http://localhost:8501`）中上传图片并成功获得检测结果的界面
   - **性能测试**：你必须截图你转换模型前后，推理速度（FPS 或延迟）的对比测试结果
   - **运维测试**：你必须截图你在浏览器（`http://localhost:3000`）中成功配置的、包含那 4 个关键指标的 Grafana 监控仪表盘
   - **终极演示**：你必须录制一段简短的视频或 GIF，展示你的实时摄像头检测功能。视频需要清晰地展示出，你本人（或一个物体）在摄像头前移动，而你的系统能够流畅、准确地进行实时跟踪检测。同时，请将 Grafana 仪表盘放在旁边，让我们能看到在"实时"压力下，你的 QPS、延迟、GPU 利用率等指标的动态变化
