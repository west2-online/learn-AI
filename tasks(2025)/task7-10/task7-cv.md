# Task 7：CV

## **学习目的：从理解原理到高效实践**

你已经成功穿越了深度学习前沿的重重迷雾，亲手触及并理解了诸如 **CNN** 和 **Transformer** 这样改变世界的魔法核心。你现在已经能够深刻洞察这些视觉模型（CV）的底层运作机制，甚至可以从零开始勾勒出它们的符文结构（比如卷积层和注意力层）。

然而，真正的力量，并非仅仅在于理解咒语的构成，更在于如何巧妙地运用这些咒语，去解决现实世界中纷繁复杂的问题。回想一下，当你需要快速施展一个强大的视觉法术（比如训练一个高精度的SOTA模型）时，你是会选择从头开始刻画每一个卷积核，还是会直接拿起那柄由无数先贤共同淬炼、镶满了奥秘符文的**传奇法杖**呢？

**Task 7，正是你从理论家向CV高效开发者蜕变的关键时刻！**

此阶段的学习目的在于：

* **拥抱业界最强生态，效率至上**：你将告别纯粹的底层复现与手搓模型，转而拥抱并深度掌握由全球AI社区共同构建的、工业界最顶尖的 CV 魔法圣器——以 **OpenMMLab**, **timm**, **Albumentations** 和 **OpenCV** 为代表的工具链。学习如何高效地加载SOTA模型、构建复杂数据增强、并使用框架驱动训练，让你的开发效率实现质的飞跃。
* **掌握核心视觉魔法，实现核心功能**：你将不仅仅停留在手写训练循环的层面。你将学习如何灵活运用这些生态工具，通过标准化的配置（Configs）和强大的API，高效实现**图像分类**、**目标检测**、**图像分割**等基础而强大的视觉智能功能。
* **奠定CV实战基础，指引未来方向**：通过本阶段的学习与实践，你将建立起扎实的 CV 应用开发能力，清楚地了解从数据处理、模型选型、SOTA训练范式到应用原型设计的全链路。这不仅是技能树的拓展，更是你未来在 CV 领域进行更高级部署、前沿科研探索及商业化落地的坚实基石。你将从一个旁观者，成长为一名能够真正创造和引领视觉智能未来的先行者。

---

## **学习内容：解锁视觉魔法的工具宝库**

本阶段将聚焦于 CV 领域最核心、最实用的应用开发工具与技术，助你从理论走向实践。

* **`OpenCV`：你的数字暗房**

  * **图像I/O**：深入学习 `cv2.imread`, `cv2.imwrite`, `cv2.imshow`，掌握不同图像格式的读写。
  * **色彩空间**：理解并实践 `cv2.cvtColor` (如 BGR <-> RGB, BGR <-> GRAY)。
  * **基础变换**：掌握 `cv2.resize`, `cv2.flip`, `cv2.rotate`。
  * **图像处理**：学习高斯模糊 (`GaussianBlur`)、边缘检测 (`Canny`)、形态学操作 (`erode`, `dilate`) 等经典算法。

* **`Albumentations`：你的SOTA数据增强工坊**

  * **核心 Pipeline**：理解 `A.Compose` 的概念，学习如何构建一个强大的、可序列化的数据增强流水线。
  * **像素级增强**：掌握 `RandomBrightnessContrast`, `CLAHE`, `ColorJitter` 等。
  * **空间级增强**：掌握 `ShiftScaleRotate`, `Perspective`, `GridDistortion` 等。
  * **特定任务增强**：了解如何将其应用于目标检测（同步增强BBox）和分割（同步增强Mask）。

* **`timm` (PyTorch Image Models)：你的SOTA模型军械库**

  * **`timm.create_model`**：学习如何**一键加载**海量的预训练模型（如 `ResNet`, `ViT`, `SwinTransformer`, `ConvNeXt` 等）。
  * **特征提取**：学习如何使用 `features_only=True` 或 `get_intermediate_layers` 来获取模型的中间层特征图（Feature Maps）。
  * **模型微调**：理解如何替换 `timm` 模型的分类头 (`classifier` / `head`) 以适应你自己的任务。

* **`OpenMMLab` 生态 (重点)：你的AI航母战斗群**

  * **`MMCV` / `MMEngine`**：理解 `OpenMMLab` 的灵魂——**Config 配置文件系统**和**注册器 (Registry)** 机制。这是你驾驭整个生态的基础。
  * **`MMPretrain` (原 MMClassification)**：

    * **核心实践**：学习如何**不写一行训练代码**，仅通过修改 `Config` 文件，来**复现**一个SOTA的图像分类模型（如在 CIFAR-10 或 ImageNet 上的 ResNet）。
    * 学习 `tools/train.py` 和 `tools/test.py` 脚本的使用。
  * **`MMDetection` (目标检测)**：

    * (初探) 了解 `MMDetection` 的 `Config` 结构，知道如何配置一个数据-模型-训练策略的检测任务。
  * **`MMSegmentation` (图像分割)**：

    * (初探) 了解 `MMSegmentation` 的 `Config` 结构，知道如何配置一个分割任务。

---

## **推荐教程：通往CV世界的权威指引**

