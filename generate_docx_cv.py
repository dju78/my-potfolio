import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc = docx.Document()

# Page Margins (0.6 in / 43.2 pt for clean ATS & page fit)
for section in doc.sections:
    section.top_margin = Inches(0.55)
    section.bottom_margin = Inches(0.55)
    section.left_margin = Inches(0.65)
    section.right_margin = Inches(0.65)

# Styling palette
COLOR_NAVY = RGBColor(8, 37, 84)      # #082554
COLOR_CHARCOAL = RGBColor(33, 37, 41) # #212529
COLOR_MUTED = RGBColor(100, 116, 139) # #64748B
COLOR_LINE = "D1D5DB"

def set_para_font(p, name="Calibri", size_pt=10, bold=False, italic=False, color=COLOR_CHARCOAL, space_after=2, space_before=0, line_spacing=1.1):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    for run in p.runs:
        run.font.name = name
        run.font.size = Pt(size_pt)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = color

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text.upper())
    run.font.name = "Calibri"
    run.font.size = Pt(11)
    run.bold = True
    run.font.color.rgb = COLOR_NAVY
    
    # Add bottom border to heading
    pPr = p._p.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="8" w:space="2" w:color="{COLOR_LINE}"/></w:pBdr>')
    pPr.append(pBdr)
    return p

# 1. HEADER
p_name = doc.add_paragraph()
p_name.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_name.paragraph_format.space_before = Pt(0)
p_name.paragraph_format.space_after = Pt(1)
run_name = p_name.add_run("DARAMOLA JOSEPH OMOYELE")
run_name.font.name = "Calibri"
run_name.font.size = Pt(18)
run_name.bold = True
run_name.font.color.rgb = COLOR_NAVY

p_sub = doc.add_paragraph()
p_sub.paragraph_format.space_before = Pt(0)
p_sub.paragraph_format.space_after = Pt(3)
run_sub = p_sub.add_run("Data & Research Analyst | Economic Analysis & Business Intelligence")
run_sub.font.name = "Calibri"
run_sub.font.size = Pt(11.5)
run_sub.bold = True
run_sub.font.color.rgb = COLOR_CHARCOAL

p_contact = doc.add_paragraph()
p_contact.paragraph_format.space_before = Pt(0)
p_contact.paragraph_format.space_after = Pt(6)
run_c = p_contact.add_run("Colchester, Essex, UK  |  dju78@omoyelejd.co.uk  |  Portfolio: daramolajo.co.uk  |  Business: jomovate.com\nLinkedIn: linkedin.com/in/joseph-omoyele-bbb006244/  |  GitHub: github.com/dju78  |  ORCID: 0009-0006-0347-0499")
run_c.font.name = "Calibri"
run_c.font.size = Pt(9)
run_c.font.color.rgb = COLOR_MUTED

# 2. PROFESSIONAL SUMMARY
add_heading_1("Professional Summary")
p_sum = doc.add_paragraph()
p_sum.paragraph_format.space_before = Pt(1)
p_sum.paragraph_format.space_after = Pt(5)
p_sum.paragraph_format.line_spacing = 1.15
r_sum = p_sum.add_run(
    "Data and Research Analyst with extensive experience turning complex data into clear insights and practical decision-support tools. "
    "Combines statistical methodology, econometric modelling, business intelligence, and digital product development to address operational, "
    "economic, and governance challenges. Holds an MSc in Economics with Data Analytics (Merit) from the University of Essex. Published researcher "
    "with peer-reviewed articles in development economics and institutional analysis, active contributor to UK regulatory consultations, "
    "and founder of Jomovate Digital Labs."
)
r_sum.font.name = "Calibri"
r_sum.font.size = Pt(9.5)
r_sum.font.color.rgb = COLOR_CHARCOAL

