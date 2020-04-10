# Deleting a node from BST such that the property of BST is not lost

import  unittest
class Node:
    def  __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def findMin(node):
    if node is None:
        return None
    while node.left:
        node = node.left
    return node

def delete_nodes(node, data):
    if node is None:
        return node
    elif data < node.value:
        node.left = delete_nodes(node.left, data)
    elif data > node.value:
        node.right = delete_nodes(node.right, data)
    else:
        if node.left is None and node.right is None:
            node = None
        elif node.left is None and node.right is not None:
            node = node.right
        elif node.left is not None and node.right is None:
            node = node.left
        else:
            temp = findMin(node.right)
            node.value = temp.value
            node.right = delete_nodes(node.right, temp.value)
    return node

class Test(unittest.TestCase):
    def gen_bst(self):
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

    def inorder_bst(self, node, traversal):
        if node:
            traversal = self.inorder_bst(node.left, traversal)
            traversal += str(node.value) + "-"
            traversal = self.inorder_bst(node.right, traversal)
        return traversal

    def test_delete_node_no_children(self):
        node = self.gen_bst()
        node = delete_nodes(node, 1)
        self.assertEqual(node.value, 12)
        print("remove 1: "+ self.inorder_bst(node, ""))

    def test_delete_node_one_child(self):
        node = self.gen_bst()
        node = delete_nodes(node, 3)
        self.assertEqual(node.value, 12)
        print("remove 3: "+ self.inorder_bst(node, ""))
        node = delete_nodes(node, 7)
        self.assertEqual(node.value, 12)
        print("remove 7: "+ self.inorder_bst(node, ""))

    def test_delete_node_two_children(self):
        node = self.gen_bst()
        node = delete_nodes(node, 15)
        self.assertEqual(node.value, 12)
        print("remove 15: "+ self.inorder_bst(node, ""))

if __name__=="__main__":
    unittest.main()