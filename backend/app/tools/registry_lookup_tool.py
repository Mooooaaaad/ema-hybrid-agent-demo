import json
from pathlib import Path


def lookup_registry(normalized_address: str):
    data_path = Path(__file__).resolve().parent.parent / "data" / "registry.json"

    with open(data_path, "r", encoding="utf-8") as f:
        registry = json.load(f)

    matches = [
        item for item in registry
        if item["address"] == normalized_address
    ]

    return {
        "query_address": normalized_address,
        "matches_found": len(matches),
        "matches": matches
    }