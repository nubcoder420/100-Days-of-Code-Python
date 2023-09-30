
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"You called {func.__name__}({', '.join(map(str, args))})")
        result = func(*args, **kwargs)
        print(f"It returned {result}")
        # return result
    return wrapper

@logging_decorator
def a_function(x, y, z):
    return int(x) + int(y) + int(z)

print(a_function(1, 2, 3))
