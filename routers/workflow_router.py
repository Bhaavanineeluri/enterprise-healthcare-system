from fastapi import APIRouter
from fastapi import Depends


from dependencies.auth import get_current_user
from models.user import User

from schemas.workflow_schema import (
    WorkflowRequest,
    WorkflowResponse,
)

from services.workflow_service import (
    execute_workflow_service,
)


router = APIRouter(
    prefix="/workflows",
    tags=["Workflow Engine"],
)


@router.post(
    "/execute",
    response_model=WorkflowResponse,
)
def execute_workflow(
    workflow: WorkflowRequest,
    current_user: User = Depends(get_current_user),
):

    return execute_workflow_service(
        workflow=workflow,
        current_user=current_user,
    )