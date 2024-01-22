class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int) -> None:
        self.stack1.append(val)

        if self.stack2:
            if self.stack2[-1][0] > val:
                self.stack2.append([val, 1])
            elif self.stack2[-1][0] == val:
                self.stack2[-1][1] += 1
        else:
            self.stack2.append([val, 1])
        

    def pop(self) -> None:
 
        if self.stack1 and self.stack2:
            if self.stack1[-1] == self.stack2[-1][0]:
                self.stack2[-1][1] -= 1

                if self.stack2[-1][1] == 0:
                    self.stack2.pop()

            self.stack1.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
    


# One Stack
    
class MinStack:

    def __init__(self):
        

    def push(self, val: int) -> None:
        

    def pop(self) -> None:
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()