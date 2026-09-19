# Daramola Digital Labs — Portfolio

🌐 **Live Website:** https://daramolajo.co.uk

Professional portfolio website for **Daramola Joseph Omoyele** — Data Analyst, Research Analyst, Performance Analyst, and Digital Product Builder — presented under the **Daramola Digital Labs** brand.

---

## Purpose

This portfolio showcases the intersection of:
- **Statistical Analysis & Research** — peer-reviewed journal articles, working papers, books, econometric models, and policy submissions
- **Performance Analytics & Business Intelligence** — KPI monitoring, management decision support, operational insights, and dashboard systems
- **Automation & Digital Products** — interactive analytical web applications, calculation engines, and user-centred digital platforms
- **Professional Experience** — 15+ years across public sector analytics, economic modelling, and consulting

---

## Brand Identity

| Element       | Value                                      |
|---------------|--------------------------------------------|
| Brand name    | Daramola Digital Labs                      |
| Tagline       | Data-driven tools for smarter decisions    |
| Navy          | `#082554`                                  |
| Green         | `#16864C`                                  |
| Gold          | `#C49A2C`                                  |
| Background    | `#F8FAFC`                                  |
| Heading font  | Poppins (700 / 800 / 900)                  |
| Body font     | Inter (400 / 500 / 600)                    |

---

## Featured Analytical Products & Applications

| Project | Category | Positioning / Description | Live URL |
|---|---|---|---|
| **Price Quality Explorer** | Data & Analytics | Statistical methodology, price-index construction (Jevons/Carli/Dutot), anomaly detection & data quality | [pricequality.streamlit.app](https://pricequality.streamlit.app/) |
| **Performance Insight Explorer** | Data & Analytics | Operational KPI intelligence, comparative benchmarks & decision support | [performance-insight-explorer.streamlit.app](https://performance-insight-explorer.streamlit.app/performance_overview) |
| **Care Quality Intelligence (CQI)** | Data & Analytics / Health | Quality monitoring, risk board, workforce supervision & regulatory evidence | [cqi.carephrase.com](https://cqi.carephrase.com) |
| **UKCalc Platform** | FinTech & Tools | UK tax, mortgage, savings & financial calculation tools | [ukcalc.jomovate.com](https://ukcalc.jomovate.com/) |
| **CarePhrase** | Health & Care | Healthcare communication & clinical note documentation quality | [carephrase.com](https://carephrase.com) |
| **TaxMate UK** | FinTech & Tools | Sole-trader bookkeeping, financial KPIs & HMRC deadline tracking | [taxmate.omoyelejd.co.uk](https://taxmate.omoyelejd.co.uk/) |
| **GarageProof UK** | Automotive Tech | Garage repair workflow, digital audit trail & customer approval | In Development |
| **AutoDamage Quote** | Automotive Tech | Vehicle damage assessment & algorithmic repair quotation engine | In Development |
| **CarePhrase Academy** | Digital Learning | Care communication, clinical handover & safeguarding training | [comms.carephrase.com](https://comms.carephrase.com) |
| **Professional Speaking Trainer** | Digital Learning | Interactive speaking practice, speech analytics & real-time feedback | [speech.omoyelejd.co.uk](https://speech.omoyelejd.co.uk) |
| **DEAP Tax Compliance** | FinTech / Data | Multi-source tax data aggregation & compliance dashboards | [deaptaxcompliance.netlify.app](https://deaptaxcompliance.netlify.app/) |
| **UBA Pulse** | Data & Analytics | Executive business intelligence & operational KPI prototype | [ubapulse.netlify.app](https://ubapulse.netlify.app/) |
| **NairaGuard** | FinTech & Security | AI-assisted currency verification prototype & security education | [daramol.netlify.app](https://daramol.netlify.app/) |
| **Kogi Quest** | Community | Regional civic engagement & local development initiative platform | [dju78.github.io/kogiqest](https://dju78.github.io/kogiqest/) |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Static Site Generator | [Eleventy (11ty)](https://www.11ty.dev/) v3.x |
| Templating | Nunjucks (`.njk`) |
| Content | Markdown with YAML front matter |
| Styles | Plain CSS (custom properties, CSS Grid, Flexbox) |
| Fonts | Google Fonts — Poppins + Inter |
| CMS | Netlify CMS (admin at `/admin`) |
| Deployment | Netlify |

---

## Development

**Install dependencies:**
```bash
npm install
```

**Start dev server** (live reload, port 8080):
```bash
npm run start
```

**Build for production** (outputs to `_site/`):
```bash
npm run build
```

---

## Project Structure

```
src/
├── index.njk                    # Homepage template
├── projects.njk                 # Dedicated projects & products catalog
├── styles.css                   # All styling
├── script.js                    # Interactive navigation, multi-category filters & counters
├── images/                      # Media assets & profile photography
├── admin/                       # Netlify CMS configuration
└── content/
    ├── projects/                # 15 structured analytical and digital product entries
    ├── journal-articles/        # Peer-reviewed journal articles
    ├── working-papers/          # Preprints & working papers
    ├── books/                   # Published books & handbooks
    ├── media/                   # Policy commentary & media features
    ├── research/                # Academic dissertations
    └── awards/                  # Honours & recognitions
```

---

## Copyright

© 2026 Daramola Digital Labs. All rights reserved.
Portfolio of Daramola Joseph Omoyele.
