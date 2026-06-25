# 日课一问插件仓库关联

## 📋 仓库说明

CardPack Studio 与日课一问插件仓库相互关联，形成完整的卡片生态系统。

## 🔗 仓库关联

### CardPack Studio (内容仓库)
- **地址**: https://github.com/cnfeat/CardPackStudio
- **功能**: 卡包内容创作和管理平台
- **输出**: 各种类型的卡包JSON文件

### 日课一问插件 (应用仓库)
- **地址**: https://github.com/cnfeat/DailyQApk
- **功能**: 卡片展示和应用的Chrome插件
- **输入**: CardPackStudio生成的JSON卡包文件

## 🔄 工作流程

### 1. 内容创作 (CardPack Studio)
```bash
# 在CardPack Studio中创作卡包
cd CardPackStudio
# 创作、编辑、审核卡包内容
# 生成JSON格式的卡包文件
```

### 2. 插件应用 (日课一问)
```bash
# 将JSON文件导入日课一问插件
# 在浏览器中使用卡包
# 日常决策思考
```

### 3. 反馈优化 (双向)
```bash
# 插件使用反馈 → 内容优化
# 内容创作需求 → 插件功能升级
```

## 📦 卡包格式

### CardPack Studio 输出格式
```json
{
  "id": "001",
  "question": "在AI时代，创业成功的关键到底变成了什么？",
  "extension": "你个人觉得，自己现在最需要提升的能力是什么？...",
  "domain": "事业与财富",
  "dimension": ["行动决策"],
  "depth": 2
}
```

### 日课一问插件支持格式
- 兼容CardPack Studio的JSON格式
- 支持双层结构（问题层 + 扩展层）
- 支持多维度标签分类

## 🚀 未来发展

### 短期目标
- ✅ 基础格式兼容
- 🔄 用户反馈收集
- 🔄 功能优化迭代

### 中期目标
- 🔄 自动同步机制
- 🔄 推荐算法集成
- 🔄 社区功能扩展

### 长期目标
- 🔄 生态系统完善
- 🔄 多平台支持
- 🔄 商业化运营

## 📞 技术支持

### 开发者
- **CardPack Studio**: cnfeat
- **日课一问插件**: cnfeat

### 联系方式
- **GitHub**: https://github.com/cnfeat
- **邮箱**: cnfeat@example.com
- **个人网站**: https://www.cnfeat.com

## 🎯 使用建议

### 对于内容创作者
1. 在CardPack Studio中创作卡包
2. 使用质量检查工具确保质量
3. 生成JSON文件供插件使用
4. 收集用户反馈优化内容

### 对于插件用户
1. 从CardPack Studio下载卡包JSON文件
2. 导入日课一问插件
3. 日常使用进行决策思考
4. 提供反馈帮助内容优化

---

**仓库关联说明** - 让内容创作和应用无缝衔接 🚀