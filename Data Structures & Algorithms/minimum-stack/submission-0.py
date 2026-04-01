class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1
    
    def getMin(self) -> int:
        minimum = None
        for i, val in enumerate(self.stack):
            if minimum is None or val < minimum:
                minimum = val
        return minimum

        
