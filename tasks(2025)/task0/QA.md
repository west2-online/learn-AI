# 常见问题解答（Q&A）

> **使用说明**：遇到问题时，使用 `Ctrl+F` 搜索关键词快速定位解决方案。
>
> **事教人，一次就会。**

## 目录

- [提问的正确方式](#提问的正确方式)
- [环境配置问题](#环境配置问题)
- [Git 和 GitHub 问题](#git-和-github-问题)
- [Python 运行问题](#python-运行问题)
- [代码错误问题](#代码错误问题)
- [IDE 和编辑器问题](#ide-和编辑器问题)
- [网络和下载问题](#网络和下载问题)
- [其他常见问题](#其他常见问题)

---

## 提问的正确方式

当你遇到以下没有涵盖的问题时，请这样提问：

### ✅ 好的提问

我在运行网络爬虫时遇到了问题：

【我想做什么】
我想爬取某网站的新闻标题。

【我的代码】（贴上关键代码）
```python
import requests
url = 'https://example.com'
r = requests.get(url)
print(r.status_code)  # 输出 403
```

【完整报错信息】
403 Forbidden

【我尝试过的方法】
1. 检查了网址是否正确
2. 换了其他网站也不行

【我的环境】
- Python 3.9
- Windows 10
- requests 2.28.0

### ❌ 不好的提问

我的代码运行不了，怎么办？

（没有代码、没有报错、没有上下文，神仙也帮不了你）

---

## 环境配置问题

### Q: `conda` 命令找不到 / `conda: command not found`

**现象**：
```bash
conda: The term 'conda' is not recognized as the name of a cmdlet...
```

**原因**：Conda 没有被添加到系统环境变量 PATH 中。

**解决方案**：

**Windows：**
1. 打开"编辑系统环境变量"
2. 点击"环境变量"
3. 在"用户变量"中找到 `Path`，点击"编辑"
4. 添加以下路径（根据你的安装位置调整）：
   ```
   C:\Users\你的用户名\anaconda3
   C:\Users\你的用户名\anaconda3\Scripts
   C:\Users\你的用户名\anaconda3\Library\bin
   ```
5. 重启终端

**macOS/Linux：**
```bash
# 添加到 ~/.bashrc 或 ~/.zshrc
export PATH="$HOME/anaconda3/bin:$PATH"

# 重新加载配置
source ~/.bashrc  # 或 source ~/.zshrc
```

---

### Q: pip 安装包特别慢或失败

**现象**：
```bash
pip install numpy
# 卡住不动或下载速度很慢
```

**原因**：默认使用的是国外源，网络连接慢。

**解决方案**：

**临时使用国内源：**
```bash
pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**永久配置国内源：**

Windows：在用户目录下创建 `pip/pip.ini`：
```bash
# PowerShell
mkdir $env:USERPROFILE\pip
notepad $env:USERPROFILE\pip\pip.ini
```

macOS/Linux：创建 `~/.pip/pip.conf`：
```bash
mkdir ~/.pip
nano ~/.pip/pip.conf
```

写入以下内容：
```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```

**常用国内源：**
- 清华：`https://pypi.tuna.tsinghua.edu.cn/simple`
- 阿里云：`https://mirrors.aliyun.com/pypi/simple/`
- 中科大：`https://pypi.mirrors.ustc.edu.cn/simple/`

---

### Q: 虚拟环境激活失败 / `Activate.ps1 is not digitally signed`

**现象**（Windows PowerShell）：
```
.\venv\Scripts\Activate.ps1 : File cannot be loaded because running scripts is disabled on this system.
```

**原因**：PowerShell 默认禁止运行未签名的脚本。

**解决方案**：

**方法 1：临时允许**（推荐）
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate.ps1
```

**方法 2：永久允许**（需要管理员权限）
```powershell
# 以管理员身份运行 PowerShell
Set-ExecutionPolicy RemoteSigned

# 然后激活环境
.\venv\Scripts\Activate.ps1
```

**方法 3：使用 cmd 激活**
```cmd
venv\Scripts\activate.bat
```

---

### Q: 虚拟环境中 pip 安装的包在 IDE 中无法识别

**现象**：代码能运行，但 IDE 提示 `Module not found`，没有自动补全。

**原因**：IDE 使用的 Python 解释器不是虚拟环境中的。

**解决方案**：

**VS Code：**
1. `Ctrl+Shift+P` 打开命令面板
2. 输入 `Python: Select Interpreter`
3. 选择你的虚拟环境（路径中包含 `venv` 或 `env` 的）

**PyCharm：**
1. `File` → `Settings` → `Project` → `Python Interpreter`
2. 点击齿轮图标 → `Add`
3. 选择 `Existing environment`
4. 选择虚拟环境中的 `python.exe`（Windows）或 `python`（macOS/Linux）

---

### Q: 多个 Python 版本冲突 / 不知道用的是哪个 Python

**现象**：
```bash
python --version
# Python 3.9.0

python3 --version
# Python 3.11.0

# 运行代码时使用的版本不确定
```

**原因**：系统中安装了多个 Python 版本（系统自带、Anaconda、手动安装），环境变量 PATH 中的顺序决定了默认使用哪个。

**解决方案**：

**1. 查看所有 Python 安装位置：**

Windows (PowerShell)：
```powershell
Get-Command python -All
Get-Command python3 -All

# 或者
where.exe python
where.exe python3
```

macOS/Linux：
```bash
which -a python
which -a python3

# 查看具体版本和路径
python --version
python3 --version
/usr/bin/python3 --version
~/anaconda3/bin/python --version
```

**2. 明确指定使用哪个 Python：**

**方法 A：使用完整路径**
```bash
# Windows
C:\Users\YourName\anaconda3\python.exe script.py

# macOS/Linux
/usr/local/bin/python3.11 script.py
```

**方法 B：创建虚拟环境（推荐）**
```bash
# 指定 Python 版本创建虚拟环境
python3.11 -m venv myenv

# 或使用 conda
conda create -n myenv python=3.11

# 激活后就只使用这个版本
```

**3. 调整环境变量 PATH 顺序（Windows）：**

1. 右键"此电脑" → "属性" → "高级系统设置" → "环境变量"
2. 在"用户变量"中找到 `Path`
3. 将你想要优先使用的 Python 路径移到最上面
4. 重启终端生效

**为什么会有这个问题？**
- 安装 Anaconda 时会添加 Python 到 PATH
- 从 Python 官网安装时也会添加到 PATH
- 系统可能自带 Python（macOS/Linux）
- Windows Store 也可能安装 Python
- 最终 `python` 命令调用的是 PATH 中**最先找到的那个**

**最佳实践：**
```bash
# 永远不要直接用 python/python3
# 而是在虚拟环境中工作

# 1. 创建项目文件夹
mkdir my_project
cd my_project

# 2. 创建虚拟环境（指定版本）
python3.11 -m venv venv

# 3. 激活虚拟环境
# Windows
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

# 4. 现在 python 命令就固定使用这个版本了
python --version
```

---

### Q: pip 安装的包找不到 / 多个 pip 版本冲突

**现象**：
```bash
pip install requests
# Successfully installed requests-2.28.0

python script.py
# ModuleNotFoundError: No module named 'requests'
```

**原因**：系统中有多个 pip，你用的 pip 和你用的 python 不是同一个环境。

**解决方案**：

**1. 检查 pip 和 python 是否匹配：**

```bash
# 查看 pip 对应的 Python 路径
pip --version
# pip 21.0.1 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)

# 查看 python 路径
which python  # macOS/Linux
where python  # Windows

# 查看 python 实际执行路径
python -c "import sys; print(sys.executable)"
```

**如果路径不一致，说明 pip 和 python 不匹配！**

**2. 使用 `python -m pip` 而不是 `pip`（推荐）：**

```bash
# 这样能确保使用的 pip 和 python 是同一个
python -m pip install requests
python -m pip list
```

**3. 在虚拟环境中工作（最佳实践）：**

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

# 现在 pip 和 python 肯定是匹配的
pip install requests
python script.py  # 能找到 requests
```

**4. 如果是 conda 环境：**

```bash
# 检查当前环境
conda info --envs

# 确保已激活环境
conda activate myenv

# 使用 conda 安装
conda install requests

# 或在 conda 环境中用 pip
pip install requests
```

**常见错误示例：**

```bash
# 错误：用 pip3 安装，但用 python 运行
pip3 install requests
python script.py  # 找不到

# 正确：统一使用 python3
pip3 install requests
python3 script.py

# 最佳：使用 python -m pip
python -m pip install requests
python script.py
```

**为什么会这样？**
- `pip` 可能指向 Python 2
- `pip3` 可能指向系统 Python 3
- `python` 可能指向 Anaconda Python
- 它们安装的包在不同的目录，互相找不到

---

### Q: conda 和 pip 混用导致环境混乱

**现象**：
```bash
conda install numpy
pip install pandas
# 之后出现各种奇怪的依赖冲突
```

**原因**：conda 和 pip 使用不同的包管理机制，混用可能导致依赖关系混乱。

**解决方案**：

**原则：在 conda 环境中，优先使用 conda 安装**

**1. 正确的安装顺序：**

```bash
# 1. 先尝试用 conda 安装
conda install package_name

# 2. 如果 conda 没有这个包，再用 pip
pip install package_name

# 3. 避免反过来（先 pip 再 conda）
```

**2. 如果已经混乱了，重建环境：**

```bash
# 导出已安装的包
conda list --export > packages.txt
pip freeze > requirements.txt

# 删除旧环境
conda deactivate
conda env remove -n myenv

# 创建新环境
conda create -n myenv python=3.9

# 激活环境
conda activate myenv

# 先用 conda 安装能用 conda 安装的
conda install numpy pandas matplotlib

# 再用 pip 安装 conda 没有的
pip install some-package
```

**3. 使用 conda-forge 频道（更多包）：**

```bash
# 添加 conda-forge 频道
conda config --add channels conda-forge
conda config --set channel_priority strict

# 现在可以安装更多包
conda install package_name
```

**4. 检查包的安装来源：**

```bash
# 查看包是通过 conda 还是 pip 安装的
conda list

# 显示结果中：
# <pip> 表示通过 pip 安装
# 没有标记的是通过 conda 安装
```

**为什么不建议混用？**
- conda 管理整个环境（包括 Python 本身和系统库）
- pip 只管理 Python 包
- conda 可以解决复杂的依赖关系
- pip 安装的包可能与 conda 安装的包版本冲突
- 可能导致环境无法复现

**最佳实践：**
```bash
# 方案 A：纯 conda 环境（推荐用于数据科学）
conda create -n myenv python=3.9
conda activate myenv
conda install numpy pandas matplotlib scikit-learn

# 方案 B：纯 pip 环境（推荐用于 Web 开发）
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Git 和 GitHub 问题

### Q: git push 时提示 `Permission denied (publickey)`

**现象**：
```bash
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.
```

**原因**：你的电脑没有配置 SSH 密钥，或者 GitHub 没有添加你的公钥。

**解决方案**：

**1. 生成 SSH 密钥：**
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# 一路回车（使用默认路径和空密码）
```

**2. 复制公钥：**

Windows (PowerShell)：
```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | clip
```

macOS/Linux：
```bash
cat ~/.ssh/id_ed25519.pub | pbcopy  # macOS
cat ~/.ssh/id_ed25519.pub  # Linux（手动复制）
```

**3. 添加到 GitHub：**
1. 打开 GitHub → `Settings` → `SSH and GPG keys`
2. 点击 `New SSH key`
3. 粘贴公钥内容，保存

**4. 测试连接：**
```bash
ssh -T git@github.com
# 成功会显示：Hi username! You've successfully authenticated...
```

---

### Q: git push 被拒绝 / `Updates were rejected`

**现象**：
```bash
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:username/repo.git'
```

**原因**：远程仓库有你本地没有的提交（通常是在 GitHub 网页上直接修改了文件）。

**解决方案**：

**方法 1：先拉取再推送**（推荐）
```bash
git pull --rebase origin main
git push origin main
```

**方法 2：如果确定要覆盖远程**（危险！会丢失远程的修改）
```bash
git push -f origin main  # 慎用！
```

---

### Q: 提交后发现 `.pyc` 和 `__pycache__` 被上传了

**现象**：`git status` 显示一堆 `__pycache__/` 文件。

**原因**：没有配置 `.gitignore` 文件。

**解决方案**：

**1. 创建 `.gitignore`：**
```bash
# Windows
New-Item .gitignore

# macOS/Linux
touch .gitignore
```

**2. 添加 Python 常见忽略规则：**
```gitignore
__pycache__/
*.py[cod]
*.pyc
.venv/
venv/
env/
.DS_Store
```

**3. 如果已经提交了，需要移除：**
```bash
# 从 Git 中移除但保留本地文件
git rm -r --cached __pycache__/
git rm --cached *.pyc

# 提交删除
git commit -m "Remove cached Python files"
git push
```

---

### Q: 忘记切换分支，在 main 上直接改了代码

**现象**：本来应该在新分支开发，结果在 main 上改了一堆代码。

**原因**：忘记 `git checkout -b feature-branch`。

**解决方案**：

**如果还没 commit：**
```bash
# 暂存当前修改
git stash

# 创建并切换到新分支
git checkout -b feature-branch

# 恢复修改
git stash pop
```

**如果已经 commit 但没 push：**
```bash
# 创建新分支（会带着你的提交）
git checkout -b feature-branch

# 回到 main 并重置
git checkout main
git reset --hard origin/main
```

---

## Python 运行问题

### Q: `ModuleNotFoundError: No module named 'xxx'`

**现象**：
```python
import requests
ModuleNotFoundError: No module named 'requests'
```

**原因**：包没有安装，或者安装在了错误的环境。

**解决方案**：

**1. 确认当前使用的 Python：**
```bash
# Windows
where python
Get-Command python

# macOS/Linux
which python
```

**2. 使用完整路径安装：**
```bash
# 使用 python -m pip 而不是 pip
python -m pip install requests

# 或指定虚拟环境的 pip
./venv/Scripts/pip install requests  # Windows
./venv/bin/pip install requests      # macOS/Linux
```

**3. 确认安装成功：**
```bash
python -m pip list | grep requests
```

---

### Q: 代码在终端能运行，但在 IDE 中报错

**原因**：IDE 使用的 Python 解释器和终端不同。

**解决方案**：

**检查终端使用的 Python：**
```bash
# 在终端运行
python -c "import sys; print(sys.executable)"
```

**在 IDE 中设置相同的解释器：**
- VS Code：`Ctrl+Shift+P` → `Python: Select Interpreter` → 选择终端显示的路径
- PyCharm：`Settings` → `Python Interpreter` → 添加终端显示的路径

---

### Q: `UnicodeDecodeError: 'gbk' codec can't decode byte`

**现象**：
```python
with open('data.txt', 'r') as f:
    content = f.read()
# UnicodeDecodeError: 'gbk' codec can't decode byte 0x9d in position 123
```

**原因**：文件是 UTF-8 编码，但 Windows 默认用 GBK 解码。

**解决方案**：

**指定编码为 UTF-8：**
```python
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

**写文件时也要指定：**
```python
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('你好世界')
```

**为什么会有这个问题？**
- Windows 默认使用 GBK 编码（中文 Windows 系统）
- 网络下载的文件、Linux 系统的文件通常是 UTF-8
- 解决方法：**永远显式指定 `encoding='utf-8'`**

---

### Q: 程序运行到一半就停了，没有报错

**原因 1：死循环或长时间计算**

**检查方法：**
```python
# 添加 print 调试
for i in range(1000000):
    if i % 10000 == 0:
        print(f"Progress: {i}")
    # 你的代码
```

**原因 2：等待输入**

你的代码里可能有 `input()` 等待用户输入：
```python
# 检查代码中是否有这些
input()
input("按回车继续...")
```

---

## 代码错误问题

### Q: `IndentationError: unexpected indent`

**现象**：
```python
def hello():
print("hello")  # 缩进错误
```

**原因**：Python 对缩进非常严格，混用了空格和 Tab，或者缩进不一致。

**解决方案**：

**1. 统一使用 4 个空格（不要用 Tab）**

**2. VS Code 配置：**
在 `settings.json` 中添加：
```json
{
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.detectIndentation": false
}
```

**3. 显示空白字符：**
VS Code 按 `Ctrl+Shift+P` → 输入 `Toggle Render Whitespace`

**4. 快速修复：**
选中代码 → `Shift+Tab`（减少缩进）或 `Tab`（增加缩进）

---

### Q: `NameError: name 'xxx' is not defined`

**现象**：
```python
print(result)
# NameError: name 'result' is not defined
```

**原因**：变量在使用前没有定义，或者拼写错误。

**常见情况：**

**1. 变量名拼写错误：**
```python
result = 10
print(resutl)  # 拼写错误
```

**2. 作用域问题：**
```python
def func():
    x = 10

print(x)  # x 只在函数内部可见
```

**3. 顺序问题：**
```python
print(x)  # 错误：先使用后定义
x = 10
```

**解决方案：**
- 仔细检查变量名拼写
- 确保变量在使用前已定义
- 理解变量作用域

---

### Q: `TypeError: 'int' object is not subscriptable`

**现象**：
```python
num = 123
print(num[0])  # TypeError
```

**原因**：你把整数当成列表/字符串使用了。

**常见错误：**
```python
# 错误
x = 5
print(x[0])  # 整数不能用下标访问

# 正确：转成字符串
x = 5
print(str(x)[0])  # 输出 '5'
```

---

### Q: `list index out of range`

**现象**：
```python
my_list = [1, 2, 3]
print(my_list[3])  # IndexError: list index out of range
```

**原因**：访问了不存在的索引（记住 Python 索引从 0 开始）。

**解决方案**：

**1. 检查列表长度：**
```python
if index < len(my_list):
    print(my_list[index])
```

**2. 使用 try-except：**
```python
try:
    print(my_list[3])
except IndexError:
    print("索引超出范围")
```

**3. 常见错误：循环时写错范围**
```python
# 错误
for i in range(len(my_list) + 1):  # 多了一次循环
    print(my_list[i])

# 正确
for i in range(len(my_list)):
    print(my_list[i])

# 更好的写法
for item in my_list:
    print(item)
```

---

## IDE 和编辑器问题

### Q: VS Code 中 Python 代码没有语法高亮和智能提示

**原因**：没有安装 Python 扩展。

**解决方案：**

1. 点击左侧扩展图标（或 `Ctrl+Shift+X`）
2. 搜索 `Python`
3. 安装 Microsoft 官方的 Python 扩展
4. 重启 VS Code

---

### Q: VS Code 终端显示乱码

**现象**：中文显示为问号或方块。

**解决方案**：

**1. 设置 UTF-8 编码：**
```json
// settings.json
{
    "terminal.integrated.defaultProfile.windows": "PowerShell",
    "terminal.integrated.profiles.windows": {
        "PowerShell": {
            "source": "PowerShell",
            "args": ["-NoExit", "-Command", "chcp 65001"]
        }
    }
}
```

**2. 或在终端中手动设置：**
```powershell
chcp 65001
```

---

### Q: PyCharm 提示 `PEP 8: line too long`

**现象**：代码下面出现黄色波浪线，提示行太长。

**原因**：PEP 8 规范建议每行不超过 79 个字符。

**解决方案**：

**方法 1：拆分代码**
```python
# 拆分长字符串
message = (
    "这是一个很长的字符串，"
    "需要分成多行"
)

# 拆分函数调用
result = my_function(
    argument1,
    argument2,
    argument3
)
```

**方法 2：调整 PyCharm 设置**（不推荐，但可以临时用）
`Settings` → `Editor` → `Code Style` → `Python` → 将 `Hard wrap at` 改为 120

---

## 网络和下载问题

### Q: GitHub clone 速度很慢或失败

**现象**：
```bash
git clone https://github.com/xxx/repo.git
# 速度只有几 KB/s 或直接超时
```

**解决方案**：

**方法 1：使用 GitHub 镜像站**
```bash
# 使用 ghproxy
git clone https://ghproxy.com/https://github.com/xxx/repo.git

# 使用 fastgit（需要注意可用性）
git clone https://hub.fastgit.xyz/xxx/repo.git
```

**方法 2：使用 SSH 代替 HTTPS**
```bash
# 先配置 SSH 密钥（见上面的 SSH 问题）
git clone git@github.com:xxx/repo.git
```

**方法 3：配置 Git 代理**（需要科学上网）
```bash
# HTTP 代理
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy https://127.0.0.1:7890

# 取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy
```

---

### Q: requests 请求网页返回 403 或 418

**现象**：
```python
import requests
r = requests.get('https://example.com')
print(r.status_code)  # 403
```

**原因**：网站检测到你是爬虫，拒绝访问。

**解决方案**：

**添加 User-Agent 伪装成浏览器：**
```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

r = requests.get('https://example.com', headers=headers)
print(r.status_code)
```

**更完整的 headers：**
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Referer': 'https://www.google.com/'
}
```

---

## 其他常见问题

### Q: 怎么知道我的代码运行了多久？

**解决方案：**

**方法 1：使用 time 模块**
```python
import time

start = time.time()

# 你的代码
for i in range(1000000):
    pass

end = time.time()
print(f"运行时间: {end - start:.2f} 秒")
```

**方法 2：使用 timeit（更精确）**
```python
import timeit

# 测试小段代码
time_cost = timeit.timeit('sum(range(100))', number=10000)
print(f"平均时间: {time_cost / 10000:.6f} 秒")
```

**方法 3：Jupyter Notebook 中使用魔法命令**
```python
%%time
# 你的代码
```

---

### Q: 怎么清空终端的输出？

**解决方案：**

```bash
# Windows (PowerShell)
Clear-Host
# 或
cls

# macOS/Linux
clear
```

**在 Python 代码中清屏：**
```python
import os

# 跨平台清屏
os.system('cls' if os.name == 'nt' else 'clear')
```

---

### Q: 如何让 Python 输出不换行？

**解决方案：**

```python
# 默认会换行
print("Hello")
print("World")
# 输出：
# Hello
# World

# 不换行，使用 end 参数
print("Loading", end="")
print("...", end="")
print("Done!")
# 输出：Loading...Done!

# 进度条效果
import time
for i in range(10):
    print(f"\rProgress: {i+1}/10", end="", flush=True)
    time.sleep(0.5)
print()  # 最后换行
```

---

### Q: 字典 `KeyError` 怎么避免？

**现象：**
```python
data = {'name': 'Alice', 'age': 25}
print(data['gender'])  # KeyError: 'gender'
```

**解决方案：**

**方法 1：使用 `.get()` 方法**
```python
# 返回 None 而不报错
gender = data.get('gender')

# 指定默认值
gender = data.get('gender', '未知')
```

**方法 2：检查键是否存在**
```python
if 'gender' in data:
    print(data['gender'])
else:
    print('键不存在')
```

**方法 3：使用 defaultdict**
```python
from collections import defaultdict

data = defaultdict(lambda: '未知')
data['name'] = 'Alice'
print(data['gender'])  # 输出：未知
```

---

### Q: 为什么我的文件路径在 Windows 上报错？

**现象：**
```python
file = open('C:\data\new_file.txt')  # SyntaxError 或找不到文件
```

**原因**：反斜杠 `\` 在字符串中是转义字符，`\n` 被解释为换行符。

**解决方案：**

**方法 1：使用原始字符串**
```python
file = open(r'C:\data\new_file.txt')  # 注意 r 前缀
```

**方法 2：使用正斜杠**（Python 会自动转换）
```python
file = open('C:/data/new_file.txt')
```

**方法 3：双反斜杠**
```python
file = open('C:\\data\\new_file.txt')
```

**推荐：使用 pathlib（Python 3.4+）**
```python
from pathlib import Path

file_path = Path('C:/data/new_file.txt')
with open(file_path, 'r') as f:
    content = f.read()
```

---

## 延伸阅读

如果你想系统学习这些基础知识，可以查看完整的 [Task 0 文档](task0.md)。

但是，**只有遇到问题的时候，你才会真正记住解决方案**。所以不用担心，慢慢来，遇到问题就回来查这个文档。
