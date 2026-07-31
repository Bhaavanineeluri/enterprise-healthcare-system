from typing import Literal

from pydantic import BaseModel


class BackgroundTaskRequest(BaseModel):

    task_name: Literal[
        "GENERATE_REPORT",
        "SEND_NOTIFICATION",
        "OCR_PROCESSING",
        "DATA_BACKUP",
        "CLEANUP_LOGS",
    ]


class BackgroundTaskResponse(BaseModel):

    success: bool

    task_name: str

    message: str