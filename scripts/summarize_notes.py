#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AI驱动的灵感笔记汇总与评价脚本

该脚本能够：
1. 收集当天的所有灵感笔记
2. 使用AI对这些笔记进行总结
3. 基于综合评价标准对笔记进行评分
"""

import os
import sys
import json
from datetime import datetime
import argparse
import re

# 尝试导入markdownify库用于解析markdown内容
try:
    from markdownify import markdownify
    markdownify_available = True
except ImportError:
    markdownify_available = False
    print("警告: markdownify库未安装，将使用正则表达式解析markdown内容。请运行 'pip install markdownify' 安装。")

# 尝试导入dashscope，如果没有安装则提示用户
try:
    from openai import OpenAI
    openai_available = True
except ImportError:
    openai_available = False
    print("警告: openai库未安装，AI功能将不可用。请运行 'pip install openai' 安装。")




def get_todays_notes():
    """
    获取今天的全部灵感笔记
    
    Returns:
        list: 包含今天所有灵感笔记文件路径的列表
    """
    # 项目根路径
    root_path = r"c:\Users\P30015874206\Desktop\note"
    
    # 获取今天的日期
    today = datetime.now().strftime("%Y%m%d")
    notes_dir = os.path.join(root_path, "daynote", today)
    
    # 检查目录是否存在
    if not os.path.exists(notes_dir):
        print(f"今日({today})没有找到笔记目录")
        return []
    
    # 查找所有以"灵感-"开头的笔记文件
    notes = []
    for file in os.listdir(notes_dir):
        if file.startswith("灵感-") and file.endswith(".md"):
            notes.append(os.path.join(notes_dir, file))
    
    return notes


def extract_note_content(note_path):
    """
    提取笔记的核心内容
    
    Args:
        note_path (str): 笔记文件路径
        
    Returns:
        dict: 包含各部分内容的字典
    """
    content_sections = {
        "创意点": "",
        "遇到的问题": "",
        "解决方案": "",
        "学到的知识": ""
    }
    
    try:
        with open(note_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 如果markdownify库可用，则使用markdownify来解析markdown内容
        if markdownify_available:
            # 首先使用正则表达式提取各个部分的原始内容
            for section in content_sections:
                # 匹配 ## 标题 或 ## emoji 标题 格式，使用更高效的正则表达式
                pattern = rf"##\s*[^\n]*?{section}[^\n]*\n(.*?)(?=\n##|\Z)"
                match = re.search(pattern, content, re.DOTALL)
                if match:
                    raw_content = match.group(1).strip()
                    # 使用markdownify将markdown内容转换为纯文本
                    # 这样可以正确处理markdown格式如粗体、斜体等
                    text_content = markdownify(raw_content).strip()
                    content_sections[section] = text_content
        else:
            # 如果markdownify不可用，使用正则表达式提取各个部分的内容
            # 支持带emoji的标题格式
            for section in content_sections:
                # 匹配 ## 标题 或 ## emoji 标题 格式，使用更高效的正则表达式
                pattern = rf"##\s*[^\n]*?{section}[^\n]*\n(.*?)(?=\n##|\Z)"
                match = re.search(pattern, content, re.DOTALL)
                if match:
                    content_sections[section] = match.group(1).strip()
                
    except Exception as e:
        print(f"读取笔记文件 {note_path} 时出错: {e}")
    
    return content_sections


def call_openai_api(prompt):
    """
    调用OpenAI API
    
    Args:
        prompt (str): 发送给模型的提示文本
        
    Returns:
        str: 模型返回的结果
    """
    # 检查是否安装了openai库
    if not openai_available:
        # 模拟返回结果
        return f"[模拟结果] 这是由OpenAI模型生成的对以下内容的分析:\n{prompt[:100]}..."
    
    try:
        # 从环境变量获取API密钥
        api_key = os.environ.get('OPENAI_API_KEY','3d061ebe28224561a964d4070842cb4c.UndstCPsmmdAg1uq')
        if not api_key:
            print("警告: 未设置OPENAI_API_KEY环境变量，将使用模拟AI功能")
            # 模拟返回结果
            return f"[模拟结果] 这是由OpenAI模型生成的对以下内容的分析:\n{prompt[:100]}..."
        
        # 从环境变量获取基础URL和模型名称
        base_url = os.environ.get('OPENAI_BASE_URL', 'https://open.bigmodel.cn/api/paas/v4/')
        model = os.environ.get('OPENAI_MODEL', 'glm-4.6v-flash')
        
        # 创建OpenAI客户端
        client = OpenAI(api_key=api_key, base_url=base_url)
        
        # 调用OpenAI模型
        print("正在调用OpenAI API...")
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        print("OpenAI API调用成功")
        return response.choices[0].message.content
    except Exception as e:
        print(f"调用OpenAI API时出错: {e}")
        return "AI分析暂时不可用"


def ai_summarize_notes(notes_data):
    """
    使用AI对笔记内容进行总结
    
    Args:
        notes_data (list): 包含所有笔记内容的列表
        
    Returns:
        str: AI生成的总结内容
    """
    # 构建发送给AI的完整内容
    all_content = []
    for i, note in enumerate(notes_data):
        content = f"笔记 {i+1}:\n"
        for section, text in note.items():
            if text.strip():
                content += f"{section}: {text}\n"
        all_content.append(content)
    
    full_content = "\n---\n".join(all_content)
    
    # 构造提示词
    prompt = f"""请对以下多篇笔记内容进行总结分析：

