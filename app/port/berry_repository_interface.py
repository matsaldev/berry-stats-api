from abc import ABC, abstractmethod
from typing import List

from app.entity.berry_growth import BerryGrowth


class BerryRepositoryInterface(ABC):
    """
    Repository abstraction (Port).
    Defines the contract for fetching berry data.
    """

    @abstractmethod
    async def fetch_berries(self, limit: int) -> List[BerryGrowth]:
        """
        Fetch berries with growth_time information.
        """
        pass