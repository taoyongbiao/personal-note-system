# MkDocs

## 工具概述

MkDocs 是一个用于快速生成静态文档网站的工具，特别适合项目文档、API文档和技术博客场景。它使用 Markdown 文件作为内容源，生成美观的静态网站。

## 安装

### 安装 MkDocs

```bash
# 安装基本版本
pip install mkdocs

# 安装 Material 主题
pip install mkdocs-material
```

### 验证安装

```bash
mkdocs --version
```

## 快速开始

### 创建新项目

```bash
# 创建新项目
mkdocs new my-docs

# 进入项目
cd my-docs

# 启动本地服务器
mkdocs serve
```

在浏览器中打开 http://localhost:8000 查看网站。

## 配置文件

### mkdocs.yml 配置示例

```yaml
site_name: "我的文档"
site_dir: "site"
docs_dir: "docs"

theme:
  name: material
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
    - scheme: slate
      primary: indigo
      accent: indigo

nav:
  - 首页: index.md
  - 指南:
    - 快速开始: getting-started.md
    - 高级用法: advanced.md

plugins:
  - search
  - git-revision-date-localized
```

## 主要命令

### 本地预览

```bash
mkdocs serve
```

### 构建网站

```bash
mkdocs build
```

### 部署网站

```bash
mkdocs gh-deploy
```

## 主题配置

### Material 主题特性

- 响应式设计
- 深色/浅色主题切换
- 搜索功能
- 代码高亮
- 图标支持

### 主题配置选项

```yaml
theme:
  name: material
  features:
    - navigation.expand
    - navigation.tabs
    - navigation.top
    - search.suggest
    - search.highlight
```

## 导航配置

### 基本导航

```yaml
nav:
  - 首页: index.md
  - 指南:
    - 快速开始: getting-started.md
    - 配置: configuration.md
  - API参考: api.md
```

### 多级导航

```yaml
nav:
  - 首页: index.md
  - 指南:
    - 基础:
      - 快速开始: getting-started.md
      - 安装: installation.md
    - 高级:
      - 配置: configuration.md
      - 主题: theming.md
```

## Markdown扩展

MkDocs 支持多种 Markdown 扩展：

- `admonition` - 注释框
- `toc` - 目录
- `pymdownx.highlight` - 代码高亮
- `pymdownx.superfences` - 高级代码块

## 项目中的MkDocs使用

### 启动文档服务

使用项目提供的脚本启动文档服务：

```bash
python scripts/start_docs.py serve
```

### 构建文档网站

```bash
python scripts/start_docs.py build
```

### 自定义端口

```bash
python scripts/start_docs.py serve --port 8080
```

## 常见问题

### 图片无法显示

**问题**：图片放在docs目录外，MkDocs只复制docs目录下的文件

**解决**：将图片移动到docs/images/目录下，引用路径改为./images/xxx.png

### 自定义CSS/JS

在 `mkdocs.yml` 中添加：

```yaml
extra_css:
  - stylesheets/extra.css

extra_javascript:
  - javascripts/extra.js
```