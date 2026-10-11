import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, ListFlowable, ListItem
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
import pypdf

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 0.5 * inch, 0.35 * inch, page_text)
        self.drawString(0.5 * inch, 0.35 * inch, "Daramola Joseph Omoyele  —  Data & Research Analyst  —  info@jomovate.com")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(0.5 * inch, 0.48 * inch, 8.5 * inch - 0.5 * inch, 0.48 * inch)
        self.restoreState()

def build_pdf():
    pdf_filename = "public/Daramola_Joseph_Omoyele_CV.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.55 * inch
    )

    styles = getSampleStyleSheet()

    # Colors
    c_navy = colors.HexColor("#082554")
    c_text = colors.HexColor("#1E293B")
    c_muted = colors.HexColor("#64748B")
    c_accent = colors.HexColor("#16864C")

    # Typography styles
    styles.add(ParagraphStyle(
        'CVName',
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=19,
        textColor=c_navy,
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        'CVTitle',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=c_accent,
        spaceAfter=3
    ))

    styles.add(ParagraphStyle(
        'CVContact',
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=c_muted,
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        'CVHeading',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=c_navy,
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'CVBody',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=c_text,
        spaceAfter=3
    ))

    styles.add(ParagraphStyle(
        'CVRoleTitle',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11.5,
        textColor=c_navy
    ))

    styles.add(ParagraphStyle(
        'CVRoleCompany',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=c_text
    ))

    styles.add(ParagraphStyle(
        'CVRoleDate',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        alignment=2, # Right aligned
        textColor=c_muted
    ))

    styles.add(ParagraphStyle(
        'CVRoleFocus',
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#475569"),
        spaceBefore=1,
        spaceAfter=2,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'CVBullet',
        fontName='Helvetica',
        fontSize=8.2,
        leading=10.5,
        textColor=c_text,
        spaceBefore=1,
        spaceAfter=1
    ))

    story = []

    # 1. HEADER
    story.append(Paragraph("DARAMOLA JOSEPH OMOYELE", styles['CVName']))
    story.append(Paragraph("Data &amp; Research Analyst | Economic Analysis &amp; Business Intelligence", styles['CVTitle']))
    contact_text = (
        "Colchester, Essex, UK  |  info@jomovate.com  |  Alternative email: dju78@yahoo.com<br/>"
        "Portfolio: daramolajo.co.uk  |  Business: jomovate.com  |  "
        "LinkedIn: linkedin.com/in/joseph-omoyele-bbb006244/  |  "
        "GitHub: github.com/dju78  |  ORCID: 0009-0006-0347-0499"
    )
    story.append(Paragraph(contact_text, styles['CVContact']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceBefore=1, spaceAfter=4))

    # 2. PROFESSIONAL SUMMARY
    story.append(Paragraph("PROFESSIONAL SUMMARY", styles['CVHeading']))
    summary_text = (
        "Data and Research Analyst with extensive experience turning complex data into clear insights and practical decision-support tools. "
        "Combines statistical analysis, economic research, business intelligence, and digital product development to solve operational and "
        "policy challenges. Holds an MSc in Economics with Data Analytics (Merit) from the University of Essex. Published researcher with peer-reviewed "
        "articles in development economics and institutional analysis, an active contributor to UK regulatory consultations, and founder of Jomovate Digital Labs."
    )
    story.append(Paragraph(summary_text, styles['CVBody']))

    # 3. CORE TECHNICAL & ANALYTICAL SKILLS
    story.append(Paragraph("CORE TECHNICAL &amp; ANALYTICAL SKILLS", styles['CVHeading']))
    skills_table_data = [
        [
            Paragraph("<b>Analysis &amp; Modelling:</b>", styles['CVBody']),
            Paragraph("Econometric modelling, forecasting, cost-benefit analysis, price-index construction (Jevons, Carli, Dutot), composite indices, Panel ARDL, anomaly detection, scenario analysis", styles['CVBody'])
        ],
        [
            Paragraph("<b>Languages &amp; BI Tools:</b>", styles['CVBody']),
            Paragraph("R, Python (Streamlit, Pandas, NumPy), SQL, Advanced Excel, Power BI, Tableau, Shiny", styles['CVBody'])
        ],
        [
            Paragraph("<b>Product &amp; Applications:</b>", styles['CVBody']),
            Paragraph("User &amp; business requirements gathering, interactive dashboards, calculation engines, REST APIs, TypeScript, React, QA testing &amp; validation", styles['CVBody'])
        ],
        [
            Paragraph("<b>Governance &amp; Quality:</b>", styles['CVBody']),
            Paragraph("GDPR-aligned data handling, reproducible data pipelines, regulatory evidence documentation, tax compliance analytics", styles['CVBody'])
        ]
    ]
    t_skills = Table(skills_table_data, colWidths=[1.5 * inch, 6.0 * inch])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_skills)

    # 4. PROFESSIONAL EXPERIENCE
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", styles['CVHeading']))

    def make_exp_entry(title, company, date_str, focus, bullets):
        row = [
            Paragraph(f"<b>{title}</b> — {company}", styles['CVRoleTitle']),
            Paragraph(date_str, styles['CVRoleDate'])
        ]
        t = Table([row], colWidths=[5.5 * inch, 2.0 * inch])
        t.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ]))
        story.append(t)
        if focus:
            story.append(Paragraph(f"<b>Focus:</b> {focus}", styles['CVRoleFocus']))
        for b in bullets:
            story.append(Paragraph(f"• {b}", styles['CVBullet']))
        story.append(Spacer(1, 3))

    make_exp_entry(
        title="Founder &amp; Product Business Analyst",
        company="Jomovate Digital Labs (jomovate.com)",
        date_str="July 2024 – Present",
        focus="Founded venture to develop data-driven solutions, conduct applied research, and engineer decision-support tools and analytical dashboards.",
        bullets=[
            "Gather and document user and business requirements, translating operational and analytical questions into digital products and decision tools.",
            "Engineered specialized analytical platforms including the UK AI Economic Measurement Lab, Price Quality Explorer, and UKCalc financial platform.",
            "Perform rigorous testing, data validation, calculation verification, and quality assurance across data pipelines and interactive web dashboards.",
            "Develop product documentation, methodology guides, and user-centred workflows; explore practical AI integrations for reporting.",
        ]
    )

    make_exp_entry(
        title="Data Analytics | Financial Analyst &amp; Business Intelligence",
        company="Univelcity Computing",
        date_str="July 2023 – Present",
        focus="Delivering financial, operational, survey, and research data analysis, predictive modelling, and interactive dashboards.",
        bullets=[
            "Deliver financial, operational, survey, and research data analysis for development programmes and business research.",
            "Apply econometric modelling, forecasting, cost-benefit analysis, risk assessments, and scenario analysis across multi-currency environments.",
            "Design and maintain automated dashboards and decision tools in Power BI, Tableau, Shiny, and Excel, streamlining stakeholder access to timely insights.",
            "Execute data preparation, ETL, and reporting pipelines using R, Python, SQL, and Excel to identify trends, risks, and performance gaps.",
            "Produce clear analytical summaries and policy briefings communicating complex findings to non-technical stakeholders.",
            "Strengthen data quality, governance, and GDPR-aligned handling across projects; mentor junior analysts and provide analytical quality assurance."
        ]
    )

    make_exp_entry(
        title="Financial Analyst",
        company="Nigerian Postal Service",
        date_str="January 2014 – September 2022",
        focus="Financial data evaluation, operational budgeting, revenue/cost variance reporting, and operational efficiency analysis.",
        bullets=[
            "Analysed nationwide operational, financial, and socioeconomic datasets to support service delivery planning and management reporting.",
            "Built forecasting models and performance monitoring tools to identify regional efficiency gaps and operational intervention points.",
            "Designed composite performance indices to benchmark regional facility performance and support objective resource allocation decisions.",
            "Produced analytical briefings and management summaries translating operational data into actionable service improvement recommendations.",
            "Strengthened survey design, data collection protocols, reporting standards, and data quality assurance across regional facilities."
        ]
    )

    make_exp_entry(
        title="Data Analyst/Admin",
        company="City College of Education",
        date_str="January 2008 – December 2013",
        focus="Institutional record keeping, student and administrative data verification, academic reporting, and attendance analysis.",
        bullets=[
            "Maintained assessment records and student reporting databases, strengthening institutional documentation standards and compliance.",
            "Compiled departmental reports and learning performance data to support evidence-informed learner support and curriculum planning.",
            "Liaised with academic faculty and management to enhance reporting quality and student progression tracking."
        ]
    )

    # 5. EDUCATION
    story.append(Paragraph("EDUCATION", styles['CVHeading']))
    edu_row1 = [
        Paragraph("<b>MSc Economics with Data Analytics (Merit)</b> — University of Essex", styles['CVRoleTitle']),
        Paragraph("2023", styles['CVRoleDate'])
    ]
    t_e1 = Table([edu_row1], colWidths=[5.5 * inch, 2.0 * inch])
    t_e1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_e1)
    story.append(Paragraph("<i>Dissertation:</i> Impact of Foreign Direct Investment on Economic Growth in Sub-Saharan Africa (Panel ARDL across 39 countries, 1970–2019, integrating World Bank, IMF, UNCTAD datasets).", styles['CVRoleFocus']))

    edu_row2 = [
        Paragraph("<b>BSc Economics</b> — University of Ilorin", styles['CVRoleTitle']),
        Paragraph("2006", styles['CVRoleDate'])
    ]
    t_e2 = Table([edu_row2], colWidths=[5.5 * inch, 2.0 * inch])
    t_e2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_e2)

    # 6. SELECTED ANALYTICAL PROJECTS & DIGITAL PRODUCTS
    story.append(Paragraph("SELECTED ANALYTICAL PROJECTS &amp; DIGITAL PRODUCTS", styles['CVHeading']))
    proj_items = [
        ("UK AI Economic Measurement Lab (ai-measurement.jomovate.com):", "Independent research prototype exploring National Accounts classification, Supply & Use tables, and disaggregation of AI economic activity (Python/Streamlit)."),
        ("Price Quality Explorer (pricequality.streamlit.app):", "Methodological application demonstrating automated data quality auditing, anomaly detection, and elementary price-index calculation (Jevons, Carli, Dutot)."),
        ("Performance Insight Explorer (performance-insight-explorer.streamlit.app):", "Executive decision-support tool transforming operational datasets into KPI benchmarks and trend intelligence."),
        ("Care Quality Intelligence (cqi.carephrase.com):", "Health and social care analytics dashboard delivering quality monitoring, risk oversight, and regulatory audit evidence (React/TypeScript)."),
        ("UKCalc Platform (ukcalc.jomovate.com):", "Financial calculation platform translating complex UK statutory tax, mortgage, and income rules into transparent tools.")
    ]
    for p_label, p_desc in proj_items:
        story.append(Paragraph(f"• <b>{p_label}</b> {p_desc}", styles['CVBullet']))

    # 7. SELECTED PUBLICATIONS & POLICY CONTRIBUTIONS
    story.append(Paragraph("SELECTED PUBLICATIONS &amp; POLICY CONTRIBUTIONS", styles['CVHeading']))
    pub_items = [
        ("Journal Article:", "Administrative Reach and State Capacity: Interoperability Failures in Nigeria's Digital Identification Infrastructure. International Journal of Development and Economic Sustainability, Vol. 14(1), pp. 33–44 (2026). DOI: 10.37745/ijdes.13/vol14n13344"),
        ("Journal Article:", "Dynamics of Foreign Direct Investment and Economic Growth in SADC Countries: A Panel Data Analysis. Journal of Cultural Analysis and Social Change, Vol. 11(2), pp. 222–230 (2026)."),
        ("Regulatory Submission (Ofgem):", "Consultation response on open data standards in the energy sector, focusing on data validation, schema stability, and accessibility for smaller users (2024)."),
        ("Regulatory Submission (ICO):", "Consultation response on automated decision-making and profiling under UK GDPR Article 22, examining SME impacts and vendor accountability (2024)."),
        ("Practitioner Submission (HMRC):", "Practitioner note on Making Tax Digital for Income Tax, introducing behavioural reporting noise and triage safeguards (2024).")
    ]
    for pub_label, pub_desc in pub_items:
        story.append(Paragraph(f"• <b>{pub_label}</b> {pub_desc}", styles['CVBullet']))

    doc.build(story, canvasmaker=NumberedCanvas)
    
    # Check page count
    reader = pypdf.PdfReader(pdf_filename)
    print(f"Generated {pdf_filename} successfully with {len(reader.pages)} page(s).")

if __name__ == "__main__":
    build_pdf()
