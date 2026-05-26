from __future__ import annotations

import html
import zipfile
from pathlib import Path


OUT = Path("Enterprise-Model-Lab-Team-Judge-Pitch.pptx")
NOTES = Path("Enterprise-Model-Lab-Team-5min-Script.md")
W = 12192000
H = 6858000


COLORS = {
    "navy": "101827",
    "ink": "142033",
    "muted": "5A667A",
    "blue": "2563EB",
    "cyan": "06B6D4",
    "green": "10B981",
    "amber": "F59E0B",
    "red": "EF4444",
    "paper": "F8FAFC",
    "white": "FFFFFF",
    "line": "CBD5E1",
}


def emu(x: float) -> int:
    return int(x)


def esc(value: str) -> str:
    return html.escape(value, quote=False)


def run(text: str, size: int = 2600, color: str = "ink", bold: bool = False) -> str:
    return (
        f'<a:r><a:rPr lang="zh-CN" sz="{size}" '
        f'{"b=\"1\" " if bold else ""}>'
        f'<a:solidFill><a:srgbClr val="{COLORS[color]}"/></a:solidFill>'
        f'<a:latin typeface="Aptos"/><a:ea typeface="Microsoft YaHei"/></a:rPr>'
        f"<a:t>{esc(text)}</a:t></a:r>"
    )


def textbox(idx: int, x: int, y: int, w: int, h: int, lines: list[str], size=2600, color="ink", bold=False) -> str:
    paragraphs = []
    for line in lines:
        paragraphs.append(f"<a:p>{run(line, size=size, color=color, bold=bold)}</a:p>")
    return f"""
<p:sp>
  <p:nvSpPr><p:cNvPr id="{idx}" name="Text {idx}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
  <p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{w}" cy="{h}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/><a:ln><a:noFill/></a:ln></p:spPr>
  <p:txBody><a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" bIns="0"/><a:lstStyle/>{''.join(paragraphs)}</p:txBody>
</p:sp>"""


def rect(idx: int, x: int, y: int, w: int, h: int, fill: str, line: str | None = None, radius=False) -> str:
    geom = "roundRect" if radius else "rect"
    ln = f'<a:ln w="12700"><a:solidFill><a:srgbClr val="{COLORS[line]}"/></a:solidFill></a:ln>' if line else "<a:ln><a:noFill/></a:ln>"
    return f"""
<p:sp>
  <p:nvSpPr><p:cNvPr id="{idx}" name="Shape {idx}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
  <p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{w}" cy="{h}"/></a:xfrm><a:prstGeom prst="{geom}"><a:avLst/></a:prstGeom><a:solidFill><a:srgbClr val="{COLORS[fill]}"/></a:solidFill>{ln}</p:spPr>
</p:sp>"""


def metric(idx: int, x: int, y: int, w: int, h: int, value: str, label: str, color="blue") -> str:
    return (
        rect(idx, x, y, w, h, "white", "line", True)
        + textbox(idx + 100, x + 220000, y + 180000, w - 440000, 420000, [value], 3600, color, True)
        + textbox(idx + 200, x + 220000, y + 670000, w - 440000, 360000, [label], 1650, "muted", False)
    )


def bullet_list(idx: int, x: int, y: int, w: int, h: int, items: list[str], size=2200) -> str:
    lines = [f"• {item}" for item in items]
    return textbox(idx, x, y, w, h, lines, size=size, color="ink")


