class MinStack:

    def __init__(self):
        self.stack = []
        self.minValueStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minValue = min(val, self.minValueStack[-1] if self.minValueStack else val)
        self.minValueStack.append(minValue)

    def pop(self) -> None:
        self.stack.pop()
        self.minValueStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValueStack[-1]
