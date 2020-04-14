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

def sort_stack(s):
    r = Stack()
    while not s.is_Empty():
        temp = s.pop()
        while not r.is_Empty() and r.peek() > temp:
            s.push(r.pop())
        r.push(temp)
    while not r.is_Empty():
        s.push(r.pop())
    return s

class Test(unittest.TestCase):
    def setUp(self):
        self.s = Stack()
        self.s.push(23)
        self.s.push(15)
        self.s.push(75)
        self.s.push(100)

        self.s_sorted = Stack()
        self.s_sorted.push(100)
        self.s_sorted.push(75)
        self.s_sorted.push(23)
        self.s_sorted.push(15)
    
    def test(self):
        self.assertEqual(sort_stack(self.s).list, self.s_sorted.list)

if __name__=="__main__":
    unittest.main()
        

    
