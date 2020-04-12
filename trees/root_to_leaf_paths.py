
import unittest

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def print_root_to_leaf_paths(root, stack):
    if root is None:
        return

    stack.append(root.value)
    print_root_to_leaf_paths(root.left, stack)
    if root.left is None and root.right is None:
        print(stack)
    print_root_to_leaf_paths(root.right, stack)

    stack.pop()

class Test(unittest.TestCase):
    def setup(self):
        n1 = Node(12)
        n2 = Node(5)
        n3 = Node(3)
        n4 = Node(1)
        n5 = Node(7)
        n6 = Node(9)
        n10 = Node(15)
        n1.left = n2
        n2.left = n3
        n3.left = n4
        n2.right = n5
        n5.right = n6
        n1.right = n10
        return n1

    def test_print_paths(self):
        n1 = self.setup()
        print_root_to_leaf_paths(n1, [])

if __name__=="__main__":
    unittest.main()