import redis
import config

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USER,
    password=config.REDIS_PASSWORD,
)

pubsub = redis_client.pubsub()
pubsub.subscribe("school")

print("Listening for messages from channel 'school'...")

with open("messages.txt", "a", encoding="utf-8") as file:
    for message in pubsub.listen():

        if message["type"] == "message":
            text = message["data"]
            print("Received:", text)

            if "контрольная работа" in text.lower():
                file.write(text + "\n")
                print("Saved to file!")