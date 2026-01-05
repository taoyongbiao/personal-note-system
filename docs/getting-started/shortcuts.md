# 快捷键操作

## 主要快捷键

- `Ctrl+Alt+I` - 创建灵感笔记
- `Ctrl+Alt+R` - 创建日报
- `Ctrl+Alt+C` - 创建自定义类型笔记

## 快捷键配置文件

快捷键配置位于 `.vscode/keybindings.json` 文件中，您可以根据个人喜好进行修改。

## 快捷键失效处理

如果快捷键操作失败，请尝试以下方法：

1. 检查 VSCode 是否正确加载了工作区配置
2. 确认快捷键未与其他扩展冲突
3. 使用命令面板操作作为备选方案

## 任务配置

所有快捷键关联的任务定义在 `.vscode/tasks.json` 文件中，包括：

- `create-inspiration-note` - 创建灵感笔记任务
- `create-report-note` - 创建日报任务
- `create-custom-note` - 创建自定义笔记任务

## 自定义快捷键

您可以根据需要修改快捷键配置：

1. 打开 VSCode 命令面板 (`Ctrl+Shift+P`)
2. 输入 "Preferences: Open Keyboard Shortcuts (JSON)"
3. 修改或添加您喜欢的快捷键组合

## 文档系统快捷方式

您也可以通过命令行快速启动文档服务：

```bash
python scripts/start_docs.py serve
```