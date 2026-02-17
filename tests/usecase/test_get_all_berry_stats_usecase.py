import pytest
from app.usecase.get_all_berry_stats_usecase import GetAllBerryStatsUseCase
from app.entity.berry_growth import BerryGrowth


class MockBerryRepository:
    async def fetch_berries(self, limit: int):
        return [
            BerryGrowth(name="One", growth_time=2),
            BerryGrowth(name="Two", growth_time=4),
            BerryGrowth(name="Three", growth_time=6),
        ]


@pytest.mark.asyncio
async def test_usecase_stats_computation():
    repo = MockBerryRepository()
    usecase = GetAllBerryStatsUseCase(repo)

    result = await usecase.execute(3)

    assert result.min_growth_time == 2
    assert result.max_growth_time == 6
    assert result.mean_growth_time == 4
    assert result.median_growth_time == 4
