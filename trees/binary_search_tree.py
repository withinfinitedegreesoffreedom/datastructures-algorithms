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

    def is_BST(self, cur_node, value):
        node = cur_node.left
        if node:
            if value > node.value:
                return self.is_BST(node, node.value)
            else:
                return False

        node = cur_node.right
        if node:
            if node.value > value:
                return self.is_BST(node, node.value)
            else:
                return False


    def _is_BST(self, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.value:
                return self._is_BST(cur_node.left, cur_node.left.value)
            else:
                return False
        if cur_node.right:
            if data < cur_node.right.value:
                return self._is_BST(cur_node.right, cur_node.right.value)
            else:
                return False


    def check_BST_property(self):
        if self.root:
            #is_BST = self.is_BST(self.root, self.root.value)
            _is_BST = self._is_BST(self.root, self.root.value)
            #print(is_BST)
            #print(_is_BST)
            if _is_BST is None:
                return True
            return False
        return True

    def inorder_traversal(self, node, traversal):
        if node:
            traversal = self.inorder_traversal(node.left, traversal)
            traversal += str(node.value) + "-"
            traversal = self.inorder_traversal(node.right, traversal)

        return traversal

    def check_BST(self, node, traversal, valid):
        if node:
            traversal = self.check_BST(node.left, traversal, valid)
            if len(traversal) > 0:
                if traversal[-1] > node.value:
                    valid = False
                else:
                    traversal.append(node.value)
            else:
                traversal.append(node.value)
            traversal = self.check_BST(node.right, traversal, valid)
        if valid:
            return traversal
        else:
            return valid


bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

'''# create a non-bst tree
bst=BST()
bst.root = Node(8)
bst.root.left = Node(3)
bst.root.right = Node(20)
bst.root.left.left = Node(1)
bst.root.left.right = Node(15)

bst = BST()
bst.root = Node(1)
bst.root.left = Node(2)
bst.root.right = Node(3)

tree = BST()
tree.root = Node(12)
tree.root.left = Node(3)
tree.root.right = Node(14)
tree.root.left.left = Node(1)
tree.root.left.right = Node(13)
tree.root.right.left = Node(11)
tree.root.right.right = Node(15)'''
print(bst.inorder_traversal(bst.root, ""))

#print(tree.find(100))
try:
    if bst.check_BST(bst.root, [], valid=True) == False:
        print(False)
except: 
    print(True)
