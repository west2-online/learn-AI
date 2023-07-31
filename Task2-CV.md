# 人工智能视觉方向第一轮考核文档
## 前言
欢迎大家继续进行人工智能视觉方向的学习，本次考核的主题仍然是图像分类算法，但是难度有所提升。
## 考核任务
* 自主学习一些内容并提交学习笔记，学习的关键词可参照技术名词部分（markdown格式为宜）
* 依靠pytorch库以**两种方式**实现**cifar-100**数据集的识别，要求如下：
  * 大类识别在Test集上准确率需大于65%
  * 严禁直接套用网上代码
  * 谁说图像识别一定要用卷积？其中一种方式必须含有LSTM或GRU。
  * 网络参数不得大于20M
  * 需要使用Matplotlib生成训练记录的图表，图标中xy轴说明、图例、标题均需具备。

## 技术名词（给一些相关名词自己去搜索引擎查找资料）
* python相关库：torch、matplotlib、numpy
* 网络层：Cov2D。Cov1D、BatchNormalization、LayerNormalization、LSTM、GRU、Dropout
* 损失函数：CrossEntropy、MSE、MAE、logcosh ~~（最好有人去测试不同损失函数对结果的影响）~~
* 优化方法：RMSprop、SGD、Adagrad、Adadelta、Adam、Nadam ~~（最好有人去测试不同优化方法对结果的影响）~~
* 激活函数：Softmax、ReLu、Sigmoid、Tanh、LeakyReLU
* 优秀网络（图像方向）：VGG、AlexNet、**ResNet**、**Vit**、Yolo

熟悉以上内容是入门深度学习的基础，在本次考核期间大家需要对他们有一个基础的了解。
## 考核提交
* 本次考核时长为2周
* 在第一周结束时会安排期中答辩，主要目的是push进度和解答问题。
* 在第二周结束时会收集各位工程的GitHub链接，需要包含的内容如下：
  1. 两套模型的代码
  2. 训练时模型在验真集和测试集上的accuracy和loss变化图，两个模型各一张（所以必须用上matplotlib的双y轴）
  3. 一个名为学习笔记的**文件夹**，里面是本轮的学习笔记。
* 最终答辩时将会拷打对模型的理解等内容。
* 再次强调不准抄袭网上的现成代码