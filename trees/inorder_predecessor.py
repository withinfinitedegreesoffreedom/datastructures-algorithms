
import unittest
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def findMax(node):
    if node is None:
        return None

    while node.right:
        node = node.right

    return node


def find(root, data):
    if root is None:
        return None
    if data < root.value:
        return find(root.left, data)
    elif data > root.value:
        return find(root.right, data)
    else:
        return root


def inorder_predecessor(root, data):
    if root is None:
        return None

    current = find(root, data)

    if current.left:
        predecessor = findMax(current.left)
    else:
        predecessor = None
        ancestor = root
        while ancestor != current:
            if current.value > ancestor.value:
                predecessor = ancestor
                ancestor = ancestor.right
            else:
                ancestor = ancestor.left
    return predecessor

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

    def test_inorder_predecessor_noleftsubtree(self):
        root = self.gen_BST()
        predecessor = inorder_predecessor(root, 9)
        self.assertEqual(predecessor.value, 7)

    def test_inorder_predecessor_leftsubtree(self):
        root = self.gen_BST()
        predecessor = inorder_predecessor(root, 15)
        self.assertEqual(predecessor.value, 13)
    
if __name__=="__main__":
    unittest.main()    

        
