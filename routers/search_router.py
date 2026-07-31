from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.search_schema import (
    SearchResponse,
)

from services.search_service import (
    global_search_service,
)


router = APIRouter(
    prefix="/search",
    tags=["Search Platform"],
)


@router.get(
    "/",
    response_model=SearchResponse,
)
def search(
    query: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return global_search_service(
        db=db,
        query=query,
        current_user=current_user,
    )