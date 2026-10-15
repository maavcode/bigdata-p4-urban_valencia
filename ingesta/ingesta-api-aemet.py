import os
import json
import time
import requests
from datetime import date
from dotenv import load_dotenv

load_dotenv()

# Configuración de la API de AEMET
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
TIMEOUT = 30
MAX_RETRIES = 3

# Funciones de ingesta de datos
def fetch_data() -> list:
    """Fetches data from the API, retrying when the rate limit is hit (429)."""
    if not API_KEY:
        raise SystemExit("Missing API_KEY in the .env file")
    headers = {"api_key": API_KEY, "accept": "application/json"}
    for attempt in range(MAX_RETRIES):
        resp = requests.get(API_URL, headers=headers, timeout=TIMEOUT)
        if resp.status_code == 429 or (resp.status_code == 500 and "429" in resp.text):
            wait = 60 * (attempt + 1)
            print(f"Rate limit reached (429). Waiting {wait}s...")
            time.sleep(wait)
            continue
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            raise SystemExit(f"API error: {data.get('descripcion', data)}")
        raise ValueError(f"Unexpected API response: {type(data).__name__}")
    raise SystemExit("API still returned 429 after several retries")

def full_ingest() -> list[dict]:
    """Downloads the full dataset from the API."""
    return fetch_data()

if __name__ == "__main__":
    records = full_ingest()
    today = date.today().isoformat()
    output_path = f"data/raw/aemet_valencia_{today}.json"
    os.makedirs("data/raw", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    print(f"Ingesta completed: {len(records)} records saved to {output_path}")