# check if a given binary tree is binary search tree
import unittest

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def IsBinarySearchTree(node):
    return IsBSTUtil(node, float("-inf"), float("inf"))


def IsBSTUtil(node, low, high):
    if node is None:
        return True

    if node.value > low and node.value < high and IsBSTUtil(node.left, low, node.value) and IsBSTUtil(node.right, node.value, high):
        return True
    else:
        return False

class Test(unittest.TestCase):
    def test_is_bst(self):
        n1 = Node(4)
        n2 = Node(2)
        n3 = Node(1)
        n4 = Node(3)
        n1.left = n2
        n2.left = n3
        n2.right = n4
        n5 = Node(6)
        n6 = Node(5)
        n1.right = n5
        n5.left =  n6
        self.assertTrue(IsBinarySearchTree(n1))
        n1 = Node(4)
        n2 = Node(2)
        n3 = Node(10)
        n4 = Node(3)
        n1.left = n2
        n2.left = n3
        n2.right = n4
        n5 = Node(6)
        n6 = Node(5)
        n1.right = n5
        n5.left =  n6
        self.assertFalse(IsBinarySearchTree(n1))
        
if __name__=="__main__":
    unittest.main()