# 3. CORE TECHNICAL & ANALYTICAL EXPERTISE
add_heading_1("Core Technical & Analytical Skills")
skills_data = [
    ("Analysis & Modelling: ", "Econometric modelling, statistical methodology, forecasting, cost-benefit analysis, price-index construction (Jevons, Carli, Dutot), composite indices, Panel ARDL, anomaly detection, scenario analysis"),
    ("Languages & Tools: ", "R, Python (Streamlit, Pandas, NumPy), SQL, Advanced Microsoft Excel, Power BI, Tableau, Shiny"),
    ("Product & Web Development: ", "Business requirements gathering, interactive dashboards, calculation engines, REST APIs, TypeScript, React, Tailwind CSS, QA testing & data validation"),
    ("Governance & Compliance: ", "GDPR-aligned data handling, data validation pipelines, regulatory evidence documentation, tax compliance analytics, audit trail workflows")
]

for title, content in skills_data:
    p_sk = doc.add_paragraph()
    p_sk.paragraph_format.space_before = Pt(0)
    p_sk.paragraph_format.space_after = Pt(2)
    p_sk.paragraph_format.line_spacing = 1.12
    r_t = p_sk.add_run(title)
    r_t.bold = True
    r_t.font.name = "Calibri"
    r_t.font.size = Pt(9.5)
    r_t.font.color.rgb = COLOR_NAVY
    r_c = p_sk.add_run(content)
    r_c.font.name = "Calibri"
    r_c.font.size = Pt(9.5)
    r_c.font.color.rgb = COLOR_CHARCOAL

# 4. PROFESSIONAL EXPERIENCE
add_heading_1("Professional Experience")

def add_experience_item(title, company, dates, focus, bullets):
    p_hdr = doc.add_paragraph()
    p_hdr.paragraph_format.space_before = Pt(4)
    p_hdr.paragraph_format.space_after = Pt(1)
    p_hdr.paragraph_format.keep_with_next = True
    
    r_role = p_hdr.add_run(title)
    r_role.bold = True
    r_role.font.name = "Calibri"
    r_role.font.size = Pt(10)
    r_role.font.color.rgb = COLOR_NAVY
    
    r_sep = p_hdr.add_run("  |  " + company + "  |  ")
    r_sep.font.name = "Calibri"
    r_sep.font.size = Pt(9.5)
    r_sep.font.color.rgb = COLOR_CHARCOAL
    
    r_dt = p_hdr.add_run(dates)
    r_dt.bold = True
    r_dt.font.name = "Calibri"
    r_dt.font.size = Pt(9.5)
    r_dt.font.color.rgb = COLOR_MUTED
    
    if focus:
        p_foc = doc.add_paragraph()
        p_foc.paragraph_format.space_before = Pt(0)
        p_foc.paragraph_format.space_after = Pt(2)
        p_foc.paragraph_format.keep_with_next = True
        r_f1 = p_foc.add_run("Focus: ")
        r_f1.bold = True
        r_f1.font.name = "Calibri"
        r_f1.font.size = Pt(9)
        r_f1.font.color.rgb = COLOR_NAVY
        r_f2 = p_foc.add_run(focus)
        r_f2.font.name = "Calibri"
        r_f2.font.size = Pt(9)
        r_f2.font.color.rgb = COLOR_CHARCOAL
    
    for b in bullets:
        p_b = doc.add_paragraph(style='List Bullet')
        p_b.paragraph_format.space_before = Pt(0)
        p_b.paragraph_format.space_after = Pt(1.5)
        p_b.paragraph_format.line_spacing = 1.1
        r_b = p_b.add_run(b)
        r_b.font.name = "Calibri"
        r_b.font.size = Pt(9)
        r_b.font.color.rgb = COLOR_CHARCOAL

add_experience_item(
    title="Founder & Product Business Analyst",
    company="Jomovate Digital Labs (jomovate.com)",
    dates="July 2024 – Present",
    focus="Founded venture to build data-driven solutions, conduct applied economic research, and engineer decision-support web applications and analytical dashboards.",
    bullets=[
        "Gather and document user and business requirements, translating operational and analytical questions into digital products and decision tools.",
        "Engineered specialized analytical platforms including the UK AI Economic Measurement Lab, Price Quality Explorer, and UKCalc financial platform.",
        "Perform end-to-end data validation, calculation verification, and quality assurance across data pipelines and interactive dashboards.",
        "Develop technical product documentation and iterate system designs based on feedback from practitioners and professional users.",
        "Explore appropriate uses of AI in communication, reporting, and operational workflows."
    ]
)

