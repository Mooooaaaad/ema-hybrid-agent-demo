from typing_extensions import Never
from agent_framework import Executor, WorkflowContext, handler

from app.models.workflow_messages import (
    NormalizedAddressMessage,
    RegistryLookupMessage,
)
from app.tools.registry_lookup_tool import lookup_registry


class RegistryLookupExecutor(Executor):
    @handler
    async def process(
        self,
        message: NormalizedAddressMessage,
        ctx: WorkflowContext[Never, RegistryLookupMessage],
    ) -> None:
        registry_result = lookup_registry(message.normalized_address)

        await ctx.send_message(
            RegistryLookupMessage(
                organization_name=message.organization_name,
                normalized_address=message.normalized_address,
                registry_result=registry_result,
            )
        )