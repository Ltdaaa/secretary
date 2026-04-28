# Enterprise Model Lab Team

一支模拟世界 500 强科技公司运作方式的多 Agent AI 公司团队。它不是单个聊天机器人，也不是单纯模型训练小组，而是一个完整的 AI Technology Company OS：从市场机会、产品定义、用户研究、数据搜查、模型训练、微调测试、MLOps、安全合规、财务资源、运营增长、客户成功到比赛展示，完整交付一个 AI 产品。

## 项目亮点

- **公司级组织架构**：覆盖 CEO、CTO、COO、CFO、法务、产品、用户研究、运营、客户成功、数据、模型、训练、测试、MLOps、安全、品牌和提交团队。
- **完整 AI 产品闭环**：从一句话目标到 30 份公司级交付物，覆盖战略、产品、设计、技术、AI、媒体、运营、销售、HR、PMO 和交付。
- **模型训练专业度**：保留数据治理、模型分析、训练设计、微调设计、评测测试和发布监控。
- **稳定可运行**：核心演示不依赖 GPU、不依赖外部 API，使用 Python 标准库即可生成交付包。
- **可验证落地**：网页端提供功能自检和证据 JSON；本地执行器会生成行动计划、跨部门工作单，把工作单执行成可复查文件，并产出可运行客户成品项目。
- **适合比赛展示**：评委可以直接看到一个世界 500 强级科技公司如何组织 AI 产品研发和商业落地。

## 目录结构

```text
enterprise-model-lab-team/
  SKILL.md                         # 核心 Skill
  scripts/create_workspace.py      # 一键生成公司级交付包
  scripts/company_os.py            # 真实执行器：扫描项目、分析数据、生成报告
  templates/                       # 交付模板
  examples/                        # 评委可读示例
  tests/validate_skill.py          # 轻量验证脚本
  tests/validate_company_os.py     # 真实执行能力验证
  tests/validate_site.py           # 网页可试用能力验证

demo-deliveries/psych-safety-ai-company/
  project-brief.yaml               # 示例项目输入
  delivery-board.md                # 公司级交付看板
  evaluation-rubric.md             # 评审评分标准
  00-company-charter.md            # 公司战略章程
  01-market-opportunity.md         # 市场机会
  02-product-requirements.md       # 产品需求 PRD
  03-user-research.md              # 用户研究
  04-data-map.md                   # 数据搜查地图
  05-data-card.md                  # 数据治理卡
  06-model-selection.md            # 模型选型矩阵
  07-training-design.md            # 训练设计书
  08-finetune-plan.md              # 微调计划
  09-evaluation-protocol.md        # 评测协议
  10-mlops-release-plan.md         # MLOps 发布计划
  11-risk-register.md              # AI 安全风险登记册
  12-agent-product-spec.md         # 智能体产品规格
  13-growth-operations-plan.md     # 运营增长计划
  14-customer-success-plan.md      # 客户成功计划
  15-finance-resource-plan.md      # 财务资源计划
  16-legal-compliance-review.md    # 法务合规审查
  17-brand-demo-playbook.md        # 品牌与展示脚本
  18-executive-dashboard.md        # 高管仪表盘
  19-judge-summary.md              # 评委摘要
  asset-inventory.json             # 真实项目资产扫描结果
  readiness-score.json             # 提交准备度评分
  action-plan.json                 # 机器可读行动计划
  work-orders.md                   # 跨部门落地工作单
  execution-status.json            # 工作单执行状态
  execution-log.md                 # 工作单执行日志
  executed-work/                   # 每个部门工作单的执行产物
  client-project-status.json       # 客户项目烟测结果
  client-project/                  # 可交付客户的成品静态项目
  run-report.md                    # 真实运行报告

site/
  index.html                       # 可部署到 GitHub Pages/Vercel 的项目展示网站
```

## 快速运行

```powershell
python enterprise-model-lab-team\scripts\create_workspace.py --name psych-safety-ai-company --goal "Build a Fortune-500-style AI company team for designing, training, evaluating, launching, and operating a psychological prompt safety model product." --output demo-deliveries --force
```

## 验证

