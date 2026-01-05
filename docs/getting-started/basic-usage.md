# 基本使用

## VSCode 任务

项目配置了以下 VSCode 任务，可通过 `Ctrl+Shift+P` > `Tasks: Run Task` 访问：

- **创建灵感笔记** - 基于灵感模板创建新笔记
- **创建日报** - 基于日报模板创建新笔记
- **创建自定义笔记** - 基于自定义模板创建新笔记

## 快捷键操作（推荐）

- `Ctrl+Alt+I` - 创建灵感笔记
- `Ctrl+Alt+R` - 创建日报
- `Ctrl+Alt+C` - 创建自定义类型笔记

**注意：如果快捷键操作失败，请使用命令面板操作**

## 命令面板操作

1. 按 `Ctrl+Shift+P` 打开 VSCode 命令面板
2. 输入 "Tasks: Run Task"
3. 选择以下任务之一：
   - `create-inspiration-note`：创建灵感笔记
   - `create-report-note`：创建日报
   - `create-custom-note`：创建自定义类型笔记

## 命令行操作（替代方法）

如果快捷键和命令面板操作失败，可以使用命令行方式：

```bash
# 创建灵感笔记
python scripts/create_note.py --template 灵感

# 创建日报
python scripts/create_note.py --template 日报

# 创建自定义类型笔记
python scripts/create_note.py --template [类型名]
```

## 手动创建笔记（备用方法）

如果以上方法都不可用，可以手动创建笔记：

1. 在 `daynote/YYYYMMDD/` 目录下创建新的 [.md](file://c:\Users\P30015874206\Desktop\note\README.md) 文件
2. 从 `daynote/model/` 目录复制相应模板内容
3. 手动替换模板中的 `{{date}}` 占位符为当前日期

## 文档系统使用

项目集成了mkdocs文档系统，可通过以下方式使用：

```bash
# 启动本地文档服务
python scripts/start_docs.py serve

# 构建文档网站
python scripts/start_docs.py build
```

文档将运行在 http://127.0.0.1:8000