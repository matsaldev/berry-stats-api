from typing import List

from app.entity.berry_growth import BerryGrowth
from app.port.berry_repository_interface import BerryRepositoryInterface
from app.infrastructure.http_client import ResilientHTTPClient
from app.config.settings import settings


class BerryRepository(BerryRepositoryInterface):
    """
    Concrete implementation using PokeAPI.
    """

    def __init__(self, http_client: ResilientHTTPClient) -> None:
        self.base_url = settings.POKEAPI_BASE_URL
        self.http_client = http_client

    async def fetch_berries(self, limit: int) -> List[BerryGrowth]:

        response = await self.http_client.get(
            f"{self.base_url}/berry",
            params={"limit": limit}
        )

        results = response.json().get("results", [])

        berries: List[BerryGrowth] = []

        for berry in results:
            berry_response = await self.http_client.get(berry["url"])
            berry_data = berry_response.json()

            berries.append(
                BerryGrowth(
                    name=berry_data["name"].capitalize(),
                    growth_time=berry_data["growth_time"]
                )
            )

        return berries
