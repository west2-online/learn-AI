# west2-online AI 考核指南

欢迎来到西二在线工作室人工智能方向的考核指南。本指南旨在为初学者提供一条循序渐进的人工智能学习路线，帮助你系统性地掌握人工智能的核心知识与技能。

## 版权声明

本项目遵循 GPL-3.0 License。如需转载，请注明本项目仓库地址。

## 文档结构

所有考核相关文档均按学习目的 - 学习内容 - 学习要求（可能没有） - 作业 - 推荐教程与参考资料的目录结构编写。

> [!TIP]
> 从往年的经验来看，无人在意“推荐教程与参考资料”这部分内容，因此将其移到作业之后。但我希望你能认真看完这部分内容，因为这部分不只是推荐教程，还有更多有用的信息。

除此之外，我们还会提供各种补充资料。这部分并非考核内容，但如果你想学得更好，可以参考这些资料。

## AI 学习路线总览

```mermaid
graph TD
    %% AI 学习路线总览
    A[环境搭建] --> B[语法基础与简单面向对象]
    B --> C[网络爬虫]
    B --> E[简单数据分析与可视化]
    C --> D[后续简介]
    E --> D[后续简介]

    %% AI 相关技能树
    D --> J((Python 前 / 后端))
    D --> F((底层 AI 学习))
    D --> G((顶层 AI 应用))
    D --> H((数据科学分析))
```

考核大致分为两个阶段：[Foundation](./tasks(2026)/foundation) 与分流阶段（[Scientific Research](./tasks(2026)/scientific-research) / [Application](./tasks(2026)/application)）。[Foundation](./tasks(2026)/foundation) 是共通路线，完成后你需要在 Scientific Research 与 Application 两条路线中选择其一。

如果你想保研，未来想进实验室，那么建议选前者。

如果你未来想找工作，那么可以选择后者。

关于更具体的建议，以及为什么会有 [Python Backend](./tasks(2026)/backend)、[Python Frontend](./tasks(2026)/frontend) 和 [Statistics](./tasks(2026)/statistic)，可见 [Foundation](./tasks(2026)/foundation) 中的 [Task 4（task4.md）](./tasks(2026)/foundation/task4.md)，这是后续方向导引。

### 成为正式成员后的权益

通过所有考核后，你将成为西二在线网络工作室的正式成员，并获得以下权益：

- 成员证书
- 使用工作室的计算资源，组队参与算法竞赛
- 获得外包项目与企业实习机会
- 拥有固定的个人工位及活动室使用权
- 参与科研合作项目
- ~~玩无人机~~

## 如何开始

请进入 [tasks(2026)](./tasks(2026)) 文件夹，从 [Foundation](./tasks(2026)/foundation) 中的 [Task 0](./tasks(2026)/foundation/task0.md) 开始学习。

我们希望学习方式是“文档引导 + 个人自学”。我们会告诉你应当如何快速上手，但你想要学好、学懂，除了我们的引导外，还需要主动进行个人提升。

从功利的角度出发，如果你想进入 west2-online 工作室，在完成基础内容后，还需要适当完成一定量的 Bonus 内容。

我们的答辩会考察你一定的知识储备。

## 作业提交方式

你需要阅读 [作业提交指南](./tasks(2026)/commit-task/work-commit.md) 来了解作业提交的具体要求和流程。

你还需要阅读 [Git 使用指南](./tasks(2026)/commit-task/git-study.md) 来了解 Git 的使用方法。

此外，由于 AI 在不断发展，作业内容在不断变化，可能你做着做着作业内容就全变了。

所以请时刻关注本仓库。

## 详细说明

更多关于考核设计的思考，请参考 [ShaddockNH3 的博客](https://shaddocknh3.github.io/2025/10/19/3.w2-ai-think/)。

这篇博客已经过时，待 ShaddockNH3 有时间再维护。

## 维护指南

维护者在修改文档前，请先阅读 [Markdown 维护规范](./docs/markdown-style-guide.md)。

提交前至少运行一次 Markdown 检查：

```powershell
.\scripts\check-markdown.ps1
```

Linux / macOS 用户可以运行：

```shell
sh scripts/check-markdown.sh
```

也可以直接使用跨平台 Node.js 入口：

```shell
node scripts/check-markdown.mjs
```

新增或修改任务文档时，请优先保持“学习目的 - 学习内容 - 作业 - 推荐教程与参考资料”的结构，并遵守中英文空格、中文数字空格、数字单位和中文标点规范。

## 致谢

感谢 [ShaddockNH3](https://github.com/ShaddockNH3)，[JadeMelody](https://github.com/wjord2023)，[Tomori Nao](https://github.com/TomoriNaoiy)，[Longxi Zheng](https://github.com/REREREGO)，[Cai](https://github.com/ACaiCat)，[Schariac125](https://github.com/Schariac125)，[柠檬味氨水](https://github.com/weijianxian)，对 2026 / 2025 / 2024 版考核的贡献。

## 加入我们

欢迎扫码加入 AI 方向学习交流群，与其他学习者共同进步。

![west2-AI-qrcode-2025](./README.assets/west2-AI-qrcode-2025.jpg)
