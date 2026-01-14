import jwt
import time
from datetime import datetime, timedelta


SECRET_KEY = "Vlad"
ALGORITHM = "HS256"

NAME = "Vlad"
AGE = 16
CITY = "kristiansund"


print("\n--- TOKEN 1000s ---")

payload_1000 = {
    "name": NAME,
    "age": AGE,
    "city": CITY,
    "exp": datetime.utcnow() + timedelta(seconds=1000)
}

token_1000 = jwt.encode(payload_1000, SECRET_KEY, algorithm=ALGORITHM)
print("TOKEN:", token_1000)

decoded_1000 = jwt.decode(token_1000, SECRET_KEY, algorithms=[ALGORITHM])
print("DECODED:", decoded_1000)


print("\n--- TOKEN 10s (expired) ---")

payload_10 = {
    "name": NAME,
    "age": AGE,
    "city": CITY,
    "exp": datetime.utcnow() + timedelta(seconds=10)
}

token_10 = jwt.encode(payload_10, SECRET_KEY, algorithm=ALGORITHM)
print("TOKEN:", token_10)

time.sleep(15)

try:
    jwt.decode(token_10, SECRET_KEY, algorithms=[ALGORITHM])
except Exception as e:
    print("ERROR:", type(e).__name__, e)



print("\n--- TOKEN 500s (secret) ---")

payload_500 = {
    "name": NAME,
    "age": AGE,
    "city": CITY,
    "exp": datetime.utcnow() + timedelta(seconds=500)
}

token_500 = jwt.encode(payload_500, SECRET_KEY, algorithm=ALGORITHM)
print("TOKEN:", token_500)

WRONG_SECRET = "wrong_secret_key"

try:
    jwt.decode(token_500, WRONG_SECRET, algorithms=[ALGORITHM])
except Exception as e:
    print("ERROR:", type(e).__name__, e)