{full_content}

请从以下几个维度进行分析：
1. 内容概览：总共多少篇笔记
2. 主题分布：涉及哪些主要领域或主题
3. 质量评估：整体内容质量如何
4. 改进建议：有哪些可以提升的地方

请用中文回答，保持专业且易于理解。"""

    # 调用OpenAI API
    ai_response = call_openai_api(prompt)
    return ai_response


def evaluate_note_with_ai(note_data):
    """
    使用AI对笔记进行评价
    
    Args:
        note_data (dict): 单条笔记的数据
        
    Returns:
        dict: 包含各项评分和总分的字典
    """
    scores = {
        "完整性": 0,
        "深度": 0,
        "实用性": 0,
        "创新性": 0,
        "反思性": 0,
        "AI评语": "",
        "总分": 0
    }
    
    # 构造发送给AI的提示词
    note_content = ""
    for section, text in note_data.items():
        if text.strip():
            note_content += f"{section}: {text}\n"
    
    if not note_content.strip():
        scores["AI评语"] = "笔记内容为空"
        return scores
    
    prompt = f"""请根据以下综合评价标准对这篇笔记进行评分（每项满分20分）：

评价标准：
1. 完整性：是否包含创意点、遇到的问题、解决方案、学到的知识等要素
2. 深度：内容是否有足够的细节和深入的思考
3. 实用性：是否提供了可操作的解决方案或有价值的知识
4. 创新性：是否有独特的见解或新颖的想法
5. 反思性：是否对问题进行了深入分析和反思

笔记内容：
{note_content}

请按以下格式返回结果：
完整性：<分数>/20
深度：<分数>/20
实用性：<分数>/20
创新性：<分数>/20
反思性：<分数>/20
评语：<简要评语>

