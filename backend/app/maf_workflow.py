import asyncio
from agent_framework import WorkflowBuilder

from app.executors.normalize_address_executor import NormalizeAddressExecutor
from app.executors.registry_lookup_executor import RegistryLookupExecutor
from app.executors.resolution_executor import ResolutionExecutor
from app.models.workflow_messages import StartResolutionMessage


def run_workflow(input_data: dict):
    start_message = StartResolutionMessage(
        organization_name=input_data.get("organization_name", ""),
        address=input_data.get("address", ""),
    )

    normalize = NormalizeAddressExecutor(id="normalize")
    lookup = RegistryLookupExecutor(id="lookup")
    resolve = ResolutionExecutor(id="resolve")

    workflow = (
        WorkflowBuilder(start_executor=normalize)
        .add_edge(normalize, lookup)
        .add_edge(lookup, resolve)
        .build()
    )

    async def _run():
        events = await workflow.run(start_message)
        outputs = events.get_outputs()
        if outputs:
            return outputs[0].result

        return {
            "decision": "REVIEW",
            "selected_candidate_id": None,
            "confidence": 0.0,
            "explanation": "No workflow output was produced."
        }

    result = asyncio.run(_run())

    return {
        "workflow": "ema-hybrid-demo-maf",
        "result": result
    }