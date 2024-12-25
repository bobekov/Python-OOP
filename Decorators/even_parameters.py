def even_parameters(func):
    def wrapper(*args):
        if any(not isinstance(el, int) or el % 2 != 0 for el in args):
            return "Please use only even numbers!"
        return func(*args)

    return wrapper