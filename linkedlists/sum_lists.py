import unittest

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val=None):
        self.head = Node(val)

    def length(self):
        if self.head is None:
            return 0
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

def  sum_lists(l1, l2):
    if l1.head is None  and l2.head is None:
        return None
    elif l1.head is None:
        return l2
    elif l2.head is None:
        return l1

    if l1.length() > l2.length():
        p1 = l1.head
        p2 = l2.head
    else:
        p1 = l2.head
        p2 = l1.head
    p3 = LinkedList()

    carry = 0
    while p1:
        if p2:
            s = p1.value + p2.value + carry
            p2 = p2.next
        else:
            s = p1.value + carry
        carry = 0
        if s>=10:
            carry = s//10
            s = s-10
        insert(p3, s)
        p1 = p1.next
    return p3

def insert(llist, value):
    if llist.head.value is None:
        llist.head = Node(value)
    else:
        cur = llist.head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)

def llist_traversal(l):
    if l.head is None:
        return []
    queue = []
    cur = l.head
    while cur:
        queue.append(cur.value)
        cur = cur.next
    return queue


class Test(unittest.TestCase):
    def setUp(self):
        l1 = LinkedList(7)
        l1.head.next = Node(1)
        l1.head.next.next = Node(6)
        #l1.head.next.next.next = Node(1)
        self.l1 = l1
        l2 = LinkedList(5)
        l2.head.next = Node(9)
        l2.head.next.next = Node(2)
        self.l2 = l2

    def test_sum_lists(self):
        self.l3 = sum_lists(self.l1, self.l2)
        self.assertEqual(llist_traversal(self.l3),[2,1,9])

if __name__=="__main__":
    unittest.main()




