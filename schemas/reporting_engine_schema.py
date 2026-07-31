from typing import Literal

from pydantic import BaseModel


class ReportRequest(BaseModel):

    report_type: Literal[
        "PATIENT",
        "APPOINTMENT",
        "BILLING",
        "LABORATORY",
        "PHARMACY",
        "INSURANCE",
    ]


class ReportResponse(BaseModel):

    report_type: str

    total_records: int

    message: str