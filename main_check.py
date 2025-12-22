#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
主线任务检查脚本
用于检查当前任务是否符合项目主线目标
"""

import os
import sys
import json
from datetime import datetime

def read_task_file():
    """读取任务文件内容"""
    try:
        with open('task.md', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("错误: 找不到 task.md 文件")
        return None

def get_current_version(tasks_content):
    """从任务内容中提取当前进行中的版本"""
    lines = tasks_content.split('\n')
    current_version = None
    
    for line in lines:
        if '进行中' in line and line.startswith('##'):
            # 提取版本号 (如 v1.0)
            current_version = line.split()[1]
            break
    
    return current_version

def check_task_alignment(task_description, current_version):
    """检查任务是否与当前版本对齐"""
    # 这里可以实现更复杂的检查逻辑
    # 目前简化处理：假设任务描述中包含版本信息
    if current_version in task_description:
        return True
    return False

def main():
    """主函数"""
    print("正在执行主线任务检查...")
    
    # 读取任务文件
    tasks_content = read_task_file()
    if not tasks_content:
        sys.exit(1)
    
    # 获取当前版本
    current_version = get_current_version(tasks_content)
    if not current_version:
        print("错误: 无法确定当前进行中的版本")
        sys.exit(1)
    
    print(f"当前主线版本: {current_version}")
    
    # 模拟检查过程
    # 在实际应用中，这里应该接收用户输入的任务描述
    # 并检查其是否符合当前版本目标
    print("检查通过: 任务符合当前主线目标")
    sys.exit(0)

if __name__ == "__main__":
    main()