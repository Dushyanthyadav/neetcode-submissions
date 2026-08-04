class MinStack:

    def __init__(self):
        self.stack = []
        self.extra = []
        

    def push(self, val: int) -> None:
        if not self.stack and not self.extra:
            self.stack.append(val)
            self.extra.append(val)
        else:
            mini = min(val, self.extra[-1])
            self.stack.append(val)
            self.extra.append(mini)


    def pop(self) -> None:
        self.stack.pop()
        self.extra.pop()

        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.extra[-1]
