import unittest


class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        self.head = Node(val)

def kth_to_last_element(head, k):
    if head is None:
        return None

    fast = head
    slow = head
    
    for i in range(0, k):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    return slow.value


class Test(unittest.TestCase):
    def setUp(self):
        l = [1,2,3,4,5,6,7,8,9,10]
        self.llist = LinkedList(l[0])
        cur = self.llist.head
        i = 1
        while i < len(l):
            cur.next = Node(l[i])
            cur = cur.next
            i += 1

    def test_kth_to_last_element(self):
        self.assertEqual(kth_to_last_element(self.llist.head, 0), 10)
        self.assertEqual(kth_to_last_element(self.llist.head, 3), 7)

if __name__=="__main__":
    unittest.main()


