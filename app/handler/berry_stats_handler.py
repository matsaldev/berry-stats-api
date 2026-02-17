from fastapi import APIRouter, Query, Depends, Request

router = APIRouter()


def get_usecase(request: Request):
    return request.app.state.usecase


def get_cache(request: Request):
    return request.app.state.cache


@router.get("/allBerryStats")
async def get_all_berry_stats(
    limit: int = Query(10, ge=1, le=100),
    usecase=Depends(get_usecase),
    cache=Depends(get_cache),
):
    """
    Returns berry statistics in JSON format.
    """

    cache_key = f"stats:{limit}"

    cached = cache.get(cache_key)
    if cached:
        return cached

    result = await usecase.execute(limit)
    response = result.__dict__

    cache.set(cache_key, response)

    return response
