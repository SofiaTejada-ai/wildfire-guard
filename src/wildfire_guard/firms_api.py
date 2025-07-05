from __future__ import annotations
import os, pathlib, requests, time
from datetime import date
from typing import Literal

API_KEY  = os.getenv("FIRMS_KEY")          # export FIRMS_KEY="real_key"
DATASET  = "VIIRS_SNPP_NRT"                # chosen feed
COUNTRY  = "USA"                           # ISO-3 code
OUTDIR   = pathlib.Path("data/raw")        # local save folder

def fetch_last_days(days: int = 1):
    """
    Download the last N days (1–10) of VIIRS SNPP NRT fires for the USA.
    Saves to data/raw/viirs_snpp_usa_last{days}d.csv
    """
    if not (1 <= days <= 10):
        raise ValueError("days must be 1–10")
    if API_KEY is None:
        raise EnvironmentError("FIRMS_KEY not set")

    url  = (
        "https://firms.modaps.eosdis.nasa.gov/api/country/csv/"
        f"{API_KEY}/{DATASET}/{COUNTRY}/{days}"
    )
    print("→", url)

    dest = OUTDIR / f"viirs_snpp_usa_last{days}d.csv"
    dest.parent.mkdir(parents=True, exist_ok=True)

    r = requests.get(url, timeout=60)
    print("  status:", r.status_code)
    r.raise_for_status()
    dest.write_bytes(r.content)
    print("✔ saved")
    return dest

# ── CLI helper ─────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    d = 1 if len(sys.argv) == 1 else int(sys.argv[1])
    fetch_last_days(d)
