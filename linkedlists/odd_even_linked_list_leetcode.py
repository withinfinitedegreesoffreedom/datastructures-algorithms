import unittest

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val=None):
        self.head = Node(val)

def oddEvenList(head):
    if head is None:
        return

    odd_head = head
    even_head = odd_head.next

    odd = odd_head
    even = even_head
    while odd.next and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return odd_head

def llist_traversal(head):
    if head is None:
        return []
    stack=[]
    cur=head
    while cur:
        stack.append(cur.value)
        cur=cur.next
    return stack

class Test(unittest.TestCase):
    def setUp(self):
        self.l = LinkedList(1)
        self.l.head.next = Node(2)
        self.l.head.next.next = Node(3)
        self.l.head.next.next.next = Node(4)
        self.l.head.next.next.next.next = Node(5)
        #self.l.head.next.next.next.next.next = Node(4)
        #self.l.head.next.next.next.next.next.next = Node(7)

    def test(self):
        o = oddEvenList(self.l.head)
        self.assertEqual(llist_traversal(o), [1,3,5,2,4])

if __name__=="__main__":
    unittest.main()


        