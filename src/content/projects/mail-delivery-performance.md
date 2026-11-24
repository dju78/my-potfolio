---
title: "Regional Mail Delivery Performance and Support Decision"
client: "Operations Analytics / Service Delivery / Decision Support"
badge: "Power BI Report"
order: 0.2
categories:
  - "data-analytics"
description: "A three-page Power BI report that tracks on-time mail delivery, late items and unit cost across six zones from 2016 to 2018, then ranks zones and states to recommend where delivery support should go first in January 2019."
image: "/images/projects/mail-delivery-overview.jpg"
gallery:
  - src: "/images/projects/mail-delivery-decision.jpg"
    caption: "January 2019 support decision page"
foot_label: "Power BI report: screenshots shown"
highlights:
  - text: "Executive overview of items due, on-time delivery rate, late items, cost per eligible item and actual against plan, with year, quarter, zone and state slicers."
  - text: "Support priority index that scores zones and states on late items, workload per delivery FTE and cost, weighted 50/30/20."
  - text: "Same-month prior-year forecast for January 2019, chosen after backtesting it against a three-month average."
  - text: "Weight sensitivity check showing the top-ranked zone stays first under all three weightings tested."
tech:
  - tag: "Power BI"
  - tag: "DAX"
  - tag: "Power Query"
  - tag: "Forecasting"
  - tag: "Decision Analysis"
  - tag: "Operational Performance"
case_study:
  problem: "Decide which delivery zone, and which state within it, should receive extra support first, using three years of monthly delivery, staffing and cost records."
  contribution: "Designed and built all three report pages, from the executive overview to the scored recommendation and the methodology notes."
  methods: "Summed totals for rates; each metric scaled against the highest value among the units scored; weighted priority index with sensitivity tests at 50/30/20, equal and 40/40/20; forecast method selected by backtest error."
  functionality: "Slicers filter the overview by year, quarter, zone and state. The decision page ranks six zones, then drills into the states of the shortlisted zone, and states a recommended first action with the checks to make before deploying staff."
  limitations: "Workload and cost are treated as signals to investigate, not proof of need. Delivery FTE is a staffing proxy, and a high cost per item is checked against how operating cost is allocated before it is read as inefficiency."
---
