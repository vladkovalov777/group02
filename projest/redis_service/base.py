"""Basic connection example.
"""

import redis
import config

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USER,
    password=config.REDIS_PASSWORD,
)

success = redis_client.set('foo', 'bar')
# True

result = redis_client.get('foo')
print(result)
# >>> bar


