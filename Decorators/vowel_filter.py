def vowel_filter(function):

    def wrapper():
        result = function()
        vowels = [char for char in result if char.lower() in 'aeouyi']
        return vowels

    return wrapper