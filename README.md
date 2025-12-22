# 个人笔记系统

这是一个基于 VSCode 的个人笔记管理系统，旨在帮助您高效地记录日常工作、自动生成日报以及评估工作状态。

## 功能特性

- 自动创建日期目录
- 模板化笔记创建
- 快捷键操作
- 自动替换日期占位符
- Git 子模块管理

## 安装设置

1. 克隆项目到本地：
   ```
   git clone https://github.com/taoyongbiao/personal-note-system.git
   ```

2. 进入项目目录并运行设置脚本：
   ```
   cd personal-note-system
   python setup.py
   ```

3. 安装过程会自动安装依赖包并配置基本环境。

## 使用方法

### VS Code 任务

项目配置了以下 VS Code 任务，可通过 `Ctrl+Shift+P` > `Tasks: Run Task` 访问：

- **创建灵感笔记** - 基于灵感模板创建新笔记
- **创建日报** - 基于日报模板创建新笔记
- **创建自定义笔记** - 基于自定义模板创建新笔记

### 快捷键

- `Ctrl+Alt+1` - 创建灵感笔记
- `Ctrl+Alt+2` - 创建日报
- `Ctrl+Alt+3` - 创建自定义笔记

## 目录结构

```
note/
├── daynote/                 # 日常笔记目录
│   ├── 20251222/           # 以日期命名的子目录
│   └── model/              # 模板目录
│       ├── 灵感.md          # 灵感笔记模板
│       └── 日报.md          # 日报模板
├── 日报/                   # 自动生成的日报目录
├── scripts/                # 脚本目录
│   └── create_note.py      # 创建笔记的Python脚本
└── .vscode/                # VSCode配置目录
    ├── tasks.json          # 任务配置
    ├── keybindings.json    # 快捷键配置
    └── settings.json       # 设置配置
```

## 更多信息

请参考以下文档了解更多详情：
- [使用说明书.md](使用说明书.md) - 系统详细使用指南
- [子模块使用说明.md](子模块使用说明.md) - Git子模块管理说明
- [task.md](task.md) - 项目任务规划