add_experience_item(
    title="Data Analyst",
    company="Univelcity Computing (UK / Remote)",
    dates="July 2023 – Present",
    focus="Data analysis, economic modelling, financial analysis, business intelligence, dashboards, and compliance assurance.",
    bullets=[
        "Deliver financial, operational, survey, and research data analysis for donor-funded development programmes and business research, informing evidence-based decision-making.",
        "Apply econometric modelling, forecasting, cost-benefit analysis, risk assessments, and scenario analysis across multi-currency environments (GBP, USD, EUR, NGN).",
        "Design and maintain automated dashboards and decision tools in Power BI, Tableau, Shiny, and Excel, streamlining stakeholder access to timely insights.",
        "Execute data preparation, ETL, and automated reporting pipelines using R, Python, SQL, and Excel to uncover trends, risks, and performance gaps.",
        "Produce clear analytical summaries and policy briefings communicating complex findings to non-technical stakeholders.",
        "Strengthen data quality, governance, and GDPR-aligned handling across projects; mentor junior analysts and provide analytical quality assurance."
    ]
)

add_experience_item(
    title="Data Analyst",
    company="Nigerian Postal Service",
    dates="January 2014 – October 2022",
    focus="Public sector data analysis, operational insight, performance monitoring, forecasting, and regional service improvement.",
    bullets=[
        "Analysed nationwide operational, financial, and socioeconomic datasets to support service delivery planning and management reporting.",
        "Built forecasting models and performance monitoring tools to identify regional efficiency gaps and operational intervention points.",
        "Designed composite performance indices to benchmark regional office performance and support objective resource allocation decisions.",
        "Produced analytical briefings and management summaries translating operational data into actionable service improvement recommendations.",
        "Strengthened survey design, data collection protocols, reporting standards, and data quality assurance across regional facilities."
    ]
)

add_experience_item(
    title="Lecturer / Education Data & Academic Administration Support",
    company="City College of Education",
    dates="April 2008 – March 2013",
    focus="Analysed student attendance, assessment outcomes, and academic progress data for departmental reporting, quality assurance, and curriculum planning.",
    bullets=[
        "Maintained assessment records and student reporting databases, strengthening institutional documentation standards and compliance.",
        "Compiled departmental reports and learning performance data to support evidence-informed learner support and curriculum planning.",
        "Liaised with academic faculty and management to enhance reporting quality and student progression tracking."
    ]
)

# 5. EDUCATION
add_heading_1("Education")
p_edu1 = doc.add_paragraph()
p_edu1.paragraph_format.space_before = Pt(2)
p_edu1.paragraph_format.space_after = Pt(1)
p_edu1.paragraph_format.keep_with_next = True
r_e1_t = p_edu1.add_run("MSc Economics with Data Analytics (Merit)")
r_e1_t.bold = True
r_e1_t.font.name = "Calibri"
r_e1_t.font.size = Pt(9.5)
r_e1_t.font.color.rgb = COLOR_NAVY
r_e1_i = p_edu1.add_run("  |  University of Essex  |  Awarded November 2023")
r_e1_i.font.name = "Calibri"
r_e1_i.font.size = Pt(9.5)

p_dis = doc.add_paragraph()
p_dis.paragraph_format.space_before = Pt(0)
p_dis.paragraph_format.space_after = Pt(2)
r_dis = p_dis.add_run("Dissertation: Econometric analysis of Foreign Direct Investment and Economic Growth in Sub-Saharan Africa (Panel ARDL across 39 countries, 1970–2019, integrating World Bank, IMF, and UNCTAD datasets).")
r_dis.font.name = "Calibri"
r_dis.font.size = Pt(9)
r_dis.font.color.rgb = COLOR_CHARCOAL

p_edu2 = doc.add_paragraph()
p_edu2.paragraph_format.space_before = Pt(1)
p_edu2.paragraph_format.space_after = Pt(3)
r_e2_t = p_edu2.add_run("BSc Economics")
r_e2_t.bold = True
r_e2_t.font.name = "Calibri"
r_e2_t.font.size = Pt(9.5)
r_e2_t.font.color.rgb = COLOR_NAVY
r_e2_i = p_edu2.add_run("  |  University of Ilorin  |  2006")
r_e2_i.font.name = "Calibri"
r_e2_i.font.size = Pt(9.5)

