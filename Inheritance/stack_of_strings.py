class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            raise 'Error'
        self.data.append(element)

    def pop(self):
        last_el = self.data.pop()
        return last_el

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        reversed_data = list(reversed(self.data))
        return f"[{', '.join(reversed_data)}]"