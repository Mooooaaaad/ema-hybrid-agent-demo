import json
import os
import requests


def _fallback_resolution(org_name: str, registry_result: dict):
    matches = registry_result.get("matches", [])

    if not matches:
        return {
            "decision": "NEW_RECORD",
            "selected_candidate_id": None,
            "explanation": "No registry candidate was found for the normalized address."
        }

    org_name_norm = (org_name or "").strip().lower()

    for candidate in matches:
        candidate_name = candidate.get("name", "").strip().lower()
        if candidate_name == org_name_norm:
            return {
                "decision": "MATCH",
                "selected_candidate_id": candidate["id"],
                "explanation": "Exact organization name match found among registry candidates."
            }

    if len(matches) == 1:
        return {
            "decision": "REVIEW",
            "selected_candidate_id": matches[0]["id"],
            "explanation": "Only one address match was found, but the organization name is not exact."
        }

    return {
        "decision": "REVIEW",
        "selected_candidate_id": None,
        "explanation": "Multiple address matches were found and the organization name is ambiguous."
    }


def resolve_entity(org_name: str, normalized_address: str, registry_result: dict):
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not endpoint or not api_key or not deployment:
        return _fallback_resolution(org_name, registry_result)

    url = f"{endpoint.rstrip('/')}/openai/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }

    prompt = f"""
You are an entity resolution agent for an EMA demo.
You must decide whether the extracted organization matches one of the registry candidates.

Return JSON only with this exact structure:
{{
  "decision": "MATCH" | "REVIEW" | "NEW_RECORD",
  "selected_candidate_id": "string or null",
  "explanation": "short explanation"
}}

Extracted organization name: {org_name}
Normalized address: {normalized_address}

Registry lookup result:
{json.dumps(registry_result, ensure_ascii=False)}
""".strip()

    payload = {
        "model": deployment,
        "messages": [
            {
                "role": "system",
                "content": "You are a careful entity resolution agent. Return valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0
    }

    response = requests.post(url, headers=headers, json=payload, timeout=60)
    response.raise_for_status()

    content = response.json()["choices"][0]["message"]["content"]

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "decision": "REVIEW",
            "selected_candidate_id": None,
            "explanation": f"Model returned non-JSON output: {content}"
        }