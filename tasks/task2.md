# Task 2

## 学习内容

- 爬虫初步学习

  - 网页抓包工具的使用
  - 网络请求的处理（requests库的使用）
  - 数据的提取（xpath(推荐)、bs4、···）
  - selenium的使用

- 数据科学基本工具学习
  - Pandas的学习
    - 数据读取与写入
    - 数据清洗
    - 数据筛选与索引
    - 数据的处理与变换
    - (optional) 数据可视化（matplotlib、plotly、pyecharts、···）
  - numpy的学习
    - TODO

## 学习要求

本轮学习内容较多也较杂，所以不会有太高的要求（毕竟我们不是搞AI的吗），爬虫只要求掌握最基础的使用requests进行请求和使用xpath等工具进行数据提取以及使用selenium进行爬取（selenium使用简单还不容易被反爬），而对于pandas也只要求有基础了解，并具有在需要时可通过查阅手册（当然AI对于写pandas特别厉害）的方式解决问题，由于有良好的numpy基础对于后期学习pytorch以及AI有较大帮助，所以建议重点学习（当然考核有不会要求过深）

## 推荐教程

爬虫推荐的教程包含内容较多，大家根据考核需求自行选择，对于numpy和pandas个人没有找到太好的教程视频还多希望大家自行探索当然读文档学习也是非常好的方式、互联网上还要更多更好更适合你的学习方式供你探索、此外对于学有余力想要深入学习numpy和pandas的同学可以去学习[UC Berkeley Data 8](https://www.data8.org/)和[Data 100](https://ds100.org/)这两门课

- 爬虫

  - [b站视频](https://www.bilibili.com/video/BV1Yh411o7Sz)
  - [Python3网络爬虫开发实战教程](https://cuiqingcai.com/5052.html)
  - [xpath教程](https://www.runoob.com/xpath/xpath-syntax.html)
  - [selenium教程](https://www.selenium.dev/documentation/)
  - devtools的使用（[edge](https://learn.microsoft.com/zh-cn/microsoft-edge/devtools-guide-chromium/elements-tool/elements-tool)、[chrome](https://developer.chrome.com/docs/devtools?hl=zh-cn)）

- Pandas

  - [官方文档](https://pandas.pydata.org/docs/)
  - [菜鸟教程](https://www.runoob.com/pandas/pandas-tutorial.html)

- Numpy
  - [官方文档](https://numpy.org/doc/stable/)
  - [菜鸟教程](https://www.runoob.com/numpy/numpy-tutorial.html)

## 作业

### 爬虫

#### 作业1 爬取福大教务通知

网址：<https://jwch.fzu.edu.cn/jxtz.htm>

##### 要求

1. 获取教务通知(至少500条，我们要进行数据分析所以越多越好 :smirk: )
2. 提取通知信息中的“通知人”(如：质量办、计划科)、标题、日期、详情链接。
3. 爬取通知详情的html，可能存在“附件”，提取附件名，附件下载次数，附件链接吗，有能力请尽可能将附件爬取下来。
4. 上述内容一律要去除回车、括号等无用符号
5. 将爬去内容存储到csv文件中

#### 作业2 使用selenium爬取知乎话题

网址：<https://www.zhihu.com/topic/19554298/top-answers>

##### 要求

1. 考核仅要求对一个话题进行爬取(爬取50条问题，每个问题爬取20条回答即可(只爬问答就可以，其他类型如文章要爬也行))，学有余力的可以从[话题广场](https://www.zhihu.com/topics)开始爬
2. 将爬取内容存储到csv文件中，格式为：问题名、问题具体内容、回答信息（只需要留下纯文字），学有余力的可以把评论也保留下来

<br>

### Pandas

#### 作业3 对作业1爬取的福大教务处信息进行数据分析

##### 要求

1. 使用jupyter notebook的形式完成代码以及分析报告
2. 统计“通知人”都有哪些，各占比例多少？
3. 分析附件下载次数与通知人是否关系，若有，有什么联系？
4. 统计每天的通知数，分析哪段时间通知比较密集？（可以使用数据可视化的方式呈现）
5. 自行思考一个感兴趣的问题，并进行数据分析

<br>

### Numpy

#### 作业4 TODO

##### TODO

#### （optional）numpy实现神经网络（巨难）

##### 要求

1. 实现一个简单的两层神经网络
2. 可以多看看网络上博客以及github上的实现
3. 可以先看看李沐使用torch的实现转化为numpy实现

## 作业要求

1. 不要抄袭
2. 遇到不会可以多使用搜索引擎，实在没有找到解决方法可以来群里提问
3. 不限制使用chatgpt等大语言模型工具，但你需要确保你了解模型生成的内容的每一个细节，最好你可以在使用大语言模型生成的代码部分注释上reference from chatgpt这样的内容
4. 你还需要学习基本的git的使用，所有考核都采用git的方式进行上传
5. 作业内容可能会进行更新，请保持关注