def slide_xml(shapes: str, bg: str = "paper") -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg><p:bgPr><a:solidFill><a:srgbClr val="{COLORS[bg]}"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{W}" cy="{H}"/><a:chOff x="0" y="0"/><a:chExt cx="{W}" cy="{H}"/></a:xfrm></p:grpSpPr>
      {shapes}
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>"""


def title(num: int, text: str, subtitle: str = "") -> str:
    sub = textbox(12, 760000, 1720000, 7600000, 900000, [subtitle], 2600, "paper") if subtitle else ""
    return (
        rect(2, 0, 0, W, H, "navy")
        + rect(3, 760000, 720000, 2400000, 90000, "cyan")
        + textbox(10, 760000, 900000, 9400000, 900000, [text], 5200, "white", True)
        + sub
        + textbox(20, 760000, 5920000, 6000000, 300000, [f"{num:02d} / Enterprise Model Lab Team"], 1400, "paper")
    )


SLIDES: list[str] = []

SLIDES.append(slide_xml(
    title(1, "不是一个 Agent，是一家可以被调用的 AI 公司", "5 分钟评委汇报 | Enterprise Model Lab Team")
    + metric(30, 760000, 3450000, 2300000, 1150000, "31", "跨部门智能体", "cyan")
    + metric(40, 3360000, 3450000, 2300000, 1150000, "30", "公司级交付物", "green")
    + metric(50, 5960000, 3450000, 2300000, 1150000, "6/6", "验收清单通过", "amber")
    + metric(60, 8560000, 3450000, 2300000, 1150000, "85", "AI交付准备度", "blue"),
    bg="navy",
))

SLIDES.append(slide_xml(
    title(2, "评委最难判断的不是文字，而是真实执行")
    + textbox(30, 760000, 2400000, 7600000, 720000, ["普通 Agent Demo 的问题：能生成很多内容，但很难证明真的完成了交付。"], 3000, "white", True)
    + bullet_list(40, 1000000, 3400000, 7800000, 1500000, [
        "是否只是模板化方案？",
        "是否有真实输入、过程、输出？",
        "是否能被客户或评委验收？",
        "是否会夸大训练、微调、上线能力？",
    ], 2400)
    + textbox(50, 1000000, 5400000, 8800000, 420000, ["我们的解法：用证据链约束多智能体协作。"], 3000, "cyan", True),
    bg="navy",
))

SLIDES.append(slide_xml(
    title(3, "网页不是装饰，是评委证据驾驶舱")
    + bullet_list(30, 820000, 2300000, 6200000, 2100000, [
        "启动 31-Agent 完整公司团队",
        "点击部门查看每个智能体的输入、决策、输出和交接",
        "上传 CSV 后实时改变数据画像与模型路线",
        "下载总报告、交付包和证据 JSON",
    ], 2350)
    + rect(60, 7800000, 2300000, 3100000, 2600000, "white", "line", True)
    + textbox(61, 8120000, 2580000, 2500000, 420000, ["Judge Proof Cockpit"], 2800, "blue", True)
    + textbox(62, 8120000, 3220000, 2500000, 1250000, ["AI Delivery Readiness", "Browser + Python", "Acceptance Evidence", "No Overclaiming"], 2100, "ink", True)
    + textbox(70, 820000, 5550000, 9800000, 520000, ["演示重点：不要只看页面，要点开部门和交付物，让评委看到多智能体的“工作链”。"], 2500, "green", True)
))

SLIDES.append(slide_xml(
    title(4, "一次真实调用，产出可复查的交付包")
    + metric(30, 760000, 2320000, 2100000, 1080000, "132", "文件被扫描", "blue")
    + metric(40, 3120000, 2320000, 2100000, 1080000, "13", "代码文件", "cyan")
    + metric(50, 5480000, 2320000, 2100000, 1080000, "117", "文档文件", "green")
    + metric(60, 7840000, 2320000, 2100000, 1080000, "30/30", "交付物存在", "amber")
    + bullet_list(80, 950000, 4050000, 8800000, 1350000, [
        "生成 run-report、asset-inventory、readiness-score",
        "生成 work-orders、execution-log、execution-status",
        "生成 capability-matrix、acceptance-checklist、next-execution-plan",
        "生成 client-project 并运行 smoke test",
    ], 2250)
))

SLIDES.append(slide_xml(
    title(5, "不是“写方案”，而是“可验收”")
    + rect(30, 820000, 2350000, 9600000, 2600000, "white", "line", True)
    + textbox(31, 1120000, 2650000, 4200000, 420000, ["验收清单 6/6 通过"], 3300, "green", True)
    + bullet_list(40, 1120000, 3350000, 7800000, 1300000, [
        "Web demo 可直接打开，无登录、无 API key、无 GPU",
        "真实项目分析包含资产、数据、模型路线和风险",
        "工作单有 owner、priority、artifact、acceptance",
        "客户项目 smoke test 返回 0",
    ], 2200)
    + textbox(60, 1120000, 5550000, 9000000, 460000, ["评委可以按文件逐项验收，而不是听我们口头承诺。"], 2850, "blue", True)
))

SLIDES.append(slide_xml(
    title(6, "GPO 案例证明：它不是写死的文本模板")
    + textbox(30, 820000, 2300000, 8000000, 520000, ["GPO 是计算机视觉分割项目，不是 LLM 文本任务。"], 3000, "white", True)
    + bullet_list(40, 1040000, 3200000, 8500000, 1600000, [
        "识别 SAM + DINOv2 / feature matching + RL/DQN prompt optimizer",
        "发现 158 个代码文件、55 个文档/日志、80 个模型资产",
        "解析 5019 条训练 episode 记录",
        "给出产品化路线：视觉分割 prompt optimization demo",
    ], 2250)
    + textbox(60, 1040000, 5420000, 8400000, 520000, ["亮点：同一套公司级流程，可以迁移到视觉模型、Agent 产品和企业 AI 项目。"], 2600, "cyan", True),
    bg="navy",
))

SLIDES.append(slide_xml(
    title(7, "核心创新：多智能体从聊天走向公司级交付")
    + bullet_list(30, 900000, 2250000, 9500000, 2350000, [
        "组织级智能体：战略、产品、技术、AI、MLOps、法务、运营、媒体、销售完整覆盖",
        "真实交付闭环：输入目标 -> 调度部门 -> 生成交付物 -> 执行工作单 -> 输出验收证据",
        "可信边界：明确区分已执行、可执行、不可声称",
        "双路径体验：网页给评委试用，company_os.py 给项目做深度执行",
    ], 2300)
    + textbox(60, 900000, 5600000, 9000000, 500000, ["一句话：我们把 Skill 做成了一家会留下证据的 AI 公司。"], 3000, "green", True)
))

SLIDES.append(slide_xml(
    title(8, "5 分钟演示路线：让评委亲眼看到证据")
    + bullet_list(30, 980000, 2200000, 9600000, 2600000, [
        "1. 首页：强调 Judge Proof Cockpit 和 AI交付准备度",
        "2. 点击启动：展示 31-Agent 调度与实时日志",
        "3. 点部门/Agent：证明不是堆名字，而是有输入、决策、输出、交接",
        "4. 下载报告：展示 85/100、6/6、executed、smoke test passed",
        "5. 打开 GPO：证明框架能迁移到真实视觉项目",
    ], 2200)
    + textbox(70, 980000, 5600000, 9000000, 520000, ["收尾口号：我们不是做了一个 Agent，我们做了一家可以被调用的 AI 公司。"], 2850, "blue", True)
))


def content_types() -> str:
    slides = "\n".join(
        f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1, len(SLIDES) + 1)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
  {slides}
</Types>"""


