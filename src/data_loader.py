# src/data_loader.py
from pathlib import Path
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SAMPLE = REPO_ROOT / "data" / "sample_jobs.csv"

def load_sample(path: str | Path = DEFAULT_SAMPLE) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Missing sample data at {p.resolve()}")
    df = pd.read_csv(p, parse_dates=["posted_date"])
    return df
