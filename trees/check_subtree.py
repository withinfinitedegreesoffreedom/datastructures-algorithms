
import unittest

class Node:
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None


def check_subtree(ltree, stree):
    if stree is None:
        return True
    elif ltree is None:
        return False
    elif ltree.value == stree.value:
        return match_tree(ltree, stree)
    return check_subtree(ltree.left, stree) or check_subtree(ltree.right, stree)

def match_tree(ltree, stree):
    if ltree is None and stree is None:
        return True
    elif ltree is None or stree is None:
        return False
    elif ltree.value != stree.value:
        return False
    else:
        return match_tree(ltree.left, stree.left) and match_tree(ltree.right, stree.right)


class Test(unittest.TestCase):
    def gen_ltree(self):
        n1 = Node(12)
        n2 = Node(5)
        n3 = Node(3)
        n4 = Node(1)
        n5 = Node(7)
        n6 = Node(9)
        n7 = Node(10)
        n8 = Node(8)
        n9 = Node(11)
        n10 = Node(15)
        n11 = Node(13)
        n12 = Node(17)
        n13 = Node(16)
        n14 = Node(18)
        n1.left = n2
        n2.left = n3
        n3.left = n4
        n2.right = n5
        n5.right = n6
        n6.right = n7
        n7.left = n8
        n7.right = n9
        n1.right = n10
        n10.left = n11
        n10.right = n12
        n12.left = n13
        n12.right = n14
        return n1

    def gen_stree(self):
        n1 = Node(10)
        n2 = Node(8)
        n3 = Node(11)
        n1.left = n2
        n1.right = n3
        return n1

    def test_check_subtree_1(self):
        ltree = self.gen_ltree()
        stree = self.gen_stree()
        self.assertTrue(check_subtree(ltree, stree))

    def test_check_subtree_2(self):
        ltree = self.gen_ltree()
        stree = self.gen_stree()
        stree.left = Node(12)
        self.assertFalse(check_subtree(ltree, stree))

if __name__=="__main__":
    unittest.main()