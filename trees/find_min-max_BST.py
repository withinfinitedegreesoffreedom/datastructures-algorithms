# Find the minimum element in a BST 
import unittest

# tree node class
class  Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

# recursive - find min 
def _find_min_BST(node):
    if node is None: 
        return -1

    if node.left is None:
        return node.value
    else:
        return _find_min_BST(node.left)

# iterative - find min
def find_min_BST(node):
    if node is None:
        return -1 

    while node.left:
        node = node.left 

    return node.value

# recursive - find max
def _find_max_BST(node):
    if node is None:
        return -1

    if node.right is None:
        return  node.value
    else:
        return _find_max_BST(node.right)

# iterative - find max
def find_max_BST(node):
    if node is None:
        return -1

    while node.right:
        node = node.right
    
    return node.value

class Test(unittest.TestCase):
    def test_check_min_max_BST(self):
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
        self.assertEqual(_find_min_BST(n1), 1)
        self.assertEqual(find_min_BST(n1), 1)
        self.assertEqual(_find_max_BST(n1), 6)
        self.assertEqual(find_max_BST(n1), 6)

if __name__=='__main__':
    unittest.main()

