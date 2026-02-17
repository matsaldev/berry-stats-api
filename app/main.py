from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.infrastructure.http_client import ResilientHTTPClient
from app.infrastructure.cache import InMemoryTTLCache
from app.repository.berry_repository import BerryRepository
from app.usecase.get_all_berry_stats_usecase import GetAllBerryStatsUseCase

from app.handler.berry_stats_handler import router as stats_router
from app.handler.berry_graph_handler import router as graph_router


# ✅ Lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifecycle management.
    Initializes shared infrastructure components
    and cleans them up gracefully.
    """

    # ✅ Initialize infrastructure
    http_client = ResilientHTTPClient()
    cache = InMemoryTTLCache(ttl_seconds=86400)  # 24 hours

    # ✅ Wire dependencies
    repository = BerryRepository(http_client)
    usecase = GetAllBerryStatsUseCase(repository)

    # ✅ Store in app state for dependency injection
    app.state.usecase = usecase
    app.state.cache = cache

    yield

    # ✅ Graceful shutdown
    await http_client.close()


# ✅ Create FastAPI app with lifespan
app = FastAPI(
    title="Berry Stats API",
    version="1.0.0",
    lifespan=lifespan
)

# ✅ Register routers
app.include_router(stats_router)
app.include_router(graph_router)
