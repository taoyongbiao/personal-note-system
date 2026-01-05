# 其他工具

## Python开发工具

### Virtual Environment (venv)

Python虚拟环境用于隔离项目依赖：

```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境 (Windows)
.venv\Scripts\activate

# 激活虚拟环境 (Linux/Mac)
source .venv/bin/activate

# 退出虚拟环境
deactivate
```

### pip包管理

```bash
# 安装依赖
pip install -r requirements.txt

# 生成依赖文件
pip freeze > requirements.txt

# 升级包
pip install --upgrade package-name
```

## Git版本控制

### 基本命令

```bash
# 克隆仓库
git clone <repository-url>

# 查看状态
git status

# 添加文件
git add .

# 提交更改
git commit -m "提交信息"

# 推送到远程
git push origin main
```

### Git子模块

```bash
# 添加子模块
git submodule add <repository-url> <path>

# 更新子模块
git submodule update --init --recursive

# 同步子模块
git submodule sync
```

## VSCode扩展

### 推荐扩展

- **Python** - Python语言支持
- **Markdown All in One** - Markdown增强功能
- **Material Icon Theme** - 文件图标主题
- **GitLens** - Git增强功能
- **Pylance** - Python语言服务器

### 工作区设置

VSCode工作区设置可以为项目提供特定配置：

```json
{
    "python.defaultInterpreterPath": "./.venv/bin/python",
    "files.associations": {
        "*.md": "markdown"
    },
    "markdown.preview.fontFamily": "'Segoe WPC', 'Segoe UI', sans-serif"
}
```

## Markdown工具

### 语法高亮

代码块语法：

```markdown
```python
def hello():
    print("Hello, World!")
```
```

### 表格

```markdown
| 列1 | 列2 | 列3 |
| --- | --- | --- |
| 内容1 | 内容2 | 内容3 |
```

### 注释框 (Admonitions)

```markdown
!!! note
    这是一个注释框

!!! tip
    这是一个提示框

!!! warning
    这是一个警告框
```

## 文档生成工具

### Sphinx

Python项目的文档生成工具，使用reStructuredText格式：

```rst
标题
====

这是一个段落。

子标题
-------

- 列表项1
- 列表项2
```

### MkDocs

Python项目的静态网站生成器，使用Markdown格式：

- [个人笔记系统文档](../index.md) - 本项目的文档系统
- [MkDocs工具说明](mkdocs.md) - MkDocs使用指南

## 自动化工具

### Make

创建Makefile自动化常见任务：

```makefile
install:
	pip install -r requirements.txt

dev:
	python scripts/create_note.py --template 灵感

docs:
	mkdocs serve

build:
	mkdocs build
```

### Taskfile (替代方案)

Task是一个用Go编写的任务运行器：

```yaml
# Taskfile.yml
version: '3'

tasks:
  install:
    cmds:
      - pip install -r requirements.txt
  docs:
    cmds:
      - mkdocs serve
    desc: 启动文档服务器
```

## AI工具集成

### OpenAI API

在项目中集成OpenAI API进行内容生成：

```python
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "Hello!"}]
)
```

### 环境变量管理

使用python-dotenv管理环境变量：

```bash
# .env文件
OPENAI_API_KEY=your_api_key_here
```

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
```