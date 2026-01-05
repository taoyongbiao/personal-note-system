# 目录结构

## 项目结构

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

## 详细说明

### daynote/
- 存放日常笔记的主要目录
- 按日期自动创建子目录，格式为 `YYYYMMDD`
- 每日笔记按类型分类存放

### model/
- 存放笔记模板的目录
- 包含各种类型的笔记模板
- 创建新笔记时会基于这些模板

### 日报/
- 自动生成的日报和评价报告目录
- 按日期组织的日报文件

### scripts/
- 存放系统脚本的目录
- [create_note.py](file://c:\Users\P30015874206\Desktop\note\scripts\create_note.py) - 创建笔记的Python脚本
- [summarize_notes.py](file://c:\Users\P30015874206\Desktop\note\scripts\summarize_notes.py) - AI驱动的笔记分析脚本

### .vscode/
- VSCode配置文件目录
- `tasks.json` - 定义VSCode任务
- `keybindings.json` - 定义快捷键
- `settings.json` - 项目特定设置