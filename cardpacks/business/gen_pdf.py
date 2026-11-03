# -*- coding: utf-8 -*-
"""生成 A6 版 + A4 横版打印 PDF"""
import os
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(BASE, "创业与商业模式决策卡包-完整版300卡.html")
url = "file:///" + html_path.replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    page.wait_for_timeout(800)

    # A6 版（使用 CSS @page A6）
    page.pdf(
        path=os.path.join(BASE, "创业与商业模式决策卡包-完整版300卡.pdf"),
        prefer_css_page_size=True,
        print_background=True,
    )
    print("A6 PDF done")

    # A4 横版打印版
    page.pdf(
        path=os.path.join(BASE, "创业与商业模式决策卡包-完整版300卡-A4横版打印.pdf"),
        format="A4",
        landscape=True,
        print_background=True,
    )
    print("A4 landscape PDF done")

    browser.close()
print("All PDFs generated.")
