# 常见问题

## 安装和配置

### Q: 安装依赖时出现错误怎么办？
**A:** 请确保Python版本为3.7或更高。如果仍有错误，尝试：
1. 升级pip: `python -m pip install --upgrade pip`
2. 使用国内镜像源: `pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/`

### Q: 快捷键不工作怎么办？
**A:** 检查以下几点：
1. 确认VSCode已正确加载工作区配置
2. 检查快捷键是否与其他扩展冲突
3. 重启VSCode后重试
4. 尝试使用命令面板操作作为备选方案

### Q: 如何修改快捷键？
**A:** 编辑 `.vscode/keybindings.json` 文件，修改或添加新的快捷键组合。

## 笔记创建

### Q: 笔记文件没有自动创建日期目录怎么办？
**A:** 系统应该自动创建日期目录。如果失败，请：
1. 检查脚本权限是否足够
2. 确认项目根目录位置是否正确
3. 手动创建 `daynote/YYYYMMDD` 目录

### Q: 模板中的 `{{date}}` 没有被替换怎么办？
**A:** 这可能是脚本中的日期替换功能出现问题。请：
1. 检查 [create_note.py](file://c:\Users\P30015874206\Desktop\note\scripts\create_note.py) 脚本是否正确处理日期替换
2. 确认模板文件中使用的是 `{{date}}` 格式

### Q: 如何创建自定义类型的笔记？
**A:** 有几种方式：
1. 在 `daynote/model/` 目录中创建新模板
2. 使用命令行: `python scripts/create_note.py --template [模板名]`
3. 通过VSCode任务系统创建自定义任务

## AI评价系统

### Q: AI评价功能无法使用怎么办？
**A:** 检查以下几点：
1. 确认已安装 `openai` 包
2. 设置了 `OPENAI_API_KEY` 环境变量
3. 网络连接正常，可以访问OpenAI API
4. API配额未用完

### Q: AI评价结果不准确怎么办？
**A:** 可以尝试：
1. 提供更详细和结构化的笔记内容
2. 调整AI请求参数（如temperature）
3. 使用更高级的模型（如gpt-4）

### Q: 使用AI功能会产生费用吗？
**A:** 是的，使用OpenAI API会产生费用。建议：
1. 监控API使用量
2. 设置API使用限额
3. 在不需要时禁用AI评价功能

## 文档系统

### Q: 如何启动文档服务？
**A:** 使用以下命令：
```bash
python scripts/start_docs.py serve
```
文档将在 http://127.0.0.1:8000 上运行。

### Q: 如何构建静态文档网站？
**A:** 使用以下命令：
```bash
python scripts/start_docs.py build
```
网站将构建到 `site/` 目录中。

### Q: 文档系统需要哪些依赖？
**A:** 项目依赖以下文档相关包：
- `mkdocs>=1.4.0`
- `mkdocs-material>=9.0.0`
- `mkdocs-git-revision-date-localized-plugin>=1.0.0`
- `mkdocs-minify-plugin>=0.5.0`
- `mkdocs-macros-plugin>=0.7.0`

## 任务检查

### Q: 任务检查功能如何工作？
**A:** 任务检查功能会：
1. 读取 [task.md](file://c:\Users\P30015874206\Desktop\note\task.md) 文件中的任务列表
2. 检查任务状态（待开始/进行中/已完成）
3. 生成任务状态报告
4. 可能自动更新某些任务的状态

### Q: 如何格式化任务文件？
**A:** 使用以下格式：

```markdown
# 项目任务规划

## 主要任务

### 高优先级
- [ ] 任务1 - 描述
- [x] 任务2 - 描述（已完成）

### 中优先级
- [ ] 任务3 - 描述
- [-] 任务4 - 描述（进行中）
```

## 系统集成

### Q: 如何将系统与其他工具集成？
**A:** 可以通过以下方式：
1. 修改Python脚本以输出其他格式
2. 添加新的API接口
3. 创建导入/导出功能
4. 集成到CI/CD流程中

### Q: 如何备份笔记数据？
**A:** 笔记数据主要存储在：
1. `daynote/` 目录 - 日常笔记
2. `日报/` 目录 - 生成的日报和评价
3. [task.md](file://c:\Users\P30015874206\Desktop\note\task.md) - 任务列表

建议定期备份这些目录和文件。

## 故障排除

### Q: 如何启用调试模式？
**A:** 在脚本中添加调试输出，或在命令行中使用详细模式（如果支持）。

### Q: 遇到错误如何寻求帮助？
**A:** 
1. 检查错误信息和日志
2. 查阅相关文档
3. 在项目仓库中提交Issue
4. 检查是否有类似问题的解决方案