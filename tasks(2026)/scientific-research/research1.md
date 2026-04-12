﻿﻿# Research 1 - 从机器学习到深度学习

> 预计耗时：90 天

## 学习目的

如果你选择偏科研方向，意味着你未来可能想做科研、进实验室、争取保研，或者只是单纯对人工智能底层原理感兴趣。

在前三轮学习中，你已经掌握了 Python 编程基础、爬虫以及基本的数据分析。

人工智能领域主要分为两大方向：计算机视觉和自然语言处理。

无论是 CV、NLP 还是其他方向，模型训练都离不开共同的核心理论基础：反向传播算法。

诚然，使用 PyTorch 等现代的深度学习框架可以有效简化实现过程；但对科研而言，理解底层依然是必要的。

学完 Research 1 后，恭喜你，你已经具备复现顶会论文的基础能力。

从功利的角度出发，你已经可以去其他实验室面试了。

> 西二在线的负责老师可以作为保底。

$\color{red}{\text{如果你觉得 Research 1 入手晦涩难懂，这很正常。}}$

$\color{red}{\text{但是这是进实验室最基本的要求，大家都是这么学过来的。}}$

## 学习内容

从经典机器学习到深度学习。

- KNN
- SVM
- Softmax Classifier
- XGBoost
- Random Forest
- CNN
- RNN
- GAN
- Transformer
- LSTM

## 学习要求

本轮学习内容对新手而言挑战较大，尤其是首次接触全英文课程的同学。这正是我们希望你优先克服的难题。在人工智能领域，英文阅读能力不是加分项，而是必备技能，因为绝大多数前沿论文、官方文档和高质量社区讨论都以英文为载体。我们鼓励你勇敢面对这一挑战，并善用工具辅助学习。

此外，本轮需要一些前置知识：线性代数、微积分、NumPy 以及 Python 编程。

后两者已经在前几轮涉及；若前两者在学校课程中尚未开设（例如大一同学通常会在高数下学期接触偏导数），可以参考下一节的推荐教程。

对于与深度学习思想差异较大的传统机器学习算法，只需要写一篇文档描述其原理和使用场景即可，无需从零实现。

## 作业

对于本次作业，你需要完成 5 篇文档，作业 1 - 3。

### 文档 1 - 生成式 AI 的训练流程

