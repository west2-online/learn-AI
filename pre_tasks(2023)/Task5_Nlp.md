# 人工智能考核文档
## 前言
首先恭喜各位完成上一轮考核

本轮我们的任务是使用已有的预训练模型，进行学习如何进行语言模型的基准测试，具体到本次任务是给bert和各位上一轮的自己写的模型进行基准测试。

## 相关信息
1. [HuggingFace](https://www.huggingface.co/)是一个非常活跃的人工智能开源社区，维护了python上的Transformer库，可以非常方便调用各大预训练模型。调用transform库如下所示，其中的BertModel对象就是torch的nn.Model的派生类，可以同普通pytorch模型一样训练和推理。
    ```
    from torch import LongTensor
    from transformers import BertTokenizer, BertModel
    
    tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")
    bert = BertModel.from_pretrained("bert-base-chinese")
    onehot_list=tokenizer.encode("某[MASK]文字", padding="max_length", max_length=64)
    
    bert.eval()
    input_tensor=LongTensor([onehot_list])
    output_tensor=bert(input_tensor)[0]
    ```
2. 中文语言理解测评基准我们采用CLUE benchmark，它分为多个测试数据集，最终的测试成绩为所有数据集上成绩的算数平均，本轮各位需要运行的数据集有：[AFQMC' 蚂蚁语义相似度](https://storage.googleapis.com/cluebenchmark/tasks/afqmc_public.zip)、[IFLYTEK' 长文本分类](https://storage.googleapis.com/cluebenchmark/tasks/iflytek_public.zip)、[TNEWS' 今日头条中文新闻（短文本）分类](https://storage.googleapis.com/cluebenchmark/tasks/tnews_public.zip)三个数据集，其他数据集如果有余力可以自行测试并一起提交，其他数据集的下载以及微调时的参数可以参照[CLUE benchmark](https://github.com/CLUEbenchmark/CLUE)的GitHub地址。
3. 一个数据集下载下来包含3个json文件，分别是训练集开发集和测试集，用训练集对模型进行微调，后再跑测试集来看正确率
4. 使用的bert模型地址：https://www.huggingface.co/bert-base-chinese
## 资料
1. https://www.jianshu.com/p/037b81989d74
2. https://huggingface.co/docs/transformers/tasks/sequence_classification
3. https://zhuanlan.zhihu.com/p/609328862

## DDL：暂定7.20晚上进行吹逼大会兼成果验收