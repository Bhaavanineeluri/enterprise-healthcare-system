from typing import Optional

from pydantic import BaseModel


class WorkflowRequest(BaseModel):

    workflow_name: str

    entity_id: int

    remarks: Optional[str] = None


class WorkflowResponse(BaseModel):

    success: bool

    workflow: str

    message: str