阅读[李宏毅生成式人工智能教程课本](https://github.com/datawhalechina/leegenai-tutorial/releases)，整理相关内容，并以文档形式讲述大语言模型的整个训练流程。

> 本文档**不要求精确的数学公式和理论表达**，只需用你自己的话，简要描述生成式 AI 的三个训练阶段：
>
> 1. 自监督学习（Pre-training）
> 2. 监督式学习（Supervised Fine-tuning）
> 3. 人类反馈强化学习（RLHF）

### 文档 2 - 传统机器学习算法之间的区别

介绍 K-Nearest Neighbor（k-NN, K-近邻）、Support Vector Machine（SVM, 支持向量机）、Softmax Classifier（Softmax 分类器）、XGBoost、Random Forest（随机森林）这五种机器学习算法的原理和使用场景，并指出这些算法与神经网络的区别。

> 这里简要解释传统机器学习与深度学习的区别。二者最核心的区别在于如何学习和利用数据的「特征」。
>
> 例如，决策树和随机森林基于预先定义的特征（如气象状态、温度范围等），通过一系列逻辑判断逐步推理出结论，整个决策过程直观且可解释。
>
> 而支持向量机则更为抽象，它试图在数据之间找到一个最优的分界超平面。这种通过数学优化寻找复杂边界的思想，与神经网络通过调整权重来划分数据的逻辑具有相似性。
>
> 深度学习最根本的优势在于其强大的「自动特征提取」能力。我们不再需要手动设计特征，深度神经网络能够从原始数据中逐层抽象和学习出解决问题所需的高效特征表示，这正是它与传统机器学习算法最关键的区别。
>
> 对于基于树的复杂集成算法（如随机森林、XGBoost、决策树），由于其实现逻辑与神经网络差异较大，只需要了解原理并掌握 [scikit-learn](https://scikit-learn.org/stable/) 即可，无需从零实现。
>
> 但对于线性分类器（k-NN, SVM, Softmax），它们是理解神经网络损失函数和梯度下降的基石，你需要在作业 1 中实现。

### 作业 1 - Two-layer Neural Network

本轮作业的目标是让你从零实现一个两层神经网络，并且通过这个过程来深入理解神经网络的基本原理和反向传播算法。

完成 [CS231n Assignment 1](https://cs231n.github.io/assignments2025/assignment1/)，并写一份文档来描述你在完成作业过程中遇到的挑战和解决方案。

### 作业 2 - CNN

完成作业 1 后，你成功实现了一个简单的二层神经网络，并在 CIFAR-10 数据集上进行了训练。

然而，现实世界中的神经网络远比两层神经网络复杂得多。为了应对更复杂的任务，我们需要引入更多的层次、更复杂的结构，以及更高效的训练方法。

CNN 是深度学习中最重要的网络结构之一，广泛应用于计算机视觉任务中。通过卷积操作，CNN 能够有效地捕捉图像中的空间特征，从而大幅提升图像分类、目标检测等任务的性能。

因此，作业 2 将聚焦 CNN，并进一步探索现代深度学习框架（如 PyTorch）的使用方法。

完成 [CS231n Assignment 2](https://cs231n.github.io/assignments2025/assignment2/)，并写一份文档来描述你在完成作业过程中遇到的挑战和解决方案。

> 完成这次作业后请思考，我们为什么需要 PyTorch 这样的框架？

### 作业 3 - CV / LLM

人工智能的研究方向主要分为计算机视觉和自然语言处理，当然也包括其他更多方向。

鉴于每个人的时间和精力有限，在完成了作业 2 之后，你可以选择继续完成 CS231n 的作业，深入学习计算机视觉相关的内容；或者转向 CS224n，探索自然语言处理领域的知识。

不过对于本科生而言，建议两个方向都尝试一下。

福大比较强的实验室基本都是 CV 的，所以我更推荐你选择 CV。

完成 [CS231n Assignment 3](https://cs231n.github.io/assignments2025/assignment3/)，并写一份文档来描述你在完成作业过程中遇到的挑战和解决方案。

完成 [CS224n](https://web.stanford.edu/class/cs224n/)，并写一份文档来描述你在完成作业过程中遇到的挑战和解决方案。

> 建议选择 LLM 路线的同学先完成 cs224n 的前三个 assignment，然后再去完成 cs231n（毕竟都写了前两个了，而且有些东西是通用的）

## 推荐教程与参考资料

### 生成式 AI 认识

[李宏毅 2024 B 站](https://www.bilibili.com/video/BV1BJ4m1e7g8/?spm_id_from=333.337.search-card.all.click&vd_source=e3594664d709db7578f4b2e76329df18)

[李宏毅 2024 YouTube](https://www.youtube.com/watch?v=AVIKFXLCPY8&t=1s)

[李宏毅 2025 YouTube](https://www.youtube.com/watch?v=VuQUF1VVX40&list=PLJV_el3uVTsMMGi5kbnKP5DrDHZpTX0jT&index=1&t=10s)

[李宏毅生成式人工智能教程课本](https://github.com/datawhalechina/leegenai-tutorial/releases)

> 注意：生成式 AI 导论不要求完成课程作业。YouTube 上的 2025 版课程仍在持续更新，教程课本是根据 2024 年春季学期课程整理而成。
>
> 2025 年秋季版课程在前几讲就引入了较为复杂的概念，与 2024 年春季版相比难度提升较多，内容变化也较大。建议初学者优先学习 2024 年春季版课程或直接阅读教程课本，无需观看 2025 年秋季版。
>
> 学习生成式 AI 导论时，无需看完所有课程或课本，只需根据文档 1 的要求，针对性地学习相关内容即可。

### Sklearn

[scikit-learn](https://scikit-learn.org/stable/)

### CS231n

学习机器学习需要有一定的数学知识作为基础。

#### 前置知识

1. 前三轮知识：尤其是 NumPy、Pandas 和 Matplotlib。Python 基础不必多说；学习爬虫的作用主要是让你在未来进行人工智能研究时，具备补全数据或爬取所需数据的能力。
2. 多元函数复合求导（求偏导）：具体内容在高等数学 B 下学期讲授，可参考[宋浩高等数学](https://www.bilibili.com/video/BV1Eb411u7Fw?spm_id_from=333.788.videopod.episodes&vd_source=0272bb7dd0d8d9302c55fc082442b9e3&p=96)，直到能够完成一些简单的求偏导计算。
3. 线性代数：计算机专业的同学大一上已经开设线性代数课程。无论对于已学或未学的同学，都可以参考[线性代数的本质](https://www.bilibili.com/video/BV1Ys411k7yQ/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)系列视频加深对线性代数的理解。
4. NumPy：作业将大量使用 NumPy 进行向量化（Vectorization）计算。请务必完成 [CS231n 官方 NumPy 教程](https://cs231n.github.io/python-numpy-tutorial/)。对于不熟悉的 API，学会使用搜索引擎和大语言模型工具进行查询。
5. 矩阵求导：这是理解反向传播数学原理的关键。不必畏惧，你只需掌握基础的求偏导知识即可入门。推荐通过以下资源学习：
   - [B 站视频教程](https://www.bilibili.com/video/BV1av4y1b7MM/)
   - [知乎文章讲解](https://zhuanlan.zhihu.com/p/273729929)

需要注意，关于 torch 的知识并不需要你提前掌握，assignment 2 的最后一个 lab 应该会有给出教程。

但是以防万一，这里还是给出 CS224n 的 PyTorch 速成：

[CS224n PyTorch 速成](https://colab.research.google.com/drive/1Pz8b_h-W9zIBk1p2e6v-YFYThG1NkYeS?usp=sharing)

#### CS231n 课程相关链接

Stanford CS231n: Convolutional Neural Networks for Visual Recognition

- [CS231n 2024 Notes](https://cs231n.github.io/)
- [CS231n 2024 Spring](https://cs231n.github.io/)
- [CS231n 2025 Spring](https://cs231n.stanford.edu/assignments.html)
- [课程中文翻译](https://zhuanlan.zhihu.com/p/21930884)（采用 Python 2.7 版本，已过时，可作为辅助理解材料）

> 需要注意，CS231n 课程官方笔记页面提供的是 24 版的作业。当前版本的则是 25 版，不过官方的笔记没有跟进。你可以选择完成 24 年的版本或者 25 年的版本，无论选择哪个版本，核心任务和学习目标是一致的。

#### CS231n 课程视频

1. CS231n 的 [课程视频](https://www.bilibili.com/video/BV1b1agz5ERC/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)
2. 如果觉得 CS231n 的数学推导过多，建议观看[李宏毅老师的机器学习课程](https://www.bilibili.com/video/BV1Wv411h7kN/)，该课程更侧重于从直观角度理解模型原理
3. [吴恩达老师的机器学习视频](https://www.bilibili.com/video/BV1owrpYKEtP/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)

#### CS231n Assignment 3 相关链接

1. [跟李沐学AI 54 循环神经网络 RNN【动手学深度学习v2】](https://www.bilibili.com/video/BV1D64y1z7CA/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)

2. [跟李沐学AI 57 长短期记忆网络（LSTM）【动手学深度学习v2】](https://www.bilibili.com/video/BV1JU4y1H7PC?spm_id_from=333.788.recommend_more_video.4&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)

3. [跟李沐学AI GAN论文逐段精读【论文精读】](https://www.bilibili.com/video/BV1rb4y187vD/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)

4. [跟着李沐学AI Transformer论文逐段精读【论文精读】](https://www.bilibili.com/video/BV1pu411o7BE/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)

5. [自监督式学习](https://www.bilibili.com/video/BV1m3411p7wD?spm_id_from=333.788.videopod.episodes&vd_source=0272bb7dd0d8d9302c55fc082442b9e3&p=46)

6. [【Transformer 其实是个简单到令人困惑的模型【白话DeepSeek-06】](https://www.bilibili.com/video/BV1C3dqYxE3q/?share_source=copy_web&vd_source=3fbbb3c2ad24817002f9c39fad247a3b)

7. [68 Transformer【动手学深度学习v2】](https://www.bilibili.com/video/BV1Kq4y1H7FL/?p=2&share_source=copy_web&vd_source=3fbbb3c2ad24817002f9c39fad247a3b)

#### 配环境 - CS231n

学习 CS231n 需要配置环境，这里主要推荐两条路线。

- 使用 Colab

  如果你的电脑配置较低（没有 GPU），建议使用 Google Colab。

  CS231n 官方和 Google 有合作，只要你有 Google 账号，就可以直接使用 Colab 环境完成作业。

  打开 CS231n [24 Spring Assignment 1](https://cs231n.github.io/assignments2024/assignment1/) 页面或者 [25 Spring Assignment 1](https://cs231n.github.io/assignments2025/assignment1/) 页面，然后观看 Setup 这个视频，按照视频中的步骤操作即可。

  这里直接给出这个视频的链接：[CS231N Google Colab Assignment Workflow Tutorial](https://www.youtube.com/watch?v=DsGd2e9JNH4&source_ve_path=MjM4NTE&embeds_referring_euri=https%3A%2F%2Fcs231n.github.io%2F)

  如果你使用 2025 版 CS231n ，你可能会遇到如下问题：

  使用 Colab 运行 ipynb 文件带有以下两行的代码块，这两行代码在所有 ipynb 文件里面都存在

  ```python
  %load_ext autoreload
  %autoreload 2
  ```
  
  如果你没有特地去修改过 Colab 的 Python 运行版本可能会出现如下错误
  
  ```
  ModuleNotFoundError                       Traceback (most recent call last)
  …………
  ModuleNotFoundError: No module named 'cs231n'
  ```
  
  解决方法：点击右下角的 `Python 3` 选项，选择 “更改运行时类型” 将 “运行时版本” 修改为 “2025.07”，然后一定要重启 Colab 。重启后再次按顺序运行即可
  
- 本地配置环境

  本地配置环境的推荐前提是有一台性能较好的电脑，最好有 NVIDIA 显卡（支持 CUDA）。

  如果你是 Linux 或 Mac 用户，推荐直接使用系统自带的终端进行配置。

  如果你是 Windows 用户，可以考虑使用 Windows Subsystem for Linux（WSL2），不推荐直接在 Windows 系统下进行环境配置。

  不推荐使用 Linux 虚拟机，因为虚拟机的性能通常较差，可能无法满足深度学习的需求。

  如果你执意要直接使用 Windows，可以参考[weijianxian CS231n 2025 spring 的环境配置](https://github.com/weijianxian/cs231n-25)，该方法使用 uv，也可以使用传统的 venv。

  如果你想采用 Windows + conda 的方式进行配置，可以参考[rechenz CS231n 2025 spring 的环境配置](https://github.com/rechenz/SetupLocal-for-cs231n-25)。

  个人推荐使用 WSL2，微软官方有详细的[安装教程](https://learn.microsoft.com/zh-cn/windows/wsl/install)。

  这里贴出来几个下载 WSL2 碰到的常见的问题以及解决方案，如果你是 Linux 或者 Mac 用户，可以跳过这部分。

- 关于跨系统文件访问

  跨系统文件访问很慢，如果你的程序需要大量 I/O 操作，请将项目复制到 Linux 文件目录下执行。

  例如你如果直接在桌面上打开 WSL2，你可能的路径是这样的：

  ```bash
  /mnt/d/desktop/github/learn-AI
  ```

  这时候你需要将项目复制到 Linux 文件目录下，例如：

  ```bash
  cp -r /mnt/d/desktop/github/learn-AI ~/
  cd ~/learn-AI
  ```

  这样就可以在 Linux 文件目录下执行了。

- 我配完 WSL2 后，手机模拟器（例如 mumu 模拟器）非常卡顿，怎么办？

  因为市面上大多数的手机模拟器的实现技术和 WSL2 是冲突的。

  具体而言，WSL2 是基于 Hyper-V 的虚拟化技术，而大多数手机模拟器是基于 VirtualBox 或者其他虚拟化技术实现的，这两种虚拟化技术是冲突的，所以会导致手机模拟器非常卡顿。

  解决方法有两种：一种是使用蓝叠模拟器或谷歌模拟器（Beta 开发中）等支持 Hyper-V 的模拟器；另一种是按 `Win + R`，输入 `cmd` 后，再按 `Ctrl + Shift + Enter` 进入管理员模式：

  ```bash
  只能使用 wsl 时
  bcdedit /set hypervisorlaunchtype auto
  
  使用 mumu 模拟器时
  bcdedit /set hypervisorlaunchtype off
  ```

  然后重启。

  注意是重启，大部分未经过特别设置的 Windows，关机等同于深度睡眠，并不会修改你的系统设置。

> 更新中。

### CS224n

#### CS224n 相关链接

0. [CS224n PyTorch 速成](https://colab.research.google.com/drive/1Pz8b_h-W9zIBk1p2e6v-YFYThG1NkYeS?usp=sharing)
1. [cs224n](https://www.bilibili.com/video/BV1vQMBz6EvP/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)，如果你能理解 PPT 和论文内容，可以不用看视频。
2. [跟李沐学AI 词向量（word2vec）【动手学深度学习v2】](https://www.bilibili.com/video/BV1sY4y1572C/)
3. [跟李沐学AI 注意力机制【动手学深度学习v2】](https://www.bilibili.com/video/BV1ui4y1j783/)
4. [跟李沐学AI Transformer论文逐段精读【论文精读】](https://www.bilibili.com/video/BV1pu411o7BE/)
5. [【Transformer 其实是个简单到令人困惑的模型【白话DeepSeek-06】】](https://www.bilibili.com/video/BV1C3dqYxE3q/)
6. [台大李宏毅老师 机器学习2021（Self-Attention和Transformer部分）](https://www.bilibili.com/video/BV1JA411X76s?p=65)

#### 配环境 - CS224n

CS224n 的环境默认是本地配置，当然你也可以选择使用 Colab。

如果你选择使用 Colab，可以参考 [ShaddockNH3/CS224N-Nyan-Book](https://github.com/ShaddockNH3/CS224N-Nyan-Book)。

如果你选择使用本地配置，官方文档会提供帮助。

### 学习路径建议

1. 适应英文环境：积极适应全英文的学习材料。建议不要使用浏览器的全文自动翻译，可以安装划词翻译插件，强制自己阅读原文，只在遇到生词时进行查询。
2. 研读课程笔记（Notes）：CS231n 的课程 Notes 是完成作业的重要学习资源，内容详实且深入。请务必花费时间仔细阅读，这是理解所有模型原理的基础。
3. 攻克数学难点：遇到矩阵求导等数学难题时，不要直接跳过。利用推荐的视频和文章，认真推导一两个简单的例子，你会发现它并没有想象中那么困难。
4. 建立交流社区：我们希望将考核群打造成一个高效的学习社区。请积极在群里讨论问题，尤其是数学和理论方面的内容。交流能极大地提高学习效率。但严禁直接分享或抄袭代码。
