from fastapi import APIRouter
from fastapi import Depends


from dependencies.auth import get_current_user
from models.user import User

from schemas.ocr_schema import (
    OCRRequest,
    OCRResponse,
)

from services.ocr_service import (
    extract_text_service,
)


router = APIRouter(
    prefix="/ocr",
    tags=["OCR Integration"],
)


@router.post(
    "/extract",
    response_model=OCRResponse,
)
def extract_text(
    ocr: OCRRequest,
    current_user: User = Depends(get_current_user),
):

    return extract_text_service(
        ocr=ocr,
        current_user=current_user,
    )