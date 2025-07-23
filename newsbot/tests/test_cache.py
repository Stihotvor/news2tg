import pytest
from backend.cache.redis_cache import RedisCache

@pytest.fixture
def cache():
    return RedisCache(prefix='test', ttl=2)

def test_set_and_get(cache):
    cache.set('foo', {'bar': 1})
    assert cache.get('foo') == {'bar': 1}

def test_ttl_expiry(cache):
    cache.set('expire', {'baz': 2}, ttl=1)
    import time
    time.sleep(1.5)
    assert cache.get('expire') is None

def test_cache_gemini_summary(cache):
    cache.cache_gemini_summary('id1', {'summary': 'test'})
    assert cache.get_gemini_summary('id1') == {'summary': 'test'}

def test_cache_search_results(cache):
    cache.cache_search_results('query', [1,2,3])
    assert cache.get_search_results('query') == [1,2,3]
