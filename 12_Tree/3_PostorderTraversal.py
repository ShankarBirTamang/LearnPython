# DEPTH FIRST SEARCH --> POSTORDER TRAVERSAL (L,R,N)
# 1.Check if the current node is empty
# 2.Traverse left subtree by recursively calling postorder function
# 3.Traverse right subtree by recursively calling postorder function
# 4.Display the data part of the root (or current node)

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
    
    def postorder_print(self,start,traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.postorder_print(start.left,traversal)
            traversal = self.postorder_print(start.right,traversal)
            traversal += str(start.value)+" - "
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

print("Post order Traversal: ",tree.postorder_print(tree.root,""))