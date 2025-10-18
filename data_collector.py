#!/usr/bin/env python3

"""
HW3: Remote Data via APIs
Data Collection Script (World Bank API)

TODO: Implement your chosen API data collection here.

Research Question:
Do wealthier countries have better social indicators (2010-2020)?

What this script does:
1. Connects to the World Bank API to fetch data on multiple indicators across 20 countries (>= 60 requests).
2. Saves raw JSON responses to raw_data.json (for grading reproducibility).
3. Processes the data into a clean CSV file (processed_data.csv) suitable for analysis (analysis.ipynb).
4. Adds derived variables to support analysis.

Outputs:
- raw_data.json: Raw API responses.
- processed_data.csv: Cleaned and processed data for analysis.
"""

import requests
import json
import time
import pandas as pd
import os
import math
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 20 countries → 20 * 3 indicators = 60 requests (>= 50 requirement)
COUNTRIES = [
    "USA","CHN","JPN","DEU","GBR","FRA","IND","BRA","CAN","AUS",
    "KOR","ITA","ESP","MEX","RUS","ZAF","IDN","TUR","NLD","SAU"
]

# Indicator code → readable column name
INDICATORS = {
    "NY.GDP.MKTP.CD": "gdp_current_usd",     # Current US$ GDP
    "SE.ADT.LITR.ZS": "adult_literacy_rate", # % (age 15+)
    "IT.NET.USER.ZS": "internet_users_pct"   # % of population
}

START_YEAR, END_YEAR = 2010, 2020
PER_PAGE = 2000
BASE_URL = "https://api.worldbank.org/v2/country/{country}/indicator/{indicator}"
REQUEST_TIMEOUT = 30
SLEEP_SECONDS = 0.6        # polite rate limit
MAX_RETRIES = 3
RETRY_BACKOFF = 1.5        # exponential backoff multiplier

RAW_SAMPLE_SIZE = 150      # how many parsed obs to keep in raw_data.json
RAW_OUT = "raw_data.json"
PROC_OUT = "processed_data.csv"


def fetch_with_retries(url: str, params: dict) -> requests.Response:
    """GET with basic retry/backoff for transient errors."""
    attempt = 0
    while True:
        try:
            resp = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
            # World Bank returns 200 with error payload sometimes; still check status first
            if resp.status_code == 200:
                return resp
            else:
                raise requests.HTTPError(f"HTTP {resp.status_code}")
        except Exception as e:
            attempt += 1
            if attempt >= MAX_RETRIES:
                raise
            sleep_for = (RETRY_BACKOFF ** (attempt - 1))
            print(f"[warn] Request failed ({e}), retry {attempt}/{MAX_RETRIES} after {sleep_for:.1f}s …")
            time.sleep(sleep_for)


def fetch_indicator_for_country(country: str, indicator: str) -> list[dict]:
    """
    Call World Bank API for one (country, indicator).
    Returns a list of parsed dict rows (year/value).
    """
    url = BASE_URL.format(country=country, indicator=indicator)
    params = {
        "format": "json",
        "per_page": PER_PAGE,
        "date": f"{START_YEAR}:{END_YEAR}",
    }
    resp = fetch_with_retries(url, params=params)

    try:
        payload = resp.json()
        # payload[0] is metadata; payload[1] is the actual data list
        data = payload[1]
        if data is None:
            return []
    except Exception as e:
        print(f"[error] JSON parsing failed for {country}-{indicator}: {e}")
        return []

    rows = []
    for d in data:
        # Some entries have null "value"
        if d.get("value") is None:
            continue
        try:
            rows.append({
                "country": country,
                "indicator_code": indicator,
                "year": int(d["date"]),
                "value": float(d["value"])
            })
        except Exception:
            # Skip malformed entries silently
            continue
    return rows


