import io
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import Response

from app.usecase.get_all_berry_stats_usecase import GetAllBerryStatsUseCase


def get_graph_router(usecase: GetAllBerryStatsUseCase) -> APIRouter:
    """
    Separate router responsible only for graph visualization.
    """
    router = APIRouter()

    @router.get("/allBerryStats/graph", response_class=Response)
    async def get_all_berry_stats_graph(limit: int = Query(10, ge=1, le=100)):
        try:
            # Reuse repository through usecase
            berries = await usecase.repository.fetch_berries(limit)

            growth_times = [b.growth_time for b in berries]

            if not growth_times:
                raise HTTPException(status_code=404, detail="No berry data available")

            # Create histogram
            plt.figure()
            plt.hist(growth_times, bins="auto")
            plt.title("Berry Growth Time Distribution")
            plt.xlabel("Growth Time")
            plt.ylabel("Frequency")

            # Save as SVG in memory
            buffer = io.BytesIO()
            plt.savefig(buffer, format="svg")
            plt.close()
            buffer.seek(0)

            return Response(
                content=buffer.getvalue(),
                media_type="image/svg+xml"
            )

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return router
