# Backend Routine

## 学习目的

尽管 Python 后端已经不再推荐，但是仍然可以用于快速验证原型机、个人小项目以及应付大作业。

## 学习内容

[Go 后端 / 运维从入门到如土](https://github.com/west2-online/learn-go)

Flask / FastAPI

## 作业

你可以完成这些作业来检验你的学习水平。这些作业并不需要提交，当然你也可以提交展示并参与答辩。

其实我更推荐你直接去写 Go / Java 的考核，写这些东西代码不重要，重要的是你的架构思想和统筹全局的观念。

### To-Do List Demo

[To-Do List Demo](https://github.com/west2-online/learn-go/blob/main/docs/3-%E5%A4%87%E5%BF%98%E5%BD%95.md)

### TikTok Demo

[TikTok Demo](https://github.com/west2-online/learn-go/blob/main/docs/4-%E5%A4%A7%E4%BD%9C%E5%93%81.md)

### TikTok Demo PLUS

[TikTok Demo PLUS](https://github.com/west2-online/learn-go/blob/main/docs/5(2025)-%E5%BE%AE%E6%9C%8D%E5%8A%A1.md)

### TikTok Demo Ultra

[TikTok Demo Ultra](https://github.com/west2-online/learn-go/blob/main/docs/6(2025)-%E9%83%A8%E7%BD%B2%E4%B8%8E%E7%9B%91%E6%8E%A7.md)

## 推荐教程与参考资料

### 一些问题

1. ~~Q：我想学人工智能，为什么要学后端方面的知识？~~

    ~~A：人工智能不是单打独斗，也需要合作应用，很多时候训练好的模型在别人调用时，需要一些简单的接口，因此需要学习少量的后端知识，从而知道怎么发送接口，但是无需深入了解。~~

2. Q：Python 后端有前途吗？

    A：Python 后端在几年前还是很热门的，但是现在已经日渐式微，在求职方面比不过 Java 和 Go，但由于搭建速度快还是有些中小公司在产品初期使用，因此如果有想深入后端的，可以去多看看 Java 和 Go，或者转前端测试。但是如果你只想做一个个人的小项目的话，Python 开发速度快，工具多，是不错的选择。

3. Q：为什么学习 Flask 或者 FastAPI，而不是 Django？

    A：现在前后端分离是主流，前端通过接口和后端通信，而不是后端直接渲染模板，强调低耦合。对入门者而言，Flask 与 FastAPI 更轻量，便于理解接口设计和服务结构；Django 并非“不强”，只是更偏向一体化框架，在本阶段不是最优先选项。

### 偏基础阶段的文档

1. Git 和 GitHub 的使用：<https://blog.csdn.net/weixin_53315561/article/details/126802065>（PyCharm 的 Git 集成也很方便，可以了解一下）
2. Flask 文档：<https://dormousehole.readthedocs.io/en/latest/>
3. Flask 视频教程：<https://www.bilibili.com/video/BV1v7411M7us>（该教程主要讲接口开发，适合前后端分离场景）
4. FastAPI 文档：<https://fastapi.tiangolo.com/zh/>（文档体系完善，建议优先阅读官方文档）
5. 接口测试工具
    - apifox：<https://www.apifox.cn/>
    - apipost：<https://www.apipost.cn/>
    - postman：<https://www.postman.com/>
6. REST 风格 API：<https://juejin.cn/post/7025222833798119454>。请优先使用规范的 HTTP 状态码表达请求结果（如 200/201/400/401/403/404/500），返回体可包含 `code`、`msg`、`data` 等业务字段。

    ```json
    HTTP/1.1 404 Not Found
    Content-Type: application/json
    Server: example.com
    #失败
    {
        "code": 404,
        "msg": "该活动不存在",
    }
    #成功
    {
        "code": 200,
        "msg": "success",
        "data": {
            ...
        }
    }
    ```

7. RESTful API 部分相关前置知识：<https://cloud.tencent.com/developer/article/1448167> 、<https://blog.csdn.net/D_R_L_T/article/details/82562902>
8. 多种传参方式：Query 传参和 Body 传参，具体请看相应框架文档
9. GitHub 是一个很好的学习平台，可以看别人的代码的架构了解自己的不足
10. PyCharm 可以在创建项目时选择 Flask 或 FastAPI 模板，让项目快速启动

### 稍微进一步的文档

1. REST API
2. JWT 鉴权知识：<https://learnku.com/articles/17883>
3. JWT 用法：<https://blog.csdn.net/yangbindxj/article/details/125344291>（这里使用的是 FastAPI 示例，核心思路同样适用于 Flask）
4. ORM：Flask 推荐 Flask-SQLAlchemy，FastAPI 推荐 SQLAlchemy
5. 蓝图（Flask）/ APIRouter（FastAPI）：参考各自官方文档
6. 通过异常处理器（`@app.errorhandler` / `@app.exception_handler`）捕获异常（参数错误、Token 错误等），并将其格式化为统一返回结构
7. 文件的上传，响应文件下载
8. 推荐使用 logging 日志工具打印运行时的日志
9. 在登录后于 Token 中加入权限信息；对于需要鉴权的接口，在 JWT 解码后执行权限校验并拦截非法请求。Flask 可使用装饰器，FastAPI 可使用依赖注入或中间件
10. FastAPI 可使用 Pydantic 做参数校验；Flask 可结合 Flask-RESTful 或 Marshmallow 进行参数与序列化校验 [Flask-RESTful](http://www.pythondoc.com/Flask-RESTful/index.html)
11. 在框架中接入 Redis 等进行缓存，读写很快，可以用于缓存验证码，以及一些经常读写的信息
12. 部署项目环境弄起来非常难受，建议大家学习 Docker，使用 Docker 将项目部署到服务器
13. 各种 ID 可以使用雪花算法生成，防止数据库自增 ID 过程出错

### 偏进阶阶段的文档

1. [Flask-SocketIO](https://flask-socketio.readthedocs.io/)：经常打不开，不过网上有很多它的翻译，可以查看
2. [fastapi-socketio](https://github.com/pyropy/fastapi-socketio)：文档相对少一些，不过网上有一些实战经验可供参考
3. [Socket.IO](https://socket.io/zh-CN/)：较完善的 Socket.IO 文档，不过服务端示例以 Node.js 为主，不是 Python；客户端 API 在写前端时可能会用到
4. 建议使用 `logging` 打印运行日志
5. 使用 pytest 编写单元测试，并用 pytest-cov 查看覆盖率（不强求固定数值，但应覆盖核心业务逻辑）
6. 建议准备一台云服务器用于部署实践，部署时建议使用 `gunicorn`（Flask/FastAPI）等生产级启动方式
7. 建议学习 Docker，将项目容器化后再部署
8. 建议使用 Type Hint 与必要注释，增强可读性和可维护性
9. 继续扩展学习可参考：[awesome-flask](https://github.com/humiaozuzu/awesome-flask) 与 [awesome-fastapi](https://github.com/mjhea0/awesome-fastapi)

### 开源相关

这里我们推荐以下站点，可以关注一下：

1. 开源软件供应链点亮计划（开源之夏）：<https://summer-ospp.ac.cn/>
2. Google Summer of Code (GSoC)：<https://summerofcode.withgoogle.com/>
3. GLCC开源夏令营：<https://opensource.alibaba.com/>
4. 腾讯犀牛鸟开源人才培养计划：<https://opensource.tencent.com/summer-of-code>

除此之外，可以关注一下一些大厂的开源网站

1. 阿里开源：<https://opensource.alibaba.com/>
2. 腾讯开源：<https://opensource.tencent.com/>
3. Meta Open Source：<https://opensource.fb.com/>
4. Google Open Source：<https://opensource.google/>
5. Uber Open Source：<https://uber.github.io/#/>
6. 开源 - 美团技术团队：[https://tech.meituan.com/tags/%E5%BC%80%E6%BA%90.html](https://tech.meituan.com/tags/开源.html)
