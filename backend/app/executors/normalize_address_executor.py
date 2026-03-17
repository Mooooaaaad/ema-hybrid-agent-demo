from typing_extensions import Never
from agent_framework import Executor, WorkflowContext, handler

from app.models.workflow_messages import (
    StartResolutionMessage,
    NormalizedAddressMessage,
)
from app.tools.normalize_address_tool import normalize_address


class NormalizeAddressExecutor(Executor):
    @handler
    async def process(
        self,
        message: StartResolutionMessage,
        ctx: WorkflowContext[Never, NormalizedAddressMessage],
    ) -> None:
        normalized = normalize_address(message.address)

        await ctx.send_message(
            NormalizedAddressMessage(
                organization_name=message.organization_name,
                original_address=message.address,
                normalized_address=normalized["normalized"],
            )
        )