```powershell
python enterprise-model-lab-team\tests\validate_skill.py
python enterprise-model-lab-team\tests\validate_company_os.py
python enterprise-model-lab-team\tests\validate_site.py --site site
node enterprise-model-lab-team\tests\validate_site_runtime.js site
python enterprise-model-lab-team\tests\validate_submission_package.py --submission submission-ready --zip enterprise-model-lab-team-submission.zip
```

验证通过后会输出：

```text
enterprise-model-lab-team validation passed
enterprise-model-lab-team company_os validation passed
enterprise-model-lab-team site validation passed
enterprise-model-lab-team site runtime validation passed
enterprise-model-lab-team submission package audit passed
```

## 真实执行

这个项目不只生成模板。`company_os.py` 会扫描本地项目，统计代码、文档、数据、模型文件，分析 CSV/表格数据，判断是否具备训练 baseline 的条件，给出模型路线建议，并写入可复查的报告。

```powershell
python enterprise-model-lab-team\scripts\company_os.py --workspace demo-deliveries\psych-safety-ai-company --source .
```

运行后会生成：

```text
demo-deliveries/psych-safety-ai-company/run-report.md
demo-deliveries/psych-safety-ai-company/asset-inventory.json
demo-deliveries/psych-safety-ai-company/readiness-score.json
demo-deliveries/psych-safety-ai-company/action-plan.json
demo-deliveries/psych-safety-ai-company/work-orders.md
demo-deliveries/psych-safety-ai-company/execution-status.json
demo-deliveries/psych-safety-ai-company/execution-log.md
demo-deliveries/psych-safety-ai-company/executed-work/
demo-deliveries/psych-safety-ai-company/client-project-status.json
demo-deliveries/psych-safety-ai-company/client-project/
```

## 网页端真实能力

`site/index.html` 是纯静态页面，但不是死页面。它在浏览器本地完成 CSV 解析、文本/标签字段识别、标签分布统计、空值和重复文本检查、模型路线建议、31-Agent 调度展示、交付物下载、报告下载、证据 JSON 下载和功能自检。Agent 协作日志是确定性的前端调度展示，深度文件系统扫描、工作单执行和客户成品项目生成由 `company_os.py` 负责。

网页还提供“部门作战室”：评委可以点击 Executive、Technology、AI Platform、Growth & Media、Operations 等部门，直接查看该部门下每个智能体的输入、决策、输出、交接对象、交付物和落地动作。

每张交付物卡片也可以点击。评委可以进入单份交付物工作台，查看负责人、部门、输入、决策、输出、交接对象、验收标准、落地动作和 Markdown 预览，并单独下载该交付物。

## 比赛展示建议

1. 将 `site/index.html` 部署到 GitHub Pages、Vercel 或 Netlify，作为项目展示网站。
2. 打开 `enterprise-model-lab-team/SKILL.md`，说明这是一个“AI 科技公司数字团队”。
3. 展示 `demo-deliveries/psych-safety-ai-company/project-brief.yaml` 作为一句话输入。
4. 展示 `delivery-board.md`，证明 30 个公司级交付物覆盖完整部门协作。
5. 展示 `run-report.md`，证明系统真的扫描了项目、分析了数据、识别了模型资产，并给出模型路线建议。
6. 展示 `action-plan.json`、`work-orders.md`、`execution-status.json`、`execution-log.md` 和 `executed-work/`，证明它能把分析转成部门负责人、优先级、验收标准，并按工作单执行出证据文件。
7. 展示 `client-project/` 和 `client-project-status.json`，证明它能给客户生成可打开、可部署、可验收的成品项目。
8. 展示 `02-product-requirements.md`、`06-model-selection.md`、`07-training-design.md`、`09-evaluation-protocol.md`、`13-growth-operations-plan.md`，证明它不是只有模型，而是产品、技术、运营闭环。
9. 最后用 `19-judge-summary.md` 做 3 分钟收尾。

## 安全说明

本仓库不需要上传任何本地认证文件。不要提交 `.codex/`、`auth.json`、API key、模型密钥或私人数据集。

## 部署

项目展示网站是纯静态页面，部署 `submission-ready/site/` 即可。详细步骤见 [DEPLOYMENT.md](DEPLOYMENT.md)。
