# LinkedIn Job Market Analysis (2023–2024)



**What:** Explore skill demand, locations, and compensation signals from large LinkedIn job datasets (cleaned + aggregated).  

**Why:** Identify high-demand skills/roles and guide hiring or career decisions.



## Data

- Multiple CSV extracts (hundreds of thousands of rows).  

- **No raw data committed.** Repo includes a tiny synthetic `data/sample\_jobs.csv` for dev.



## Method

- Data cleaning & joins, feature engineering (skills parsing), EDA (role/skill/location trends).

- Charts: top skills by postings, pay signals by role/location, time trends.



## Quickstart

```bash

python -m venv .venv

source .venv/Scripts/activate   # PowerShell: .venv\\Scripts\\Activate.ps1

pip install -r requirements.txt

jupyter notebook



