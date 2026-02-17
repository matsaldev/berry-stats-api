import time
from typing import Any, Dict, Tuple


class InMemoryTTLCache:
    """
    Simple in-memory cache with TTL support.
    """

    def __init__(self, ttl_seconds: int = 300):
        self.ttl = ttl_seconds
        self.store: Dict[str, Tuple[Any, float]] = {}

    def get(self, key: str):
        if key in self.store:
            value, timestamp = self.store[key]
            if time.time() - timestamp < self.ttl:
                return value
            else:
                del self.store[key]
        return None

    def set(self, key: str, value: Any):
        self.store[key] = (value, time.time())
