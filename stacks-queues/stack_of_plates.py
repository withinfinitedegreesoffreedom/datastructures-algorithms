import unittest

class SetOfStacks:
    def __init__(self,stack_capacity):
        self.stack_capacity = stack_capacity
        self.list = []
        self.acting_stack = 1

    def push(self, data):
        self.list.append(data)
        self.acting_stack = (self.length() // self.stack_capacity) + 1
        return True

    def pop(self):
        if not self.is_Empty():
            item = self.list.pop()
            self.acting_stack = (self.length() // self.stack_capacity) + 1
            return item
        else:
            raise IndexError("Empty stack")
        
    def popAt(self, stack_num):
        if stack_num == self.acting_stack:
            return self.pop()
        elif stack_num < self.acting_stack:
            idx = (stack_num-1) * self.stack_capacity + (self.stack_capacity - 1)
            item = self.list.pop(idx)
            self.acting_stack = (self.length() // self.stack_capacity) + 1
            return item
        elif stack_num > self.acting_stack:
            raise IndexError("Requested stack doesn't exist")
        elif stack_num == 0:
            raise ValueError("Stack number has to be > 0")

    def length(self):
        return len(self.list)

    def is_Empty(self):
        return self.length() == 0

class Test(unittest.TestCase):
    def setUp(self):
        self.stacks = SetOfStacks(4)

    def test_setofstacks(self):
        l = [1,2,3,4,5,6,7,8,9]
        for item in l:
            self.stacks.push(item)
            self.assertEqual(self.stacks.acting_stack, (len(self.stacks.list)//self.stacks.stack_capacity)+1)
        self.assertEqual(self.stacks.pop(), 9)
        self.assertEqual(self.stacks.popAt(1), 4)
        self.assertTrue(self.stacks.push(11))
        #print(self.stacks.list)
        self.assertEqual(self.stacks.popAt(2), 11)

if __name__=="__main__":
    unittest.main()