import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from fastapi import APIRouter, Query, Depends, Request
from fastapi.responses import Response

router = APIRouter()


def get_usecase(request: Request):
    return request.app.state.usecase


def get_cache(request: Request):
    return request.app.state.cache


@router.get("/allBerryStats/graph")
async def get_all_berry_stats_graph(
    limit: int = Query(10, ge=1, le=100),
    usecase=Depends(get_usecase),
    cache=Depends(get_cache),
):
    """
    Returns berry growth histogram as SVG.
    """

    cache_key = f"graph:{limit}"

    cached = cache.get(cache_key)
    if cached:
        return Response(content=cached, media_type="image/svg+xml")

    berries = await usecase.repository.fetch_berries(limit)

    names = [b.name for b in berries]
    growth_times = [b.growth_time for b in berries]

    plt.figure(figsize=(10, 6))
    plt.bar(names, growth_times)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format="svg")
    plt.close()
    buffer.seek(0)

    svg_data = buffer.getvalue()

    cache.set(cache_key, svg_data)

    return Response(content=svg_data, media_type="image/svg+xml")
