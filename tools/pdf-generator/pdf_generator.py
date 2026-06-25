#!/usr/bin/env python3
"""
PDF生成工具
用于将CardPack Studio的卡包转换为PDF格式
"""

import json
import markdown
from jinja2 import Template
import os
import sys

def load_questions(json_file):
    """加载问题数据"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def generate_html(questions, template_file=None):
    """生成HTML内容"""
    if template_file and os.path.exists(template_file):
        with open(template_file, 'r', encoding='utf-8') as f:
            template_content = f.read()
        template = Template(template_content)
    else:
        # 使用默认模板
        template = Template(get_default_template())
    
    html_content = template.render(questions=questions)
    return html_content

def get_default_template():
    """默认HTML模板"""
    return """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body {
            font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .card {
            margin-bottom: 30px;
            padding: 25px;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            background: #fafafa;
        }
        .card-number {
            font-size: 14px;
            color: #666;
            margin-bottom: 10px;
        }
        .question {
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-bottom: 15px;
            line-height: 1.4;
        }
        .extension {
            font-size: 14px;
            color: #666;
            line-height: 1.5;
        }
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        .header h1 {
            color: #2c3e50;
            margin-bottom: 10px;
        }
        .header p {
            color: #7f8c8d;
            font-size: 16px;
        }
        @media print {
            body {
                background-color: white;
                margin: 0;
                padding: 0;
            }
            .container {
                box-shadow: none;
                margin: 0;
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{{ title }}</h1>
            <p>{{ subtitle }}</p>
        </div>
        {% for card in questions %}
        <div class="card">
            <div class="card-number">🎴 {{ card.id }}</div>
            <div class="question">{{ card.question }}</div>
            <div class="extension">{{ card.extension }}</div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
    """

def save_html(html_content, output_file):
    """保存HTML文件"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("使用方法: python pdf_generator.py <input_json> <output_html> [title] [subtitle]")
        sys.exit(1)
    
    input_json = sys.argv[1]
    output_html = sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else "CardPack Studio"
    subtitle = sys.argv[4] if len(sys.argv) > 4 else "知识卡片集合"
    
    # 加载数据
    questions = load_questions(input_json)
    
    # 生成HTML
    html_content = generate_html(questions, title=title, subtitle=subtitle)
    
    # 保存文件
    save_html(html_content, output_html)
    print(f"HTML文件已生成: {output_html}")

if __name__ == "__main__":
    main()