
import unittest
import random

class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.value = val
        self.left = left
        self.right = right
        self.parent = parent
        self.left_size = 0

    def insert(self, node):
        if node.value < self.value:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
            self.left_size += 1
        else:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def find_node(self, data):
        if self is None:
            return False
        elif self.value == data:
            return True
        elif data < self.value and self.left:
            return self.left.find_node(data)
        elif data > self.value and self.right:
            return self.right.find_node(data)

    def _get_rank(self):
        if not self.parent:
            return self.left_size
        elif self.parent.value > self.value:
            return self.left_size
        else:
            return self.left_size + self.parent._get_rank() + 1

    def _find_node_by_rank(self, rank):
        current_rank = self._get_rank()

        if rank == current_rank:
            return self
        elif rank < current_rank:
            return self.left._find_node_by_rank(rank)
        else:
            return self.right._find_node_by_rank(rank)

    def _get_highest_rank_in_tree(self):
        if self.right is None:
            return self._get_rank()
        else:
            return self.right._get_highest_rank_in_tree()

    def _generate_random_rank(self):
        return random.randint(0, self._get_highest_rank_in_tree())

    def generate_random_node(self):
        rand_rank = self._generate_random_rank()
        rand_node = self._find_node_by_rank(rand_rank)
        return rand_node

    def _find_min(self):
        if self is None:
            return None
        while self.left:
            self = self.left
        return self

    def delete_node(self, data):
        if self is None:
            return None
        elif data < self.value:
            self.left = self.left.delete_node(data)
        elif data > self.value:
            self.right = self.right.delete_node(data)
        else:
            if self.left is None and self.right is None:
                self = None
            elif self.left is None and self.right is not None:
                self = self.right
            elif self.left is not None and self.right is None:
                self = self.left
            else:
                right_subtree_min = self.right._find_min()
                self.value = right_subtree_min.value
                self.right = self.right.delete_node(right_subtree_min.value)
        return self

    def _inorder_traversal(self, start_node, traversal):
        if start_node:
            traversal = self._inorder_traversal(start_node.left, traversal)
            traversal += str(start_node.value) + "-"
            traversal = self._inorder_traversal(start_node.right, traversal)
        return traversal

class Test(unittest.TestCase):
     
    def setUp(self):
        self.binary_tree = TreeNode(7)
        self.n3 = TreeNode(3)
        self.n1 = TreeNode(1)
        self.n5 = TreeNode(5)
        self.n10 = TreeNode(10)
        self.n8 = TreeNode(8)
        self.n12 = TreeNode(12)
 
        self.binary_tree.insert(self.n3)
        self.binary_tree.insert(self.n1)
        self.binary_tree.insert(self.n5)
        self.binary_tree.insert(self.n10)
        self.binary_tree.insert(self.n8)
        self.binary_tree.insert(self.n12)

    def test_get_rank(self):
        self.assertEqual(self.binary_tree._get_rank(), 3)
        self.assertEqual(self.n1._get_rank(), 0)
        self.assertEqual(self.n5._get_rank(), 2)
        self.assertEqual(self.n10._get_rank(), 5)
        self.assertEqual(self.n12._get_rank(), 6)

    def test_get_highest_rank(self):
        self.assertEqual(self.binary_tree._get_highest_rank_in_tree(), 6)

    def test_find_node(self):
        self.assertTrue(self.binary_tree.find_node(10))
        self.assertFalse(self.binary_tree.find_node(11))

    def test_insert(self):
        self.assertEqual(self.binary_tree._inorder_traversal(self.binary_tree, ""), "1-3-5-7-8-10-12-")

    def test_delete_node(self):
        new_tree = self.binary_tree.delete_node(10)
        self.assertEqual(new_tree._inorder_traversal(new_tree, ""), "1-3-5-7-8-12-")    
    

if __name__=="__main__":
    unittest.main()