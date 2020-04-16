import unittest

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val=None):
        self.head = Node(val)

    def length(self):
        if not self.head:
            return 0

        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count
    

def check_lists_intersect(list1, list2):
    if list1 is None and list2 is None:
        return False
    elif list1 is None:
        return False
    elif list2 is None:
        return False

    while list1:
        list1_prev = list1
        list1 = list1.next

    while list2:
        list2_prev = list2
        list2 = list2.next

    if list1_prev == list2_prev:
        return True
    else:
        return False

def make_same_length(list1, list2):
    if list1.length() > list2.length():
        small = list2
        large = list1
    else:
        small = list1
        large = list2

    diff = abs(list1.length()-list2.length())
    l = large.head
    while diff > 0:
        l = l.next
        diff -= 1
    
    return l, small.head

def intersection(list1, list2):
    if check_lists_intersect(list1.head, list2.head):
        large, small = make_same_length(list1, list2)
        while large:
            if large == small:
                return large.value           
            large = large.next
            small = small.next
    else:
        return None

class Test(unittest.TestCase):
    def setUp(self):
        # common body
        self.body = LinkedList(7)
        self.body.head.next = Node(2)
        self.body.head.next.next = Node(1)
        # list 1 preamble
        self.list1 = LinkedList(3)
        self.list1.head.next =  Node(1)
        self.list1.head.next.next =  Node(5)
        self.list1.head.next.next.next =  Node(9)
        # list 2 preamble
        self.list2 = LinkedList(4)
        self.list2.head.next =  Node(6)
        # merge two lists
        self.list1.head.next.next.next.next = self.body.head
        self.list2.head.next.next = self.body.head

    def test_list_intersect(self):
        self.assertTrue(check_lists_intersect(self.list1.head, self.list2.head))

    def test_intersection(self):
        self.assertEqual(intersection(self.list1, self.list2), 7)

if __name__=="__main__":
    unittest.main()