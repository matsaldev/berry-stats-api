from fastapi import FastAPI

from app.infrastructure.http_client import ResilientHTTPClient
from app.repository.berry_repository import BerryRepository
from app.usecase.get_all_berry_stats_usecase import GetAllBerryStatsUseCase
from app.handler.berry_stats_handler import get_router


app = FastAPI(title="Berry Stats API")

# ✅ Create shared HTTP client
http_client = ResilientHTTPClient()

# ✅ Inject into repository
repository = BerryRepository(http_client)

# ✅ Inject into usecase
usecase = GetAllBerryStatsUseCase(repository)

app.include_router(get_router(usecase))


@app.on_event("shutdown")
async def shutdown_event():
    await http_client.close()
