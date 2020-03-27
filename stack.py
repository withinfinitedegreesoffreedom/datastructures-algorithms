class Stack:
    def __init__(self):
        self.list = []

    def display(self):
        return self.list

    def length(self):
        return len(self.list)

    def isEmpty(self):
        return self.length() == 0

    def push(self, item):
        self.list.append(item)
        return

    def pop(self):
        if self.length():
            self.list = self.list[0:len(self.list)-1]
            return
        else:
            print("Nothing to pop!")

    def peek(self):
        return self.list[-1]


mystack = Stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
print(mystack.display())
print(mystack.peek())
mystack.pop()
print(mystack.display())



