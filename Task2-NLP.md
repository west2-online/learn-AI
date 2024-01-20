# 人工智能考核文档
## 前言
首先恭喜各位完成上一轮考核

本轮我们的任务是写一个自然语言处理（NLP）模型，基本上能够理解中文语义

## 具体要求
1. 基于 Attention 机制搭建一个 Transformer 模型，模型可以参考 pytorch 的教程、参考开源模型如 Bert、GPT 等
2. 本轮要求完成的任务是MLM(Masked Language Modeling)，就是遮蔽一些字然后模型能还原被\<mask\>的字  
训练时采用无监督学习，预测掩蔽字的方法训练，  
> 输入输出样例：  
> 输入“\<S\>古娜拉黑\<mask\>之神，呜呼啦呼，黑魔变身。\<T\>”  
> 输出“\<S\>古娜拉黑暗之神，呜呼啦呼，黑魔变身。\<T\>”  
> 其中\<S\>、\<mask\>、\<T\>都是特殊标识符，类似的还有\<UNK\>等。
3. 不能用预训练模型超近路，所以权重必须从随机训练至收敛,但是可以改进其结构然后自己训练
4. 训练集得自己用爬虫爬，大小参考去年用的数据集约60mb

## 训练完成后，使用3个数据集进行模型评估benchmark
1. 中文语言理解测评基准我们采用CLUE benchmark，它分为多个测试数据集，最终的测试成绩为所有数据集上成绩的算数平均，本轮各位需要运行的数据集有：[AFQMC' 蚂蚁语义相似度](https://storage.googleapis.com/cluebenchmark/tasks/afqmc_public.zip)、[IFLYTEK' 长文本分类](https://storage.googleapis.com/cluebenchmark/tasks/iflytek_public.zip)、[TNEWS' 今日头条中文新闻（短文本）分类](https://storage.googleapis.com/cluebenchmark/tasks/tnews_public.zip)三个数据集，其他数据集如果有余力可以自行测试并一起提交，其他数据集的下载以及微调时的参数可以参照[CLUE benchmark](https://github.com/CLUEbenchmark/CLUE)的GitHub地址。
2. 一个数据集下载下来包含3个json文件，分别是训练集开发集和测试集，用训练集对模型进行微调，后再跑测试集来看正确率
### 资料
1. https://www.jianshu.com/p/037b81989d74
2. https://huggingface.co/docs/transformers/tasks/sequence_classification
3. https://zhuanlan.zhihu.com/p/609328862

## 参考建议
1. 如果自己电脑跑不了可以晚上十二点去阿里云租搭载 V100 的抢占式服务器，夜间小时
计费非常便宜划算,另外可以报销服务器购买费用,仅限抢占式GPU例程,每人报销上限为50元。
2. 建议将**每个中文单字作为句子拆分的单位**而不是词。如果想尝试拆词建议使用 jieba 分
词算法。
3. 迭代次数可能回明显多于前几轮，有时候 30 多个 epoch 才看得出损失在下降，最终训
练时间可能会花费十多个小时，使用一开始看前几轮没啥变化不要急着停。
4. 有问题及时交流


## 提交内容
-------
将提交文件打个zip发到群里，典型的提交文件如下
```
ProjetcFodder
├─src
    ├─data
        └─(自己爬的数据集,最好弄成json格式)
    ├─save_models
        └─weight.pth(保存的模型参数)
    ├─model.py
    ├─utils.py(处理数据集的文件)
    └─trainer.py(训练器，包含trainer类)
├─train.py(具体训练的过程代码)
├─test.py(用测试集测试的过程代码)
├─requirements.txt
├─network.jpg
└─result.jpg(训练结果图)
```

具体的文件内容建议如下

+ test.py 包含一个测试函数def test(input_str: str),输入含有[BEGIN]、[END]、[MASK]等字段的字符串，自动调用模型对[MASK]处的字进行预测。
+ model.py 仅包含模型的类定义，具体训练、数据处理的代码最好放在诸如train.py、tokenlizer.py当中。
+ weight.pth 模型的权重文件，该文件应当只包含模型权重而不包含文件结构。
+ requirements.txt 环境配置文件，可由pip一键生成，但是请剔除一些绝对用不上的包
+ network.jpg 使用tensorwatch画的网络结构图，本轮可以不用tensorwatch画，可以手画


> 提交文件中包括但不限于以上文件，但是**禁止提交venv、.idea等环境文件**，所提交的代码应是在在执行以下代码安装环境后就可直接运行的最精简文件
> ```
> pip install -r requirement.txt
> ```

## 评价指标
1. 本次考核侧重各位模型构建和查找资料的能力，最后应该会有一个关于模型的答辩，最
终模型的效果不是考核的大头。
2. 自建数据集、阅读论文等这些都可以为最后考核加分
