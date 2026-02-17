from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse

from app.usecase.get_all_berry_stats_usecase import GetAllBerryStatsUseCase


def get_router(usecase: GetAllBerryStatsUseCase, cache) -> APIRouter:
    router = APIRouter()

    @router.get("/allBerryStats")
    async def get_all_berry_stats(limit: int = Query(10, ge=1, le=100)):
        cache_key = f"stats:{limit}"

        cached = cache.get(cache_key)
        if cached:
            return cached

        result = await usecase.execute(limit)
        response = result.__dict__

        cache.set(cache_key, response)

        return response

    return router
