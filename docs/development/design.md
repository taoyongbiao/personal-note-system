# 设计文档

## 项目概述

### 项目目标
个人笔记系统是一个基于VSCode的笔记管理工具，旨在帮助用户高效记录日常工作、自动生成日报以及评估工作状态。系统通过模板化笔记创建、AI驱动的笔记评价等功能，提升个人知识管理效率。

### 核心功能
- 自动创建日期目录
- 模板化笔记创建
- 快捷键操作
- AI驱动的笔记汇总与评价
- 主线任务检查机制

## 系统架构

### C4组件图

```mermaid
graph TB
    subgraph "用户界面层"
        A[用户]
    end
    
    subgraph "配置管理层"
        B[VSCode Tasks]
        C[VSCode Keybindings]
    end
    
    subgraph "核心功能层"
        D[create_note.py]
        E[summarize_notes.py]
        F[main_check.py]
        G[start_docs.py]
    end
    
    subgraph "数据存储层"
        H[daynote/*]
        I[日报/*]
        J[docs/*]
        K[model/*.md]
    end
    
    subgraph "外部服务"
        L[AI服务 - OpenAI API]
    end
    
    A --> B
    A --> C
    B --> D
    B --> E
    B --> F
    B --> G
    D --> K
    D --> H
    E --> H
    E --> I
    E --> L
    F --> H
    G --> J
</mermaid>

### 容器图

```mermaid
graph TB
    subgraph "个人笔记系统"
        A[VSCode界面]
        B[快捷键]
        C[命令面板]
        
        subgraph "脚本组件"
            D[create_note.py - 笔记创建]
            E[summarize_notes.py - AI分析]
            F[main_check.py - 任务检查]
            G[start_docs.py - 文档服务]
        end
        
        subgraph "存储组件"
            H[daynote/* - 笔记存储]
            I[日报/* - 报告存储]
            J[docs/* - 文档源码]
            K[model/*.md - 模板文件]
        end
    end
    
    L[AI服务 - OpenAI API]
    M[VSCode环境]
    
    A --> B
    A --> C
    B --> D
    C --> D
    C --> E
    C --> F
    C --> G
    D --> K
    D --> H
    E --> H
    E --> I
    E --> L
    G --> J
    F --> H
    M --> A
    M --> B
</mermaid>

## 组件设计

### create_note.py 组件

#### 功能
- 根据模板创建笔记文件
- 自动创建日期目录
- 生成带时间戳的文件名
- 替换模板中的日期占位符

#### 主要函数
- `get_project_root()` - 查找项目根目录
- [create_note(template_name)](file://c:\Users\P30015874206\Desktop\note\scripts\create_note.py#L18-L89) - 创建笔记的主要逻辑
- `get_current_time_str()` - 获取当前时间字符串

#### 输入输出
- 输入：模板名称
- 输出：创建的笔记文件路径

### summarize_notes.py 组件

#### 功能
- 扫描当日笔记
- 调用AI API进行分析
- 生成评价报告

#### 主要函数
- `get_today_notes()` - 获取当日笔记
- `summarize_with_ai()` - 使用AI总结笔记
- `save_summary()` - 保存总结报告

#### 输入输出
- 输入：笔记内容
- 输出：评价报告

### main_check.py 组件

#### 功能
- 检查任务状态
- 更新任务进度
- 生成任务报告

#### 主要函数
- `check_main_tasks()` - 检查主线任务
- `update_task_status()` - 更新任务状态

### start_docs.py 组件

#### 功能
- 启动mkdocs文档服务
- 构建文档网站

#### 主要函数
- `start_docs_serve()` - 启动文档服务
- `build_docs()` - 构建文档网站
- `check_mkdocs_installed()` - 检查mkdocs是否已安装

## 数据流

### 笔记创建流程
1. 用户触发创建笔记操作（快捷键或命令面板）
2. VSCode执行相应任务
3. [create_note.py](file://c:\Users\P30015874206\Desktop\note\scripts\create_note.py) 脚本运行
4. 读取指定模板
5. 创建日期目录（如不存在）
6. 生成带时间戳的文件名
7. 替换模板中的日期占位符
8. 保存笔记文件

### AI评价流程
1. 用户运行AI评价脚本
2. 脚本扫描当日笔记
3. 将笔记内容发送到AI API
4. 接收AI分析结果
5. 生成评价报告
6. 保存报告到指定位置

### 文档服务流程
1. 用户运行文档启动脚本
2. 检查mkdocs相关依赖是否安装
3. 启动mkdocs服务
4. 在指定端口提供文档网站访问

## 扩展性设计

### 模板扩展
- 通过添加新模板文件扩展笔记类型
- 无需修改核心代码

### 功能扩展
- 通过添加新Python脚本扩展功能
- 在VSCode配置中添加相应任务和快捷键

### AI服务扩展
- 支持不同的AI服务提供商
- 可配置的AI参数和选项

### 文档系统扩展
- 通过添加新的文档文件扩展文档内容
- 利用mkdocs插件系统扩展功能