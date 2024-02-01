from functools import reduce
numbers = [89, 92, 78, 83,]
avg = reduce(lambda x,y: x+y, numbers) / len(numbers)


def lowercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func()
        return result.lower()
    return wrapper

@lowercase_decorator
def greet():
    return f"Your Average is, {avg}!"

print(greet("average"))