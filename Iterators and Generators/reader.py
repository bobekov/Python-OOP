def read_next(*args):
    for collection in args:
        for el in collection:
            yield el