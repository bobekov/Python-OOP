def type_check(param_type):
    def decorator(func):
        def wrapper(param):
            if not isinstance(param, param_type):
                return "Bad Type"
            return func(param)

        return wrapper

    return decorator