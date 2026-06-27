# Daramola Digital Labs — Portfolio

🌐 **Live Website:** https://daramolajo.co.uk

Professional portfolio website for **Daramola Joseph Omoyele** — Research Analyst, Data Analyst, and AI Product Builder — presented under the **Daramola Digital Labs** brand.
---

## Purpose

This portfolio showcases:
- **Digital products** — CarePhrase UK, TaxMate UK, Speaking Trainer, DEAP, GACE, Kogi Quest
- **Research & publications** — peer-reviewed journal articles, working papers, books and policy commentary
- **Professional experience** — 15+ years across public sector and consulting
- **Skills & certifications** — econometrics, data science, compliance analytics, visualisation

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

## Featured Projects

| Project | Category | URL |
|---|---|---|
| CarePhrase | Healthcare Communication | https://carephrase.com |
| CarePhrase Communication Academy | AI Communication Training | https://comms.carephrase.com |
| TaxMate UK | Tax & Compliance Platform | https://taxmate.omoyelejd.co.uk |
| Speaking Trainer | AI Language Coach | https://speech.omoyelejd.co.uk |
| DEAP | Data Analytics Platform | https://deaptaxcompliance.netlify.app |
| GACE | Governance & Accountability | — |
| Kogi Quest | Tourism & Discovery | https://dju78.github.io/kogiquest |
| Research & Publications | Academic & Policy Output | See Publications section |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Static Site Generator | [Eleventy (11ty)](https://www.11ty.dev/) v3.x |
| Templating | Nunjucks (`.njk`) |
| Content | Markdown with YAML front matter |
| Styles | Plain CSS (custom properties, Grid, Flexbox) |
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
├── index.njk                    # Main page template
├── styles.css                   # All styles
├── script.js                    # JS — nav, counters, filters, read-more
├── images/                      # Images (profile photo, books, awards)
├── admin/                       # Netlify CMS config
└── content/
    ├── projects/                # Project markdown files
    ├── journal-articles/        # Published journal articles
    ├── working-papers/          # Preprints & working papers
    ├── books/                   # Books & handbooks
    ├── media/                   # Policy commentary & media
    ├── research/                # Academic dissertations
    └── awards/                  # Awards & honours
```

### Adding your profile photo

Place your professional headshot at:
```
src/images/profile-photo.jpg
```
The hero section will automatically display it inside the gold circular frame.

---

## Deployment

Deployed via **Netlify** from the `main` branch. Every push triggers an automatic rebuild.

Configuration: `netlify.toml`

---

## Copyright

© 2026 Daramola Digital Labs. All rights reserved.
Portfolio of Daramola Joseph Omoyele.
