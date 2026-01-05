# 笔记创建指南

## 笔记类型

### 灵感笔记
- 用于记录日常想法、创意、问题和解决方案
- 文件名格式：`灵感-HHMMSS.md`
- 存储位置：`daynote/YYYYMMDD/`

### 日报
- 用于总结当日工作内容和计划
- 文件名格式：`日报-YYYY-MM-DD.md`
- 存储位置：`日报/`

### 自定义笔记
- 用于创建特定类型的笔记
- 文件名格式：`{类型}-HHMMSS.md`
- 存储位置：`daynote/YYYYMMDD/`

## 创建方法

### 1. 快捷键创建（推荐）
- 灵感笔记：`Ctrl+Alt+I`
- 日报：`Ctrl+Alt+R`
- 自定义笔记：`Ctrl+Alt+C`

### 2. 命令面板创建
1. 按 `Ctrl+Shift+P` 打开命令面板
2. 输入 "Tasks: Run Task"
3. 选择相应的创建任务

### 3. 命令行创建
```bash
# 创建灵感笔记
python scripts/create_note.py --template 灵感

# 创建日报
python scripts/create_note.py --template 日报

# 创建自定义类型笔记
python scripts/create_note.py --template [类型名]
```

## 笔记模板

### 灵感笔记模板
包含以下章节：
- 创意点
- 遇到的问题
- 解决方案
- 学到的知识

### 日报模板
包含以下章节：
- 今日完成
- 今日遇到的问题
- 明日计划
- 学到的新知识
- 其他事项

## 文件生成位置

- 灵感笔记：`daynote/YYYYMMDD/灵感-HHMMSS.md`
- 日报：`日报/日报-YYYY-MM-DD.md`
- 自定义笔记：`daynote/YYYYMMDD/{类型}-HHMMSS.md`