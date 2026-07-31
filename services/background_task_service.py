from fastapi import BackgroundTasks

from models.user import User

from schemas.background_task_schema import (
    BackgroundTaskRequest,
)


def execute_task(
    task_name: str,
):

    """
    Future implementation examples:

    - Celery
    - Redis Queue (RQ)
    - APScheduler
    - RabbitMQ
    """

    print(f"Executing background task: {task_name}")


def run_background_task_service(
    background_tasks: BackgroundTasks,
    task: BackgroundTaskRequest,
    current_user: User,
):

    background_tasks.add_task(
        execute_task,
        task.task_name,
    )

    return {

        "success": True,

        "task_name": task.task_name,

        "message":
            "Background task started successfully.",
    }