def main():
    """
    Main function - implement your data collection logic here.
    
    Steps to implement:
    1. Set up API credentials from environment variables
    2. Define your search terms/parameters
    3. Make API requests (with error handling!)
    4. Process the JSON responses
    5. Save raw data and processed CSV
    """
    
    # TODO: Get API credentials from environment variables
    # api_key = os.getenv('YOUR_API_KEY')
    
    # TODO: Check if API key exists
    # if not api_key:
    #     print("Please set YOUR_API_KEY in .env file")
    #     return
    
    print("Starting data collection (World Bank API)...")
    started_at = datetime.now()

    all_rows = []
    request_count = 0
    
    # TODO: Implement your API calls here
    # Remember to:
    # - Handle errors (network issues, rate limits, invalid responses)
    # - Add delays between requests (time.sleep)
    # - Save raw JSON responses
    # - Process data into clean format
    
        # Loop over countries and indicators (>= 60 requests)
    for c in COUNTRIES:
        for ind_code in INDICATORS.keys():
            url = BASE_URL.format(country=c, indicator=ind_code)
            print(f"[fetch] {c} - {ind_code}  ->  {url}")
            try:
                rows = fetch_indicator_for_country(c, ind_code)
                request_count += 1
                all_rows.extend(rows)
            except Exception as e:
                print(f"[error] Failed: {c}-{ind_code}: {e}")
            finally:
                time.sleep(SLEEP_SECONDS)

    print(f"Total HTTP requests attempted: {request_count}")
    print(f"Total parsed records: {len(all_rows)}")

    # Save a sample of raw records for grading reproducibility
    try:
        with open(RAW_OUT, "w", encoding="utf-8") as f:
            json.dump(all_rows[:RAW_SAMPLE_SIZE], f, ensure_ascii=False, indent=2)
        print(f"✅ Saved raw sample -> {RAW_OUT}  (n={min(RAW_SAMPLE_SIZE, len(all_rows))})")
    except Exception as e:
        print(f"[error] Writing raw_data.json failed: {e}")

    if not all_rows:
        print("[fatal] No data collected. Exiting.")
        return

    # ------------------------------
    # Cleaning & Reshaping
    # ------------------------------
    df_long = pd.DataFrame(all_rows)
    # Map indicator code -> readable name
    df_long["indicator"] = df_long["indicator_code"].map(INDICATORS)

    # Keep years in range, just in case
    df_long = df_long[(df_long["year"] >= START_YEAR) & (df_long["year"] <= END_YEAR)]

    # Pivot to wide format
    wide = (
        df_long
        .pivot_table(index=["country", "year"], columns="indicator", values="value")
        .reset_index()
        .sort_values(["country", "year"])
    )

    # Derived features that help with the research Q
    # 1) GDP per internet user (rough proxy for economic resources per connected person)
    if {"gdp_current_usd", "internet_users_pct"}.issubset(set(wide.columns)):
        wide["gdp_per_internet_user"] = wide["gdp_current_usd"] / (wide["internet_users_pct"] / 100.0)
    else:
        wide["gdp_per_internet_user"] = pd.NA

    # 2) Year-over-year growth of internet usage (%-point change)
    if "internet_users_pct" in wide.columns:
        wide["internet_users_pct_yoy"] = (
            wide.sort_values(["country", "year"])
                .groupby("country")["internet_users_pct"]
                .diff(1)
        )

    # 3) GDP YoY growth rate (approx; using simple pct change)
    if "gdp_current_usd" in wide.columns:
        wide["gdp_yoy_growth"] = (
            wide.sort_values(["country", "year"])
                .groupby("country")["gdp_current_usd"]
                .pct_change()
        )

    # Save processed CSV
    try:
        wide.to_csv(PROC_OUT, index=False)
        print(f"✅ Saved processed -> {PROC_OUT}  shape={wide.shape}")
    except Exception as e:
        print(f"[error] Writing processed_data.csv failed: {e}")

    elapsed = datetime.now() - started_at
    print(f"Data collection complete! Elapsed: {elapsed}")

if __name__ == "__main__":
    main()