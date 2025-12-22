#!/usr/bin/env python3
import os
import sys
import shutil
from datetime import datetime
import argparse

def create_note(template_type="inspiration"):
    """根据模板类型创建笔记"""
    # 获取当前日期和时间
    date_str = datetime.now().strftime("%Y%m%d")
    time_str = datetime.now().strftime("%H%M%S")
    date_display = datetime.now().strftime("%Y-%m-%d")
    
    # 项目根路径
    root_path = r"c:\Users\P30015874206\Desktop\note"
    
    # 根据模板类型确定路径和文件名
    if template_type == "inspiration":
        template_path = os.path.join(root_path, "daynote", "model", "灵感.md")
        target_dir = os.path.join(root_path, "daynote", date_str)
        file_name = f"灵感-{time_str}.md"
    elif template_type == "report":
        template_path = os.path.join(root_path, "daynote", "model", "日报.md")
        target_dir = os.path.join(root_path, "日报")
        file_name = f"日报-{date_display}.md"
    else:
        # 支持自定义模板
        template_path = os.path.join(root_path, "daynote", "model", f"{template_type}.md")
        target_dir = os.path.join(root_path, "daynote", date_str)
        file_name = f"{template_type}-{time_str}.md"
        
        # 如果自定义模板不存在，则创建一个基本模板
        if not os.path.exists(template_path):
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(f"# {template_type} - {{date}}\n\n")
                f.write("## 🎯 目标\n\n")
                f.write("## 📚 调研内容\n\n")
                f.write("## 💡 发现\n\n")
                f.write("## ⚠️ 问题\n\n")
                f.write("## ✅ 解决方案\n\n")
                f.write("## 📝 总结\n\n")
            print(f"已创建新的模板文件: {template_path}")
    
    # 创建目标目录（如果不存在）
    os.makedirs(target_dir, exist_ok=True)
    
    # 复制模板文件
    target_path = os.path.join(target_dir, file_name)
    
    # 如果目标文件已存在，则添加序号
    counter = 1
    original_target_path = target_path
    while os.path.exists(target_path):
        name, ext = os.path.splitext(original_target_path)
        target_path = f"{name}_{counter}{ext}"
        counter += 1
    
    # 复制模板文件
    if os.path.exists(template_path):
        shutil.copy2(template_path, target_path)
        
        # 读取并替换日期占位符
        with open(target_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = content.replace("{date}", date_display)
        
        with open(target_path, 'w', encoding='utf-8') as file:
            file.write(content)
            
        print(f"已创建笔记: {target_path}")
        return target_path
    else:
        # 如果模板不存在，创建一个基本文件
        with open(target_path, 'w', encoding='utf-8') as file:
            file.write(f"# {template_type.capitalize()} - {date_display}\n\n")
        print(f"模板不存在，已创建基本文件: {target_path}")
        return target_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="根据模板创建笔记")
    parser.add_argument("--template", "-t", default="inspiration", 
                        help="模板类型: inspiration(灵感), report(日报), 或自定义")
    
    args = parser.parse_args()
    
    created_file = create_note(args.template)