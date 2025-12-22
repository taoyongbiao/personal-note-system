#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Personal Note System 安装和设置脚本
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """检查Python版本"""
    if sys.version_info < (3, 6):
        print("错误: 需要Python 3.6或更高版本")
        return False
    return True

def install_requirements():
    """安装依赖包"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("依赖包安装成功")
        return True
    except subprocess.CalledProcessError:
        print("错误: 依赖包安装失败")
        return False

def setup_vscode_tasks():
    """设置VS Code任务"""
    if not os.path.exists('.vscode'):
        os.makedirs('.vscode')
        print("创建 .vscode 目录")
    
    # 检查是否存在tasks.json
    if not os.path.exists('.vscode/tasks.json'):
        print("请手动配置 .vscode/tasks.json 文件")
    
    return True

def main():
    """主函数"""
    print("开始设置 Personal Note System...")
    
    # 检查Python版本
    if not check_python_version():
        sys.exit(1)
    
    # 安装依赖
    if not install_requirements():
        sys.exit(1)
    
    # 设置VS Code任务
    if not setup_vscode_tasks():
        sys.exit(1)
    
    print("设置完成!")
    print("\n使用说明:")
    print("1. 使用 Ctrl+Shift+P 打开命令面板")
    print("2. 输入 'Tasks: Run Task' 并选择以下任务之一:")
    print("   - 创建灵感笔记")
    print("   - 创建日报")
    print("   - 创建自定义笔记")

if __name__ == "__main__":
    main()