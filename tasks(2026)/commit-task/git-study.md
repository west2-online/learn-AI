# Git 相关教程、规范

## Git 相关教程

Git 入门：<https://west2-online.feishu.cn/wiki/Lsz9w3CiGinXzgkevtmceHZknrf>

GitHub 如何 Fork 与 PR（如何交作业）：<https://west2-online.feishu.cn/wiki/Zvqow0CUxig3iWkWQgBcHp4AnHe>

Git 使用与西二作业提交教程：<https://github.com/west2-online-reserve/collection-ai>

Git 工作流和核心原理 | GitHub 基本操作 | VS Code 里使用 Git 和关联 GitHub：<https://www.bilibili.com/video/BV1r3411F7kn/?share_source=copy_web&vd_source=31019e44b62a4369d4eab7afea0fcfdf>

Git 工作流：<https://www.bilibili.com/video/BV19e4y1q7JJ/?spm_id_from=333.337.search-card.all.click&vd_source=0272bb7dd0d8d9302c55fc082442b9e3>

## Git 规范

### 妥善使用 .gitignore

一些对于项目无用的，如 `__pycache__` 文件夹，`.vscode` 文件夹等不需要提交到 Git 仓库。

可以通过 `.gitignore` 文件忽略这些文件夹。

### 不要上传大文件到 GitHub

GitHub 建议单文件大小不超过 50MB，超过 100MB 的文件无法上传。另外，二进制文件不适合上传到 GitHub，建议使用云盘存储后在仓库中放置下载链接。

例如图片是二进制存储，一旦你提交了修改，GitHub 会保留历史版本，容易导致仓库体积持续膨胀。

旧图藏在了历史版本里，肉眼是看不到的。

所以，不要把大文件直接上传到 GitHub。

例如训练前的数据，训练好的模型文件，你爬虫爬到的东西，请使用 .gitignore 忽略掉。

### Commit 信息规范

对于这部分，刚开始可以相对随意一些，等你熟悉了 Git 的使用之后，再来规范这部分内容。

```bash
git commit -m "feat: add xxx feature"
git commit -m "fix: fix xxx bug"
git commit -m "docs: update xxx doc"
git commit -m "style: format xxx code"
git commit -m "refactor: refactor xxx code"
git commit -m "test: add xxx test"
git commit -m "chore: update xxx config"
```
