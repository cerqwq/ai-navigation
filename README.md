# 🧭 AI Navigation

AI导航组件工具，支持导航设计、菜单、面包屑。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🧭 导航设计
- 📱 导航栏生成
- 📂 侧边栏生成
- 🍞 面包屑生成
- 📑 标签页生成
- 📄 分页生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_navigation import create_tools

tools = create_tools()

# 导航设计
nav = tools.design_navigation(pages, "modern")

# 导航栏
navbar = tools.generate_navbar("MyApp", links, "react")

# 侧边栏
sidebar = tools.generate_sidebar(menu_items, "react")

# 面包屑
breadcrumbs = tools.generate_breadcrumbs("/products/123", "react")

# 标签页
tabs = tools.generate_tabs(tab_items, "react")

# 分页
pagination = tools.generate_pagination(100, "react")

# 步骤条
stepper = tools.generate_stepper(["填写信息", "确认", "完成"], "react")
```

## 📁 项目结构

```
ai-navigation/
├── tools.py       # 导航工具核心
└── README.md
```

## 📄 许可证

MIT License
