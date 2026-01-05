"""
mkdocs-gen-files插件脚本
用于动态生成导航结构和页面内容
"""

import os
from pathlib import Path
import mkdocs_gen_files

# 项目根目录
project_root = Path(__file__).parent.parent
docs_dir = project_root / "docs"

# 生成笔记索引页面
def generate_note_index():
    # 获取所有笔记文件
    note_dirs = [d for d in (project_root / "daynote").iterdir() if d.is_dir() and d.name != "model"]
    
    if not note_dirs:
        # 创建一个空的note_index.md文件
        with mkdocs_gen_files.open('note_index.md', 'w', encoding='utf-8') as f:
            f.write("# 笔记索引\n\n当前没有可用的笔记。")
        return

    # 创建笔记索引内容
    index_content = f"""# 笔记索引

这是自动生成的笔记索引页面，包含了所有日期的笔记。

## 笔记列表

"""
    
    # 按日期倒序排列
    note_dirs = sorted(note_dirs, key=lambda x: x.name, reverse=True)
    
    for note_dir in note_dirs:
        index_content += f"### {note_dir.name}\n\n"
        for note_file in note_dir.glob("*.md"):
            # 获取文件标题（第一行）
            with open(note_file, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
                title = first_line[2:].strip() if first_line.startswith('# ') else note_file.stem
            # 创建一个副本到docs目录，以便mkdocs可以正确链接
            relative_path = note_file.relative_to(project_root)
            docs_copy_path = docs_dir / "notes" / note_dir.name / note_file.name
            docs_copy_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 复制文件内容并确保正确的链接
            with open(note_file, 'r', encoding='utf-8') as src:
                content = src.read()
            with mkdocs_gen_files.open(f"notes/{note_dir.name}/{note_file.name}", 'w', encoding='utf-8') as dest:
                dest.write(content)
                
            index_content += f"- [{title}](notes/{note_dir.name}/{note_file.name})\n"
        index_content += "\n"
    
    # 写入到docs目录下的note_index.md
    with mkdocs_gen_files.open('note_index.md', 'w', encoding='utf-8') as f:
        f.write(index_content)

# 生成任务索引页面
def generate_task_index():
    task_file = project_root / "task.md"
    if not task_file.exists():
        with mkdocs_gen_files.open('task_index.md', 'w', encoding='utf-8') as f:
            f.write("# 任务索引\n\n当前没有可用的任务文件。")
        return
    
    # 读取任务文件内容
    with open(task_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 创建任务索引内容
    index_content = f"""# 任务索引

这是自动生成的任务索引页面。

{content}
"""
    
    # 创建一个副本到docs目录
    docs_copy_path = docs_dir / "task.md"
    with mkdocs_gen_files.open("task.md", 'w', encoding='utf-8') as dest:
        dest.write(content)
    
    # 写入到docs目录下的task_index.md
    with mkdocs_gen_files.open('task_index.md', 'w', encoding='utf-8') as f:
        f.write(index_content)

# 生成日报索引页面
def generate_daily_report_index():
    daily_reports = list((project_root / "日报").glob("*.md"))
    
    if not daily_reports:
        with mkdocs_gen_files.open('daily_report_index.md', 'w', encoding='utf-8') as f:
            f.write("# 日报索引\n\n当前没有可用的日报。")
        return

    # 创建日报索引内容
    index_content = f"""# 日报索引

这是自动生成的日报索引页面。

## 日报列表

"""
    
    # 按文件名倒序排列
    daily_reports = sorted(daily_reports, key=lambda x: x.name, reverse=True)
    
    for report_file in daily_reports:
        # 获取文件标题（第一行）
        with open(report_file, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            title = first_line[2:].strip() if first_line.startswith('# ') else report_file.stem
        
        # 创建一个副本到docs目录
        docs_copy_path = docs_dir / "reports" / report_file.name
        docs_copy_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 复制文件内容
        with open(report_file, 'r', encoding='utf-8') as src:
            content = src.read()
        with mkdocs_gen_files.open(f"reports/{report_file.name}", 'w', encoding='utf-8') as dest:
            dest.write(content)
            
        index_content += f"- [{title}](reports/{report_file.name})\n"
    
    # 写入到docs目录下的daily_report_index.md
    with mkdocs_gen_files.open('daily_report_index.md', 'w', encoding='utf-8') as f:
        f.write(index_content)

# 主函数
def main():
    # 确保子目录存在
    (docs_dir / "notes").mkdir(parents=True, exist_ok=True)
    (docs_dir / "reports").mkdir(parents=True, exist_ok=True)
    
    # 生成各个索引页面
    generate_note_index()
    generate_task_index()
    generate_daily_report_index()

# 仅当作为mkdocs-gen-files脚本执行时运行
if __name__ != '__main__':
    main()