# 6. SELECTED ANALYTICAL PROJECTS
add_heading_1("Selected Analytical Projects & Digital Products")
projects_cv = [
    ("UK AI Economic Measurement Lab (ai-measurement.jomovate.com): ", "Independent research prototype exploring National Accounts classification, Supply & Use tables, and disaggregation of AI-related economic activity (Python/Streamlit)."),
    ("Price Quality Explorer (pricequality.streamlit.app): ", "Methodological application demonstrating automated data quality auditing, anomaly detection, and elementary price-index calculation (Jevons, Carli, Dutot)."),
    ("Performance Insight Explorer (performance-insight-explorer.streamlit.app): ", "Executive decision-support tool transforming operational datasets into KPI benchmarks and trend intelligence."),
    ("Care Quality Intelligence (cqi.carephrase.com): ", "Health and social care analytics dashboard delivering quality monitoring, risk oversight, and regulatory audit evidence (React/TypeScript)."),
    ("UKCalc Platform (ukcalc.jomovate.com): ", "Financial calculation platform translating complex UK statutory tax, mortgage, and income rules into transparent tools.")
]

for p_title, p_desc in projects_cv:
    p_pr = doc.add_paragraph(style='List Bullet')
    p_pr.paragraph_format.space_before = Pt(0)
    p_pr.paragraph_format.space_after = Pt(1.5)
    p_pr.paragraph_format.line_spacing = 1.1
    r_pt = p_pr.add_run(p_title)
    r_pt.bold = True
    r_pt.font.name = "Calibri"
    r_pt.font.size = Pt(9)
    r_pt.font.color.rgb = COLOR_NAVY
    r_pd = p_pr.add_run(p_desc)
    r_pd.font.name = "Calibri"
    r_pd.font.size = Pt(9)
    r_pd.font.color.rgb = COLOR_CHARCOAL

# 7. PUBLICATIONS & POLICY CONTRIBUTIONS
add_heading_1("Selected Publications & Policy Contributions")
pubs_cv = [
    ("Journal Article: ", "Administrative Reach and State Capacity: Interoperability Failures in Nigeria's Digital Identification Infrastructure. International Journal of Development and Economic Sustainability, Vol. 14(1), pp. 33–44 (2026). DOI: 10.37745/ijdes.13/vol14n13344"),
    ("Journal Article: ", "Dynamics of Foreign Direct Investment and Economic Growth in SADC Countries: A Panel Data Analysis. Journal of Cultural Analysis and Social Change, Vol. 11(2), pp. 222–230 (2026)."),
    ("Regulatory Submission (Ofgem): ", "Consultation response on open data standards in the energy sector, focusing on data validation, schema stability, and accessibility for smaller users (2024)."),
    ("Regulatory Submission (ICO): ", "Consultation submission on automated decision-making and profiling under UK GDPR Article 22, examining SME impacts and vendor accountability (2024)."),
    ("Practitioner Submission (HMRC): ", "Practitioner note on Making Tax Digital for Income Tax, introducing behavioural reporting noise and triage safeguards (2024).")
]

for p_tag, p_detail in pubs_cv:
    p_pb = doc.add_paragraph(style='List Bullet')
    p_pb.paragraph_format.space_before = Pt(0)
    p_pb.paragraph_format.space_after = Pt(1.5)
    p_pb.paragraph_format.line_spacing = 1.1
    r_tag = p_pb.add_run(p_tag)
    r_tag.bold = True
    r_tag.font.name = "Calibri"
    r_tag.font.size = Pt(9)
    r_tag.font.color.rgb = COLOR_NAVY
    r_det = p_pb.add_run(p_detail)
    r_det.font.name = "Calibri"
    r_det.font.size = Pt(9)
    r_det.font.color.rgb = COLOR_CHARCOAL

doc.save("public/Daramola_Joseph_Omoyele_CV.docx")
print("Saved public/Daramola_Joseph_Omoyele_CV.docx successfully")
