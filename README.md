# LinkedIn Job Market Analysis (2023–2024)



**What:** Explore skill demand, locations, and compensation signals from large LinkedIn job datasets (cleaned + aggregated).  

**Why:** Identify high-demand skills/roles and guide hiring or career decisions.



## Data

Source: “LinkedIn Job Postings (2023–2024)” (owner: Arsh Koneru-Ansari).

Scale: Main postings table ≈ 123,850 rows, ~31 columns; 10 additional tables (companies, skills, industries, etc.) add ~741,793 rows → ~865,643 total records; ~556.5 MB across CSVs. 

Linkedin Job Market Analysis

Format: CSVs (multiple folders).

Access: Kaggle dataset page (see project notebook/notes).

⚠️ No raw data is committed to the repo. Use the tiny data/sample_jobs.csv for dev sanity checks; place full CSVs under data/ locally (gitignored)


## Questions we answer

How do average salaries vary across IT industries and position types?

Which U.S. states show the highest vs. lowest compensation signals?

Which industries attract the most applicants (competition hot spots)?

## Pipeline (end-to-end)

**A. Ingestion & quality checks**

Validate CSV structure with csvkit (csvclean -n, csvstat) and xsv (xsv headers, xsv select).

Drop/repair problematic text columns that break CSV parsing (e.g., very long descriptions), and keep only analysis-relevant fields. 

Linkedin Job Market Analysis

**B. Normalization & de-duplication**

Deduplicate company metadata and left-join auxiliary tables (industries, employee counts) on company_id; remove duplicate header artifacts post-joins. 

Linkedin Job Market Analysis

Create a cleaned postings table with consistent salary fields (normalize min/med/max → comparable annual figures).

**C. Dimensional modeling (analytics-friendly)**

Build a star schema:

Fact: fact_postings (job_id, salary metrics, applies/views, listed/expiry timestamps).

Dims: dim_company (size, industry, employee_count), dim_job (title, work_type, experience), dim_geo (city/state/zip/fips), dim_time (derived from listed/expiry).

Implemented in notebooks (pandas) and validated with basic SQL flows (PostgreSQL). 

Linkedin Job Market Analysis

**D. Analysis & visualization**

Salary distributions and grouped summaries (industry × role level; geo).

Applicant intensity per industry.

Reproducible plots saved to figures/ (optional).


## Repo layout
```bash
linkedin-job-market-analysis/
  README.md
  requirements.txt        # pinned for reproducibility
  .gitignore
  data/                   # gitignored (put full CSVs here)
    sample_jobs.csv       # tiny synthetic sample for dev
  src/
    data_loader.py        # robust pathing to sample/real data
    ...                   # (cleaning / features / viz helpers as you add)
  notebooks/
    01_ingest_and_clean.ipynb
    02_skill_parsing_and_features.ipynb
    03_eda_roles_skills_locations.ipynb
    04_compensation_signals.ipynb
    05_outputs_figures_tables.ipynb
  models/                 # (optional, gitignored)
  figures/                # (optional: charts exported for README)
```

## Quickstart
```bash
# 1) create env
python -m venv .venv
# Git Bash:
source .venv/Scripts/activate
# PowerShell:
# .venv\Scripts\Activate.ps1

# 2) install deps
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3) sanity check on sample data
jupyter notebook
# open notebooks/01_ingest_and_clean.ipynb and run cells

```
## Run on the full dataset

Download the Kaggle CSVs; place them under data/ (keep folders the dataset uses).

In 01_ingest_and_clean.ipynb, point the loader to your local data/ path.

Run notebooks 01 → 05 in order.

Tip: keep raw CSVs out of Git. The repo already ignores data/.



