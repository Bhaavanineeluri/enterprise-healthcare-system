from models.user import User

from schemas.ocr_schema import (
    OCRRequest,
)


def extract_text_service(
    ocr: OCRRequest,
    current_user: User,
):

    """
    Future OCR Integrations:

    - Tesseract OCR
    - Google Vision API
    - AWS Textract
    - Azure Document Intelligence
    """

    return {

        "extracted_text":
            f"OCR processing placeholder for: {ocr.file_path}"
    }