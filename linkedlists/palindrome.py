import unittest

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        self.head = Node(val)

def panlindrome(llist):
    if llist.head is None:
        return True

    slow = llist.head
    fast = llist.head

    stack = []
    while fast is not None and fast.next is not None:
        stack.append(slow.value)
        slow = slow.next        
        fast = fast.next.next
    
    if fast != None:
        slow = slow.next
    
    while slow:
        if stack.pop() != slow.value:
            return False
        slow = slow.next
    return True

class Test(unittest.TestCase):
    def setUp(self):
        self.l = [5,4,3,2,1,2,3,4,5]
        self.llist = LinkedList(self.l[0])
        cur = self.llist.head
        i = 1
        while i < len(self.l):
            cur.next = Node(self.l[i])
            cur = cur.next
            i += 1

    def test_palindrome(self):
        self.assertTrue(panlindrome(self.llist))

if __name__=="__main__":
    unittest.main()


