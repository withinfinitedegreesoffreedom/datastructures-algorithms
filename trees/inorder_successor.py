
import unittest
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def find(node, data):
    if node is None:
        return None
    if data < node.value:
        return find(node.left, data)
    elif data > node.value:
        return find(node.right, data)
    else:
        return node

def findMin(node):
    if node is None:
        return None

    while node.left:
        node = node.left
    return node

def inorder_successor(root, data):
    if root is None:
        return None

    if root:
        current = find(root, data)

    if current.right:
        successor = findMin(current.right)
    else:
        successor = None
        ancestor = root
        while ancestor != current: 
            if current.value < ancestor.value:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right
    return successor 

def find_inorder_successor(root, data):
    successor = inorder_successor(root, data)
    return successor

class Test(unittest.TestCase):
    def gen_BST(self):
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

    def test_inorder_successor_norightsubtree(self):
        root = self.gen_BST()
        successor = find_inorder_successor(root, 3)
        self.assertEqual(successor.value, 5)

    def test_inorder_successor_rightsubtree(self):
        root = self.gen_BST()
        successor = find_inorder_successor(root, 15)
        self.assertEqual(successor.value, 16)
    
if __name__=="__main__":
    unittest.main()    
