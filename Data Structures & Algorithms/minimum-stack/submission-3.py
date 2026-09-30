class MinStack:

    def __init__(self):
        self.minItem = None
        self.stack = []

    def push(self, val: int) -> None:
        if self.minItem is None or self.minItem > val:
            self.minItem = (val)
        self.stack.append((val, self.minItem))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            if self.stack:
                self.minItem = self.stack[-1][1]
            else:
                self.minItem = None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minItem