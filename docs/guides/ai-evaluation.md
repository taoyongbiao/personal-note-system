# AI评价系统

## 功能概述

AI评价系统是一个AI驱动的脚本，用于自动汇总和评价您的灵感笔记。该系统可以：

- 自动扫描`daynote`目录下的今日笔记
- 使用AI对笔记进行总结和评价
- 生成详细的评价报告

## 依赖安装

确保已安装所需的依赖包：

```bash
pip install -r requirements.txt
```

主要依赖：
- `openai` - 用于调用OpenAI API

## 配置API密钥

设置API密钥环境变量：

```bash
export OPENAI_API_KEY=your_api_key
```

或者在系统环境变量中设置 `OPENAI_API_KEY`。

## 运行脚本

### 基本运行
```bash
python scripts/summarize_notes.py
```

### 指定日期运行
```bash
python scripts/summarize_notes.py --date 2025-12-22
```

## 生成的文件

AI评价系统会生成以下文件：

- 评价报告：`日报/灵感笔记评价报告-YYYY-MM-DD.md`
- 包含对当天笔记的总结和评价

## 评价报告结构

评价报告通常包含：

- **笔记内容摘要** - AI对笔记内容的总结
- **质量评估** - 对笔记质量的评价
- **改进建议** - 提高笔记质量的建议
- **关键点提取** - 从笔记中提取的重要信息

## 注意事项

1. **API成本** - 使用AI服务可能会产生费用，请注意API使用量
2. **隐私保护** - 确保不通过AI服务处理敏感信息
3. **网络连接** - 需要稳定的网络连接以访问AI服务
4. **错误处理** - 如果API调用失败，脚本会记录错误并继续执行