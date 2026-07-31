from pydantic import BaseModel


class NotificationRequest(BaseModel):

    recipient: str

    subject: str

    message: str


class NotificationResponse(BaseModel):

    success: bool

    message: str