class Stack:
    def __init__(self, items=None, limit=1000):
        self.items = items if items is not None else []
        self.limit = limit

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        # Search from top of the stack: top is end of list
        try:
            index = self.items[::-1].index(target)
            return index
        except ValueError:
            return -1
