from pydantic import BaseModel


class MonitoringResponse(BaseModel):

    application: str

    status: str

    database: str

    logging: str