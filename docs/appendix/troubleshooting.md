# 故障排除

## 常见错误

### 依赖安装错误

**错误信息：** `Could not find a version that satisfies the requirement`

**解决方案：**
1. 升级pip工具：
   ```bash
   python -m pip install --upgrade pip
   ```
2. 使用国内镜像源：
   ```bash
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
   ```
3. 检查Python版本是否满足要求（3.7+）

### 脚本执行错误

**错误信息：** `ModuleNotFoundError: No module named 'openai'`

**解决方案：**
1. 确认已安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 检查Python环境是否正确
3. 如果使用虚拟环境，确保已激活

### 权限错误

**错误信息：** `PermissionError: [Errno 13] Permission denied`

**解决方案：**
1. 检查当前用户是否有写入目录的权限
2. 尝试以管理员身份运行命令
3. 检查文件是否被其他程序占用

## VSCode相关问题

### 任务无法运行

**症状：** 点击任务无响应或报错

**排查步骤：**
1. 检查 `.vscode/tasks.json` 文件是否存在且格式正确
2. 确认Python路径是否正确配置
3. 检查脚本路径是否正确
4. 在VSCode终端中直接运行脚本测试：
   ```bash
   python scripts/create_note.py --template 灵感
   ```

### 快捷键冲突

**症状：** 快捷键被其他扩展占用

**排查步骤：**
1. 打开VSCode命令面板（Ctrl+Shift+P）
2. 输入"Preferences: Open Keyboard Shortcuts"
3. 搜索冲突的快捷键
4. 修改或删除冲突的快捷键绑定

## AI功能问题

### API连接失败

**错误信息：** `openai.error.APIConnectionError`

**排查步骤：**
1. 检查网络连接是否正常
2. 确认 `OPENAI_API_KEY` 环境变量已设置
3. 检查API密钥是否有效
4. 确认API服务状态（可能临时不可用）

### API密钥错误

**错误信息：** `openai.error.AuthenticationError`

**排查步骤：**
1. 检查 `OPENAI_API_KEY` 环境变量值是否正确
2. 确认API密钥未过期
3. 检查账户是否有足够余额或配额
4. 在OpenAI控制台重新生成API密钥

## 文档系统问题

### MkDocs未安装

**错误信息：** `mkdocs is not recognized as an internal or external command`

**解决方案：**
1. 确认已安装mkdocs：
   ```bash
   pip install mkdocs mkdocs-material
   ```
2. 检查Python环境是否正确
3. 确认环境变量PATH中包含Python脚本目录

### 文档服务启动失败

**症状：** 运行 `python scripts/start_docs.py serve` 失败

**排查步骤：**
1. 检查mkdocs相关依赖是否安装：
   ```bash
   pip install -r requirements.txt
   ```
2. 确认 `mkdocs.yml` 配置文件是否存在且格式正确
3. 检查端口是否被占用，尝试使用不同端口：
   ```bash
   python scripts/start_docs.py serve --port 8080
   ```

### 文档构建失败

**症状：** 运行 `python scripts/start_docs.py build` 失败

**排查步骤：**
1. 检查 `mkdocs.yml` 配置文件语法
2. 确认 `docs/` 目录及其中的文档文件存在
3. 检查文档中链接是否正确

## 文件系统问题

### 目录创建失败

**症状：** 无法创建日期目录

**排查步骤：**
1. 检查项目根目录路径是否正确
2. 确认有写入权限
3. 检查磁盘空间是否充足
4. 确认文件名长度未超过系统限制

### 文件编码问题

**症状：** 中文字符显示异常或保存失败

**解决方案：**
1. 确保Python脚本使用UTF-8编码
2. 在脚本中明确指定编码：
   ```python
   with open(file_path, 'w', encoding='utf-8') as f:
       # 处理文件
   ```

## 脚本调试

### 启用详细日志

在脚本中添加调试输出：

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### 逐步调试

1. 在脚本中添加print语句输出关键变量
2. 使用Python调试器：
   ```python
   import pdb; pdb.set_trace()
   ```
3. 检查每一步的返回值和状态

## 环境问题

### Python路径问题

**症状：** 系统找不到Python解释器

**解决方案：**
1. 在VSCode中选择正确的Python解释器：
   - Ctrl+Shift+P 打开命令面板
   - 输入 "Python: Select Interpreter"
   - 选择正确的Python版本
2. 检查系统PATH变量是否包含Python路径

### 虚拟环境问题

**症状：** 在虚拟环境中无法运行脚本

**排查步骤：**
1. 确认虚拟环境已激活
2. 检查虚拟环境中是否安装了所需依赖
3. 确认VSCode使用的是虚拟环境中的Python解释器

## 性能问题

### 脚本运行缓慢

**可能原因：**
1. 网络请求延迟（AI功能）
2. 文件系统I/O缓慢
3. 大量文件扫描

**优化方案：**
1. 限制扫描的目录范围
2. 添加缓存机制
3. 异步处理网络请求

## 系统恢复

### 重置配置

如果配置文件损坏，可以：

1. 备份当前配置
2. 从版本控制中恢复配置文件
3. 重新运行setup.py脚本

### 清理缓存

清理VSCode缓存：

1. 关闭VSCode
2. 删除 `.vscode` 目录下的缓存文件
3. 重新打开项目

## 联系支持

如果以上方法都无法解决问题：

1. 检查项目仓库的Issues页面
2. 提交新的Issue，包含：
   - 详细的操作步骤
   - 错误信息截图
   - 系统环境信息
   - 已尝试的解决方案