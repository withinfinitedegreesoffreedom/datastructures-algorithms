import unittest

class MultiStack:
    def __init__(self, num_stacks, stack_capacity):
        self.stack_capacity = stack_capacity
        self.num_stacks = num_stacks
        self.list = [None] * (self.num_stacks*self.stack_capacity)
        self.size = [0] * self.num_stacks

    def push(self, stack_num, data):
        if stack_num <= self.num_stacks:
            if self.size[stack_num-1] != self.stack_capacity:
                idx = (stack_num-1)*self.stack_capacity+self.size[stack_num-1]
                self.list[idx] = data
                self.size[stack_num-1] += 1
                return True
            else:
                raise IndexError("Stack is full")
        else:
            raise ValueError("Requested stack doesn't exist")

    def pop(self, stack_num):
        if stack_num <= self.num_stacks:
            if self.size[stack_num-1] > 0:
                idx = (stack_num-1)*self.stack_capacity+(self.size[stack_num-1]-1)
                value = self.list[idx]
                self.list[idx] = None
                self.size[stack_num-1] -= 1
                return value
            else:
                raise ValueError("Empty stack")
        else:
            raise ValueError("Requested stack doesn't exist")

    def peek(self, stack_num):
        if self.size[stack_num-1] > 0:
            idx = (stack_num-1)*self.stack_capacity+(self.size[stack_num-1]-1)
            return self.list[idx]
        else:
            raise IndexError("Empty stack")

    def isEmpty(self, stack_num):
        if self.size[stack_num-1] == 0:
            return True
        else:
            return False


class Test(unittest.TestCase):
    def setUp(self):
        self.multistack = MultiStack(3, 4)
    
    def test_1(self):
        self.assertTrue(self.multistack.push(2, 10))
        print(self.multistack.list)
        self.assertTrue(self.multistack.push(3, 11))
        print(self.multistack.list)
        self.assertTrue(self.multistack.push(1, 9))
        print(self.multistack.list)
        self.assertEqual(self.multistack.pop(2), 10)
        self.assertEqual(self.multistack.pop(3), 11)
        print(self.multistack.list)
        with self.assertRaises(IndexError) as ctx:
            self.multistack.peek(2)
        self.assertEqual("Empty stack", str(ctx.exception))


if __name__=="__main__":
    unittest.main()