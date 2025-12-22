# 🧠 【MkDocs】学习笔记

> - **一句话定位**：这是一个用于**快速生成静态文档网站**的工具，特别适合**项目文档、API文档和技术博客**场景
> - **我的状态**：✅ 了解 ◻️ 能用 ◻️ 熟练 ◻️ 精通
> - **学习优先级**：✅ P0立即学 ◻️ P1本周学 ◻️ P2有空学

---

## 🎯 生存指南（新手必填）

### 🔍 第一印象
**它是什么类型？**
- [ ] 开发工具（构建/测试/部署）
- [x] **文档工具**（编写/生成/发布）
- [ ] 效率工具（自动化/管理/协作）
- [ ] 数据工具（处理/分析/可视化）
- [ ] 其他：____

**一句话价值**：
> 用Markdown写文档，一键生成漂亮的静态网站，省去前端开发的麻烦

**最像哪个熟悉工具？**
- 像 **GitBook** 但更**轻量、配置更简单、Python生态友好**
- 不像 **Sphinx** 因为**不使用reStructuredText而使用更简单的Markdown**

### 📦 快速启动
**安装方式**：
```bash
# 最常用方式：
pip install mkdocs

# 备选方式：
pip install mkdocs-material  # 包含Material主题
```

**验证安装**：
```bash
# 检查版本
mkdocs --version
# 运行帮助
mkdocs --help
```

**最小示例**：
```bash
# 创建新项目
mkdocs new my-docs

# 进入项目
cd my-docs

# 启动本地服务器
mkdocs serve

# 在浏览器打开 http://localhost:8000
```

### 🚦 关键三件事
1. **如何启动/运行？**
   ```bash
   mkdocs serve  # 开发模式，实时预览
   ```

2. **如何配置基本参数？**
   ```yaml
   # mkdocs.yml
   site_name: My Docs
   docs_dir: docs
   site_url: https://example.com/
   ```

3. **如何看到结果？**
   - 成功标志：**终端显示"Serving on http://localhost:8000"**
   - 输出位置：**本地：`site/`目录，部署：GitHub Pages等**
   - 验证方法：**访问localhost:8000看到网站，或构建后检查site/目录**

### ⚠️ 第一个坑
```
时间：初次使用时
错误信息：图片无法显示，返回404
原因：图片放在docs目录外，MkDocs只复制docs目录下的文件
解决：将图片移动到docs/images/目录下，引用路径改为./images/xxx.png
教训：所有静态资源（图片、CSS、JS）必须放在docs目录内
```

---

## 📚 工作手册（使用中填写）

### 🗺️ 我的使用场景
**当前项目用途**：
```
项目：API文档项目
用途：为Python项目自动提取代码中的docstring生成API文档并与用户指南集成
频率：每天使用
重要性：核心依赖（团队文档统一平台）
```

### 🧩 配置解析
**基础配置**（能工作）：
```yaml
# mkdocs.yml - 必须有的配置
site_name: 项目文档  # 作用：网站标题
docs_dir: docs       # 作用：源文档目录
site_url: http://localhost:8000  # 作用：网站URL
```

**优化配置**（更好用）：
```yaml
# mkdocs.yml - 推荐的配置
theme:
  name: material  # 好处：现代化响应式主题
  features:
    - navigation.tabs  # 好处：支持标签式导航
    - search.suggest   # 好处：搜索建议功能

nav:
  - 首页: index.md  # 好处：清晰定义导航结构
  - 用户指南: user-guide.md
  - API参考: api-reference.md

plugins:
  - search  # 好处：启用搜索功能（默认其实已启用）
  - mkdocstrings: #
      default_handler: python  # 设置默认处理器为Python[citation:1][citation:7]
      handlers:
        python:
          options:
            docstring_style: google  # 指定docstring风格 (google, numpy, sphinx)
            show_root_heading: true  # 显示根级标题[citation:1]
            show_source: false       # 不显示源代码
            merge_init_into_class: true  # 将__init__方法合并到类中
            heading_level: 1         # 标题起始等级
```

### 🔌 插件/扩展生态
**已安装插件**：
```
✅ mkdocs-material - 解决了：美观主题和高级UI组件问题
✅ mkdocstrings - 提升了：自动从代码生成API文档的效率
✅ mkdocstrings-python (Python处理器)：专为Python设计的处理器，其核心依赖是一个名为 Griffe 的库
```

