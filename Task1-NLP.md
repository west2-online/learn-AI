# 人工智能考核文档
## 前言
首先恭喜各位完成上一轮考核，本轮我们的任务是完成IMDB数据集的训练，IMDB是NLP领域中一个很简单的数据集，是入门NLP的好选择

## 教程
1. 跟李沐学AI的b站教程（推荐）:https://www.bilibili.com/video/BV1if4y147hS 以及配套的课程网站：https://courses.d2l.ai/zh-v2/
2. Pytorch的官方教程（英文）：https://pytorch.org/tutorials/

## 数据集下载
下载群文件里的IMDB数据集，词表文件可以用自己的也可以用数据集自带的  
数据集包含一个json文件和一个vocab文件  
json文件的格式为  
```json
{
    'train': [
        'seq': ...
        'label': '0'/'1'
    ]
    'test': [
        'seq': ...
        'label': '0'/'1'
    ]
}
```
其中0为负面评论，1为正面评论

## 具体要求
1. 自主完成IMDB数据集的正负语义判断，可以用RNN的各种模型和自己从写的各类Transformer模型，或者可以试试MLP和CNN以及杂糅的模型
2. 用matplotlib画训练集的精确度(train_acc)和损失(train_loss)曲线
3. 从群文件下载数据后，自行完成数据集的处理，并实例化成pytorch的一个dataset类，代码放在utils.py里
4. 不能直接用李沐老师教程里的d2l库，不能直接copy代码
5. 不能用预训练模型超近路

## 提交内容
-------
用pull request发到github上，不用包含训练完的模型，典型的提交文件如下
```
ProjetcFodder
├─src
    ├─model.py
    ├─utils.py(处理数据集的文件)
    └─trainer.py(训练器，包含trainer类)
├─train.py(具体训练的过程代码)
├─test.py(用测试集测试的过程代码)
├─requirements.txt
└─result.jpg(训练结果图)
```

> 提交文件中包括但不限于以上文件，但是**禁止提交venv、.idea等环境文件**，所提交的代码应是在在执行以下代码安装环境后就可直接运行的最精简文件
> ```
> pip install -r requirement.txt
> ```

## 最终提交
1. 为营造学习氛围，结束后会开一次~~吹逼大会~~，主要各位交流自己学习经验经历，以及互相解答问题，不需要准备ppt什么乱七八糟的，分享内容也不纳入考核
2. 提交可实现功能的代码即可进入下一轮的考核
3. 有任何问题或者遇到难题可以在群里提问
