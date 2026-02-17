import time
from app.infrastructure.cache import InMemoryTTLCache


def test_cache_set_get():
    cache = InMemoryTTLCache(ttl_seconds=10)
    cache.set("x", {"value": 1})
    assert cache.get("x")["value"] == 1


def test_cache_expire():
    cache = InMemoryTTLCache(ttl_seconds=1)
    cache.set("x", 100)
    time.sleep(2)
    assert cache.get("x") is None
