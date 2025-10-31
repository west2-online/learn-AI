# Task 5 深度学习与深度学习现代框架

## 学习目的

在 Task 4 中，你已经通过亲手实现反向传播，锻炼了作为人工智能工程师的核心技能。现在，你将在此基础上，进一步深入学习和实践专业方向的核心技术。本轮考核将是你专业方向的重要阶段，你将深入学习那些定义了现代深度学习的模块化设计思想与核心网络架构。

这次，你的任务不再是构建一个写死的两层网络，而是要学会如何设计和实现一个可扩展、可组合的深度神经网络，并最终亲手实现计算机视觉领域的核心技术——**卷积神经网络（Convolutional Neural Network, CNN）**。

## 学习内容

本轮的学习将从整体架构转向模块化实现，你将深入理解并实现构成现代神经网络的各个独立组件：

* **网络优化与正则化**：批量归一化（Batch Normalization）、Dropout
* **模块化网络设计**：将网络层（如全连接层、ReLU 激活层）抽象为独立的、拥有 `forward` 和 `backward` 接口的模块
* **卷积神经网络核心**：卷积层（Convolutional Layer）的前向与反向传播、池化层（Pooling Layer）的前向与反向传播
* **现代框架实践**：在手动实现所有核心组件后，使用高层框架（如 PyTorch）快速搭建一个高性能的 CNN 模型

## 学习要求

本轮考核的难度相较于 Task 4 有显著提升，主要体现在以下两个方面：

1. **抽象思维的转变**：你需要从为整个网络编写一个统一的 `loss` 和 `gradient` 函数，转变为为**每一个独立的层**编写 `forward` 和 `backward` 函数。这种模块化的设计思想是所有现代深度学习框架的基石。
2. **数学与实现的挑战**：卷积层的反向传播在数学上和实现上都比全连接层更为复杂。你需要花费大量时间阅读课程笔记，理解梯度是如何在卷积和池化操作中流动的。

请务必将课程笔记（Notes）作为你最主要的学习材料。只有在真正理解了每一层的计算原理后，你才有可能成功地完成代码实现。

## 作业

### 作业 1：完成 CS231n Assignment 2

