from redis_namespace_client import redis_set, redis_get, redis_delete, redis_key_exists, list_all_keys

redis_set("test123", {"hello": "world"}, ex=10)
print(redis_get("test123"))
