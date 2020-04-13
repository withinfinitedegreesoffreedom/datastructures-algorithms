from stack import Stack

class MinStack:
    def __init__(self):
        self.list = []
        self.mins = Stack()

    def push(self, item):
        self.list.append(item)
        if self.mins.isEmpty():
            self.mins.push(item)
        else:
            if self.mins.peek() > item:
                self.mins.push(item)
        return 

    def pop(self):
        last_item = self.list[-1]               
        self.list = self.list[0:-1]
        if self.mins.peek() == last_item:
            self.mins.pop()
        return

    def min(self):
        if not self.mins.isEmpty():
            return self.mins.peek()
        return 

min_stack = MinStack()
min_stack.push(5)
print(min_stack.min())
min_stack.push(6)
print(min_stack.min())
min_stack.push(3)
print(min_stack.min())
min_stack.push(7)
print(min_stack.min())
min_stack.pop()
print(min_stack.min())
min_stack.pop()
print(min_stack.min())


