import statistics
from collections import Counter
from typing import List

from app.entity.berry_growth import BerryGrowth
from app.entity.berry_stats import BerryStats
from app.port.berry_repository_interface import BerryRepositoryInterface


class GetAllBerryStatsUseCase:

    def __init__(self, repository: BerryRepositoryInterface) -> None:
        self.repository = repository

    async def execute(self, limit: int) -> BerryStats:
        """
        Retrieves berries from repository and computes
        statistical aggregation over growth_time.
        """

        berry_entities: List[BerryGrowth] = await self.repository.fetch_berries(limit)

        if not berry_entities:
            raise ValueError("No berries found")

        # ✅ Correct attribute access (NOT subscriptable)
        growth_times: List[int] = [berry.growth_time for berry in berry_entities]

        # ✅ Statistical calculations
        min_growth = min(growth_times)
        max_growth = max(growth_times)
        mean_growth = round(statistics.mean(growth_times), 2)
        median_growth = round(statistics.median(growth_times), 2)
        variance_growth = round(statistics.pvariance(growth_times), 2)

        # ✅ Frequency distribution
        frequency = dict(Counter(growth_times))

        # ✅ Return structured Entity
        return BerryStats(
            berries_names=[berry.name for berry in berry_entities],
            min_growth_time=min_growth,
            median_growth_time=median_growth,
            max_growth_time=max_growth,
            variance_growth_time=variance_growth,
            mean_growth_time=mean_growth,
            frequency_growth_time=frequency
        )
