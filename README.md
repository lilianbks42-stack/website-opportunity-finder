# Website Opportunity Finder

An AI-assisted prospecting agent that looks for publicly visible signs of
**commercial intent** — people or businesses publicly saying they need a
website, landing page, or better online presence — and turns those signals
into a scored, human-reviewed lead list.

This is **not** a scraper that logs into private accounts or pulls data from
restricted/private sources. It is designed to work only with public,
permitted data sources (search engines, public APIs, public posts), and to
be source-agnostic so sources can be added or removed later.

## Status

🚧 **Phase 1: Foundation.** This starter repository just confirms the
project runs. No real search source is connected yet.

## Project structure

```
website-opportunity-finder/
├── agent/
│   ├── __init__.py
│   ├── main.py          # entry point — confirms the project runs
│   ├── intent_terms.py  # phrases that signal "I need a website" intent
│   ├── scorer.py        # opportunity scoring logic (0-100)
│   └── leads.py         # lead data structure + saving leads
├── config/
│   └── __init__.py
├── data/
│   └── .gitkeep         # leads will eventually be saved here
├── tests/
│   ├── __init__.py
│   └── test_scorer.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Roadmap

1. **Foundation** — project skeleton runs (this repo, right now)
2. **Search** — connect a permitted public search/data source
3. **AI analysis** — classify intent, business, industry, location, etc.
4. **Scoring** — automatic 0-100 opportunity score
5. **Storage** — save qualified leads (CSV / Google Sheets)
6. **Outreach assistant** — AI drafts a personalized message; human approves
7. **Dashboard/automation** — recurring searches, filters, dedupe, etc.

## Getting started

See the setup walkthrough provided alongside this repo. In short:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python agent/main.py
```

## Scoring model (initial, will be refined)

| Signal                          | Points |
|----------------------------------|--------|
| Explicit website request         | +35    |
| Explicit landing-page request    | +40    |
| No website found                 | +25    |
| Active business/social presence  | +15    |
| Public business contact          | +10    |
| Established business             | +10    |

**Labels:** 90-100 HOT · 70-89 WORTH REVIEW · 50-69 POTENTIAL · below 50 LOW PRIORITY
