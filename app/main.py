from fastapi import FastAPI

from app.handler.berry_graph_handler import get_graph_router
from app.handler.berry_stats_handler import get_router
from app.infrastructure.cache import InMemoryTTLCache
from app.infrastructure.http_client import ResilientHTTPClient
from app.repository.berry_repository import BerryRepository
from app.usecase.get_all_berry_stats_usecase import GetAllBerryStatsUseCase


app = FastAPI(title="Berry Stats API")

# ✅ Create shared HTTP client
http_client = ResilientHTTPClient()

# ✅ Create cache with TTL
cache = InMemoryTTLCache(ttl_seconds=86400) # 24 hours

# ✅ Inject into repository
repository = BerryRepository(http_client)

# ✅ Inject into usecase
usecase = GetAllBerryStatsUseCase(repository)

# ✅ Register routers (with usecase and cache)
app.include_router(get_router(usecase, cache))
app.include_router(get_graph_router(usecase, cache))


@app.on_event("shutdown")
async def shutdown_event():
    await http_client.close()
