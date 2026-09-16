# Global Business Problem Discovery Dashboard

## Overview
The **Global Business Problem Discovery Dashboard** is a data-driven tool designed to collect, validate, analyze, and visualize complex business challenges across industries and regions worldwide.

## Features
- **JSON Schema Validation**: Strict data structure enforcement for sample problem datasets.
- **Interactive Web Dashboard**: Dynamic visualization of business problems by industry, severity, impact, and region.
- **Automated Dashboard Generation**: Python script to build `index.html` directly from data files.
- **Automated Startup Scripts**: Windows `.bat` and PowerShell scripts for quick launch and service management.

## Project Structure
```
├── Launch Dashboard.bat
├── start_dashboard.bat
├── stop_dashboard.bat
├── setup_autostart.ps1
├── index.html
├── PROMPT.md
├── README.md
├── .gitignore
├── prompts/
│   └── master_prompt.md
├── schema/
│   └── schema.json
├── data/
│   ├── sample_problems.json
│   └── sample_problems.csv
├── scripts/
│   ├── __init__.py
│   ├── validate_schema.py
│   └── generate_dashboard.py
├── tests/
│   ├── __init__.py
│   └── test_dashboard.py
└── Global_Business_Problem_Dashboard.zip
```

## Quick Start
1. **Validate Data**:
   ```bash
   python scripts/validate_schema.py
   ```
2. **Generate Dashboard**:
   ```bash
   python scripts/generate_dashboard.py
   ```
3. **Run Unit Tests**:
   ```bash
   python -m unittest discover -s tests
   ```
4. **Launch Dashboard**:
   Open `index.html` in any browser or launch a local web server on port 8000:
   ```bash
   python -m http.server 8000
   ```
