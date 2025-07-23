import os
import redis
import json

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

class RedisCache:
    def __init__(self, prefix='newsbot', ttl=3600):
        self.client = redis.Redis.from_url(REDIS_URL)
        self.prefix = prefix
        self.ttl = ttl

    def _make_key(self, key):
        return f"{self.prefix}:{key}"

    def set(self, key, value, ttl=None):
        ttl = ttl or self.ttl
        self.client.set(self._make_key(key), json.dumps(value), ex=ttl)

    def get(self, key):
        val = self.client.get(self._make_key(key))
        if val:
            return json.loads(val)
        return None

    def cache_gemini_summary(self, article_id, summary):
        self.set(f"gemini:{article_id}", summary)

    def get_gemini_summary(self, article_id):
        return self.get(f"gemini:{article_id}")

    def cache_search_results(self, query, results):
        self.set(f"search:{query}", results)

    def get_search_results(self, query):
        return self.get(f"search:{query}")
