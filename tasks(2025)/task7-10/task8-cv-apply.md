# Task 8：CV-Apply

## 学习内容

### 自定义数据集构建

- 数据收集：从网络（Task 2）、公开数据集或自行拍摄等渠道，获取针对特定任务的原始图像
- 数据标注：学习使用专业的标注工具（如 `LabelImg`、`LabelMe`、`CVAT`），为图像数据制作目标检测（Bounding Box）或实例分割（Polygon）标签
- 数据格式转换：学习如何将标注数据转换为常用框架所需的格式（如 `COCO JSON` 或 `YOLO TXT`）

### SOTA 模型微调

- 工业级框架深入：深入学习 `OpenMMLab`（如 `MMDetection`）或 `Ultralytics (YOLO)` 等主流框架，掌握其配置文件驱动（Config-driven）的训练方式
- 模型选型与训练：根据任务需求（速度 vs 精度），选择合适的模型（如 `YOLOv8`、`Faster R-CNN`、`Mask R-CNN`），加载预训练权重，并在自定义数据集上进行微调
- 关键指标解读：深入理解衡量模型性能的核心指标，如 `mAP`（mean Average Precision）用于目标检测，`mIoU`（mean Intersection over Union）用于分割

### 高级数据增强

深入学习 `Albumentations`，掌握如何构建适用于特定场景的数据增强流水线（如 `Compose`），应用 `Mosaic`、`MixUp` 等高级增强策略，有效抑制过拟合。

### 模型分析与可视化

- 学习如何将模型的预测结果（检测框、分割蒙版）可视化到原始图片上
- 分析模型的失败案例（Failure Cases），思考可能的原因与改进方向

## 推荐教程

### 数据标注

- [LabelImg（目标检测标注）](https://github.com/HumanSignal/labelImg)
- [LabelMe（分割/多边形标注）](https://github.com/HumanSignal/labelme)
- [CVAT.ai（开源在线标注平台）](https://www.cvat.ai/)

### 模型训练框架

- [Ultralytics YOLOv8 官方文档](https://docs.ultralytics.com/)
- [OpenMMLab MMDetection 官方文档](https://mmdetection.readthedocs.io/en/latest/)
- [B 站/知乎搜索 YOLOv8/MMDetection 训练自定义数据集](https://www.google.com/search?q=YOLOv8+%E8%AE%AD%E7%BB%83%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%B0%E6%8D%AE%E9%9B%86)

## 作业

本阶段的考核重点是项目完整性和解决实际问题的能力。你需要将 task1-7 学到的技能整合成一个完整的应用项目。

### 作业 1：数据集构建

1. 定义问题，选择一个具有实际价值的视觉任务（例如：识别特定种类的花卉、检测教室里空余的座位、识别围棋棋盘上的棋子等）

2. 收集并标注数据

- 收集至少 100-200 张相关图片
- 使用 `LabelImg`（检测）或 `LabelMe`（分割）等工具完成数据标注工作，并划分为训练集和验证集

### 作业 2：模型训练与调优

1. 选择框架与模型，选择一个主流框架（推荐 `YOLOv8` 或 `MMDetection`）和一个 SOTA 模型
2. 配置与训练
    1. 将阶段一制作的数据集转换为框架要求的格式
    2. 通过修改配置文件，配置数据集路径、模型参数、训练策略（如学习率、迭代次数），并启动训练
3. 调优或对比实验（至少完成以下一项）
    1. 优化 A（数据增强）：设计两套不同的数据增强策略（一套简单，一套复杂），对比它们对最终模型性能（`mAP` / `mIoU`）的影响
    2. 优化 B（模型对比）：使用完全相同的数据和训练配置，训练两个不同的模型（如 `YOLOv8s` vs `YOLOv8m`，或 `Faster R-CNN` vs `RetinaNet`），并对比分析它们的性能差异

### 作业 3：评估、分析与可视化

1. 评估模型，在验证集上运行评估脚本，得到并报告模型的核心性能指标（`mAP` / `mIoU`）
2. 可视化结果，编写脚本，将模型应用在测试图片（从未用于训练或验证）上，并将检测框或分割蒙版可视化到图片上

### 作业 4：报告与演示

1. 以 Jupyter Notebook 或 Markdown 形式提交代码和分析报告

2. 报告中需详细说明：
    1. 项目设计（要解决什么问题）、数据收集与标注流程
    2. 模型训练配置（使用了哪个模型、关键参数是什么）
    3. 实验过程与结果对比分析
    4. 最终模型的性能指标，以及对结果的分析
3. 最终演示：

展示至少 5 张测试图片的可视化结果。这些结果需要能清晰地展示出模型在不同场景下的表现（需要包含成功和失败的案例），并对失败的案例进行简要的原因分析
