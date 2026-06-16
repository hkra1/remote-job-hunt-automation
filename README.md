# Remote Job Hunt Automation

**Professional toolkit for automating remote job applications with ethical AI assistance.** Inspired by high standards from NASA open source projects.

## Overview
This repository provides scripts, tools, and workflows to streamline your remote job hunt:
- Automated job discovery
- AI resume & cover letter tailoring
- Application tracking dashboard
- Integration with platforms like Workday, Greenhouse, Indeed

**⚠️ Important**: Use responsibly. Respect platform TOS. Automation is for efficiency, not spam.

## Features
- Modular Python scripts
- LLM integration (OpenAI/Groq/etc.)
- Spreadsheet tracking
- Browser automation options (Playwright)

## Repository Structure (NASA-style)
```
.
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── requirements.txt
├── .env.example
├── src/              # Core modules
│   ├── __init__.py
│   ├── job_discovery.py
│   ├── resume_tailor.py
│   ├── tracker.py
│   └── utils.py
├── data/             # Resumes, tracking CSVs
├── docs/             # Guides & architecture
├── notebooks/        # Experimentation
└── templates/        # Resume & letter templates
```

## Quick Start
1. `git clone https://github.com/hkra1/remote-job-hunt-automation.git`
2. `cd remote-job-hunt-automation`
3. `python -m venv venv && source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `cp .env.example .env` and add your keys
6. Place master resume in `data/master_resume.pdf`

Run examples in `src/`.

## Development
See CONTRIBUTING.md

## License
MIT License - see [LICENSE](LICENSE)