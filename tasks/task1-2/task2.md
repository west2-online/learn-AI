# Task 2

## 学习目的

AI的训练来源是大量的数据，获取数据有两种方式，第一种是直接下载已有的数据集，第二种是利用网络爬虫爬取想要的数据。

## 学习内容

- 爬虫初步学习

  - 网页抓包工具的使用
  - 网络请求的处理（requests库的使用）
  - 数据的提取（XPath（推荐）、bs4、……）
  - selenium的使用

## 学习要求

本轮学习内容不会有太高的要求（毕竟我们不是搞AI的吗），爬虫只要求掌握最基础的使用requests进行请求和使用XPath等工具进行数据提取，以及更强大的浏览器模拟工具Selenium（它能有效应对许多反爬机制）

虽说不是重点，但这门技术是你不得不掌握的知识。当某日陷入训练数据丢失，或者曾经写的爬虫脚本失效时，你得亲手去修改这些爬虫，让他们获取到正确的数据。

## 推荐教程

爬虫推荐的教程包含内容较多，大家根据考核需求自行选择。

- 爬虫
  - [b站视频](https://www.bilibili.com/video/BV1Yh411o7Sz)看到药企实战前，注意阿贾克斯
  - [50分钟超快速入门Python爬虫](https://www.bilibili.com/video/BV1EHdUYEEEj)
  - [Python3网络爬虫开发实战教程](https://cuiqingcai.com/5052.html)
  - [xpath教程](https://www.runoob.com/xpath/xpath-syntax.html)
  - [selenium教程](https://www.selenium.dev/documentation/)
  - devtools的使用（[edge](https://learn.microsoft.com/zh-cn/microsoft-edge/devtools-guide-chromium/elements-tool/elements-tool)、[chrome](https://developer.chrome.com/docs/devtools?hl=zh-cn)）

## 作业

第二轮的考核截止至12月中旬，本轮作业的重点在于实现核心功能并成功运行，不必在细节上追求完美，更鼓励你大胆尝试，让程序先跑起来，can run is ok.

### 作业1 爬取福大教务通知

网址：[https://jwch.fzu.edu.cn/jxtz.htm](https://jwch.fzu.edu.cn/jxtz.htm)

#### 要求

**Baymaxwish**从小就有一个黑客梦，但是奈何死活学不到那种动动手指就可以黑掉别人手机的技术，这让他试图**偷窥浏览记录**的伟大愿景无法实现。

但是偶然一天，他发现了**爬虫**这个可以自动爬取网页上的数据好玩技术。

疯狂的往各种网站发送请求并爬取大量信息的感觉......

让他觉得自己像一名真正的“**黑客**”一样

“**这不就是黑客吗？！**”

于是，为了成为一名顶尖“**黑客**” 他向某211大学的教务处发起了“攻击”。

以下是你的任务：

1. 获取教务通知(至少500条，我们要进行数据分析所以越多越好 :smirk: )
2. 提取通知信息中的“通知人”(如：质量办、计划科)、标题、日期、详情链接。
3. 爬取通知详情的html，可能存在“附件”，提取附件名，附件下载次数，附件链接码，有能力请尽可能将附件爬取下来。
4. 上述内容一律要去除回车、括号等无用符号
5. 将爬取内容存储到csv文件中

#### 提示

1. 使用校园网爬取不会遭到任何反爬机制

### 作业2 使用selenium爬取知乎话题

网址：[知乎](https://www.zhihu.com/topic/19554298/top-answers)

#### 要求

“城里的图书馆，书又多又厚，看完一本要好久好久... 可莉听说，在一个叫‘知乎’的神秘地方，藏着好多好多‘亮闪闪的宝物’！里面有关于‘蜥蜴能不能被炸晕’和‘最好的炸鱼地点’的超级大秘密！”

可莉挥舞着小拳头，眼睛里闪烁着好奇的火花。

但那个地方被一个看不见的“风墙”保护着，直接跑过去（requests）会被弹回来！琴团长说，那需要一种叫 Selenium 的“温和”的办法，就像派一个会隐身的嘟嘟可，悄悄地飞进去，把里面的“宝物”一个一个地抄在小本本上拿回来。

知乎是一个神秘的地方，有的地方大佬云集，有的地方满是糟粕，但无一例外的是，它们都具有高度的反爬机制，因此寻常的request请求很容易被ban.

于是Selenium应运而生，它是一个基于浏览器模拟的软件，可以有效避免反爬。

以下是你的任务：

1. 仅要求对一个话题进行爬取（爬取20条问题，每个问题爬取10条回答即可），学有余力的可以从[话题广场](https://www.zhihu.com/topics)开始爬
2. 将爬取内容存储到csv文件中，格式为：问题名、问题具体内容、回答信息（只需要留下纯文字），学有余力的可以把评论也保留下来

#### 提示

1. 登录知乎有两种方式，第一种是直接扫码登录，第二种是采用cookies

### 作业3 通过抓取接口爬取开源之夏2025项目列表

网址：[https://summer-ospp.ac.cn/org/projectlist](https://summer-ospp.ac.cn/org/projectlist)

#### 要求

weijianxian是一只可爱的猫娘，她对bs4的不优雅颇有微词。碰巧她曾经写过开源之夏，所以她知道，直接去解析那个网页的HTML，就像在一大团乱糟糟的毛线球里找线头一样，真是太麻烦了喵！才不要用那种笨办法呢！(｡･`ω´･｡) 

她记得很清楚，开源之夏的网站前端背后，藏着一个可以直接返回项目列表的整洁接口。我们只要找到那个接口，就能拿到干干净净、排排坐好的JSON数据，这才是最聪明的做法呀~♪

有些网页使用了前后端分离的技术，直接使用requests等库是无法获取到网页内容的，而使用selenium等浏览器模拟工具又显得过于重型。

幸运的是，这类网站一般会通过接口与后端进行数据交互，我们可以通过在浏览器控制台的network中找到这些接口并进行请求，从而获取到我们想要的数据。

以下是你的任务：

1. 通过浏览器抓包工具找到开源之夏项目列表的接口，并使用requests等库进行请求，获取到项目列表
2. 获得每个项目的 项目名 项目难度 技术领域标签
3. 获取每个项目的 具体信息,包括 项目简述 项目产出要求
4. (进阶) 下载项目申请书的pdf

### bonus wiki

网址：

[https://wiki.biligame.com/blhx/api.php](https://wiki.biligame.com/blhx/api.php)

[https://wiki.biligame.com/blhx/%E5%88%86%E7%B1%BB:%E6%96%B9%E6%A1%88%E8%88%B0%E5%A8%98](https://wiki.biligame.com/blhx/%E5%88%86%E7%B1%BB:%E6%96%B9%E6%A1%88%E8%88%B0%E5%A8%98)

#### 要求

为了完成ShaddockNH3自己给自己布置的[task7-nlp-作业2](../task7/task7_nlp.md)最终完整版项目，可怜的[Gemini](https://gemini.google.com/)被当成黑奴一样，天天被ShaddockNH3驱使着爬取wiki的内容。

wiki是一个开放的知识库，通常由社区成员共同维护和编辑。它允许用户创建、修改和链接页面，以便共享信息和知识。wiki通常具有版本控制功能，可以跟踪页面的历史变化，并允许用户回滚到之前的版本。

api是应用程序编程接口（Application Programming Interface）的缩写，是不同软件系统之间进行交互和通信的桥梁。它定义了一组规则和协议，允许一个软件应用程序访问另一个软件应用程序的功能或数据，而无需了解其内部实现细节。

事实上，在大多数情况，爬虫不需要从零开始编写，而是可以直接使用网站提供的api进行数据获取。

以下是你的任务：
1. 通过wiki的api获取wiki中“方案舰娘”分类下的所有页面，不需要整理文本（洗数据非常麻烦，直接获取原始数据即可）

#### 提示

1. 比较抽象的是，wiki的页面上显示允许爬虫，但是具体种类的具体参数只有管理员才能访问，因此可以使用抓包工具或者直接试出来具体的页面信息，涉及到一定的逆向思维
2. ~~当你实在猜不到api，红温了，直接上模拟浏览器~~
3. api的访问需要遵循礼仪，如wiki的api建议每次访问间隔1秒以上，且当服务器繁忙时，最长等待5秒，否则放弃请求。此外，不可以采用并行请求的方式，否则会被ban掉ip
4. 这里直接给出请求头，category是“方案舰娘”

```python
# --- 全局配置 ---
API_URL = "https://wiki.biligame.com/blhx/api.php"
OUTPUT_DIR = "name_you_like"  # 输出文件夹名称

# 规范化请求头
HEADERS = {
    'User-Agent': '',
    'Accept-Encoding': 'gzip', # 启用Gzip压缩，节约带宽
}

# 最终验证过的 分类 -> 文件名前缀 映射表
CATEGORY_PREFIX_MAP = {
    "Category:方案舰娘": "PR",
}
```

以及请求参数

```python
        params = {
            "action": "query", 
            "list": "categorymembers", 
            "cmtitle": category, 
            "cmlimit": "500", 
            "format": "json", 
            "formatversion": "2",
            "maxlag": "5"  
        }
```

5. 可以参考[实现](https://github.com/ShaddockNH3/Nya-Akashi-Workshop/blob/dev/get_knowledge/get_ships.py)

> 不要拿ShaddockNH3的HEADERS，也不要运行这个文件，谢谢。由于本作业带私货，且设置的不严谨，所以作为bonus，可以选择性完成

## 作业要求

1. 不要抄袭，代码会查重
2. 遇到不会的问题可以多使用搜索引擎，实在没有找到解决方法可以来群里提问
3. 不限制使用chatgpt等大语言模型工具，但你需要确保你了解模型生成的内容的每一个细节，最好你可以在使用大语言模型生成的代码部分注释上reference from ChatGPT这样的内容
4. 你还需要学习基本的git的使用，所有考核都采用git的方式进行上传
5. 作业内容可能会进行更新，请保持关注