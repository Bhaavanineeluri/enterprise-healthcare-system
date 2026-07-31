from models.user import User

from schemas.cache_schema import (
    CacheRequest,
)


_cache = {}


def set_cache_service(
    cache: CacheRequest,
    current_user: User,
):

    _cache[cache.key] = cache.value

    return {

        "success": True,

        "message": "Cache updated successfully.",
    }


def get_cache_service(
    key: str,
    current_user: User,
):

    return {

        "success": True,

        "message": _cache.get(
            key,
            "Cache not found.",
        ),
    }


def clear_cache_service(
    current_user: User,
):

    _cache.clear()

    return {

        "success": True,

        "message": "Cache cleared successfully.",
    }