import unittest

class Stack:
    def __init__(self):
        self.list =  []

    def push(self, item):
        self.list.append(item)

    def peek(self):
        return self.list[-1]

    def pop(self):
        return self.list.pop()

    def is_Empty(self):
        return len(self.list) == 0

class MinStack:
    def  __init__(self):
        self.list = []
        self.mins = Stack()

    def push(self, data):
        self.list.append(data)
        if self.mins.is_Empty():
            self.mins.push(data)
        elif self.mins.peek() > data:
            self.mins.push(data)
    
    def pop(self):
        if len(self.list) > 0:
            item = self.list.pop()
            if self.mins.peek() == item:
                self.mins.pop()
            return item
        else:
            return None
    
    def min(self):
        if not self.mins.is_Empty():
            return self.mins.peek()
        else:
            return None

class Test(unittest.TestCase):
    def setUp(self):
        self.minstack = MinStack()
        self.minstack.push(10)
        self.minstack.push(5)
        self.minstack.push(3)

    def test_minstack(self):
        self.assertEqual(self.minstack.min(), 3)
        self.minstack.pop()
        self.assertEqual(self.minstack.min(), 5)
        self.minstack.pop()
        self.assertEqual(self.minstack.min(), 3)
        self.minstack.pop()
        self.assertEqual(self.minstack.min(), None)

if __name__=="__main__":
    unittest.main()