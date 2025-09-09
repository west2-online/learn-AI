# Task 1

### 学习内容

Python基础语法、认识生成式AI

### 疑问解答

- 是否需要好的显卡？

学习人工智能有一个好的显卡会有一定帮助，但是不是刚需，你完全可以使用[Colab](https://colab.research.google.com/)或者gpu云服务器来进行机器学习代码的编写和运行

### 考核内容

#### 1. 配置环境

- 魔(ti)法(zhi)的使用

- 安装IDE集成开发环境

初学者可以选择使用[PyCharm](https://www.jetbrains.com.cn/pycharm/), 可以[申请学生免费许可证](https://blog.jetbrains.com/zh-hans/blog/2022/08/24/2022-jetbrains-student-program/)以使用专业版

个人更建议使用[VSCode](https://code.visualstudio.com/)（主要是PyCharm的Jupyter notebook太过难用， 建议初学者可以多使用Jupyter来编写程序）

- 安装Conda环境

使用[miniconda](https://docs.anaconda.com/miniconda/)就可以了,当然如果你不喜欢conda这样会污染命令窗口，使用pyenv或venv也都是可以的

- 学习python虚拟环境的配置

初学者一定要注意这个问题，从一开始就养成好的习惯

#### 2. 推荐教程

- python基础：

1. Crossin编程教室 [Python 入门指南 (python666.cn)](https://python666.cn/cls/lesson/list/)
2. Python - 100天从新手到大师的前10节课 [jackfrued/Python-100-Days: Python - 100天从新手到大师 (github.com)](https://github.com/jackfrued/Python-100-Days)
3. Python官方文档 [3.10.7 Documentation (python.org)](https://docs.python.org/zh-cn/3/)
4. 菜鸟教程 [Python3 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python3-tutorial.html)
5. 廖雪峰的官⽅教程 [Python教程 - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/wiki/1016959663602400)
6. B站上有大量的入门基础课程，大家可以自行探索，找到适合自己的是最好的
7. 如果你想要系统的学习的话，我强烈推荐来自UCB的神课[CS61A](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/Python/CS61A/)（课程难度较大，建议可以先选择一个更为友好的入门编程课程入门， 需要学习相关学习资料的话可以来群里问）

- 生成式AI认识：

[李宏毅2024 B站](https://www.bilibili.com/video/BV1BJ4m1e7g8/?spm_id_from=333.337.search-card.all.click&vd_source=e3594664d709db7578f4b2e76329df18)

[李宏毅2024 油管](https://www.youtube.com/watch?v=AVIKFXLCPY8&t=1s)

#### 3. 检验学习内容

在你完成python基础的知识学习后，你需要确保你对以下知识点能正确回答（如果不能你仍可以通过b站视频以及网上文档的方式进行弥补）

- 数据结构List,Dict的使用
- Lambda匿名函数
- Decorator装饰器
- 类Class，Magic Methods的使用
- re正则表达式的使用
- 列表推导式
- generator生成器（yield关键字）
- OOP面向对象编程思想
- Type Hint 类型注释

你可以写一个文档详细解释这些内容以加深印象（可以使用markdown/jupyter的形式编写）

在完成生成式AI认识的学习后，你可以写一个文档详细向我们介绍一下一个大型语言模型训练的基本步骤

#### 4. 完成作业

- ##### 作业一 娜比娅偷吃事件

某日，在前往ShaddockNH3办公室的路上，重樱的神子大人 **长门** 意外地发现，一个塞壬人形“娜比娅”正鬼鬼祟祟地躲在角落里偷吃军粮！

「汝，竟敢在余之港区放肆！」

为了维护港区的和平（和食物！），长门决定亲自出手，给这个不懂礼数的闯入者一点教训！

你的任务，就是为长门大人编写战斗的核心逻辑，帮助她赶跑偷吃的娜比娅！

请下载task1文件夹下的压缩文件`Nabia_Snack_Incident`，解压后阅读`README.md`，根据指引完成8个函数的编写。

这份作业并不难，只涉及到`if`,`else`,`while`，所以请不要看`Nabia_Snack_Incident`下的`answer.py`

### 作业要求

1. 不要抄袭
2. 遇到不会可以多使用搜索引擎，实在没有找到解决方法可以来群里提问，作为一个CSer学习问问题的方式也非常重要，强烈建议阅读[别像弱智一样提问](https://github.com/tangx/Stop-Ask-Questions-The-Stupid-Ways/blob/master/README.md)这篇文章
3. 不限制使用chatgpt等大语言模型工具，但你需要确保你了解模型生成的内容的每一个细节，最好你可以在使用大语言模型生成的代码部分注释上reference from chatgpt这样的内容
4. 你还需要学习基本的git的使用，所有考核都采用git的方式进行上传
5. 作业内容可能会进行更新，请保持关注

### 作业提交方式

1. 你需要学习github的使用，创建一个你自己的仓库用来存放你的代码实现
2. 接着你需要如何使用git进行pr操作，在[solutions](https://github.com/west2-online-reserve/collection-ai/blob/main/task1/solutions.md)中填写你的仓库地址，这样便于你对你的实现进行更新

相关教程

<https://github.com/west2-online-reserve/collection-ai> 里面有git使用和西二作业提交教程

[Git工作流和核心原理 | GitHub基本操作 | VS Code里使用Git和关联GitHub](https://www.bilibili.com/video/BV1r3411F7kn/?share_source=copy_web&vd_source=31019e44b62a4369d4eab7afea0fcfdf)

### Bonus

完成CS61A的学习，完成相应的作业和lab（不要畏惧全英文的学习，你完全可以使用各类翻译软件帮助你学习(包括gpt)）,如果能啃下这门课那么你的编程水平将会超过绝大多数毕业生
