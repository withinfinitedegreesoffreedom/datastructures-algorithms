# one linkedlist per level of a binary tree

from binary_tree import *

# simpled linkedlist and node classes
class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        self.head = LinkedNode(val)

# BFS solution 
def bfs_tree_to_linkedlist(q,llists):
    new_nodes=[]
    if len(q) > 0:
        llist = LinkedList(q[0].value)
        prev = llist.head
        if q[0].left:
            new_nodes.append(q[0].left)
        if q[0].right:
            new_nodes.append(q[0].right)
    else:
        return llists
    if len(q) == 1:
        llists.append(llist)
    else:
        for i in range(1, len(q)):
            prev.next = LinkedNode(q[i].value)
            if q[i].left:
                new_nodes.append(q[i].left)
            if q[i].right:
                new_nodes.append(q[i].right)
            prev = prev.next
        llists.append(llist)
    llists = bfs_tree_to_linkedlist(new_nodes, llists)     
    return llists
 
# create a binary tree
tree=BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.right = Node(8)
tree.root.left.left.left = Node(9)
# some checks
print(tree.print_tree("levelorder"))
llists = bfs_tree_to_linkedlist([tree.root],[])
print(llists)

# traverse the linkedlists returned 
traversal = ""
for llist in llists:
    cur_node = llist.head
    while cur_node is not None:
        traversal += str(cur_node.val)+"-"
        cur_node = cur_node.next

print(traversal)
    