只需返回以上内容，不要添加其他文字。"""

    # 调用AI获取评分
    print("开始调用AI进行笔记评价...")
    ai_response = call_openai_api(prompt)
    print("AI评价完成")
    scores["AI评语"] = ai_response
    
    # 解析AI返回的评分
    try:
        lines = ai_response.split('\n')
        for line in lines:
            if '完整性：' in line:
                score = int(line.split('：')[1].split('/')[0])
                scores["完整性"] = min(20, max(0, score))
            elif '深度：' in line:
                score = int(line.split('：')[1].split('/')[0])
                scores["深度"] = min(20, max(0, score))
            elif '实用性：' in line:
                score = int(line.split('：')[1].split('/')[0])
                scores["实用性"] = min(20, max(0, score))
            elif '创新性：' in line:
                score = int(line.split('：')[1].split('/')[0])
                scores["创新性"] = min(20, max(0, score))
            elif '反思性：' in line:
                score = int(line.split('：')[1].split('/')[0])
                scores["反思性"] = min(20, max(0, score))
    except Exception as e:
        print(f"解析AI评分时出错: {e}")
        # 如果AI评分解析失败，使用原有规则进行评分
        return evaluate_note(note_data)
    
    # 计算总分
    scores["总分"] = sum(scores[key] for key in scores if key not in ["总分", "AI评语"])
    
    return scores


def evaluate_note(note_data):
    """
    根据综合评价标准对单条笔记进行评分（基础版本）
    
    Args:
        note_data (dict): 单条笔记的数据
        
    Returns:
        dict: 包含各项评分和总分的字典
    """
    scores = {
        "完整性": 0,
        "深度": 0,
        "实用性": 0,
        "创新性": 0,
        "反思性": 0,
        "总分": 0
    }
    
    # 完整性评分 (最高20分)
    complete_fields = sum(1 for v in note_data.values() if v.strip())
    scores["完整性"] = min(20, complete_fields * 5)  # 每个非空字段5分
    
    # 深度评分 (最高20分)
    # 根据内容长度评估深度
    total_length = sum(len(v) for v in note_data.values())
    scores["深度"] = min(20, total_length // 50)  # 每50字符1分
    
    # 实用性评分 (最高20分)
    # 主要基于解决方案和学到的知识部分
    practical_content = len(note_data.get("解决方案", "")) + len(note_data.get("学到的知识", ""))
    scores["实用性"] = min(20, practical_content // 30)  # 每30字符1分
    
    # 创新性评分 (最高20分)
    # 基于创意点部分的内容长度
    innovation_content = len(note_data.get("创意点", ""))
    scores["创新性"] = min(20, innovation_content // 20)  # 每20字符1分
    
    # 反思性评分 (最高20分)
    # 基于遇到的问题和解决方案部分的内容长度
    reflection_content = len(note_data.get("遇到的问题", "")) + len(note_data.get("解决方案", ""))
    scores["反思性"] = min(20, reflection_content // 25)  # 每25字符1分
    
    # 计算总分
    scores["总分"] = sum(scores[key] for key in scores if key != "总分")
    
    return scores


def evaluate_all_notes(notes_data):
    """
    对所有笔记进行评价
    
    Args:
        notes_data (list): 所有笔记的数据列表
        
    Returns:
        list: 包含每条笔记评价结果的列表
    """
    evaluations = []
    
    for i, note_data in enumerate(notes_data):
        evaluation = evaluate_note(note_data)
        evaluation["笔记编号"] = i + 1
        evaluations.append(evaluation)
    
    return evaluations


def generate_report(notes_paths, notes_data, summary, evaluations):
    """
    生成完整的评估报告
    
    Args:
        notes_paths (list): 笔记文件路径列表
        notes_data (list): 笔记内容数据列表
        summary (str): AI生成的总结
        evaluations (list): 评价结果列表
        
    Returns:
        str: 完整的评估报告
    """
    report_lines = []
    
    # 报告标题
    report_lines.append("# 灵感笔记AI总结与评价报告")
    report_lines.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("")
    
    # 总结部分
    report_lines.append("## AI总结")
    report_lines.append(summary)
    report_lines.append("")
    
    # 评价部分
    report_lines.append("## 笔记评价")
    
    for i, (path, data, eval_result) in enumerate(zip(notes_paths, notes_data, evaluations)):
        report_lines.append(f"### 笔记 {i+1}: {os.path.basename(path)}")
        report_lines.append(f"- 完整性: {eval_result['完整性']}/20")
        report_lines.append(f"- 深度: {eval_result['深度']}/20")
        report_lines.append(f"- 实用性: {eval_result['实用性']}/20")
        report_lines.append(f"- 创新性: {eval_result['创新性']}/20")
        report_lines.append(f"- 反思性: {eval_result['反思性']}/20")
        report_lines.append(f"- 总分: {eval_result['总分']}/100")
        # 如果有AI评语，也显示出来
        if 'AI评语' in eval_result and eval_result['AI评语']:
            report_lines.append(f"- AI评语: {eval_result['AI评语']}")
        report_lines.append("")
    
    # 综合建议
    report_lines.append("## 综合建议")
    avg_score = sum(e['总分'] for e in evaluations) / len(evaluations) if evaluations else 0
    report_lines.append(f"平均得分: {avg_score:.1f}/100")
    
    if avg_score >= 80:
        report_lines.append("表现优秀！继续保持高质量的记录习惯。")
    elif avg_score >= 60:
        report_lines.append("表现良好，建议在某些方面进一步深入思考。")
    else:
        report_lines.append("还有提升空间，建议增加内容深度和实用性。")
    
    return "\n".join(report_lines)


def save_report(report_content):
    """
    保存报告到文件
    
    Args:
        report_content (str): 报告内容
    """
    # 项目根路径
    root_path = r"c:\Users\P30015874206\Desktop\note"
    
    # 创建报告目录（如果不存在）
    reports_dir = os.path.join(root_path, "日报")
    os.makedirs(reports_dir, exist_ok=True)
    
    # 生成报告文件名
    date_str = datetime.now().strftime("%Y-%m-%d")
    report_filename = f"灵感笔记评价报告-{date_str}.md"
    report_path = os.path.join(reports_dir, report_filename)
    
    # 保存报告
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"报告已保存至: {report_path}")
    return report_path


def main():
    """主函数"""
    print("开始收集和评价今日灵感笔记...")
    
    # 1. 获取今天的笔记
    notes_paths = get_todays_notes()
    if not notes_paths:
        print("未找到今天的灵感笔记")
        return
    
    print(f"找到 {len(notes_paths)} 篇笔记")
    
    # 2. 提取笔记内容
    notes_data = []
    for path in notes_paths:
        print(f"正在处理: {os.path.basename(path)}")
        content = extract_note_content(path)
        print(f"笔记 {os.path.basename(path)} 内容提取完成")
        notes_data.append(content)
    
    # 3. AI总结
    print("正在进行AI总结...")
    summary = ai_summarize_notes(notes_data)
    print("AI总结完成")
    
    # 4. 评价所有笔记（使用AI辅助评分）
    print("正在评价笔记...")
    evaluations = []
    for i, note_data in enumerate(notes_data):
        print(f"正在评价笔记 {i+1}/{len(notes_data)}: {notes_paths[i]}...")
        evaluation = evaluate_note_with_ai(note_data)
        evaluation["笔记编号"] = i + 1
        evaluations.append(evaluation)
        print(f"笔记 {i+1} 评价完成")
    print("笔记评价完成")
    
    # 5. 生成报告
    print("正在生成报告...")
    report = generate_report(notes_paths, notes_data, summary, evaluations)
    
    # 6. 保存报告
    report_path = save_report(report)
    print("报告生成完成")
    
    # 7. 显示摘要
    print("\n=== 报告摘要 ===")
    print(summary)
    print(f"\n详细报告已保存至: {report_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI驱动的灵感笔记汇总与评价")
    parser.add_argument("--verbose", "-v", action="store_true", help="显示详细信息")
    
    args = parser.parse_args()
    
    main()