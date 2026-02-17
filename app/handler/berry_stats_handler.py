from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse

from app.usecase.get_all_berry_stats_usecase import GetAllBerryStatsUseCase


def get_router(usecase: GetAllBerryStatsUseCase) -> APIRouter:
    router = APIRouter()

    @router.get("/allBerryStats")
    async def get_all_berry_stats(limit: int = Query(10, ge=1, le=100)):
        try:
            result = await usecase.execute(limit)

            return JSONResponse(
                content=result.__dict__,
                media_type="application/json"
            )

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return router
