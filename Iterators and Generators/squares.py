def squares(n):
    current = 1
    while not current > n:
        yield current * current
        current += 1