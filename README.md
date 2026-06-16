# Remote Job Hunt Automation

**Professional toolkit for automating your remote job search ethically and efficiently.**

## Overview
This repo helps automate job discovery, resume/cover letter tailoring, application tracking for platforms like Workday, Greenhouse, Indeed, LinkedIn etc.

**⚠️ Ethical Use Only**: Respect ToS. Review all applications manually. No spam.

## Features
- AI-powered resume & cover letter tailoring
- Job search aggregation
- Application tracker (CSV/Excel)
- Modular Python scripts
- Ready for browser automation

## Quick Start
1. Clone the repo
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add API keys
4. Add your master resume to `data/master_resume.docx` or `.pdf`
5. Run scripts in `src/`

## Structure
```
.
├── src/                 # Main Python modules
├── data/                # Your resumes, job data
├── templates/           # Resume & letter templates
├── docs/                # Documentation
├── tests/               # Unit tests
├── .github/workflows/   # CI/CD
├── requirements.txt
├── LICENSE
└── README.md
```

See `docs/` for details.