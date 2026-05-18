
import requests
import pandas as pd
import boto3
import json
from datetime import datetime, timezone
import io
import logging

# ── Configuration ──────────────────────────────────────────
S3_BUCKET = "weather-pipeline-saif-2025"  
S3_PREFIX = "raw/weather"
REGION    = "us-east-1"

# Cities to track (lat/lon pairs)
CITIES = {
    "cairo":    (30.0444, 31.2357),
    "london":   (51.5074, -0.1278),
    "new_york": (40.7128, -74.0060),
    "tokyo":    (35.6762, 139.6503),
}

# ── Logging ─────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)

# ── Fetch from Open-Meteo API ───────────────────────────────
def fetch_weather(city: str, lat: float, lon: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat, "longitude": lon,
        "current": [
            "temperature_2m", "relative_humidity_2m",
            "wind_speed_10m", "weather_code",
            "apparent_temperature"
        ],
        "timezone": "auto"
    }
    r = requests.get(url, params=params, timeout=15)
    r.raise_for_status()
    return r.json()

# ── Transform raw API response ──────────────────────────────
def transform(city: str, raw: dict, ingestion_ts: str) -> dict:
    curr = raw["current"]
    return {
        "city":                city,
        "ingestion_timestamp": ingestion_ts,
        "api_timestamp":       curr["time"],
        "temperature_c":       curr["temperature_2m"],
        "feels_like_c":        curr["apparent_temperature"],
        "humidity_pct":        curr["relative_humidity_2m"],
        "wind_speed_kmh":      curr["wind_speed_10m"],
        "weather_code":        curr["weather_code"],
        "latitude":            raw["latitude"],
        "longitude":           raw["longitude"],
        "timezone":            raw["timezone"],
    }

# ── Upload Parquet to S3 ────────────────────────────────────
def upload_to_s3(df: pd.DataFrame, bucket: str, key: str):
    s3 = boto3.client("s3", region_name=REGION)
    buf = io.BytesIO()
    df.to_parquet(buf, engine="pyarrow", index=False, compression="snappy")
    buf.seek(0)
    s3.upload_fileobj(buf, bucket, key)
    log.info(f"Uploaded → s3://{bucket}/{key}")

# ── Main Orchestration ──────────────────────────────────────
def run_pipeline():
    now = datetime.now(timezone.utc)
    ts  = now.strftime("%Y-%m-%dT%H-%M-%SZ")
    date_partition = now.strftime("year=%Y/month=%m/day=%d")

    records = []
    for city, (lat, lon) in CITIES.items():
        try:
            log.info(f"Fetching weather for {city}...")
            raw = fetch_weather(city, lat, lon)
            record = transform(city, raw, ts)
            records.append(record)
        except Exception as e:
            log.error(f"Failed for {city}: {e}")

    if not records:
        log.warning("No records fetched. Exiting.")
        return

    df = pd.DataFrame(records)
    log.info(f"Transformed {len(df)} records:\n{df.to_string()}")

    # Partitioned S3 key for Athena compatibility
    s3_key = f"{S3_PREFIX}/{date_partition}/weather_{ts}.parquet"
    upload_to_s3(df, S3_BUCKET, s3_key)
    log.info("Pipeline run complete ✓")

if __name__ == "__main__":
    run_pipeline()