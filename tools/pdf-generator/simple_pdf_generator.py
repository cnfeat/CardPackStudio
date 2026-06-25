#!/usr/bin/env python3
"""
简单PDF生成工具
使用Python内置库生成PDF
"""

import json
import os
import sys
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.colors import black, blue
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def load_questions(json_file):
    """加载问题数据"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def generate_pdf(questions, output_file, title="AI创业决策卡包", subtitle="基于《创始人行动手册》的决策框架"):
    """生成PDF文件"""
    # 创建PDF文档
    doc = SimpleDocTemplate(output_file, pagesize=A4)
    story = []
    
    # 样式设置
    styles = getSampleStyleSheet()
    
    # 标题样式
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=blue,
        alignment=1  # 居中
    )
    
    # 副标题样式
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=20,
        textColor=black,
        alignment=1  # 居中
    )
    
    # 卡片标题样式
    card_title_style = ParagraphStyle(
        'CardTitle',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=10,
        textColor=blue,
        leftIndent=20
    )
    
    # 卡片内容样式
    card_content_style = ParagraphStyle(
        'CardContent',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=15,
        textColor=black,
        leftIndent=20,
        rightIndent=20,
        leading=16
    )
    
    # 添加标题
    story.append(Paragraph(title, title_style))
    story.append(Paragraph(subtitle, subtitle_style))
    story.append(Spacer(1, 20))
    
    # 添加卡片
    for card in questions:
        # 添加卡片编号
        card_number = f"🎴 {card['id']}"
        story.append(Paragraph(card_number, card_title_style))
        
        # 添加问题
        question = f"问题：{card['question']}"
        story.append(Paragraph(question, card_content_style))
        
        # 添加扩展层
        extension = f"思考：{card['extension']}"
        story.append(Paragraph(extension, card_content_style))
        
        # 添加间距
        story.append(Spacer(1, 10))
        
        # 如果不是最后一张卡片，添加分页符
        if card != questions[-1]:
            story.append(PageBreak())
    
    # 生成PDF
    doc.build(story)
    print(f"PDF文件已生成: {output_file}")

def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("使用方法: python simple_pdf_generator.py <input_json> <output_pdf> [title] [subtitle]")
        sys.exit(1)
    
    input_json = sys.argv[1]
    output_pdf = sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else "AI创业决策卡包"
    subtitle = sys.argv[4] if len(sys.argv) > 4 else "基于《创始人行动手册》的决策框架"
    
    # 加载数据
    questions = load_questions(input_json)
    
    # 生成PDF
    generate_pdf(questions, output_pdf, title, subtitle)

if __name__ == "__main__":
    main()