**核心任务：完成 [CS231n Assignment 2](https://cs231n.github.io/assignments2025/assignment2/)**

本次作业分为三个循序渐进的部分，将引导你完成一次从底层构建到高层应用的完整体验：

#### 第一部分：模块化全连接网络（Fully-Connected Nets）

在这一部分，你将改进 Task 4 中的整体化网络设计，开始构建一个可以自由堆叠层数的深度神经网络。你需要：

* 为**每一个基础层**（Affine、ReLU、Softmax Loss 等）实现独立的 `forward` 和 `backward` 函数。
* 在此基础上，实现**批量归一化（Batch Normalization）**和 **Dropout** 层的前向与反向传播。
* 将这些独立的层组合起来，构建一个可以任意指定层数和隐藏单元数量的全连接网络。
* 实现一个通用的 `Solver` 类来训练你的模型，并用它来寻找最佳的网络配置。

#### 第二部分：卷积神经网络（Convolutional Nets）

这是本次作业的核心与亮点。你将深入学习 CNN 的内部机制，实现其最重要的两个组成部分：

* **卷积层（Convolutional Layer）**：实现其 `forward` 和 `backward` 传播。这是整个作业中最具挑战性的部分。
* **最大池化层（Max-Pooling Layer）**：实现其 `forward` 和 `backward` 传播。
* 将这些新的卷积组件与你之前实现的全连接层组合起来，构建一个真正的卷积神经网络。

#### 第三部分：现代框架实践（PyTorch）

在经历了手动实现所有核心组件的过程之后，你将体验到现代深度学习框架的强大与便捷。在这一部分，你需要：

* 使用 **PyTorch** 重新搭建一个更为复杂的卷积神经网络。
* 利用框架提供的自动求导、GPU 加速等功能，在 CIFAR-10 数据集上训练你的模型，并冲击尽可能高的准确率。

> 完成这次作业后，你将深刻理解一个重要问题：「我们为什么需要 PyTorch 这样的框架？」因为你已经亲身经历了完整的底层实现过程。这种从底层到高层的学习路径，将让你对深度学习的理解远超仅使用现成库的学习者。

### 作业 2：根据 MNIST 数据集实现一个简单的识别数字的 Demo（选做）

**核心任务：实现并部署一个基于 TensorFlow.js 的 MNIST 手写数字识别 Web 应用。**

该项目的最终成果可以在[这里](https://shaddocknh3.github.io/tfjs-mnist-digit-recognizer/)体验。

本次作业的目标是让你亲历一个人工智能应用从训练到部署的全过程。你将以[该项目](https://github.com/ShaddockNH3/tfjs-mnist-digit-recognizer)为基础框架，但核心的识别模型需要由你自己亲手训练和替换。

你的任务是基于 MNIST 数据集训练一个识别数字的 Demo，应该 fork [该项目](https://github.com/ShaddockNH3/tfjs-mnist-digit-recognizer)，然后替换原仓库 model 文件夹下的两个训练文件。

你不需要实现前端。

#### 第一部分：训练你的专属识别模型（Train Your Own Recognition Model）

原项目（指的是旧版实现，本人已替换为新版实现）中的模型存在版本兼容性或识别效果不佳的问题。现在，你的首要任务是使用 CNN 亲自训练一个全新的、更强大的识别模型。

* **环境与工具**：你需要在 Python 环境下，使用 Keras 框架来完成此任务。
* **模型构建**：在经典的 MNIST 数据集上，从零开始构建并训练一个卷积神经网络（CNN）。你需要自行设计网络结构、选择优化器和损失函数，并进行超参数调整，以达到尽可能高的识别准确率。
* **产出**：训练完成后，你将得到一个 Keras 模型文件（通常是 `.h5` 格式），这是我们后续工作的基础。

#### 第二部分：模型转换与前端整合（Model Conversion & Frontend Integration）

由于浏览器环境无法直接运行 Python 代码，我们需要通过转换工具，将训练好的模型迁移到 Web 环境中。

* **模型转换**：你需要学习并使用 `tensorflowjs_converter` 这个官方工具。它的作用是将上一步得到的 `.h5` 模型文件，转换成 TensorFlow.js 能够加载和理解的格式，即一个 `model.json`（模型结构）和一个 `.bin` 权重文件。
* **核心替换**：将你生成的新模型文件（`model.json` 和 `.bin` 文件），替换掉基础项目仓库中 `/model/` 文件夹下的所有旧文件。这是实现模型更新的关键步骤。

#### 第三部分：部署、验证与优化（Deploy, Verify & Optimize）

测试可以参考[该项目](https://github.com/ShaddockNH3/tfjs-mnist-digit-recognizer)的部署，一般而言，报错了是版本不匹配，而不是前端出了问题。

* **在线部署**：将你修改后的整个项目，通过 **GitHub Pages** 功能发布，生成一个任何人都可以通过浏览器访问的公开网页链接。
* **多端验证**：在 PC 和**移动端（手机）**上打开你的应用，在画板上写下数字进行测试。检验识别功能是否正常工作，特别是解决原项目在手机上无法正确识别的问题。
* **调试与修复**：仔细观察浏览器开发者工具（F12）中的控制台。如果在加载模型或进行预测时出现任何报错信息，你需要系统地分析问题根源，并尝试修复它。

在完成最终的模型后，你应该替换 `index.html` 的第 6 行为自己的 GitHub 用户名。

#### 参考资料

* [参考实现：使用 Keras.js 的旧版思路](https://github.com/starkwang/keras-js-demo)
* [参考教程：从训练到部署的详细步骤](https://www.cnblogs.com/chinasoft/p/17084356.html)
* [TensorFlow.js 官方文档](https://www.tensorflow.org/js/guide?hl=zh-cn)

#### 提示

- 该项目可以全程跑在 Colab 上，你可以参考答案 [train.ipynb](https://github.com/ShaddockNH3/tfjs-mnist-digit-recognizer/blob/train/training/train.ipynb)，但不要抄袭代码

## 作业要求

1. 不要抄袭
2. 遇到不会可以多使用搜索引擎，实在没有找到解决方法可以来群里提问，作为一个CSer学习提问的方式也非常重要，强烈建议阅读[Stop-Ask-Questions-The-Stupid-Ways](https://github.com/tangx/Stop-Ask-Questions-The-Stupid-Ways/blob/master/README.md)这篇文章
3. 不限制使用 ChatGPT 等大语言模型工具，但你需要确保你了解模型生成的内容的每一个细节，最好你可以在使用大语言模型生成的代码部分注释上「reference from ChatGPT」这样的内容
4. 你还需要学习基本的 Git 的使用，所有考核都采用 Git 的方式进行上传
5. 作业内容可能会进行更新，请保持关注

## 作业提交方式

1. 你需要学习 GitHub 的使用，创建一个你自己的仓库用来存放你的代码实现
2. 接着你需要学习如何使用 Git 进行 PR 操作，在 [solutions](https://github.com/west2-online-reserve/collection-ai) 中进行操作