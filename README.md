# Daramola Joseph Omoyele — Professional Portfolio

🌐 **Live Website:** https://daramolajo.co.uk  
🏢 **Business Website:** https://jomovate.com  

Professional portfolio website for **Daramola Joseph Omoyele** — Data & Research Analyst specialising in Economic Analysis & Business Intelligence, presented alongside **Jomovate Digital Labs**, the digital solutions and applied research studio he founded.

---

## Purpose & Professional Positioning

This portfolio positions Daramola Joseph Omoyele primarily as a **Data and Research Analyst** with core strengths in:
- **Statistical Analysis & Economic Research** — peer-reviewed journal articles, working papers, econometric models (Panel ARDL), price index construction, and independent regulatory submissions
- **Performance Analytics & Business Intelligence** — KPI monitoring, management decision support, operational insights, and dashboard systems in Power BI, Tableau, Shiny, and Excel
- **Digital Product Development & Automation** — interactive analytical web applications (Streamlit/Python), financial calculation engines, and user-centred digital platforms
- **Professional Experience** — 15+ years spanning public sector analytics, economic modelling, academic administration, and product business analysis

---

## Brand Identity

| Element | Value |
|---|---|
| Personal Brand | Daramola Joseph Omoyele |
| Business Brand | Jomovate Digital Labs (Founder) |
| Tagline | Data-driven tools for smarter decisions |
| Navy | `#082554` |
| Green | `#16864C` |
| Gold | `#C49A2C` |
| Background | `#F8FAFC` |
| Heading font | Poppins (600 / 700 / 800) |
| Body font | Inter (400 / 500 / 600) |

---

## Featured Analytical Products & Applications

| Project | Category | Positioning / Description | Live URL / Status |
|---|---|---|---|
| **UK AI Economic Measurement Lab** | Data & Analytics / Economic Research | Independent research prototype exploring UK National Accounts classification, SUT frameworks, and AI activity disaggregation | [ai-measurement.jomovate.com](https://ai-measurement.jomovate.com) |
| **Price Quality Explorer** | Data & Analytics / Economic Research | Statistical methodology, price-index construction (Jevons/Carli/Dutot), anomaly detection & data quality | [pricequality.streamlit.app](https://pricequality.streamlit.app/) |
| **Performance Insight Explorer** | Data & Analytics | Operational KPI intelligence, comparative benchmarks & decision support | [performance-insight-explorer.streamlit.app](https://performance-insight-explorer.streamlit.app/performance_overview) |
| **Care Quality Intelligence (CQI)** | Data Analytics / Healthcare | Quality monitoring, risk board, workforce supervision & regulatory evidence | [cqi.carephrase.com](https://cqi.carephrase.com) |
| **UKCalc Platform** | FinTech & Tools / Business Apps | UK tax, mortgage, savings & financial calculation tools | [ukcalc.jomovate.com](https://ukcalc.jomovate.com/) |
| **CarePhrase** | Healthcare & Communication | Healthcare communication & clinical note documentation quality | [carephrase.com](https://carephrase.com) |
| **TaxMate UK** | FinTech & Tools / Business Apps | Sole-trader bookkeeping, financial KPIs & HMRC deadline tracking | [taxmate.omoyelejd.co.uk](https://taxmate.omoyelejd.co.uk/) |
| **GarageProof UK** | Business Apps / Automotive | Garage repair workflow, digital audit trail & customer approval | In Development |
| **AutoDamage Quote** | Business Apps / Automotive | Vehicle damage assessment & algorithmic repair quotation engine | In Development |
| **CarePhrase Academy** | Healthcare / Digital Learning | Care communication, clinical handover & safeguarding training | [comms.carephrase.com](https://comms.carephrase.com) |
| **Professional Speaking Trainer** | Digital Learning / Business Apps | Interactive speaking practice, speech analytics & real-time feedback | [speech.omoyelejd.co.uk](https://speech.omoyelejd.co.uk) |
| **DEAP Tax Compliance** | FinTech / Data Analytics | Multi-source tax data aggregation & compliance dashboards | [deaptaxcompliance.netlify.app](https://deaptaxcompliance.netlify.app/) |
| **UBA Pulse** | Data & Analytics / Business Apps | Executive business intelligence & operational KPI prototype | [ubapulse.netlify.app](https://ubapulse.netlify.app/) |
| **NairaGuard** | FinTech & Security / Business Apps | Proof-of-concept currency verification & security education | [daramol.netlify.app](https://daramol.netlify.app/) |
| **Kogi Quest** | Community / Websites | Regional civic engagement & local development initiative platform | [dju78.github.io/kogiqest](https://dju78.github.io/kogiqest/) |
| **Takete-Ide Platform & Celebration Studio** | Community / Digital Tools | Cultural heritage archives & private in-browser centenary Celebration Studio | [takete-ide.org](https://takete-ide.org/) |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Static Site Generator | [Eleventy (11ty)](https://www.11ty.dev/) v3.x |
| Templating | Nunjucks (`.njk`) |
| Content | Markdown with YAML front matter |
| Styles | Plain CSS (custom properties, CSS Grid, Flexbox) |
| Fonts | Google Fonts — Poppins + Inter |
| Deployment | Netlify |

---

## Development & Build Instructions

**Install dependencies:**
```bash
npm install
```

**Start dev server** (live reload):
```bash
npm run start
```

**Build for production** (outputs to `_site/`):
```bash
npm run build
```

**Generate downloadable CV files:**
```bash
# Generates ATS-friendly PDF CV
python generate_pdf_cv.py

# Generates editable ATS-friendly Word CV (.docx)
python generate_docx_cv.py
```

---

## Adding Future Projects

To add a new project to the portfolio:
1. Create a markdown file in `src/content/projects/` (e.g. `16-new-project.md`).
2. Include the following YAML frontmatter schema:
```markdown
---
title: "Project Name"
client: "Domain / Focus Area / Solution Type"
badge: "Live Analytical App" # or "Live Platform", "Research Prototype", "In Development"
status: "Live" # or "In Development", "Prototype"
order: 17
categories:
  - "data-analytics" # Choose from: data-analytics, economic-research, health-care, fintech, business-applications, websites-platforms
description: "A concise 1-2 sentence description explaining the problem, solution, and decision value."
link: "https://your-project-url.com" # or "#" if in development
highlights:
  - text: "Key analytical feature or technical capability"
  - text: "Measurable or verifiable outcome"
tech:
  - tag: "Python"
  - tag: "Streamlit"
  - tag: "SQL"
---
```
3. Run `npm run build` to verify the new project automatically compiles into both the homepage previews and the dedicated `/projects/` filterable catalogue.

---

## Copyright & Ownership

© 2026 Daramola Joseph Omoyele. All rights reserved.  
Founder, Jomovate Digital Labs (https://jomovate.com).
