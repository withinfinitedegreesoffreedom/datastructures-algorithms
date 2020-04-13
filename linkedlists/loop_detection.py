import unittest

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val=None):
        self.head = Node(val)


def loop_detection(llist):
    if llist.head is None:
        return None

    slow = llist.head
    fast = llist.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    
    if not fast or not fast.next:
        return None

    slow = llist.head
    while slow!=fast:
        slow = slow.next
        fast = fast.next
    
    return fast

class Test(unittest.TestCase):
    def setUp(self):
        n1 = LinkedList(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        n7 = Node(7)
        n8 = Node(8)
        n9 = Node(9)
        n10 = Node(10)
        n11 = Node(11)
        n1.head.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n6
        n6.next = n7
        n7.next = n8
        n8.next = n9
        n9.next = n10
        n10.next = n11
        n11.next  = n4
        self.llist = n1

    def test_loop_detection(self):
        self.assertEqual(loop_detection(self.llist).value, 4)

if __name__=="__main__":
    unittest.main()