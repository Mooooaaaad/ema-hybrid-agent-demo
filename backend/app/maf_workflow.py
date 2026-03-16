from app.tools.normalize_address_tool import normalize_address
from app.tools.registry_lookup_tool import lookup_registry
from app.agents.resolution_agent import resolve_entity


def run_workflow(input_data: dict):
    org_name = input_data.get("organization_name", "")
    address = input_data.get("address", "")

    normalized = normalize_address(address)
    registry_result = lookup_registry(normalized["normalized"])
    resolution = resolve_entity(
        org_name=org_name,
        normalized_address=normalized["normalized"],
        registry_result=registry_result
    )

    return {
        "workflow": "ema-hybrid-demo",
        "steps": {
            "normalize_address": normalized,
            "registry_lookup": registry_result,
            "resolution_agent": resolution
        }
    }