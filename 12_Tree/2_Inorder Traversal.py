# DEPTH FIRST SEARCH --> INORDER TRAVERSAL (L,N,R)
# 1.Check if the current node is empty
# 2.Traverse left subtree by recursively calling inorder function
# 3.Display the data part of the root (or current node)
# 4.Traverse right subtree by recursively calling inorder function

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
    
    def inorder_print(self,start,traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal += str(start.value)+" - "
            traversal = self.inorder_print(start.right,traversal)
        return traversal

#               1
#              /  \
#             2    3
#            / \    \
#           4   5    6
#          / \
#         7   8

# Set up tree
tree = BinaryTree(1)
tree.root.left=Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
tree.root.left.left.left = Node(7)
tree.root.left.left.right = Node(8)

print("Inorder traversal: ",tree.inorder_print(tree.root,""))