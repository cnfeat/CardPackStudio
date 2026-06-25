#!/usr/bin/env python3
"""
插件适配工具
用于将CardPack Studio的卡包适配为日课一问插件格式
"""

import json
import os
import sys
from datetime import datetime

def load_questions(json_file):
    """加载问题数据"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def validate_card_structure(card):
    """验证卡片结构"""
    required_fields = ['id', 'question', 'extension']
    for field in required_fields:
        if field not in card:
            return False, f"缺少必需字段: {field}"
    
    # 检查问题长度
    if len(card['question']) > 50:
        return False, f"问题层过长（超过50字）: {card['question']}"
    
    # 检查扩展层
    if len(card['extension']) > 150:
        return False, f"扩展层过长（超过150字）: {card['extension']}"
    
    return True, "验证通过"

def generate_plugin_json(questions, output_file):
    """生成插件格式JSON"""
    plugin_data = {
        "_instructions": {
            "说明": "「AI创业·日课」测试题库。按最新设定生成。",
            "四层结构": {
                "question": "问题层：独立完整的核心问题，约35字",
                "extension": "扩展层：3个小问连续不分行，约100字"
            },
            "生成时间": datetime.now().isoformat(),
            "来源": "CardPack Studio",
            "版本": "1.0.0"
        },
        "questions": []
    }
    
    for card in questions:
        # 验证卡片
        is_valid, message = validate_card_structure(card)
        if not is_valid:
            print(f"警告: 卡片 {card.get('id', 'unknown')} 验证失败: {message}")
            continue
        
        # 构建插件格式卡片
        plugin_card = {
            "id": card['id'],
            "question": card['question'],
            "extension": card['extension'],
            "domain": card.get('domain', '综合'),
            "dimension": card.get('dimension', ['思维']),
            "depth": card.get('depth', 2)
        }
        
        plugin_data['questions'].append(plugin_card)
    
    # 保存文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(plugin_data, f, ensure_ascii=False, indent=2)
    
    return len(plugin_data['questions'])

def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("使用方法: python plugin_adapter.py <input_json> <output_json>")
        sys.exit(1)
    
    input_json = sys.argv[1]
    output_json = sys.argv[2]
    
    # 加载数据
    questions = load_questions(input_json)
    
    # 生成插件格式
    valid_count = generate_plugin_json(questions, output_json)
    
    print(f"插件格式JSON已生成: {output_json}")
    print(f"有效卡片数量: {valid_count}")
    print(f"总卡片数量: {len(questions)}")

if __name__ == "__main__":
    main()