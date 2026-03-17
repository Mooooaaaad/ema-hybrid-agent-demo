from agent_framework import Executor, WorkflowContext, handler

from app.models.workflow_messages import (
    RegistryLookupMessage,
    ResolutionResultMessage,
)
from app.agents.resolution_agent import resolve_entity


class ResolutionExecutor(Executor):
    @handler
    async def process(
        self,
        message: RegistryLookupMessage,
        ctx: WorkflowContext[None, ResolutionResultMessage],
    ) -> None:
        result = resolve_entity(
            org_name=message.organization_name,
            normalized_address=message.normalized_address,
            registry_result=message.registry_result,
        )

        await ctx.yield_output(
            ResolutionResultMessage(result=result)
        )