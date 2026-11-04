"""Refresh the dataset from zullfa.com and rebuild the CSV.

    python3 scripts/build.py            # download the current zones.geojson, then write the CSV
    python3 scripts/build.py --offline  # only rebuild the CSV from data/zones.geojson

Standard library only.
"""
import csv
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GEOJSON = ROOT / "data" / "zones.geojson"
CSV = ROOT / "data" / "zones.csv"
SOURCE = "https://zullfa.com/data/zones.geojson"

COLUMNS = [
    "zone_code", "name", "name_official", "name_ar", "city", "area_m2",
    "distance_boundary_m", "distance_farthest_m", "distance_centroid_m",
    "walk_minutes_min", "walk_minutes_max", "within_an_hour_on_foot",
    "eligible_buyers", "ownership_pct", "usufruct_max_years",
    "permitted_uses", "excluded_uses", "permitted_rights",
    "gazetted_on", "url", "source_url", "retrieved",
]


def download() -> None:
    req = urllib.request.Request(SOURCE, headers={"User-Agent": "makkah-madinah-ownership-zones/1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    data.pop("generated", None)  # a build date, not a data change; keeps diffs to real changes
    GEOJSON.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def rows(data: dict):
    for f in data["features"]:
        p = f["properties"]
        d = p.get("distance_to_haram_m") or {}
        row = {k: p.get(k) for k in COLUMNS if k in p}
        row["distance_boundary_m"] = d.get("boundary")
        row["distance_farthest_m"] = d.get("farthest")
        row["distance_centroid_m"] = d.get("centroid")
        for k in ("eligible_buyers", "permitted_uses", "excluded_uses", "permitted_rights"):
            row[k] = ";".join(p.get(k) or [])
        yield {k: ("" if row.get(k) is None else row.get(k)) for k in COLUMNS}


def write_csv() -> int:
    data = json.loads(GEOJSON.read_text(encoding="utf-8"))
    out = list(rows(data))
    with CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(out)
    return len(out)


if __name__ == "__main__":
    if "--offline" not in sys.argv:
        download()
    print(f"{write_csv()} zones written to {CSV.relative_to(ROOT)}")
