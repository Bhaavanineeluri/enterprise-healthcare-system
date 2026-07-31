from fastapi import APIRouter
from fastapi import BackgroundTasks
from fastapi import Depends


from dependencies.auth import get_current_user
from models.user import User

from schemas.background_task_schema import (
    BackgroundTaskRequest,
    BackgroundTaskResponse,
)

from services.background_task_service import (
    run_background_task_service,
)


router = APIRouter(
    prefix="/background-tasks",
    tags=["Background Processing"],
)


@router.post(
    "/run",
    response_model=BackgroundTaskResponse,
)
def run_background_task(
    task: BackgroundTaskRequest,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
):

    return run_background_task_service(
        background_tasks=background_tasks,
        task=task,
        current_user=current_user,
    )