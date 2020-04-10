
import unittest
class Node:
    def  __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def find_node(root, data):
    if root is None:
        return None
    if root.value == data:
        return root
    else: 
        return find_node(root.left, data) or find_node(root.right, data)

def findFCA(root, node1, node2):
    if root is None:
        return None

    if root == node1 or root == node2:
        return root

    left = findFCA(root.left, node1, node2)
    right = findFCA(root.right, node1, node2)

    if left and right:
        return root
    elif left is None and right is not None:
        return right
    elif right is None and left is not None:
        return left

def fca_driver(root, data1, data2):
    node1 = find_node(root, data1)
    node2 = find_node(root, data2)
    return findFCA(root, node1, node2)

class Test(unittest.TestCase):
    def get_tree(self):
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

    def test_common_ancestor_root(self):
        root = self.get_tree()
        fca = fca_driver(root, 7, 13)
        self.assertEqual(fca.value, 12)

    def test_common_ancestor_onennode(self):
        root = self.get_tree()
        fca = fca_driver(root, 7, 9)
        self.assertEqual(fca.value, 7)

    def test_common_ancestor_normal(self):
        root = self.get_tree()
        fca = fca_driver(root, 3, 10)
        self.assertEqual(fca.value, 5)


if __name__=="__main__":
    unittest.main()