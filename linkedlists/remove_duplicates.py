import unittest

class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        self.head = Node(val)

def remove_duplicates(head):
    if head is None:
        return None
    else:
        dup = {}
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            if cur.value not in dup:
                dup[cur.value] = 1
                prev = cur
                cur = cur.next
            else:
                prev.next = nxt
                cur = nxt
    return head

def llist_traversal(head):
    if head is None:
        return []
    queue = []
    cur = head 
    while cur:
        queue.append(cur.value)
        cur =cur.next
    return queue

class Test(unittest.TestCase):
    def setUp(self):
        self.llist = LinkedList(1)
        self.llist.head.next = Node(2)
        self.llist.head.next.next = Node(2)
        self.llist.head.next.next.next = Node(3)
        self.llist.head.next.next.next.next = Node(4)
        
    def test_remove_duplicates(self):
        self.assertEqual(llist_traversal(remove_duplicates(self.llist.head)), [1,2,3,4])

if __name__=="__main__":
    unittest.main()
        


