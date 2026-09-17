# 大数据与人工智能课程

本仓库用于 **大数据与人工智能** 课程的学习记录、代码与作业提交。

> 作者：新闻学专业 · 课程作业仓库
> 最后更新：2026-09-17

## 目录结构

| 目录 | 用途 |
|---|---|
| `scripts/` | 逐课练习代码（`.py` 脚本与 `.ipynb` 笔记本） |
| `notebooks/` | 规模较大的分析型笔记本 |
| `assignments/` | 按次归档的课程作业 |
| `data/` | 数据文件（大文件不入库） |
| `docs/` | 文档、报告与实验记录 |
| `concept-learning-materials/` | 知识点补充学习资料 |
| `notes/` | 学习笔记与 HTML 学习资料 |

## 课程作业

### 第 1 课（2026-09-17）

课堂要求：安装 VS Code / Python / Git，配置 pip 国内源，把 VS Code 设为中文界面与自动保存；
完成作业：创建并运行 `.py` 与 `.ipynb` 文件，提交到 GitHub 远程仓库。

| 作业项 | 文件 |
|---|---|
| 创建 `.py` 文件并运行 | [`scripts/01.py`](scripts/01.py) |
| 创建 `.ipynb` 文件并运行 | [`scripts/01.ipynb`](scripts/01.ipynb) |
| 提交到 GitHub 远程仓库 | 本仓库 |
| 仓库级 Skill | [`.workbuddy/skills/coursework-submit/`](.workbuddy/skills/coursework-submit/SKILL.md) |

## 学习材料

### Python 基础 · 13 次课（新闻学方向）

本学期的 Python 基础课程学习套件。人工智能理论与应用是后续另一门课，这里只打地基。

- [`notes/python-basics/index.html`](notes/python-basics/index.html) — **课程目录**：四条能力链、13 课清单、前置/解锁依赖关系表，全部资料的总入口
- [`notes/python-basics/learning-map.html`](notes/python-basics/learning-map.html) — **学习地图**：13 课的知识点、新闻场景、当堂产出、课后练习与四个进度检查点
- `notes/python-basics/01-*.html` ~ `13-*.html` — **13 份逐课学习资料**：每份含 1 分钟核心要点速览 + 分层自适应自测（答对升级、答错降级），全部知识点标注官方来源可溯源

> 从 `index.html` 进最方便，13 份资料之间可以连续翻页。进度勾选存在本机浏览器，目录页与学习地图共用一份记录。

### Agent Skill 图解版（推荐先看）

用 6 张图讲清「AI 技能包」是什么、怎么工作，全部知识点标注官方来源。

- [`notes/agent-skill-visual.html`](notes/agent-skill-visual.html) — **图解可视化版**，含交互自测
- [`notes/agent-skill-one-minute.html`](notes/agent-skill-one-minute.html) — 文字版，一分钟掌握
- [`notes/agent-skill-layered.html`](notes/agent-skill-layered.html) — 分层自适应测评版

> 打开方式：克隆仓库后双击 HTML 文件，或直接拖进浏览器。

## 环境

- 系统：macOS (Apple Silicon)
- Python：3.12.10（项目内 `.venv`）
- Git：2.50.1
- VS Code：1.138.0（中文界面，自动保存已开启）

### 首次安装

```bash
# 1. 创建虚拟环境
python3 -m venv .venv

# 2. 安装依赖（已配置清华源）
.venv/bin/python -m pip install -r requirements.txt

# 3. 注册 Jupyter 内核
.venv/bin/python -m ipykernel install --user --name python-basics --display-name "Python (.venv 3.12.10)"
```

> **注意**：本机 Python 进程会继承 `PYTHONPATH` 指向的钩子文件，pip 卸载旧包时可能被拦截。
> 遇到中断时改用 `env -u PYTHONPATH .venv/bin/python -m pip install <包名>`。

### pip 国内源

```bash
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```

## Git 学习备忘

```bash
git clone <仓库地址>          # 拷贝远程仓库到本地
git status                   # 看当前改了什么
git add <文件名>              # 把改动加入暂存区
git commit -m "说明"          # 提交暂存区改动到本地
git push                     # 把本地提交推送到远程
git log --oneline            # 查看提交历史
```

## 许可证

本项目采用 [MIT License](LICENSE)。
