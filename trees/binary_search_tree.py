# Implement a binary search tree with insert and find methods 

import unittest
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(data) 
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already in BST.")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)

        if is_found:
            return is_found
        else:
            return False

    def _find(self, data, cur_node):
        if data < cur_node.value and cur_node.left:
            return self._find(data, cur_node.left)
        elif data > cur_node.value and cur_node.right:
            return self._find(data, cur_node.right)
        elif data == cur_node.value:
            return True

    def inorder_traversal(self, node, traversal):
        if node:
            traversal = self.inorder_traversal(node.left, traversal)
            traversal += str(node.value) + "-"
            traversal = self.inorder_traversal(node.right, traversal)

        return traversal


class Test(unittest.TestCase):
    def test_bst_find_1(self):
        # insert will always insert the nodes such that BST property is obeyed
        bst = BST()
        bst.insert(4)
        bst.insert(2)
        bst.insert(8)
        bst.insert(5)
        bst.insert(10)
        self.assertTrue(bst.find(2))

    def test_bst_find_2(self):
        bst = BST()
        bst.insert(4)
        bst.insert(2)
        bst.insert(8)
        bst.insert(5)
        bst.insert(10)
        self.assertFalse(bst.find(11))
    

if __name__=="__main__":
    unittest.main()