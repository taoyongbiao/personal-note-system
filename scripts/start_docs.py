#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
启动文档服务脚本
用于快速启动mkdocs文档服务器
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def get_project_root():
    """获取项目根目录"""
    current_path = Path(__file__).parent.parent
    return current_path


def check_mkdocs_installed():
    """检查mkdocs是否已安装"""
    try:
        import mkdocs
        return True
    except ImportError:
        return False


def install_mkdocs():
    """安装mkdocs及其相关插件"""
    print("正在安装mkdocs及其插件...")
    requirements = [
        "mkdocs>=1.4.0",
        "mkdocs-material>=9.0.0",
        "mkdocs-git-revision-date-localized-plugin>=1.0.0",
        "mkdocs-minify-plugin>=0.5.0",
        "mkdocs-macros-plugin>=0.7.0"
    ]
    
    for req in requirements:
        result = subprocess.run([sys.executable, "-m", "pip", "install", req], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"安装 {req} 失败: {result.stderr}")
            return False
        else:
            print(f"已安装 {req}")
    
    return True


def start_docs_serve(docs_dir=None, port=8000):
    """启动文档服务器"""
    project_root = get_project_root()
    
    # 切换到项目根目录
    os.chdir(project_root)
    
    # 检查mkdocs配置文件是否存在
    mkdocs_config = project_root / "mkdocs.yml"
    if not mkdocs_config.exists():
        print("错误: 未找到 mkdocs.yml 配置文件")
        return False
    
    # 构建命令
    cmd = ["mkdocs", "serve", "--dev-addr", f"127.0.0.1:{port}"]
    if docs_dir:
        cmd.extend(["--config-file", docs_dir])
    
    print(f"正在启动文档服务器，地址: http://127.0.0.1:{port}")
    print("按 Ctrl+C 停止服务器")
    
    try:
        result = subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"启动文档服务器失败: {e}")
        return False
    except KeyboardInterrupt:
        print("\n文档服务器已停止")
        return True


def build_docs():
    """构建文档"""
    project_root = get_project_root()
    os.chdir(project_root)
    
    mkdocs_config = project_root / "mkdocs.yml"
    if not mkdocs_config.exists():
        print("错误: 未找到 mkdocs.yml 配置文件")
        return False
    
    print("正在构建文档...")
    try:
        result = subprocess.run(["mkdocs", "build"], check=True)
        print("文档构建成功！")
        print(f"输出目录: {project_root / 'site'}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"构建文档失败: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='启动个人笔记系统文档服务')
    parser.add_argument('action', nargs='?', default='serve', 
                       choices=['serve', 'build'], 
                       help='操作类型: serve(启动服务) 或 build(构建文档)')
    parser.add_argument('--port', type=int, default=8000, 
                       help='服务端口 (默认: 8000)')
    
    args = parser.parse_args()
    
    # 检查mkdocs是否已安装
    if not check_mkdocs_installed():
        print("mkdocs未安装，正在安装...")
        if not install_mkdocs():
            print("安装失败，请手动安装mkdocs相关包")
            sys.exit(1)
    
    if args.action == 'serve':
        start_docs_serve(port=args.port)
    elif args.action == 'build':
        build_docs()


if __name__ == "__main__":
    main()