class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        mina = None
        for i in self.stack:
            if isinstance(i, int):
                if mina is None:
                    mina = i
                else:
                    mina = min(mina, i)
        return mina
