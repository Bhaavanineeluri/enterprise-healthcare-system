from fastapi import APIRouter
from fastapi import Depends


from dependencies.auth import get_current_user
from models.user import User


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me")
def get_profile(
    current_user: User = Depends(get_current_user)
):

    return current_user