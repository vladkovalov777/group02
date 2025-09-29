from functools import wraps
from typing import Callable, Any

def round_result(ndigits: int):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)
            if isinstance(result, (int, float)):
                return round(result, ndigits)
            return result
        return wrapper
    return decorator

@round_result(2)
def divide(a: float, b: float) -> float:
    return a / b

@round_result(3)
def multiply(a: float, b: float) -> float:
    return a * b

@round_result(2)
def get_text() -> str:
    return "Hello!"

print(divide(10, 3))
print(multiply(2.3456, 7.8912))
print(get_text())