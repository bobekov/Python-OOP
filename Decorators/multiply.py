def multiply(n):

    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * n
        return wrapper

    return decorator