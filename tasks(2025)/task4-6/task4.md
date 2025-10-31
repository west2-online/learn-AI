# Task 4 机器学习

## 学习目的

在前三轮学习中，你已经掌握了 Python 编程基础和基本的人工智能概念。

人工智能领域主要分为两大方向：计算机视觉（Computer Vision, CV）和自然语言处理（Natural Language Processing, NLP）。

无论是 CV、NLP 还是其他方向，它们的训练都基于共同的核心理论基础——反向传播（Backpropagation）算法。

诚然，使用 PyTorch 等现代成熟的深度学习框架可以有效简化实现过程。然而，本课程的目标不是培养「调用工具」的使用者，而是培养「理解原理」的研究者。

作为计算机专业的学生，我们的核心竞争力在于**深入理解基本原理，并具备从零实现算法、调试和优化模型的能力**。本轮学习将是你实现这一目标的关键阶段。

对于传统机器学习算法（与深度学习、神经网络在技术路线上有所不同的算法），只需要了解基本原理并掌握 [scikit-learn](https://scikit-learn.org/stable/) 的使用即可，无需从零实现。我们的重点在于更前沿的深度学习技术。

这里简要解释传统机器学习与深度学习的区别。二者最核心的区别在于如何学习和利用数据的「特征」（Feature）。

例如，决策树（Decision Tree）和随机森林（Random Forest）基于预先定义的特征（如气象状态、温度范围等），通过一系列逻辑判断逐步推理出结论，整个决策过程直观且可解释。

而支持向量机（Support Vector Machine, SVM）则更为抽象，它试图在数据之间找到一个最优的分界超平面（Hyperplane）。这种通过数学优化寻找复杂边界的思想，与神经网络通过调整权重来划分数据的逻辑具有相似性。

深度学习最根本的优势在于其强大的「自动特征提取」（Automatic Feature Extraction）能力。我们不再需要手动设计特征，深度神经网络能够从原始数据中逐层抽象和学习出解决问题所需的高效特征表示，这正是它与传统机器学习算法最关键的区别。

## 学习内容

本轮的核心学习内容将围绕一系列经典的机器学习模型与概念展开，最终导向对神经网络核心机制的理解：

- **分类器基础**：K-Nearest Neighbor（k-NN, K-近邻）、Support Vector Machine（SVM, 支持向量机）、Softmax Classifier（Softmax 分类器）、XGBoost、Random Forest（随机森林）
- **神经网络核心**：Two-Layer Neural Network（两层神经网络）、Fully-Connected Networks（全连接网络）
- **特征工程**：Image Features（图像特征，包括 Histogram of Oriented Gradients、Color Histograms）

## 学习要求

本轮学习内容对新手而言具有相当的挑战性，尤其对于首次接触全英文课程的同学。但这正是我们希望你克服的首要难题。在人工智能领域，**英文阅读能力不是加分项，而是必备技能**，因为绝大多数前沿论文、官方文档和高质量社区讨论都以英文为载体。我们鼓励你勇敢面对这个挑战，并善用工具辅助学习。

此外，本轮需要一些前置知识：线性代数、微积分、NumPy 以及 Python 编程。

后两者已经在前几轮涉及，前两者如果学校课程尚未开设（对于大一学生，偏导数（Partial Derivative）部分在高等数学大一下学期讲授），可以参考下一节的推荐教程。

## 推荐教程

### 核心课程

**Stanford CS231n: Convolutional Neural Networks for Visual Recognition**

- [课程英文主页（Notes & Assignments）](https://cs231n.github.io/)
- [课程中文翻译（Notes）](https://zhuanlan.zhihu.com/p/21930884)（采用 Python 2.7 版本，已过时，可作为辅助理解材料）

### Scikit-learn

[scikit-learn 官方学习指南](https://scikit-learn.org/stable/user_guide.html)

### 前置知识及辅助资料

1. **前三轮知识**：尤其是 NumPy、Pandas 和 Matplotlib 库。Python 基础不必多说，爬虫的作用主要是为未来进行人工智能研究时，具备补全数据或爬取所需数据的能力。

2. **多元函数复合求导（求偏导）**：具体内容在高等数学 B 下学期讲授，可参考[宋浩高等数学](https://www.bilibili.com/video/BV1Eb411u7Fw?spm_id_from=333.788.videopod.episodes&vd_source=0272bb7dd0d8d9302c55fc082442b9e3&p=96)，直至能够完成一些简单的求偏导计算。

3. **线性代数**：计算机专业的同学大一上已经开设线性代数课程。无论对于已学或未学的同学，都可以参考[线性代数的本质](https://www.bilibili.com/video/BV1Ys411k7yQ/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)系列视频加深对线性代数的理解。

4. **NumPy**：作业将大量使用 NumPy 进行向量化（Vectorization）计算。请务必完成 [CS231n 官方 NumPy 教程](https://cs231n.github.io/python-numpy-tutorial/)。对于不熟悉的 API，学会使用搜索引擎和大语言模型工具进行查询。

5. **矩阵求导**：这是理解反向传播数学原理的关键。不必畏惧,你只需掌握基础的求偏导知识即可入门。推荐通过以下资源学习：
   - [B 站视频教程](https://www.bilibili.com/video/BV1av4y1b7MM/)
   - [知乎文章讲解](https://zhuanlan.zhihu.com/p/273729929)

6. **课程视频**：
   - CS231n 的[课程视频](https://www.bilibili.com/video/BV1b1agz5ERC/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)是很好的补充材料
   - 如果觉得 CS231n 的数学推导过多，建议观看[李宏毅老师的机器学习课程](https://www.bilibili.com/video/BV1Wv411h7kN/)，该课程更侧重于从直观角度理解模型原理
   - [吴恩达老师的机器学习视频](https://www.bilibili.com/video/BV1owrpYKEtP/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)
   - 一些经典的机器学习方法，包括与神经网络在技术原理和路线上有所不同的[经典机器学习方法](https://www.bilibili.com/video/BV1T84y167U9/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3)

---

## 学习路径建议

1. **适应英文环境**：积极适应全英文的学习材料。建议不要使用浏览器的全文自动翻译，可以安装划词翻译插件，强制自己阅读原文，只在遇到生词时进行查询。
2. **研读课程笔记（Notes）**：CS231n 的课程 Notes 是完成作业的重要学习资源，内容详实且深入。请务必花费时间仔细阅读，这是理解所有模型原理的基础。
3. **攻克数学难点**：遇到矩阵求导等数学难题时，不要直接跳过。利用推荐的视频和文章，认真推导一两个简单的例子，你会发现它并没有想象中那么困难。
4. **建立交流社区**：我们希望将考核群打造成一个高效的学习社区。请积极在群里讨论问题，尤其是数学和理论方面的内容。交流能极大地提高学习效率。**但严禁直接分享或抄袭代码。**

---

## 作业

### 作业 1：完成 CS231n Assignment 1

**核心任务：完成 [CS231n Assignment 1](https://cs231n.github.io/assignments2025/assignment1/)**

本次作业将引导你从零开始，系统地实现多个经典的机器学习与神经网络模型，为后续更复杂的挑战奠定坚实的基础。

#### 第一部分：经典图像分类器（Classic Image Classifiers）

在这一部分，你将深入理解图像分类的基础理论，通过手动实现三个经典的线性分类器来构建对模型内部工作原理的直观认知。你需要：

* 实现一个简单的 **k-近邻（k-NN）** 分类器，体验非参数方法（Non-parametric Method）的直观与简洁。
* 为强大的 **支持向量机（SVM）** 推导并实现其损失函数（Loss Function）与梯度（Gradient）的向量化计算。
* 为多分类问题实现 **Softmax** 分类器，包括其损失函数与梯度的计算。
* 使用 **随机梯度下降（Stochastic Gradient Descent, SGD）** 算法来优化你实现的 SVM 和 Softmax 模型，并学习如何调整超参数（Hyperparameter）以获得更好的性能。

#### 第二部分：你的第一个神经网络（Your First Neural Network）

在掌握了线性分类器的基础上，你将进一步学习神经网络的构建，从零开始实现一个完整的神经网络。你需要：

* 搭建一个 **两层的全连接神经网络**，并实现其 **前向传播（Forward Pass）** 过程，计算出分类得分（Score）。
* 完成整个作业中最核心、最关键的一步：为你的神经网络手动实现 **反向传播（Backpropagation）** 算法，计算所有可训练参数的梯度。
* 最后，在经典的 **CIFAR-10** 数据集上训练并验证你亲手搭建的所有模型（k-NN、SVM、Softmax、两层神经网络），直观地比较它们的性能表现。

这个过程将引导你深入理解算法的每一个实现细节，而不是简单地使用现成的库函数，从而真正建立起对深度学习核心原理的深刻认知。

### 作业 2：掌握 scikit-learn 库并实践经典机器学习算法（选做）

**核心任务：以 Kaggle 经典入门赛 [Titanic: Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic) 为实战项目，熟练运用 `scikit-learn` 完成一个完整的机器学习流程。**

scikit-learn 是一个强大的机器学习库，内部封装了众多经过验证的经典机器学习算法，在数据科学竞赛和实际应用中表现出色。

我们后续主要探索更前沿的深度学习，这部分内容只需要浅尝辄止，不需要深入研究其内部复杂的实现原理，重点是了解其功能，并在未来需要时，能够熟练地查阅官方文档，直接调用其提供的强大接口（API）来解决问题。

推荐了解以下这些经典的机器学习算法，它们与我们主攻的深度学习（神经网络）在技术原理和路线上有所不同，但在许多场景下（尤其是数据科学竞赛中）依然是非常强大和高效的工具：

1. [决策树（Decision Tree）](https://scikit-learn.org/stable/modules/tree.html)
2. [随机森林（Random Forest）](https://scikit-learn.org/stable/modules/ensemble.html)
3. XGBoost（Extreme Gradient Boosting）

本次作业将引导你直面一个真实的预测任务，你将不再使用简单的示例数据集，而是要亲手处理带有缺失值和噪音的原始数据，最终提交你的预测结果，体验一次完整的数据科学竞赛之旅。

#### 第一部分：数据探索与预处理（Data Exploration & Preprocessing）

在这一部分，你将对数据进行全面的探索和分析，清洗和整理泰坦尼克号的乘客数据，为后续的模型训练做好准备。

* **加载与分析**：使用 `pandas` 库加载 `train.csv` 数据，并进行探索性数据分析（Exploratory Data Analysis, EDA），理解每个特征的含义，并找出其中的缺失值（如 `Age`、`Embarked` 等）。
* **数据清洗**：对缺失值进行合理的填充（例如，使用均值、中位数或众数）。
* **特征工程**：将非数值的类别特征（如 `Sex`、`Embarked`）转换为模型可以理解的数值格式（例如，独热编码（One-hot Encoding）或标签编码（Label Encoding））。此外，你需要决定哪些特征（如 `Name`、`Ticket`）对于预测生存率是无关的，并将其舍弃。

#### 第二部分：训练与评估多种分类模型（Training & Evaluating Models）

在完成数据准备后，你将使用 `scikit-learn` 训练多种模型，并比较它们在预测乘客生还率上的表现。

* **数据划分**：使用 `sklearn.model_selection.train_test_split` 将你的训练数据划分为新的训练集和验证集，以便客观地评估模型性能。
* **模型训练**：至少实现以下模型中的三种，并特别推荐尝试 **随机森林**，因为它在该类任务中通常表现出色：

  * 逻辑回归（`sklearn.linear_model.LogisticRegression`）
  * K-近邻（`sklearn.neighbors.KNeighborsClassifier`）
  * 支持向量机（`sklearn.svm.SVC`）
  * **随机森林（`sklearn.ensemble.RandomForestClassifier`）**
* **模型评估**：在验证集上评估每一个模型，使用 `sklearn.metrics.accuracy_score` 和 `sklearn.metrics.classification_report` 来比较它们的准确率（Accuracy）、精确度（Precision）、召回率（Recall）等指标，并选出表现最佳的模型。

#### 第三部分：模型调优与生成提交文件（Tuning & Submission）

为了在 Kaggle 排行榜上获得更好的名次，你需要对你的最佳模型进行精细的优化和调整。

* **超参数调优**：使用 `sklearn.model_selection.GridSearchCV` 对你在第二部分中选出的最佳模型进行自动化超参数搜索，找到最优的参数组合。
* **最终预测**：用你找到的最佳参数，在**全部**的 `train.csv` 数据上重新训练最终模型。
* **生成提交文件**：加载并用**完全相同**的预处理步骤处理 `test.csv` 数据，使用你最终训练好的模型进行预测，并按照 Kaggle 要求的格式（包含 `PassengerId` 和 `Survived` 两列）生成 `submission.csv` 文件。

#### 注意

1. 提交的最终成绩至少达到 0.9
2. 可以参考 [ShaddockNH3 关于 Titanic 的思考](https://github.com/ShaddockNH3/MyKaggle/tree/main/titanic)

完成这个作业后，你不仅将熟练掌握 `scikit-learn` 的核心用法，更将获得一次宝贵的、端到端解决实际问题的项目经验。

---

## 作业要求

1. 不要抄袭
2. 遇到不会可以多使用搜索引擎，实在没有找到解决方法可以来群里提问，作为一个CSer学习提问的方式也非常重要，强烈建议阅读[Stop-Ask-Questions-The-Stupid-Ways](https://github.com/tangx/Stop-Ask-Questions-The-Stupid-Ways/blob/master/README.md)这篇文章
3. 不限制使用 ChatGPT 等大语言模型工具，但你需要确保你了解模型生成的内容的每一个细节，最好你可以在使用大语言模型生成的代码部分注释上「reference from ChatGPT」这样的内容
4. 你还需要学习基本的 Git 的使用，所有考核都采用 Git 的方式进行上传
5. 作业内容可能会进行更新，请保持关注

## 作业提交方式

1. 你需要学习 GitHub 的使用，创建一个你自己的仓库用来存放你的代码实现
2. 接着你需要学习如何使用 Git 进行 PR 操作，在 [solutions](https://github.com/west2-online-reserve/collection-ai) 中进行操作
