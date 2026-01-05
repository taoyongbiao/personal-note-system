# 项目配置

## 项目结构配置

### setup.py

项目初始化脚本，负责：

- 安装依赖包
- 配置基本环境
- 创建必要的目录结构

### requirements.txt

Python依赖包列表：

```
argparse==1.4.0
openai>=1.0.0
mkdocs>=1.4.0
mkdocs-material>=9.0.0
mkdocs-git-revision-date-localized-plugin>=1.0.0
mkdocs-minify-plugin>=0.5.0
mkdocs-macros-plugin>=0.7.0
```

## 脚本配置

### create_note.py

笔记创建脚本的配置：

- 模板路径：`daynote/model/`
- 输出路径：`daynote/YYYYMMDD/` 或 `日报/`
- 文件命名规则：基于时间戳和笔记类型

### summarize_notes.py

AI评价脚本配置：

- API密钥：通过环境变量 `OPENAI_API_KEY`
- 扫描路径：`daynote/` 目录
- 输出路径：`日报/`

### main_check.py

任务检查脚本配置：

- 任务文件：[task.md](file://c:\Users\P30015874206\Desktop\note\task.md)
- 检查规则：自定义逻辑

### start_docs.py

文档服务脚本配置：

- 文档源目录：`docs/`
- 构建输出目录：`site/`
- 服务端口：默认8000

## 目录配置

### 自动创建目录

系统会自动创建以下目录：

- `daynote/YYYYMMDD/` - 按日期的笔记目录
- `日报/` - 日报输出目录

### 模板目录

- `daynote/model/` - 存放笔记模板
- `docs/` - 存放文档源文件

## 环境变量

### 必需的环境变量

- `OPENAI_API_KEY` - AI服务API密钥（可选，仅AI功能需要）

### 可选的环境变量

- `NOTE_OUTPUT_DIR` - 自定义笔记输出目录
- `NOTE_TEMPLATE_DIR` - 自定义模板目录

## 配置最佳实践

### 1. 环境隔离

建议使用虚拟环境：

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate     # Windows
```

### 2. 依赖管理

定期更新依赖：

```bash
pip list --outdated
pip install --upgrade [package-name]
```

### 3. 配置备份

定期备份以下配置：

- `.vscode/` 目录下的配置文件
- `setup.py` 和 `requirements.txt`
- 自定义模板文件

## 自定义配置

### 修改模板路径

如需修改模板路径，可以：

1. 修改 `create_note.py` 中的模板路径
2. 更新VSCode任务配置中的路径
3. 测试新配置是否正常工作

### 添加新功能

如需添加新功能，可以：

1. 创建新的Python脚本
2. 在 `.vscode/tasks.json` 中添加新任务
3. 在 `.vscode/keybindings.json` 中添加新快捷键
4. 在文档中添加相应说明