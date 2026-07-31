from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class AuditReportResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    user_id: int

    module: str

    action: str

    created_at: datetime