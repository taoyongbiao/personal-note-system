#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Personal Note System 安装和设置脚本
"""

import os
import sys
from pathlib import Path

def get_project_root():
    """获取项目根目录"""
    return Path(__file__).resolve().parent

def ensure_directory_exists(path):
    """确保目录存在，如果不存在则创建"""
    path = Path(path)
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        print(f"创建目录: {path}")

def check_python_version():
    """检查Python版本"""
    if sys.version_info < (3, 6):
        print("错误: 需要Python 3.6或更高版本")
        return False
    return True

def install_dependencies():
    """安装依赖包"""
    print("正在安装依赖包...")
    
    # 依赖列表（包括mkdocs相关包）
    dependencies = [
        "argparse==1.4.0",
        "openai>=1.0.0",
        "mkdocs>=1.4.0",
        "mkdocs-material>=9.0.0",
        "mkdocs-git-revision-date-localized-plugin>=1.0.0",
        "mkdocs-minify-plugin>=0.5.0",
        "mkdocs-macros-plugin>=0.7.0"
    ]
    
    for dep in dependencies:
        print(f"安装 {dep}...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", dep], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"安装 {dep} 失败: {result.stderr}")
            return False
        else:
            print(f"成功安装 {dep}")
    return True

def setup_project_structure():
    """设置项目目录结构"""
    project_root = get_project_root()
    
    # 确保必要的目录存在
    directories = [
        project_root / "daynote" / "model",
        project_root / "日报",
        project_root / "scripts",
        project_root / "docs",
        project_root / "docs" / "overview",
        project_root / "docs" / "getting-started",
        project_root / "docs" / "guides",
        project_root / "docs" / "configuration",
        project_root / "docs" / "development",
        project_root / "docs" / "tools",
        project_root / "docs" / "appendix"
    ]
    
    for directory in directories:
        ensure_directory_exists(directory)

def setup_vscode_tasks():
    """设置VS Code任务"""
    project_root = get_project_root()
    vscode_dir = project_root / ".vscode"
    
    ensure_directory_exists(vscode_dir)
    
    # 创建 tasks.json 文件（如果不存在）
    tasks_file = vscode_dir / "tasks.json"
    if not tasks_file.exists():
        tasks_config = {
            "version": "2.0.0",
            "tasks": [
                {
                    "label": "创建灵感笔记",
                    "type": "shell",
                    "command": "python",
                    "args": ["${workspaceFolder}/daynote/create_idea_note.py"],
                    "group": "none",
                    "presentation": {
                        "echo": True,
                        "reveal": "always",
                        "focus": False,
                        "panel": "shared"
                    }
                },
                {
                    "label": "创建日报",
                    "type": "shell",
                    "command": "python",
                    "args": ["${workspaceFolder}/daynote/create_daily_note.py"],
                    "group": "none",
                    "presentation": {
                        "echo": True,
                        "reveal": "always",
                        "focus": False,
                        "panel": "shared"
                    }
                },
                {
                    "label": "创建自定义笔记",
                    "type": "shell",
                    "command": "python",
                    "args": ["${workspaceFolder}/daynote/create_custom_note.py"],
                    "group": "none",
                    "presentation": {
                        "echo": True,
                        "reveal": "always",
                        "focus": False,
                        "panel": "shared"
                    }
                }
            ]
        }
        
        import json
        with open(tasks_file, 'w', encoding='utf-8') as f:
            json.dump(tasks_config, f, indent=4, ensure_ascii=False)
        print(f"已创建 {tasks_file}")

def create_mkdocs_config():
    """创建 MkDocs 配置文件"""
    project_root = get_project_root()
    mkdocs_config = project_root / "mkdocs.yml"
    
    if not mkdocs_config.exists():
        config_content = '''site_name: 个人笔记系统文档
site_url: https://example.com
site_author: Personal Note System
site_description: 个人知识管理与笔记系统

theme:
  name: material
  language: zh
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.indexes
    - navigation.top
  icon:
    logo: material/book-open-page-variant

nav:
  - 概述: 
    - overview/home.md
  - 入门指南:
    - getting-started/installation.md
    - getting-started/usage.md
  - 使用指南:
    - guides/daily-notes.md
    - guides/idea-notes.md
    - guides/custom-notes.md
  - 配置:
    - configuration/settings.md
  - 开发:
    - development/contributing.md
    - development/api.md
  - 工具:
    - tools/scripts.md
  - 附录:
    - appendix/glossary.md
    - appendix/changelog.md

plugins:
  - search
  - git-revision-date-localized:
      type: timeago
      fallback_to_build_date: true
  - minify:
      minify_html: true
  - macros

extra_css:
  - stylesheets/extra.css

markdown_extensions:
  - admonition
  - abbr
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - tables
  - pymdownx.arithmatex
  - pymdownx.betterem
  - pymdownx.caret
  - pymdownx.details
  - pymdownx.emoji
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.magiclink
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.superfences
  - pymdownx.tabbed
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.tilde
'''
        with open(mkdocs_config, 'w', encoding='utf-8') as f:
            f.write(config_content)
        print(f"已创建 {mkdocs_config}")

def create_docs_skeleton():
    """创建文档骨架文件"""
    project_root = get_project_root()
    
    # 创建基本的文档文件
    docs_files = {
        "docs/overview/home.md": "# 欢迎使用个人笔记系统\n\n这是一个帮助您提高生产力的个人笔记管理系统。",
        "docs/getting-started/installation.md": "# 安装指南\n\n## 系统要求\n\n- Python 3.6+\n- pip 包管理器",
        "docs/getting-started/usage.md": "# 使用方法\n\n## 快速开始\n\n介绍如何开始使用本系统。",
        "docs/guides/daily-notes.md": "# 日报指南\n\n如何创建和管理日报。",
        "docs/guides/idea-notes.md": "# 灵感笔记指南\n\n如何记录和整理灵感。",
        "docs/guides/custom-notes.md": "# 自定义笔记指南\n\n如何创建不同类型的笔记。",
        "docs/configuration/settings.md": "# 配置选项\n\n系统配置说明。",
        "docs/development/contributing.md": "# 贡献指南\n\n欢迎贡献代码！",
        "docs/development/api.md": "# API 文档\n\n系统API接口说明。",
        "docs/tools/scripts.md": "# 工具脚本\n\n可用的工具脚本说明。",
        "docs/appendix/glossary.md": "# 术语表\n\n常用术语解释。",
        "docs/appendix/changelog.md": "# 更新日志\n\n## v1.0.0\n\n- 初始版本"
    }
    
    for file_path, content in docs_files.items():
        filepath = project_root / file_path
        if not filepath.exists():
            ensure_directory_exists(filepath.parent)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"已创建 {filepath}")

def main():
    """主函数"""
    print("开始设置 Personal Note System...")
    
    # 检查Python版本
    if not check_python_version():
        sys.exit(1)
    
    # 设置项目结构
    setup_project_structure()
    
    # 安装依赖
    if not install_dependencies():
        sys.exit(1)
    
    # 设置VS Code任务
    setup_vscode_tasks()
    
    # 创建MkDocs配置文件
    create_mkdocs_config()
    
    # 创建文档骨架
    create_docs_skeleton()
    
    print("\n设置完成！")
    print("您可以执行以下操作：")
    print("1. 使用 Ctrl+Alt+I 快捷键创建灵感笔记")
    print("2. 使用 Ctrl+Alt+R 快捷键创建日报")
    print("3. 使用 Ctrl+Alt+C 快捷键创建自定义笔记")
    print("4. 运行 'mkdocs serve' 启动文档服务")
    print("5. 运行 'mkdocs build' 构建静态网站")
    print("6. 文档将在 docs/ 目录中，配置文件为 mkdocs.yml")

if __name__ == "__main__":
    main()