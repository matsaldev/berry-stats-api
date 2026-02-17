import pytest
from app.repository.berry_repository import BerryRepository
from app.entity.berry_growth import BerryGrowth


class MockHTTPClient:
    async def get(self, url: str, params=None):
        class MockResponse:
            def raise_for_status(self):
                pass

            def json(self_inner):
                # ✅ First call: list endpoint (params is not None)
                if params is not None:
                    return {
                        "results": [
                            {"url": "https://pokeapi.co/api/v2/berry/1/"},
                            {"url": "https://pokeapi.co/api/v2/berry/2/"}
                        ]
                    }

                # ✅ Subsequent calls: berry detail endpoint
                return {
                    "name": "TestBerry",
                    "growth_time": 3
                }

        return MockResponse()


@pytest.mark.asyncio
async def test_fetch_berries_returns_entities():
    """
    Ensures repository returns BerryGrowth entities
    and correctly parses growth_time.
    """
    mock_client = MockHTTPClient()
    repository = BerryRepository(mock_client)

    berries = await repository.fetch_berries(limit=2)

    # ✅ Assert correct number of berries returned
    assert len(berries) == 2

    # ✅ Assert entity type
    assert isinstance(berries[0], BerryGrowth)

    # ✅ Assert data parsing
    assert berries[0].name == "Testberry"
    assert berries[0].growth_time == 3
