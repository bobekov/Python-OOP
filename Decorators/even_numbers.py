def even_numbers(function):

    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        even_nums = [num for num in result if num % 2 == 0]
        return even_nums
    return wrapper