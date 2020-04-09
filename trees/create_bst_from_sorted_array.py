# create a bst from sorted array

# Node and binary tree classes 
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, val=None):
        self.root = Node(val)

# helper
def _create_minimal_bst(array):
    return create_minimal_bst(array, 0, len(array)-1)

# function with logic
def create_minimal_bst(array, start, end):
    if end < start:
        return

    mid = (start+end)//2
    treenode = Node(array[mid])
    treenode.left = create_minimal_bst(array, start, mid-1)
    treenode.right = create_minimal_bst(array, mid+1, end)
    return treenode

# test code 
array = [1,2,3,4,5,6,7] # should be sorted in ascending order
treenode = _create_minimal_bst(array)
print(treenode)