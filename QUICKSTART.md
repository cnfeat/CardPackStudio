# 快速开始指南

## 🎯 项目概述

CardPack Studio 是一个开放卡片创作平台，旨在为终身学习者提供结构化的知识管理工具。

## 📦 安装和使用

### 1. 克隆仓库
```bash
git clone https://github.com/cnfeat/CardPackStudio.git
cd CardPackStudio
```

### 2. 探索卡包
```bash
cd cardpacks/ai-decision
# 查看 AI 创业决策卡包
```

### 3. 使用工具

#### PDF生成工具
```bash
cd tools/pdf-generator
python pdf_generator.py ../cardpacks/ai-decision/questions.json output.html "AI创业决策卡包" "基于《创始人行动手册》的决策框架"
```

#### 插件适配工具
```bash
cd tools/plugin-adapter
python plugin_adapter.py ../cardpacks/ai-decision/questions.json output.json
```

#### 质量检查工具
```bash
cd tools/quality-check
python quality_check.py ../cardpacks/ai-decision/questions.json
```

## 🚀 下一步

1. **阅读文档**：
   - [卡片创作指南](docs/creation-guide/creation-guide.md)
   - [贡献指南](CONTRIBUTING.md)

2. **参与贡献**：
   - 提交新的卡包
   - 改进现有工具
   - 完善文档

3. **社区交流**：
   - GitHub Discussions
   - Issues 反馈
   - 邮件联系

## 📞 联系方式

- **GitHub**: https://github.com/cnfeat/CardPackStudio
- **作者**: cnfeat
- **邮箱**: cnfeat@example.com
- **个人网站**: https://www.cnfeat.com

---

**CardPack Studio** - 让知识创作和分享更简单 🚀