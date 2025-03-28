class reverse_iter :
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.current_index = len(self.iter_obj) - 1
        self.end_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.end_index:
            raise StopIteration
        index = self.current_index
        self.current_index -= 1
        return self.iter_obj[index]