# -*- coding: utf-8 -*-
"""创业与商业模式决策卡包 · 生成脚本"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

CSS = """
  @page { size: A6; margin: 0; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: "Microsoft YaHei","PingFang SC","Hiragino Sans GB",sans-serif;
    background: #e8e5e0;
    color: #1a1a1a;
  }
  .page {
    width: 105mm;
    height: 148mm;
    margin: 16px auto;
    position: relative;
    overflow: hidden;
    background: #ffffff;
    border: 1.5px solid #4338CA;
  }
  .page::before {
    content: '';
    position: absolute;
    top: -1.5px; left: -1.5px; right: -1.5px;
    height: 4px;
    background: #4338CA;
    z-index: 1;
  }
  @media print {
    body { background: white; }
    .page {
      box-shadow: none;
      margin: 0;
      width: 100%;
      height: 148mm;
      page-break-after: always;
      overflow: hidden;
    }
    .page:last-child { page-break-after: avoid; }
    .page::before { display: none; }
  }

  .cover {
    background: #EEF2FF;
    display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;
    padding: 10mm;
  }
  .cover .tag {
    font-size: 8pt; color: #312E81; background: #E0E7FF;
    padding: 4px 18px; border-radius: 14px; letter-spacing: 5px; margin-bottom: 18px;
  }
  .cover h1 { font-size: 20pt; font-weight: bold; color: #1a1a1a; line-height: 1.4; margin-bottom: 6px; }
  .cover .sub { font-size: 10pt; color: #5c5852; margin-bottom: 24px; }
  .cover .meta { font-size: 8.5pt; color: #5c5852; line-height: 2.2; }
  .cover .studio { position: absolute; bottom: 8mm; font-size: 7pt; color: #b0aba5; letter-spacing: 3px; }

  .txt { padding: 10mm 9mm; display: flex; flex-direction: column; }
  .txt .bq { font-size: 14pt; font-weight: bold; color: #1a1a1a; line-height: 1.8; margin-bottom: 8px; }
  .txt .bt { font-size: 9.5pt; color: #5c5852; line-height: 2; margin-bottom: 3px; }
  .txt .dv { width: 14mm; border-top: 1px solid #4338CA; margin: 8px 0; }
  .txt .rl { display: flex; gap: 8px; margin-bottom: 6px; font-size: 8.5pt; line-height: 1.8; }
  .txt .rn { flex-shrink: 0; font-family: Georgia,serif; font-size: 12pt; color: #4338CA; width: 18px; text-align: center; }
  .txt .rt { color: #5c5852; }
  .txt .ft { margin-top: auto; font-size: 7pt; color: #b0aba5; text-align: center; letter-spacing: 3px; padding-top: 8px; }

  .intro-page { padding: 11mm 9mm; display: flex; flex-direction: column; }
  .intro-page .hd { font-size: 15pt; font-weight: bold; color: #1a1a1a; line-height: 1.7; margin-bottom: 10mm; }
  .intro-page .bt { font-size: 9.5pt; color: #5c5852; line-height: 2.2; margin-bottom: 2px; }
  .intro-page .dv { width: 14mm; border-top: 1px solid #4338CA; margin: 6mm 0; }
  .intro-page .pull { font-size: 11pt; font-weight: 500; color: #1a1a1a; line-height: 1.9; padding: 0 0 0 6px; border-left: 2px solid #4338CA; margin-bottom: 6mm; }
  .intro-page .soft { font-size: 8pt; color: #C7D2FE; font-style: italic; margin-top: auto; text-align: center; }
  .intro-page .ft { font-size: 7pt; color: #b0aba5; text-align: center; letter-spacing: 3px; padding-top: 6px; }

  .end-page { padding: 11mm 9mm; display: flex; flex-direction: column; justify-content: center; }
  .end-page h3 { font-size: 15pt; font-weight: bold; color: #1a1a1a; line-height: 1.7; margin-bottom: 6mm; }
  .end-page .bt { font-size: 9.5pt; color: #5c5852; line-height: 2.2; margin-bottom: 2px; }
  .end-page .dv { width: 14mm; border-top: 1px solid #4338CA; margin: 5mm 0; }
  .end-page .pull { font-size: 10pt; font-weight: 500; color: #1a1a1a; line-height: 1.9; padding-left: 8px; border-left: 2px solid #4338CA; margin: 5mm 0; }
  .end-page .close { font-size: 9pt; color: #5c5852; font-style: italic; line-height: 1.8; margin-top: 8mm; }
  .end-page .ft { font-size: 7pt; color: #b0aba5; text-align: center; letter-spacing: 3px; margin-top: 8mm; }

  .ch { display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 10mm; background: #EEF2FF; }
  .ch .ci { font-family: Georgia,serif; font-size: 9pt; color: #4338CA; letter-spacing: 4px; margin-bottom: 20px; }
  .ch .ct { font-size: 20pt; font-weight: bold; color: #1a1a1a; margin-bottom: 8px; }
  .ch .cd { font-size: 9pt; color: #5c5852; line-height: 2; max-width: 80%; }
  .ch .cc { color: #4338CA; font-size: 10pt; opacity: 0.4; margin: 14px 0; }
  .ch .cr { font-size: 7pt; color: #b0aba5; letter-spacing: 3px; }

  .qc { display: flex; flex-direction: column; padding: 8mm 8mm 5mm 8mm; position: relative; }
  .qc .qh { display: flex; justify-content: space-between; align-items: center; margin-bottom: 3mm; }
  .qc .qt { font-size: 6.5pt; color: #312E81; background: #E0E7FF; padding: 2px 10px; border-radius: 8px; letter-spacing: 2px; }
  .qc .qn { font-size: 6.5pt; color: #b0aba5; letter-spacing: 2px; }
  .qc .bn { font-family: Georgia,"Microsoft YaHei",serif; font-size: 28pt; color: #C7D2FE; line-height: 0.85; letter-spacing: 4px; margin-bottom: 2mm; }
  .qc .qq { font-size: 13pt; font-weight: bold; color: #1a1a1a; line-height: 1.6; margin-bottom: 2mm; }
  .qc .dk { width: 14mm; border-top: 1px solid #4338CA; margin-bottom: 2mm; }
  .qc .hh { font-size: 8.5pt; font-weight: 300; color: #5c5852; line-height: 1.7; margin-bottom: 3mm; padding-left: 6px; border-left: 2px solid #C7D2FE; }
  .qc .qa { flex: 1; min-height: 10mm; background-color: #fff; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1' height='28'%3E%3Cline x1='0' y1='27' x2='1' y2='27' stroke='%23C7D2FE' stroke-width='1'/%3E%3C/svg%3E"); background-size: 100% 28px; background-repeat: repeat-y; }

  .fw { display: flex; flex-direction: column; padding: 8mm 8mm 5mm 8mm; position: relative; background: #F5F6FF; }
  .fw .qh { display: flex; justify-content: space-between; align-items: center; margin-bottom: 3mm; }
  .fw .qt { font-size: 6.5pt; color: #ffffff; background: #4338CA; padding: 2px 10px; border-radius: 8px; letter-spacing: 2px; }
  .fw .qn { font-size: 6.5pt; color: #b0aba5; letter-spacing: 2px; }
  .fw .bn { font-family: Georgia,"Microsoft YaHei",serif; font-size: 24pt; color: #C7D2FE; line-height: 0.85; letter-spacing: 4px; margin-bottom: 2mm; }
  .fw .fname { font-size: 13pt; font-weight: bold; color: #312E81; line-height: 1.5; margin-bottom: 2mm; }
  .fw .dk { width: 14mm; border-top: 1px solid #4338CA; margin-bottom: 2mm; }
  .fw .fdesc { font-size: 8pt; color: #5c5852; line-height: 1.8; margin-bottom: 3mm; }
  .fw .fit { display: flex; gap: 6px; margin-bottom: 3px; font-size: 8pt; line-height: 1.6; }
  .fw .fno { flex-shrink: 0; font-family: Georgia,serif; font-size: 11pt; color: #4338CA; width: 16px; text-align: center; font-weight: bold; }
  .fw .ftx { color: #3a3a3a; }
  .fw .fnote { margin-top: auto; font-size: 6.5pt; color: #b0aba5; line-height: 1.7; padding-top: 6px; }

  .ce { display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 10mm; background: #EEF2FF; }
  .ce .cs { font-size: 28pt; color: #4338CA; opacity: 0.3; margin-bottom: 16px; }
  .ce .ct { font-size: 16pt; font-weight: bold; color: #1a1a1a; line-height: 1.8; margin-bottom: 14px; }
  .ce .cx { font-size: 10pt; color: #5c5852; line-height: 2.4; }

  .copyright-page { padding: 8mm 9mm; display: flex; flex-direction: column; justify-content: center; }
  .copyright-page h4 { font-size: 12pt; font-weight: bold; color: #1a1a1a; margin-bottom: 4mm; }
  .copyright-page .dv { width: 14mm; border-top: 1px solid #4338CA; margin: 4mm 0; }
  .copyright-page .info { font-size: 7.5pt; color: #5c5852; line-height: 2.2; }
  .copyright-page .info a { color: #312E81; text-decoration: none; word-break: break-all; }
  .copyright-page .info .label { font-weight: bold; color: #1a1a1a; }
  .copyright-page .cclogo { font-size: 6.5pt; color: #b0aba5; margin-top: 6mm; line-height: 1.8; }
  .copyright-page .ft { font-size: 7pt; color: #b0aba5; text-align: center; letter-spacing: 3px; margin-top: 4mm; }
"""


def load():
    meta = json.load(open(os.path.join(BASE, "meta.json"), "r", encoding="utf-8"))
    chapters = []
    for i in range(1, 13):
        with open(os.path.join(BASE, "ch%02d.json" % i), "r", encoding="utf-8") as f:
            chapters.append(json.load(f))
    return {"meta": meta, "chapters": chapters}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(data):
    meta = data["meta"]
    out = []
    out.append('<!DOCTYPE html>')
    out.append('<html lang="zh-CN">')
    out.append('<head>')
    out.append('<meta charset="UTF-8">')
    out.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    out.append('<title>%s</title>' % meta["title"])
    out.append('<style>')
    out.append(CSS)
    out.append('</style>')
    out.append('</head>')
    out.append('<body>')

    # 封面
    out.append('<div class="page cover">')
    out.append('  <div class="tag">%s</div>' % meta["cover_tag"])
    out.append('  <h1>%s</h1>' % meta["cover_h1"])
    out.append('  <div class="sub">%s</div>' % meta["cover_sub"])
    out.append('  <div class="meta">%s</div>' % meta["cover_meta"])
    out.append('  <div class="studio">卡片创作实验室 出品</div>')
    out.append('</div>')

    # 介绍页
    out.append('<div class="page intro-page">')
    out.append('  <p class="hd">%s</p>' % meta["intro_hd"])
    for p in meta["intro_bt"]:
        out.append('  <p class="bt">%s</p>' % p)
    out.append('  <div class="dv"></div>')
    out.append('  <p class="pull">%s</p>' % meta["intro_pull"])
    for p in meta["intro_bt2"]:
        out.append('  <p class="bt">%s</p>' % p)
    out.append('  <p class="soft">%s</p>' % meta["intro_soft"])
    out.append('  <div class="ft">卡片创作实验室 出品</div>')
    out.append('</div>')

    # 使用说明
    out.append('<div class="page txt">')
    out.append('  <p class="bq" style="margin-bottom:8px">使用说明</p>')
    for i, r in enumerate(meta["usage"], 1):
        out.append('  <div class="rl"><span class="rn">%02d</span><span class="rt">%s</span></div>' % (i, r))
    out.append('  <div class="dv"></div>')
    out.append('  <div class="ft">卡片创作实验室 出品</div>')
    out.append('</div>')

    # 版权声明
    out.append('<div class="page copyright-page">')
    out.append('  <h4>版权声明</h4>')
    out.append('  <div class="dv"></div>')
    out.append('  <div class="info">')
    out.append('    <p><span class="label">产品名称</span>：%s</p>' % meta["copyright_name"])
    out.append('    <p><span class="label">出品方</span>：卡片创作实验室</p>')
    out.append('    <p><span class="label">官方网站</span>：<a href="https://www.cnfeat.com/">https://www.cnfeat.com/</a></p>')
    out.append('    <p><span class="label">开源仓库</span>：<a href="https://github.com/cnfeat/CardPackStudio">https://github.com/cnfeat/CardPackStudio</a></p>')
    out.append('    <p><span class="label">联系方式</span>：微信 cnfeat</p>')
    out.append('  </div>')
    out.append('  <div class="dv"></div>')
    out.append('  <div class="cclogo">')
    out.append('    <p>本卡包内容采用 <strong>CC BY-NC-SA 4.0</strong> 许可协议</p>')
    out.append('    <p>署名 - 非商业性使用 - 相同方式共享</p>')
    out.append('    <p>最新版请查看开源仓库</p>')
    out.append('  </div>')
    out.append('  <div class="ft">卡片创作实验室 出品</div>')
    out.append('</div>')

    # 卡片
    total = 0
    for ch in data["chapters"]:
        out.append('<div class="page ch">')
        out.append('  <div class="ci">CHAPTER %s</div>' % ch["num"])
        out.append('  <div class="ct">%s</div>' % ch["title"])
        out.append('  <div class="cd">%s</div>' % ch["desc"])
        out.append('  <div class="cc">-- * --</div>')
        out.append('  <div class="cr">%s</div>' % ch["range"])
        out.append('</div>')

        for card in ch["cards"]:
            total += 1
            no = "%03d" % total
            if card.get("type") == "framework":
                out.append('<div class="page fw">')
                out.append('  <div class="qh"><span class="qt">工具 · 框架</span><span class="qn">%s / %s</span></div>' % (no, meta["total"]))
                out.append('  <div class="bn">%s</div>' % no)
                out.append('  <div class="fname">%s</div>' % card["name"])
                out.append('  <div class="dk"></div>')
                if card.get("desc"):
                    out.append('  <div class="fdesc">%s</div>' % card["desc"])
                for j, it in enumerate(card["items"], 1):
                    out.append('  <div class="fit"><span class="fno">%d</span><span class="ftx">%s</span></div>' % (j, it))
                if card.get("note"):
                    out.append('  <div class="fnote">%s</div>' % card["note"])
                out.append('</div>')
            else:
                out.append('<div class="page qc">')
                out.append('  <div class="qh"><span class="qt">%s</span><span class="qn">%s / %s</span></div>' % (ch["title"], no, meta["total"]))
                out.append('  <div class="bn">%s</div>' % no)
                out.append('  <div class="qq">%s</div>' % card["q"])
                out.append('  <div class="dk"></div>')
                out.append('  <div class="hh">%s</div>' % card["h"])
                out.append('  <div class="qa"></div>')
                out.append('</div>')

        if ch.get("milestone"):
            out.append('<div class="page ce">')
            out.append('  <div class="cs">*</div>')
            out.append('  <div class="ct">%s</div>' % ch["milestone_title"])
            out.append('  <div class="cx">')
            for p in ch["milestone"]:
                out.append('    <p>%s</p>' % p)
            out.append('  </div>')
            out.append('</div>')

    # 结尾页
    out.append('<div class="page end-page">')
    out.append('  <h3>%s</h3>' % meta["end_h3"])
    for p in meta["end_bt"]:
        out.append('  <p class="bt">%s</p>' % p)
    out.append('  <div class="dv"></div>')
    for p in meta["end_bt2"]:
        out.append('  <p class="bt">%s</p>' % p)
    out.append('  <div class="pull">%s</div>' % meta["end_pull"])
    out.append('  <p class="close">%s</p>' % meta["end_close"])
    out.append('  <div class="ft">卡片创作实验室 出品</div>')
    out.append('</div>')

    out.append('</body>')
    out.append('</html>')
    return "\n".join(out)


def main():
    data = load()
    html = build(data)
    out_path = os.path.join(BASE, "创业与商业模式决策卡包-完整版300卡.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated:", out_path, "| cards:", sum(len(c["cards"]) for c in data["chapters"]))


if __name__ == "__main__":
    main()
