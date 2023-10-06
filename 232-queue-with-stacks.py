from collections import deque

# [1,2,3,4]
# Stack [1,2,3,4]

class MyQueue:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)
                
    def pop(self) -> int:
        while self.queue1:
            self.queue2.append(self.queue1.pop())
        x = self.queue2.pop()
        while self.queue2:
            self.queue1.append(self.queue2.pop())
        return x

    def peek(self) -> int:
        while self.queue1:
            self.queue2.append(self.queue1.pop())
        x = self.queue2[-1]
        while self.queue2:
            self.queue1.append(self.queue2.pop())
        return x

    def empty(self) -> bool:
        return len(self.queue1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



class MyQueue:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:

        while self.queue1:
            self.queue2.append(self.queue1.pop())

        self.queue1.append(x)

        while self.queue2:
            self.queue1.append(self.queue2.pop())
                
    def pop(self) -> int:
        return self.queue1.pop()

    def peek(self) -> int:
        self.queue1[-1]

    def empty(self) -> bool:
        return len(self.queue1) == 0
        

### Amortized Solution

class MyQueue:

    def __init__(self):
        self.input = deque()
        self.output = deque()

    def push(self, x: int) -> None:
        self.input.append(x)
                
    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output