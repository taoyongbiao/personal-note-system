# 安装设置

## 环境要求

- Python 3.7 或更高版本
- VSCode 编辑器
- Git（可选，用于版本控制）

## 安装步骤

### 1. 克隆项目到本地

```bash
git clone https://github.com/taoyongbiao/personal-note-system.git
```

### 2. 进入项目目录并安装依赖

```bash
cd personal-note-system
pip install -r requirements.txt
```

### 3. 运行设置脚本

```bash
python setup.py
```

安装过程会自动安装依赖包并配置基本环境。

## 依赖说明

项目依赖以下Python包：

- `argparse==1.4.0` - 命令行参数解析
- `openai>=1.0.0` - AI服务接口（用于AI驱动的笔记评价）
- `mkdocs>=1.4.0` - 文档生成工具
- `mkdocs-material>=9.0.0` - 文档主题
- `mkdocs-git-revision-date-localized-plugin>=1.0.0` - 修订日期插件
- `mkdocs-minify-plugin>=0.5.0` - 压缩插件
- `mkdocs-macros-plugin>=0.7.0` - 宏插件

## 配置AI服务（可选）

如果需要使用AI驱动的笔记评价功能，需要设置API密钥：

```bash
export OPENAI_API_KEY=your_api_key
```

或者在环境变量中设置 `OPENAI_API_KEY`。

## 启动文档服务（可选）

如果需要本地查看文档，可以启动文档服务：

```bash
python scripts/start_docs.py serve
```

文档将运行在 http://127.0.0.1:8000