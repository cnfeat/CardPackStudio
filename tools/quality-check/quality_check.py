#!/usr/bin/env python3
"""
质量检查工具
用于检查CardPack Studio卡包的质量和规范性
"""

import json
import re
import os
import sys
from typing import List, Dict, Tuple

class QualityChecker:
    """质量检查器"""
    
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.passed = []
    
    def check_card_structure(self, card: Dict) -> bool:
        """检查卡片结构"""
        required_fields = ['id', 'question', 'extension']
        for field in required_fields:
            if field not in card:
                self.issues.append(f"卡片 {card.get('id', 'unknown')} 缺少必需字段: {field}")
                return False
        return True
    
    def check_question_length(self, card: Dict) -> bool:
        """检查问题长度"""
        question = card.get('question', '')
        if len(question) == 0:
            self.issues.append(f"卡片 {card.get('id', 'unknown')} 问题为空")
            return False
        
        if len(question) > 50:
            self.warnings.append(f"卡片 {card.get('id', 'unknown')} 问题过长（{len(question)}字）")
        
        if len(question) < 20:
            self.warnings.append(f"卡片 {card.get('id', 'unknown')} 问题过短（{len(question)}字）")
        
        return True
    
    def check_extension_length(self, card: Dict) -> bool:
        """检查扩展层长度"""
        extension = card.get('extension', '')
        if len(extension) == 0:
            self.issues.append(f"卡片 {card.get('id', 'unknown')} 扩展层为空")
            return False
        
        if len(extension) > 150:
            self.warnings.append(f"卡片 {card.get('id', 'unknown')} 扩展层过长（{len(extension)}字）")
        
        if len(extension) < 80:
            self.warnings.append(f"卡片 {card.get('id', 'unknown')} 扩展层过短（{len(extension)}字）")
        
        return True
    
    def check_extension_format(self, card: Dict) -> bool:
        """检查扩展层格式"""
        extension = card.get('extension', '')
        
        # 检查是否包含3个问题
        question_count = len(re.findall(r'[？?]', extension))
        if question_count < 3:
            self.warnings.append(f"卡片 {card.get('id', 'unknown')} 扩展层问题数量不足（{question_count}个）")
        
        # 检查是否包含列表符号
        if re.search(r'^[\s]*- ', extension, re.MULTILINE):
            self.issues.append(f"卡片 {card.get('id', 'unknown')} 扩展层包含列表符号")
        
        return True
    
    def check_id_format(self, card: Dict) -> bool:
        """检查ID格式"""
        card_id = card.get('id', '')
        if not re.match(r'^\d{3}$', card_id):
            self.issues.append(f"卡片 {card_id} ID格式错误，应为3位数字")
            return False
        return True
    
    def check_duplicate_ids(self, questions: List[Dict]) -> bool:
        """检查重复ID"""
        ids = [q.get('id', '') for q in questions]
        duplicate_ids = []
        seen = set()
        
        for card_id in ids:
            if card_id in seen:
                duplicate_ids.append(card_id)
            else:
                seen.add(card_id)
        
        if duplicate_ids:
            self.issues.append(f"发现重复ID: {', '.join(duplicate_ids)}")
            return False
        
        return True
    
    def check_content_quality(self, card: Dict) -> bool:
        """检查内容质量"""
        question = card.get('question', '')
        extension = card.get('extension', '')
        
        # 检查是否包含敏感词
        sensitive_words = ['测试', '示例', 'demo', 'test']
        for word in sensitive_words:
            if word in question.lower() or word in extension.lower():
                self.warnings.append(f"卡片 {card.get('id', 'unknown')} 包含测试词汇: {word}")
        
        # 检查是否包含HTML标签
        if re.search(r'<[^>]+>', question) or re.search(r'<[^>]+>', extension):
            self.issues.append(f"卡片 {card.get('id', 'unknown')} 包含HTML标签")
        
        return True
    
    def check_metadata(self, card: Dict) -> bool:
        """检查元数据"""
        if 'domain' not in card:
            self.warnings.append(f"卡片 {card.get('id', 'unknown')} 缺少domain字段")
        
        if 'dimension' not in card:
            self.warnings.append(f"卡片 {card.get('id', 'unknown')} 缺少dimension字段")
        
        if 'depth' not in card:
            self.warnings.append(f"卡片 {card.get('id', 'unknown')} 缺少depth字段")
        
        return True
    
    def check_file_structure(self, json_file: str) -> bool:
        """检查文件结构"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 检查是否是列表格式
            if not isinstance(data, list):
                self.issues.append("文件格式错误：应为JSON数组")
                return False
            
            return True
        
        except json.JSONDecodeError as e:
            self.issues.append(f"JSON解析错误: {e}")
            return False
        except Exception as e:
            self.issues.append(f"文件读取错误: {e}")
            return False
    
    def run_checks(self, json_file: str) -> Tuple[int, int, int]:
        """运行所有检查"""
        self.issues.clear()
        self.warnings.clear()
        self.passed.clear()
        
        # 检查文件结构
        if not self.check_file_structure(json_file):
            return len(self.issues), len(self.warnings), len(self.passed)
        
        # 加载数据
        with open(json_file, 'r', encoding='utf-8') as f:
            questions = json.load(f)
        
        # 检查重复ID
        self.check_duplicate_ids(questions)
        
        # 检查每个卡片
        for card in questions:
            card_id = card.get('id', 'unknown')
            
            checks = [
                self.check_card_structure(card),
                self.check_id_format(card),
                self.check_question_length(card),
                self.check_extension_length(card),
                self.check_extension_format(card),
                self.check_content_quality(card),
                self.check_metadata(card)
            ]
            
            if all(checks):
                self.passed.append(card_id)
        
        return len(self.issues), len(self.warnings), len(self.passed)
    
    def generate_report(self) -> str:
        """生成检查报告"""
        report = []
        report.append("=== 质量检查报告 ===")
        report.append(f"总检查数量: {len(self.passed) + len(self.warnings) + len(self.issues)}")
        report.append(f"通过检查: {len(self.passed)}")
        report.append(f"警告: {len(self.warnings)}")
        report.append(f"错误: {len(self.issues)}")
        report.append("")
        
        if self.issues:
            report.append("❌ 错误:")
            for issue in self.issues:
                report.append(f"  - {issue}")
            report.append("")
        
        if self.warnings:
            report.append("⚠️ 警告:")
            for warning in self.warnings:
                report.append(f"  - {warning}")
            report.append("")
        
        if self.passed:
            report.append("✅ 通过:")
            for passed_id in self.passed[:10]:  # 只显示前10个
                report.append(f"  - {passed_id}")
            if len(self.passed) > 10:
                report.append(f"  ... 还有 {len(self.passed) - 10} 个通过")
        
        return "\n".join(report)

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("使用方法: python quality_check.py <json_file>")
        sys.exit(1)
    
    json_file = sys.argv[1]
    
    if not os.path.exists(json_file):
        print(f"文件不存在: {json_file}")
        sys.exit(1)
    
    checker = QualityChecker()
    issues, warnings, passed = checker.run_checks(json_file)
    
    print(checker.generate_report())
    
    # 根据检查结果设置退出码
    if issues > 0:
        sys.exit(2)  # 有错误
    elif warnings > 0:
        sys.exit(1)  # 有警告
    else:
        sys.exit(0)  # 全部通过

if __name__ == "__main__":
    main()