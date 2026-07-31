from fastapi import APIRouter
from fastapi import Depends

from models.user import User


from dependencies.auth import get_current_user
from schemas.cache_schema import (
    CacheRequest,
    CacheResponse,
)

from services.cache_service import (
    clear_cache_service,
    get_cache_service,
    set_cache_service,
)


router = APIRouter(
    prefix="/cache",
    tags=["Redis Cache"],
)


@router.post(
    "/",
    response_model=CacheResponse,
)
def set_cache(
    cache: CacheRequest,
    current_user: User = Depends(get_current_user),
):

    return set_cache_service(
        cache,
        current_user,
    )


@router.get(
    "/{key}",
    response_model=CacheResponse,
)
def get_cache(
    key: str,
    current_user: User = Depends(get_current_user),
):

    return get_cache_service(
        key,
        current_user,
    )


@router.delete(
    "/",
    response_model=CacheResponse,
)
def clear_cache(
    current_user: User = Depends(get_current_user),
):

    return clear_cache_service(
        current_user,
    )