**待考察插件**：
```
🔍 mkdocs-git-revision-date-localized-plugin - 可能解决：显示文档最后更新时间
⚡ mkdocs-minify-plugin - 据说能：压缩HTML/JS/CSS减小文件体积
```

### 🧪 实战配方
**配方1：创建API文档项目**
```yaml
# mkdocs.yml 配置
site_name: API文档
theme:
  name: material
  palette:
    primary: deep purple
    accent: purple

plugins:
  - mkdocstrings:
      handlers:
        python:
          options:
            show_source: true
            show_root_heading: true

nav:
  - 首页: index.md
  - API参考:
    - 核心模块: api/core.md
    - 工具函数: api/utils.md
```

**配方2：部署到GitHub Pages**
```bash
# 步骤
1. 在GitHub创建仓库
2. 本地构建：mkdocs build
3. 将site/目录内容推送到gh-pages分支
# 或使用一键命令：mkdocs gh-deploy --force
```

### 🚨 问题诊断库
**问题卡模板**：
```
## 问题：简短描述

### 现象
- 期望：应该发生什么
- 实际：实际发生了什么
- 环境：版本、系统、依赖

### 排查过程
1. 检查了：____
2. 尝试了：____
3. 排除了：____

### 根本原因
表层原因 → 深层原因

### 解决方案
临时方案：快速修复
彻底方案：根本解决

### 预防措施
- [ ] 配置检查点
- [ ] 监控指标
- [ ] 文档更新
```

**已解决问题示例**：
```
## 问题：mkdocs serve时修改Markdown文件不自动刷新

### 现象
- 期望：修改docs/下的.md文件，浏览器自动刷新
- 实际：需要手动刷新页面
- 环境：MkDocs 1.5.3，Windows 11，Python 3.10

### 排查过程
1. 检查了：配置文件是否有watch相关设置
2. 尝试了：重启服务、清除浏览器缓存
3. 排除了：不是浏览器问题，不是文件权限问题

### 根本原因
Windows文件系统监控问题 → MkDocs的livereload功能在某些Windows配置下不工作

### 解决方案
临时方案：手动刷新浏览器
彻底方案：使用 `mkdocs serve --livereload` 明确启用，或使用WSL2

### 预防措施
- [x] 总是使用 `mkdocs serve --livereload` 命令
- [ ] 考虑在WSL2中开发以避免Windows文件系统问题
```

---

*注：第三部分"深度档案"和后续内容将在深入使用后填写*

---

## 📈 学习轨迹

### 🗓️ 时间线
```timeline
今天: 初识工具，记录第一印象
3天后: 完成第一个小任务
1周后: 遇到并解决第一个问题
2周后: 形成常用工作流
1月后: 开始定制配置
3月后: 理解架构原理
```

### 📊 掌握程度自评
**知识维度**：
- [✅] 基本使用（能用）
- [ ] 配置调优（熟练）
- [ ] 问题排查（专家）
- [ ] 源码理解（精通）
- [ ] 扩展开发（贡献者）

---

## 💎 精华总结

### 🎯 给三个月后的自己
> 如果只记得三件事，应该是：
> 1. **mkdocs new → mkdocs serve → mkdocs build** 是核心工作流
> 2. 所有资源必须放在docs目录内才能被复制
> 3. Material主题 + mkdocstrings插件 = 强大API文档方案

### 📝 迭代建议
**当前笔记质量**：
- [✅] 骨架完整，待填充血肉
- [ ] 实用为主，缺少深度
- [ ] 内容全面，需要精简
- [ ] 结构合理，持续更新

**下一步计划**：
- 短期：**配置mkdocstrings插件从Python代码自动生成API文档**
- 中期：**尝试自定义主题和开发简单插件**
- 长期：**在生产环境中部署并建立团队协作流程**

---

## 🚀 使用建议

1. **立即开始**：使用此模板创建一个新的MkDocs项目
2. **边用边记**：每次遇到问题都回到"问题诊断库"记录
3. **定期回顾**：每周五检查哪些部分可以填充更多内容
4. **分享学习**：将你的笔记分享给团队成员，帮助他人快速上手

这个笔记模板的关键优势：**在你不知道该写什么时，它告诉你该问什么问题**。随着使用MkDocs的深入，你会自然填充更多内容。