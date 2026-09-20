# Application 4 - AI 应用算法、Infra、后训练与预训练

> [!NOTE]
> 预计耗时：？ 天

## 学习目的

这部分内容不作为考核的一部分，因为 211 本科生学了也没啥用，起码得是一个 9 硕的学历才有资格干这些活。

并且，如果你想学这部分内容，你至少得先拥有后端、运维、AI 底层以及前面的 Agent 的知识。

这部分内容还相当的粗糙，待施工。

## 作业

### 作业 1 - 复现 MiniMind

微调是 AI 应用算法的一种，另一种是训练一个小型专用模型。

微调有两种主流方式。

第一种是直接修改大语言模型本身的参数，另一种是基于 LoRA 的低秩适配。

你应该知道大语言模型由大量高维参数矩阵组成：前者直接更新原始参数，后者可以用一个简化公式表示为：

$$ W' = W + \Delta W,\quad \Delta W = BA $$

其中 $W$ 是原始权重矩阵， $A$ 和 $B$ 是低秩矩阵， $\Delta W$ 是低秩增量， $W'$ 是微调后的权重。

$\Delta W$ 的参数量通常远小于 $W$，因此微调的计算资源和数据需求可以大幅降低。

在实际实现中，低秩增量通常会作用在多个层上，例如每层对应一组 $A_i, B_i$，这样可以更细粒度地控制微调过程。

举一个简单的例子，假设我们现在要获得一个具备医疗知识的中文模型，但是你的初始模型 $A$ 是纯由英文资料训练来的。

所以我们首先要进行第一次微调 $P_1$，让模型可以理解中文，得到第一级模型 $P_1A$，然后进行第二次医疗训练，得到第二级模型 $P_2P_1A$。

该过程具有“可插拔”特性，所以你在分享模型时，通常只需要分享 LoRA 适配器参数，而原始底座模型可以让对方自行获取。

并且整个过程不需要你花费大量的计算资源去从头训练一个模型。