def root_rels() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>"""


def presentation_xml() -> str:
    ids = "\n".join(f'<p:sldId id="{255+i}" r:id="rId{i+1}"/>' for i in range(1, len(SLIDES) + 1))
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>
  <p:sldIdLst>{ids}</p:sldIdLst>
  <p:sldSz cx="{W}" cy="{H}" type="wide"/>
  <p:notesSz cx="6858000" cy="9144000"/>
  <p:defaultTextStyle/>
</p:presentation>"""


def presentation_rels() -> str:
    rels = ['<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>']
    for i in range(1, len(SLIDES) + 1):
        rels.append(f'<Relationship Id="rId{i+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>')
    rels.append(f'<Relationship Id="rId{len(SLIDES)+2}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>')
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{''.join(rels)}</Relationships>"""


def slide_rels() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>"""


def master_xml() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{W}" cy="{H}"/><a:chOff x="0" y="0"/><a:chExt cx="{W}" cy="{H}"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
  <p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst>
  <p:txStyles><p:titleStyle/><p:bodyStyle/><p:otherStyle/></p:txStyles>
</p:sldMaster>"""


def layout_xml() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1">
  <p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{W}" cy="{H}"/><a:chOff x="0" y="0"/><a:chExt cx="{W}" cy="{H}"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>"""


def simple_theme() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="EnterpriseModelLab">
  <a:themeElements>
    <a:clrScheme name="Custom"><a:dk1><a:srgbClr val="101827"/></a:dk1><a:lt1><a:srgbClr val="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="142033"/></a:dk2><a:lt2><a:srgbClr val="F8FAFC"/></a:lt2><a:accent1><a:srgbClr val="2563EB"/></a:accent1><a:accent2><a:srgbClr val="06B6D4"/></a:accent2><a:accent3><a:srgbClr val="10B981"/></a:accent3><a:accent4><a:srgbClr val="F59E0B"/></a:accent4><a:accent5><a:srgbClr val="EF4444"/></a:accent5><a:accent6><a:srgbClr val="5A667A"/></a:accent6><a:hlink><a:srgbClr val="2563EB"/></a:hlink><a:folHlink><a:srgbClr val="5A667A"/></a:folHlink></a:clrScheme>
    <a:fontScheme name="Aptos"><a:majorFont><a:latin typeface="Aptos"/><a:ea typeface="Microsoft YaHei"/></a:majorFont><a:minorFont><a:latin typeface="Aptos"/><a:ea typeface="Microsoft YaHei"/></a:minorFont></a:fontScheme>
    <a:fmtScheme name="Clean"><a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst><a:lnStyleLst><a:ln w="6350"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst><a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst><a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst></a:fmtScheme>
  </a:themeElements>