* **OpenCV 官方文档与教程 (中文友好)**

  * [OpenCV-Python 教程 (官方)](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
  * [B站 搜索 OpenCV Python](https://www.google.com/search?q=OpenCV+Python+%E6%95%99%E7%A8%8B+Bilibili) (有大量的入门和实战教程)
* **Albumentations 官方文档 (实例丰富)**

  * [Albumentations 官方文档](https://albumentations.ai/docs/) (重点看 `Examples` 和 `API Reference`)
* **timm 官方文档与社区**

  * [timm 官方文档](https://timm.fast.ai/) (虽然简洁，但 `README` 和 `Docs` 包含核心用法)
  * [Hugging Face Spaces 上的 timm 模型搜索](https://huggingface.co/models?library=timm)
* **OpenMMLab 官方文档与教程 (中文支持完善)**

  * [OpenMMLab 2.0 官方文档 (中文)](https://www.google.com/search?q=https://openmmlab.com/docs/zh_cn/) (**必读**，从MMEngine: OpenMMLab 2.0 核心开始)
  * [MMPretrain (MMClassification) 官方教程](https://www.google.com/search?q=https://mmpretrain.readthedocs.io/zh-CN/latest/user_guides/basics.html) (重点看Config 文件和训练与测试)
  * [OpenMMLab B站官方账号](https://www.google.com/search?q=https://space.bilibili.com/1275924838) (有大量的入门和实战视频)
* **实战平台 Kaggle**

  * 关注 Kaggle 上的 CV 竞赛，查看 Top 选手的 Notebooks，学习他们是如何组合使用 `Albumentations` 和 `timm` 的。

## **作业：CV入门试炼**

### **作业1: 魔法照片的百变戏法 (OpenCV & Albumentations)**

在我们正式开始训练强大的模型之前，首先要学会如何料理我们的材料——也就是图像数据。

**要求：**

1. 请先找一张你最喜欢的图片（比如...可爱的小猫咪图片），使用 `OpenCV` 将它读取进来。
2. **基本变换 (OpenCV)**：

   * 将这张图片缩放（`resize`）到 `256x256` 像素。
   * 将彩色图片转换为**灰度图** (`GRAY`)。
   * 将原图进行一次**水平翻转** (`flip`)。
   * 请将处理后的三张图片并排显示出来（可以使用 `matplotlib` 辅助显示）。
3. **高级增强 (Albumentations)**：

   * 使用 `Albumentations.Compose` 构建一个数据增强流水线。
   * 在这个流水线中，请至少包含 **3 种**不同的增强操作，例如：

     * 随机亮度或对比度调整 (`RandomBrightnessContrast`)
     * 随机旋转、缩放、平移 (`ShiftScaleRotate`)
     * 添加一些随机噪点 (`GaussNoise`)
   * 将你的原始图片输入到这个流水线中，循环 **5 次**，并将这 5 张被魔法变得焕然一新的图片展示出来，感受一下数据增强的威力吧！

---

### **作业2: 召唤SOTA军械库 (timm)**

`timm` 就像一个传说中的军械库，里面收藏着无数由先贤打造的、战功赫赫的SOTA英灵（预训练模型）。现在让我们来学习如何召唤并驾驭它们。

**要求：**

1. **召唤模型**：

   * 使用 `timm.create_model`，加载一个预训练好的 `resnet50` 模型。
   * 打印出这个模型的结构，观察它的不同层级。
2. **改造模型**：

   * 假设你现在有一个新的 **10 分类**任务（比如 CIFAR-10）。请找到 `resnet50` 模型的最后一层（分类头，通常是 `.fc` 层），并将其**替换**为一个新的、输出维度为 10 的全连接层。
3. **提取特征**：

   * 学习如何让 `timm` 模型不仅仅是输出分类结果。请想办法（提示：可以查看 `features_only=True` 或 `get_intermediate_layers` 等方法），将一张 `224x224` 的随机图片输入到原始的 `resnet50` 中，并**提取出全局平均池化层之前**的特征图（Feature Map）。
   * 打印出这个特征图的 `shape`，感受一下图像是如何被浓缩成深度特征的。

---

### **作业3: 工业级终极咒文 (OpenMMLab)**

欢迎来到——`OpenMMLab`！在这里我们不再需要自己手写繁琐的训练循环，而是通过使用Config来编写程序。

**要求：**

1. **环境配置**：请根据官方文档，成功安装 `MMCV` / `MMEngine` 和 `MMPretrain`。
2. **理解咒文 (Config)**：

   * 在 `MMPretrain` 的 `configs` 文件夹中，找到 `resnet/resnet18_8xb16_cifar10.py` 这个配置文件。
   * 请仔细阅读这个文件，**不要运行它**，先试着理解其中 `model`, `data`, `optim_wrapper` 等字段分别代表了什么。
3. **咏唱与修改**：

   * **你的任务**：将这个 `resnet18` 的训练任务，**修改**为一个使用 `resnet50` 的任务。
   * **具体操作**：请**复制**一份 `resnet18_8xb16_cifar10.py` 文件，并重命名为 `resnet50_8xb16_cifar10.py`。然后，**仅修改**这个新的配置文件，将其中与模型定义相关的部分从 `ResNet-18` 改为 `ResNet-50`。（提示：可能需要修改 `model` 字典里的 `depth` 字段）。
4. **启动训练**：

   * 使用 `tools/train.py` 脚本，加载你**修改后**的 `resnet50_8xb16_cifar10.py` 配置文件，启动训练。
   * 让训练运行 **1-2 个 epoch** 即可，然后手动停止。
5. **提交成果**：

   * 请提交你**修改后的 `resnet50_8xb16_cifar10.py` 配置文件**。
   * 请附上一张**训练过程开始时的命令行截图**，以证明你的咒文成功咏唱并驱动了整个训练流程！
