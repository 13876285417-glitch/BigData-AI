---
name: coursework-submit
description: 本仓库（大数据与人工智能课程）的作业提交规范与固定流程。当需要新建一次课的程序作业、把代码提交到 GitHub 远程仓库、检查作业是否满足老师要求时使用。涵盖目录约定、文件命名、.py / .ipynb 的创建与运行、环境自检、git 提交推送的完整步骤，以及提交前的自查清单。
agent_created: true
---

# 课程作业提交规范（大数据与人工智能）

本技能把每次课的作业流程固定下来，避免每次重新摸索目录、命名和提交方式。
执行对象是本仓库根目录：`/Volumes/BU110/大数据与人工智能的相关作业/BigData-AI`。

## 一、目录约定

| 目录 | 放什么 | 说明 |
|---|---|---|
| `scripts/` | 第 N 课的 `.py` 脚本与 `.ipynb` 笔记本 | 课堂作业的主要产出 |
| `notebooks/` | 规模较大的分析型笔记本 | 与 `scripts/` 区分：这里是"项目级"分析 |
| `assignments/` | 按次归档的作业 | 需要单独交的作业放这里 |
| `data/` | 数据文件 | `.gitignore` 已排除大文件，只提交小样本 |
| `docs/` | 文档、报告 | 作业说明、实验记录 |
| `concept-learning-materials/` | 概念学习资料 | 课程知识点的补充材料 |
| `notes/` | 学习笔记与 HTML 学习资料 | Python 基础 13 课套件在这里 |

**文件命名**：`NN-简短英文描述.py` / `NN-简短英文描述.ipynb`，`NN` 是课次两位数字。
例：`01.py`、`02-string-basics.py`、`03-list-analysis.ipynb`。

## 二、新建一次作业的标准动作

1. **建文件**：在 `scripts/` 下按命名规范新建 `.py` 和 `.ipynb`。
2. **写内容**：文件开头用三引号 docstring 写明「第 N 课作业 / 课程 / 用途 / 运行方式」。代码里关键处写中文注释——这是给未来自己看的。
3. **配环境**：确认 `.venv` 存在，VS Code 右下角选择解释器为本仓库的 `.venv`。
4. **运行验证**（必须做，不能只写不跑）：
   - `.py`：`cd scripts && ../.venv/bin/python 01.py`，确认终端有预期输出
   - `.ipynb`：逐格运行，**保存后输出会写进文件**，GitHub 上别人才能看到结果
5. **提交推送**：见下一节。

## 三、git 提交与推送

```bash
cd "/Volumes/BU110/大数据与人工智能的相关作业/BigData-AI"

git status                       # 先看改了什么，防止误提交
git add -A                       # 加入暂存区
git commit -m "第1课：创建并运行py与ipynb文件"
git push                         # 推送到 GitHub 远程仓库
```

**提交前必须检查**：

```bash
git status --short               # 不该出现的文件（.venv/、._*、__pycache__/）是否被漏掉了
wc -c scripts/*.py               # 0 字节说明文件是空的，没真正写内容
```

## 四、环境已知问题与处理

### 1. pip 安装包报 SSL 证书错误

现象：`SSLCertVerificationError: unable to get local issuer certificate`

原因：python.org 官方安装包默认不带 CA 证书包。

处理（已修复，如重装 Python 后复发则重做）：

```bash
/usr/local/bin/python3 -m pip install --user --cert /etc/ssl/cert.pem certifi
ln -sfn "$(/usr/local/bin/python3 -c 'import certifi;print(certifi.where())')" \
  /Library/Frameworks/Python.framework/Versions/3.12/etc/openssl/cert.pem
```

### 2. pip 安装被拦截 / 进程莫名中断

本机 Python 进程会继承 `PYTHONPATH` 指向的钩子，pip 卸载旧包时可能被拦。
处理：安装时清掉该变量。

```bash
env -u PYTHONPATH .venv/bin/python -m pip install <包名>
```

### 3. Jupyter 内核启动失败（缺少模块 packaging）

```bash
env -u PYTHONPATH .venv/bin/python -m pip install ipykernel packaging
.venv/bin/python -m ipykernel install --user --name python-basics --display-name "Python (.venv 3.12.10)"
```

然后在 VS Code 右上角内核选择器里选 `Python (.venv 3.12.10)`。

### 4. pip 国内源

```bash
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
pip config list          # 验证
```

配置写在 `~/.config/pip/pip.conf`。

### 5. HTML 被预览面板注入 `data-page-node-id`

**现象**：用 WorkBuddy 预览面板打开 `notes/` 下的 HTML 后，本地文件里每个标签都被加上
`data-page-node-id="XXXXXX"` 属性，一个文件能多出几百处、几十 KB。这是预览工具为了定位页面
元素自动加的，**不是文件内容的一部分，不该提交进仓库**。

**检查与清理**：

```bash
# 1. 看有哪些文件被污染
grep -rl "data-page-node-id" --include="*.html" .

# 2. 清理（只删该属性，不动其他内容）
python3 .workbuddy/skills/coursework-submit/scripts/clean_page_node_id.py $(find . -name "*.html" -not -path "./.venv/*")
```

`clean_page_node_id.py` 在写回前会用 `html.parser` 比对清理前后的标签序列，
**结构一旦不一致就跳过该文件不写回**，避免清理动作本身把文件改坏。
清理完再用同样的思路复核一遍标签闭合即可。

## 五、提交前自查清单

- [ ] `scripts/` 下每个 `.py` 都**非 0 字节**且有实际内容
- [ ] 每个 `.py` 都**实际运行过**，输出符合预期
- [ ] `.ipynb` 的每个代码格**都运行过且已保存**（输出可见，不是空白）
- [ ] `.ipynb` 顶部的内核与实际使用的一致（不要显示成不存在的环境）
- [ ] `.gitignore` 生效：`.venv/`、`._*`、`__pycache__/`、`.ipynb_checkpoints/` 没进仓库
- [ ] `notes/` 下的 HTML 没有 `data-page-node-id` 注入属性（用预览面板打开过就会产生）
- [ ] `git commit` 信息能说清这次做了什么
- [ ] `git push` 成功，GitHub 网页上能看到最新文件

## 六、卡住了怎么办

- 先看**终端原话**的报错，不要只看「失败了」三个字
- 环境问题优先怀疑三处：用的是哪个解释器、`PYTHONPATH`、SSL 证书
- 外接硬盘（本仓库所在卷）有掉线风险，操作前可先 `ls /Volumes/` 确认在线
