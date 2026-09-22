class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_ = float('inf')

    def push(self, val: int) -> None:
        if val < self.min_:
            self.min_ = val
        self.stack.append((val, self.min_))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min_ = self.stack[-1][1]
        else:
            self.min_ = float('inf')
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
