"""Basic connection example.
"""

import redis
import config

import redis
import datetime as dt
import time

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USER,
    password=config.REDIS_PASSWORD,
)

redis_client.set("car", "Tesla y")
print("Car saved:", redis_client.get("car"))

redis_client.set("pet", "Dog", ex=2 * 60 * 60)
print("Pet saved with TTL:", redis_client.get("pet"))

redis_client.delete("products")
redis_client.rpush("products", "milk", "bread", "eggs", "cheese")
redis_client.expire("products", 7 * 24 * 60 * 60)
print("Products list:", redis_client.lrange("products", 0, -1))

redis_client.hset("cake", mapping={"flour": 250, "milk": 500})
print("Cake ingredients:", redis_client.hgetall("cake"))

redis_client.hset("cake", "sugar", 300)
print("Add sugar:", redis_client.hgetall("cake"))

redis_client.hset("cake", "sugar", 500)
print("Fix sugar:", redis_client.hgetall("cake"))

redis_client.delete("cake")
print("Cake deleted:", redis_client.hgetall("cake"))

for i in range(10):
    message = input("Enter message to publish: ")
    redis_client.publish("school", message)
    print(f"Sent: {message}")
    time.sleep(1)
