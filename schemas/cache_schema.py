from pydantic import BaseModel


class CacheRequest(BaseModel):

    key: str

    value: str


class CacheResponse(BaseModel):

    success: bool

    message: str