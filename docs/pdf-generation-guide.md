# PDF生成说明

## 📋 概述

本文档说明如何为CardPack Studio的卡包生成PDF文件。

## 🛠️ 生成方法

### 方法一：使用HTML文件（推荐）

1. **生成HTML文件**
```bash
cd CardPackStudio
python tools/pdf-generator/pdf_generator.py cardpacks/ai-decision/questions.json AI创业决策卡包.html "AI创业决策卡包" "基于《创始人行动手册》的决策框架"
```

2. **转换为PDF**
可以使用以下工具将HTML转换为PDF：

#### Chrome浏览器打印（简单）
- 打开HTML文件
- 按 `Ctrl+P` 打印
- 选择"另存为PDF"
- 调整页面设置

#### VS Code插件（推荐）
- 安装 "PDF Export" 插件
- 右键HTML文件，选择 "Export PDF"

#### 在线转换工具
- 使用在线HTML转PDF工具
- 例如：https://www.sejda.com/html-to-pdf

### 方法二：安装专业工具

#### 安装wkhtmltopdf（Windows）
```bash
# 使用winget安装
winget install wkhtmltopdf

# 或手动下载安装
# https://wkhtmltopdf.org/downloads.html
```

#### 使用wkhtmltopdf转换
```bash
wkhtmltopdf AI创业决策卡包.html AI创业决策卡包.pdf
```

#### 安装weasyprint（Python）
```bash
pip install weasyprint
python -c "from weasyprint import HTML; HTML('AI创业决策卡包.html').write_pdf('AI创业决策卡包.pdf')"
```

## 📁 文件结构

```
CardPackStudio/
├── cardpacks/ai-decision/
│   ├── questions.json          # 卡包数据
│   └── README.md              # 卡包说明
├── AI创业决策卡包.html         # 生成的HTML文件
├── AI创业决策卡包.pdf          # 生成的PDF文件
└── tools/pdf-generator/
    └── pdf_generator.py      # PDF生成工具
```

## 🎨 样式说明

生成的HTML文件包含以下样式：

- **响应式设计**：适配不同屏幕尺寸
- **打印优化**：针对打印进行样式优化
- **美观排版**：专业的卡片布局和样式
- **中文支持**：完整的中文字体支持

## 🔧 自定义样式

如果需要自定义PDF样式，可以修改 `tools/pdf-generator/pdf_generator.py` 文件中的 `get_default_template()` 函数。

## 📞 技术支持

如有问题，请：
1. 查看 [README.md](README.md)
2. 提交 [GitHub Issue](https://github.com/cnfeat/CardPackStudio/issues)
3. 联系作者：cnfeat@example.com

---

**PDF生成说明** - 让知识分享更简单 🚀