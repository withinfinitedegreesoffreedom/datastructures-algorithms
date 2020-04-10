from binary_search_tree import *
from binary_tree import *

def validate_bst(node):
    return validate_bst_helper(node, float("-inf"), float("inf"))

def validate_bst_helper(node, low, high):
    if not node:
        return True

    if node.value < low or node.value > high:
        return False

    left = validate_bst_helper(node.left, low, node.value)
    right = validate_bst_helper(node.right, node.value, high)
    return left and right

bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

bst=BinaryTree(8)
bst.root.left = Node(3)
bst.root.right = Node(20)
bst.root.left.left = Node(1)
bst.root.left.right = Node(15)

print(validate_bst(bst.root))