你在本次作业的任务是复刻一个经典的微调任务：[MiniMind](https://github.com/jingyaogong/minimind)

#### 1. 准备环境  

如果你想在本地从零开始训练模型，需要一张性能较高的显卡（如 RTX 5080、4090、5090 等）。

如果没有，可以使用 AutoDL、Colab 或 OpenDL 等平台完成训练。

不过，本作业的重点是 LoRA 微调，因此下面会教你如何下载已训练好的 PyTorch 模型，并在此基础上进行 LoRA 微调。

LoRA 微调对显卡要求较低，使用 RTX 4060 等入门级显卡即可完成。

如果你没有 N 卡，或显卡性能太弱，同样可以考虑使用 AutoDL、Colab 或 OpenDL 等平台来完成训练。

注意，使用 AutoDL、Colab 或 OpenDL 等平台请使用 VSCode 的远程开发功能来完成训练。

这样可以更方便地管理代码和文件，请注意 VSCode 远程开发下扩展需要重新安装。

> [!TIP]
> RTX 4070 Laptop 完成训练需要约 20+ 小时，完成微调需 1+ 小时  
> RTX 5090 完成训练需要约 4+ 小时，完成微调需 2 分钟左右

#### 2. 克隆 MiniMind 的代码库

```shell
git clone --depth 1 https://github.com/jingyaogong/minimind
# 如果机器在国内可以考虑使用 GitCode 镜像仓库
git clone --depth 1 https://gitcode.com/GitHub_Trending/min/minimind.git
```

#### 3. 阅读文档

阅读 [项目介绍](https://github.com/jingyaogong/minimind#-%E9%A1%B9%E7%9B%AE%E4%BB%8B%E7%BB%8D) 以及 [LoRA (Low-Rank Adaptation)](https://github.com/jingyaogong/minimind#4-lora-low-rank-adaptation)

#### 4. 配置环境

- 远程环境

  远程环境通常已经预装了 Python 和对应的 CUDA 版本的 PyTorch，你只需要安装一些额外的依赖即可。

  ```shell
  pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
  ```

- 本地环境

  如果你没有安装 CUDA，请先阅读 CUDA 安装文档：

  <https://developer.nvidia.com/cuda-toolkit-archive>

  这里以 CUDA 12.8 版本为例。请注意，PyTorch 官方的安装包与 CUDA 版本是严格绑定的。

  例如，标有 cu128 的 PyTorch 包必须配合 CUDA 12.8 使用，请务必确认你的 CUDA 版本和 PyTorch 版本的对应关系。

  同时，建议安装最新版 NVIDIA 驱动（游戏驱动即可），确保驱动支持的 CUDA 版本不低于你安装的 CUDA 工具包版本。

  在本地环境极不推荐使用 `pip` 在全局环境安装，建议使用 `uv` 创建一个虚拟环境，并且使用国内镜像源来安装依赖。下面是 `uv` 的参考配置文件 `pyproject.toml`：

  ```toml
  [project]
  name = "minimind"
  version = "2.0.0"
  description = "64M-parameter LLM from scratch in just 2h!"
  readme = "README.md"
  requires-python = ">=3.12"
  
  # 这里的依赖是基于commit 4497610的并升级了pytorch和torchvision，可能会和你的版本不完全一致，如果遇到问题可以参考原仓库的requirements.txt来修改这里的依赖。
  dependencies = [
    "datasets==3.6.0",
    "datasketch==1.6.4",
    "einops==0.8.1",
    "flask==3.0.3",
    "flask-cors==4.0.0",
    "jieba==0.42.1",
    "jinja2==3.1.2",
    "jsonlines==4.0.0",
    "marshmallow==3.22.0",
    "modelscope==1.37.0",
    "ngrok==1.4.0",
    "nltk==3.8",
    "numpy==1.26.4",
    "openai==1.59.6",
    "psutil==5.9.8",
    "pydantic==2.11.5",
    "rich==13.7.1",
    "scikit-learn==1.5.1",
    "sentence-transformers==2.3.1",
    "simhash==2.1.2",
    "streamlit==1.50.0",
    "swanlab==0.7.11",
    "tiktoken==0.10.0",
    "transformers==4.57.6",
    "trl==0.13.0",
    "ujson==5.1.0",
    "wandb==0.18.3",
    "torch==2.11.0",
    "torchvision==0.26.0",
  ]
  
  # 注意这里以 pytorch-cu128 为例
  # 如果你使用的 CUDA 版本不同，请替换为对应的版本，请务必确认你的 CUDA 版本和 PyTorch 版本的兼容性。
  
  # 如果你使用国外环境如 colab，请使用官方源，否则可能反向加速，导致安装速度更慢。
  
  # 指定torch和torchvision的安装源
  [tool.uv.sources]
  torch = [{ index = "pytorch-cu128" }]
  torchvision = [{ index = "pytorch-cu128" }]
  
  # 南京大学的PyTorch镜像源
  [[tool.uv.index]]
  name = "pytorch-cu128"
  url = "https://mirrors.nju.edu.cn/pytorch/whl/cu128"
  explicit = true
  # 官方源: https://download.pytorch.org/whl/cu128
  
  # 清华大学的PyPI镜像源（作为默认源），如果你已经在uv全局配置文件设置了默认源，这里可以省略。
  [[tool.uv.index]]
  url = "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/"
  default = true
  # 官方源: https://pypi.org/simple
  ```

使用`uv sync`命令安装依赖：

```shell
uv sync
```

#### 5. 下载模型 (如果你想从 0 训练模型，可以跳过这一步)

```shell
mkdir out
wget -O ./out/full_sft_768.pth https://www.modelscope.cn/models/gongjy/minimind-3-pytorch/resolve/master/pretrain_zero_768.pth
```

#### 6. 下载数据集

```shell
wget -P ./dataset https://www.modelscope.cn/datasets/gongjy/minimind_dataset/resolve/master/lora_medical.jsonl
wget -P ./dataset https://www.modelscope.cn/datasets/gongjy/minimind_dataset/resolve/master/lora_identity.jsonl
# 从0训练需要下载以下数据集
# wget -P ./dataset https://www.modelscope.cn/datasets/gongjy/minimind_dataset/resolve/master/pretrain_t2t_mini.jsonl
# wget -P ./dataset https://www.modelscope.cn/datasets/gongjy/minimind_dataset/resolve/master/sft_t2t_mini.jsonl

```

#### 7. 进行训练和微调

此处在 MiniMind 仓库有详细说明，你需要参考 README 完成微调过程。

> [!NOTE]
>
> 1. 使用 uv 的同学需要使用`uv run`跑脚本  
> 2. 请注意运行脚本的目录  
> 3. 想要完成 Bonus 的同学需要开启训练可视化
> 4. 模型训练中断是可以恢复的，具体参考 MiniMind 文档
> 5. 模型能力有限，别指望它和豆包打一架

#### 8. 测试模型

| 类型 | 测试问题示例 | 预期行为 |
| ---- | ------------ | -------- |
| 身份询问 | "你是谁？" | 回答设定的身份信息 |
| 身份追问 | "谁创造了你？" | 回答创造者信息 |
| 医疗知识 | "什么是糖尿病？" | 给出基本正确的医学解释 |
| 医疗建议 | "感冒了怎么办？" | 给出合理的建议 |
| 组合测试 | "你是谁？你懂医学吗？" | 先确认身份，再展示医疗能力 |
| 边界测试 | "帮我写一个冒泡排序" | 观察是否仍保留基础能力 |

#### 作业要求 - 作业 1

- 你需要完成医疗微调和身份微调，得到两个 LoRA 适配器。
- 然后你需要将这两个适配器进行组合，得到一个同时具备医疗知识和特定身份的模型。
- 你需要在本地测试微调后的模型，验证其是否具备医疗知识和特定身份。
- 你需要撰写一份报告，总结你的微调过程、遇到的挑战以及最终的结果（需要包含步骤 8 中模型的测试结果）。
- （Bonus）从 0 训练模型。
- （Bonus）在报告里给出 Loss 曲线（使用 swanlab 或 wandb 可视化）。
- （Bonus）使用 peft 库重写 lora 微调脚本。
