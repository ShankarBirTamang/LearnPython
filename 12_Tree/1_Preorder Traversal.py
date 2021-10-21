# BINARY TREE is a data structure in which each node has at most two children , referred as left child and right child.
# COMPLETE BINARY TREE : every level except possibly the last is completely filled , and all nodes in the last level are as far left as possible
# FULL BINARY TREE / PROPER OR PLANE BINARY TREE : every node has either 0 or 2 children

# DEPTH FIRST SEARCH --> PREORDER TRAVERSAL(N,L,R)
# 1.Check if the current node is empty
# 2.Display the data part of the root (or current node)
# 3.Traverse left subtree by recursively calling the preorder function
# 4.Traverse right subtree by recursively calling the preorder function

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def preorder_print(self,start,traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += str(start.value)+" - "
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal


#               1
#              /  \
#             2    3
#            / \    \
#           4   5    6
#          / \
#         7   8

# main
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
tree.root.left.left.left = Node(7)
tree.root.left.left.right = Node(8)

print("Preorder traversal: ",tree.preorder_print(tree.root,""))

