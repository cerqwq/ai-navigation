"""
AI Navigation - AI导航组件工具
支持导航设计、菜单、面包屑
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AINavigationTools:
    """
    AI导航组件工具
    支持：设计、菜单、面包屑
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_navigation(self, pages: List[Dict], style: str = "modern") -> Dict:
        """设计导航"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        pages_text = json.dumps(pages, ensure_ascii=False)

        prompt = f"""请设计{style}风格的导航：

页面：{pages_text}

请返回JSON格式：
{{
    "structure": "导航结构",
    "components": ["组件"],
    "responsive": "响应式方案",
    "animation": "动画效果"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"navigation": content}

    def generate_navbar(self, brand: str, links: List[Dict], framework: str = "react") -> str:
        """生成导航栏"""
        if not self.client:
            return "LLM客户端未配置"

        links_text = json.dumps(links, ensure_ascii=False)

        prompt = f"""请生成{framework}导航栏：

品牌：{brand}
链接：{links_text}

要求：
1. 响应式
2. 移动端菜单
3. 活跃状态
4. 可访问性"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_sidebar(self, menu_items: List[Dict], framework: str = "react") -> str:
        """生成侧边栏"""
        if not self.client:
            return "LLM客户端未配置"

        items_text = json.dumps(menu_items, ensure_ascii=False)

        prompt = f"""请生成{framework}侧边栏：

菜单项：{items_text}

要求：
1. 折叠展开
2. 多级菜单
3. 图标支持
4. 活跃状态"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_breadcrumbs(self, path: str, framework: str = "react") -> str:
        """生成面包屑"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{framework}面包屑组件：

路径：{path}

要求：
1. 结构化数据
2. 可访问性
3. 响应式
4. 分隔符自定义"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_tabs(self, tab_items: List[Dict], framework: str = "react") -> str:
        """生成标签页"""
        if not self.client:
            return "LLM客户端未配置"

        items_text = json.dumps(tab_items, ensure_ascii=False)

        prompt = f"""请生成{framework}标签页组件：

标签项：{items_text}

要求：
1. 动画切换
2. 键盘导航
3. 懒加载
4. 可访问性"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content

    def generate_pagination(self, total_pages: int, framework: str = "react") -> str:
        """生成分页"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{framework}分页组件：

总页数：{total_pages}

要求：
1. 页码导航
2. 上一页/下一页
3. 跳转输入
4. 响应式"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_stepper(self, steps: List[str], framework: str = "react") -> str:
        """生成步骤条"""
        if not self.client:
            return "LLM客户端未配置"

        steps_text = ", ".join(steps)

        prompt = f"""请生成{framework}步骤条组件：

步骤：{steps_text}

要求：
1. 进度显示
2. 点击导航
3. 状态标识
4. 响应式"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AINavigationTools:
    """创建导航工具"""
    return AINavigationTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Navigation Tools")
    print()

    # 测试
    nav = tools.design_navigation([{"name": "首页", "path": "/"}, {"name": "关于", "path": "/about"}])
    print(json.dumps(nav, ensure_ascii=False, indent=2))
