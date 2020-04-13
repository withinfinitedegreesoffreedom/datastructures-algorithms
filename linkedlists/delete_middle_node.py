import unittest

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        self.head = Node(val)

def delete_middle_node(node):
    if not node or not node.next:
        return False

    cur = node
    cur.value = cur.next.value
    cur.next = cur.next.next
    return True

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
        self.l = [1,2,3,4,5,6,7,8,9,10]
        self.llist = LinkedList(self.l[0])
        cur = self.llist.head
        i = 1
        while i < len(self.l):
            cur.next = Node(self.l[i])
            cur = cur.next
            i += 1

    def test_delete_middle_node(self):
        cur = self.llist.head
        i = 0
        while i < 4:
            cur = cur.next
            i += 1
        self.assertTrue(delete_middle_node(cur))
        cur = self.llist.head
        i = 0
        while i < len(self.l)-1:
            cur = cur.next
            i += 1
        self.assertFalse(delete_middle_node(cur))

if __name__=="__main__":
    unittest.main() 

