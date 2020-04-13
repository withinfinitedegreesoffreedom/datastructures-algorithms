import unittest

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val=None):
        self.head = Node(val)

def partition(head, part):
    if head:
        main = head
    after = LinkedList(None)
    before = LinkedList(None)

    pa = after.head
    pb = before.head

    while main:
        if main.value < part:
            insert(before, main.value)
            #pb = pb.next
        else:
            insert(after, main.value)
            #pa = pa.next
        main=main.next
    
    llist = join(before, after)
    return llist

def insert(ptr, value):
    if ptr.head.value is None:
        ptr.head.value = value
    else:
        cur = ptr.head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)

def join(l1, l2):
    if l1.head is None and l2.head is None:
        return l1

    if l1.head is None:
        return l2
    
    if l2.head is None:
        return l1

    cur = l1.head
    while cur.next:
        cur = cur.next
    
    cur.next = l2.head

    return l1

def llist_traversal(head):
    if head is None:
        return []
    queue = []
    cur = head
    while cur:
        queue.append(cur.value)
        cur = cur.next
    return queue

class Test(unittest.TestCase):
    def setUp(self):
        self.l = [3,5,8,5,10,2,1]
        self.llist = LinkedList(self.l[0])
        cur = self.llist.head
        i = 1
        while i < len(self.l):
            cur.next = Node(self.l[i])
            cur = cur.next
            i += 1

    def test_partition(self):
        new = partition(self.llist.head, 5)
        new = llist_traversal(new.head)
        self.assertEqual(set(new), set([3,1,2,10,5,5,8]))

if __name__=="__main__":
    unittest.main()

