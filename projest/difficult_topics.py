from typing import Callable, Any, Dict

def ensure_dict_result(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> Dict[str, Any]:
        result = func(*args, **kwargs)
        return {"result": result}
    return inner


@ensure_dict_result
def foo(number: int = 10) -> int:
    return number + 5


@ensure_dict_result
def bar(text: str) -> str:
    return text.upper()

print(foo(10))
print(bar("hello"))