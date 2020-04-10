# find the height of a binary tree

import unittest
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return -1

    leftheight = height(node.left)
    rightheight = height(node.right)
    return max(leftheight, rightheight)+1


class Test(unittest.TestCase):
    def test_height(self):
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
        n6.right = Node(7)
        self.assertEqual(height(n1), 3)
        print(height(n1))

if __name__=='__main__':
    unittest.main()