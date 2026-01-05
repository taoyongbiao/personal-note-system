# API参考

## create_note.py

### get_project_root()

查找项目根目录，通过搜索setup.py文件来确定项目根路径。

**返回值**

- `str` - 项目根目录路径

### create_note(template_name)

根据指定模板创建笔记文件。

**参数**

- `template_name` (str) - 模板名称

**返回值**

- `str` - 创建的笔记文件路径

### get_current_time_str()

获取当前时间字符串，格式为YYYY-MM-DD或HHMMSS。

**参数**

- `format_type` (str) - "date"获取日期格式，"time"获取时间格式

**返回值**

- `str` - 格式化的时间字符串

### extract_note_content(file_path)

从笔记文件中提取内容。

**参数**

- `file_path` (str) - 笔记文件路径

**返回值**

- `str` - 笔记内容

## summarize_notes.py

### get_today_notes(date_str=None)

获取指定日期的笔记文件列表。

**参数**

- `date_str` (str, optional) - 日期字符串，格式为YYYY-MM-DD，默认为今天

**返回值**

- `list` - 笔记文件路径列表

### summarize_with_ai(notes_content)

使用AI对笔记内容进行总结和评价。

**参数**

- `notes_content` (str) - 笔记内容

**返回值**

- `str` - AI生成的总结和评价

### save_summary(summary, date_str=None)

保存AI生成的总结到文件。

**参数**

- `summary` (str) - 总结内容
- `date_str` (str, optional) - 日期字符串，默认为今天

## main_check.py

### check_main_tasks()

检查主线任务的完成状态。

**返回值**

- `dict` - 任务状态统计

### update_task_status()

更新任务状态。

**返回值**

- `bool` - 更新是否成功

## start_docs.py

### start_docs_serve(docs_dir=None, port=8000)

启动文档服务器。

**参数**

- `docs_dir` (str, optional) - 文档目录路径
- `port` (int) - 服务端口，默认为8000

**返回值**

- `bool` - 启动是否成功

### build_docs()

构建文档网站。

**返回值**

- `bool` - 构建是否成功

### check_mkdocs_installed()

检查mkdocs是否已安装。

**返回值**

- `bool` - 是否已安装

### install_mkdocs()

安装mkdocs及其相关插件。

**返回值**

- `bool` - 安装是否成功

## 工具函数

### find_project_root()

在指定路径下查找项目根目录。

**参数**

- `start_path` (str) - 开始搜索的路径

**返回值**

- `str` - 项目根目录路径，如果未找到则返回None

### ensure_directory_exists(path)

确保指定目录存在，如果不存在则创建。

**参数**

- `path` (str) - 目录路径

**返回值**

- `bool` - 操作是否成功

### read_template(template_name)

读取指定名称的模板内容。

**参数**

- `template_name` (str) - 模板名称

**返回值**

- `str` - 模板内容，如果模板不存在则返回None
