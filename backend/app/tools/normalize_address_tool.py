def normalize_address(address: str):
    if not address:
        return {
            "original": "",
            "normalized": ""
        }

    normalized = " ".join(address.strip().lower().split())

    return {
        "original": address,
        "normalized": normalized
    }