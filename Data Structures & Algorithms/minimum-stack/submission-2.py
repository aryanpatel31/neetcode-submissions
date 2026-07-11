class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum == []:
            self.minimum.append((None, val))
        elif val <= self.minimum[-1][1]:
            self.minimum.append((self.minimum[-1][1], val))
        
        

    def pop(self) -> None:
        pop = self.stack.pop(-1)
        if pop is self.minimum[-1][1]:
            self.minimum.pop(-1)
        
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1][1]

        
