class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_traversal(self, start_node, traversal):
        # Root->left->right
        if start_node:
            traversal += str(start_node.value) + "-"
            traversal = self.preorder_traversal(start_node.left, traversal)
            traversal = self.preorder_traversal(start_node.right, traversal)
        return traversal

    def inorder_traversal(self, start_node, traversal):
        #  Left->root->right
        if start_node:
            traversal = self.inorder_traversal(start_node.left, traversal)
            traversal += str(start_node.value) + "-"
            traversal = self.inorder_traversal(start_node.right, traversal)
        return traversal

    def postorder_traversal(self, start_node, traversal):
        # Left->right->root
        if start_node:
            traversal = self.postorder_traversal(start_node.left, traversal)
            traversal = self.postorder_traversal(start_node.right, traversal)
            traversal += str(start_node.value) + "-"
        return traversal

    def levelorder_traversal(self, q, traversal):
        if len(q) > 0:
            start_node = q.pop(0)
            traversal += str(start_node.value) + "-"
        else:
            return traversal

        if start_node.left:
            q.append(start_node.left)

        if start_node.right:
            q.append(start_node.right)

        traversal = self.levelorder_traversal(q, traversal)
        return traversal

    def _levelorder_traversal(self, start):
        q = []
        if start is None:
            return
        else:
            q.append(start)

        traversal = ""
        while len(q) > 0:
            traversal += str(q[0].value) + "-"
            node = q.pop(0)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return traversal

    def reverse_levelorder_traversal(self, start):
        q = []
        st = []
        if start is None:
            return
        else:
            q.append(start)

        while len(q)>0:
            node = q.pop(0)
            st.append(node.value)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        traversal =  ""
        while len(st)>0:
            traversal += str(st[-1]) + "-"
            st.pop()

        return traversal
            
    def print_tree(self, traversal):
        if traversal=="preorder":
            return self.preorder_traversal(self.root, "")
        elif traversal=="inorder":
            return self.inorder_traversal(self.root, "")
        elif traversal=="postorder":
            return self.postorder_traversal(self.root, "")
        elif traversal=="levelorder":
            return self.levelorder_traversal([self.root], "")
        elif traversal=="_levelorder":
            return self._levelorder_traversal(self.root)
        elif traversal=="reverse_levelorder":
            return self.reverse_levelorder_traversal(self.root)
        else:
            return "Traversal type not supported!"

    def height(self, start):
        if start is None:
            return -1
        leftheight = self.height(start.left)
        rightheight = self.height(start.right)
        return 1+max(leftheight, rightheight)

    def size(self, start):
        if start is None:
            return 0
        
        st = []
        size = 0
        st.append(start)
        size += 1

        while len(st) > 0:
            node = st.pop(0)
            if node.left:
                size += 1
                st.append(node.left)
            if node.right:
                size += 1
                st.append(node.right)
        return size

    def _size(self, start):
        if start is None:
            return 0
        return 1 + self._size(start.left) + self._size(start.right)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.right = Node(8)
tree.root.left.left.left = Node(9)


print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
#print(tree.print_tree("_levelorder"))
print(tree.print_tree("reverse_levelorder"))
print(tree.height(tree.root))
print(tree.size(tree.root))
print(tree._size(tree.root))