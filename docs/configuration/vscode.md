# VSCode配置

## 配置文件

项目包含以下VSCode配置文件：

- `.vscode/tasks.json` - 定义可执行任务
- `.vscode/keybindings.json` - 定义快捷键
- `.vscode/settings.json` - 项目特定设置

## 任务配置 (tasks.json)

### 创建灵感笔记任务

```json
{
    "label": "create-inspiration-note",
    "type": "shell",
    "command": "python",
    "args": [
        "${workspaceFolder}/scripts/create_note.py",
        "--template",
        "灵感"
    ],
    "group": "build",
    "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "new"
    }
}
```

### 创建日报任务

```json
{
    "label": "create-report-note",
    "type": "shell",
    "command": "python",
    "args": [
        "${workspaceFolder}/scripts/create_note.py",
        "--template",
        "日报"
    ],
    "group": "build",
    "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "new"
    }
}
```

### 创建自定义笔记任务

```json
{
    "label": "create-custom-note",
    "type": "shell",
    "command": "python",
    "args": [
        "${workspaceFolder}/scripts/create_note.py",
        "--template",
        "${input:noteType}"
    ],
    "group": "build",
    "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "new"
    },
    "inputs": [
        {
            "id": "noteType",
            "type": "promptString",
            "description": "请输入笔记类型：",
            "default": "灵感"
        }
    ]
}
```

## 快捷键配置 (keybindings.json)

```json
[
    {
        "key": "ctrl+alt+i",
        "command": "workbench.action.tasks.runTask",
        "args": "create-inspiration-note"
    },
    {
        "key": "ctrl+alt+r",
        "command": "workbench.action.tasks.runTask",
        "args": "create-report-note"
    },
    {
        "key": "ctrl+alt+c",
        "command": "workbench.action.tasks.runTask",
        "args": "create-custom-note"
    }
]
```

## 项目设置 (settings.json)

项目特定的VSCode设置，可能包含：

- 文件关联
- 编辑器配置
- 工作区特定的扩展设置

## 自定义配置

您可以根据需要修改这些配置：

### 添加新任务

在 `tasks.json` 中添加新任务：

```json
{
    "label": "new-task-name",
    "type": "shell",
    "command": "python",
    "args": [
        "${workspaceFolder}/path/to/script.py",
        "--option",
        "value"
    ],
    "group": "build"
}
```

### 修改快捷键

在 `keybindings.json` 中修改快捷键：

```json
{
    "key": "ctrl+shift+n",
    "command": "workbench.action.tasks.runTask",
    "args": "new-task-name"
}
```

## 故障排除

### 快捷键不工作

1. 检查快捷键是否与其他扩展冲突
2. 确认VSCode已正确加载工作区配置
3. 尝试重启VSCode

### 任务不执行

1. 检查Python路径是否正确
2. 确认脚本文件存在且可执行
3. 检查命令行参数是否正确