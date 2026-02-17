import httpx
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)


class ResilientHTTPClient:
    """
    Shared HTTP client with:
    - Global timeout
    - Retry logic
    - Exponential backoff
    """

    def __init__(self) -> None:
        self._client = httpx.AsyncClient(
            timeout=httpx.Timeout(10.0)  # ✅ Global timeout
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=8),
        retry=retry_if_exception_type(httpx.RequestError),
        reraise=True,
    )
    async def get(self, url: str, params: dict | None = None) -> httpx.Response:
        response = await self._client.get(url, params=params)
        response.raise_for_status()
        return response

    async def close(self) -> None:
        await self._client.aclose()