</a:theme>"""


def write_deck() -> None:
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types())
        z.writestr("_rels/.rels", root_rels())
        z.writestr("ppt/presentation.xml", presentation_xml())
        z.writestr("ppt/_rels/presentation.xml.rels", presentation_rels())
        z.writestr("ppt/slideMasters/slideMaster1.xml", master_xml())
        z.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/></Relationships>""")
        z.writestr("ppt/slideLayouts/slideLayout1.xml", layout_xml())
        z.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/></Relationships>""")
        z.writestr("ppt/theme/theme1.xml", simple_theme())
        for i, slide in enumerate(SLIDES, 1):
            z.writestr(f"ppt/slides/slide{i}.xml", slide)
            z.writestr(f"ppt/slides/_rels/slide{i}.xml.rels", slide_rels())
        z.writestr("docProps/core.xml", """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Enterprise Model Lab Team Judge Pitch</dc:title><dc:creator>Codex</dc:creator></cp:coreProperties>""")
        z.writestr("docProps/app.xml", f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"><Application>Codex</Application><Slides>{len(SLIDES)}</Slides></Properties>""")


def write_notes() -> None:
    NOTES.write_text(
        """# Enterprise Model Lab Team - 5分钟评委汇报讲稿

## 0:00-0:25 开场
各位评委好，我们做的不是一个单点 Agent，也不是一个报告生成器。我们做的是一个 Fortune-500 风格的 AI 公司操作系统。用户输入一个 AI 项目目标后，系统会调度 31 个跨部门智能体，从战略、产品、技术、数据、模型、测试、MLOps、法务、运营、媒体、销售到最终交付，形成一整套可运行、可下载、可验收的交付链路。

## 0:25-1:10 痛点
很多 Agent Demo 看起来能生成很多文字，但评委很难判断它到底有没有真的做事。所以我们把重点放在三件事：能执行、有证据、知道什么不能乱声称。比如模型训练和微调，系统不会为了显得高级就直接说“已训练完成”，而是要求有数据版本、命令、日志、指标，才允许进入训练或微调声明。

## 1:10-2:00 前端演示
现在我打开网页，点击启动 31-Agent 完整公司团队。左边是 Agent 队列，中间是部门链路和交付物，右边是实时协作日志。每个部门、每个 Agent 都能点进去看输入、决策、输出、交接对象和落地动作。这解决的是多智能体系统最容易被质疑的问题：不是堆名字，而是有组织结构、有交付物、有交接关系。

## 2:00-3:05 真实调用结果
这是我们用 Skill 跑出来的一次完整流程。它扫描了 132 个项目文件，识别 13 个代码文件和 117 个文档文件，生成 30/30 个公司级交付物，AI 交付准备度 85/100，验收清单 6/6 通过，执行状态 executed，客户项目 smoke test passed。也就是说，它不只是说应该交付什么，而是真的生成了可以验收的客户成品项目。

## 3:05-4:00 GPO案例
为了证明它不是只适用于预设文本任务，我们放了一个 GPO 计算机视觉项目案例。这个项目不是 LLM 文本任务，而是 SAM + DINOv2 / feature matching + RL/DQN prompt optimizer 的视觉分割项目。系统依然能用公司级方式分析它：识别资产、判断模型路线、生成技术架构、MLOps、评估方案、工作单、执行日志和客户项目。

## 4:00-4:40 创新点
第一个亮点是组织级智能体，不是单 Agent；第二个亮点是真实交付闭环：输入目标、调度部门、生成交付物、执行工作单、输出验收证据；第三个亮点是可信边界：明确区分已执行、可执行、不可声称，避免 AI 项目里最常见的“看起来很强但不可复查”。

## 4:40-5:00 收尾
所以这个作品的价值不是让 AI 写更多文字，而是让 AI 像一家专业科技公司一样组织工作、留下证据、交付结果。评委可以直接在网页试用，也可以查看 GitHub 中的 Skill、Company OS 执行器、GPO 案例、验收清单和 smoke test。我们不是做了一个 Agent，我们做了一家可以被调用的 AI 公司。
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    write_deck()
    write_notes()
    print(f"Wrote {OUT}")
    print(f"Wrote {NOTES}")
