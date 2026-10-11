---
title: "Price Quality Explorer"
client: "Statistical Methodology / Price Analysis / Data Quality"
badge: "Live Analytical App"
order: 2
categories:
  - "data-analytics"
  - "economic-research"
description: "An interactive Python and Streamlit analytical application demonstrating a structured, reproducible approach to price-data quality assessment and elementary price-index construction."
image: "/images/screenshot_price_quality.png"
link: "https://pricequality.streamlit.app/"
highlights:
  - text: "Automated data-quality checks, anomaly detection & scale-error identification"
  - text: "Zero/unavailable observation handling with audit trail and original data preservation"
  - text: "Matched-item price comparisons with Jevons geometric index, Carli & Dutot comparators"
  - text: "Year-on-year, category-level and seasonality exploration with sensitivity analysis"
tech:
  - tag: "Python"
  - tag: "Streamlit"
  - tag: "Statistical Methodology"
  - tag: "Price Indices"
  - tag: "Data Quality"
  - tag: "Data Visualisation"
  - tag: "Reproducible Analysis"
case_study:
  problem: "Raw price collection data frequently contains scale anomalies, missing or zero values, item substitution gaps, and seasonal collection irregularities that distort consumer and producer price index calculations if not systematically audited."
  contribution: "Developed an interactive analytical application providing automated data quality auditing, scale error identification, and reproducible elementary price-index construction."
  methods: "Elementary price index calculation comparing Jevons geometric mean, Carli arithmetic mean, and Dutot ratio-of-averages; automated distribution auditing; anomaly flagging; seasonality decomposition."
  functionality: "Interactive dataset upload or pre-loaded retail price series; automated outlier and scale diagnostic panels; matched-item index comparisons with full audit trails and formula documentation."
  limitations: "Demonstrator focused on elementary aggregate index levels; does not compute higher-level weighted Laspeyres/Törnqvist aggregations without expenditure weight datasets."
---
