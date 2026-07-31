from pydantic import BaseModel


class OCRRequest(BaseModel):

    file_path: str


class OCRResponse(BaseModel):

    extracted_text: str