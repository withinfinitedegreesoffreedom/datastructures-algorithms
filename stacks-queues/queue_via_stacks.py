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

class QueueViaStacks:
    def __init__(self):
        self.stacknewest = Stack()
        self.stackoldest = Stack()

    def enqueue(self, item):
        self.stacknewest.push(item)

    def dequeue(self):
        self._shiftstacks()
        return self.stackoldest.pop()

    def peek(self):
        self._shiftstacks()
        return self.stackoldest.peek()
        
    def _shiftstacks(self):
        if self.stackoldest.is_Empty():
            while not self.stacknewest.is_Empty():
                self.stackoldest.push(self.stacknewest.pop())
        
class Test(unittest.TestCase):
    def setUp(self):
        self.queue = QueueViaStacks()

    def test_1(self):
        self.queue.enqueue(10)
        self.queue.enqueue(11)
        self.queue.enqueue(12)
        self.queue.enqueue(13)
        self.assertEqual(self.queue.peek(), 10)
        self.assertEqual(self.queue.dequeue(), 10)
        self.queue.enqueue(14)
        self.queue.enqueue(15)
        self.assertEqual(self.queue.peek(), 11)
        self.assertEqual(self.queue.dequeue(), 11)

if __name__=="__main__":
    unittest.main()


