class BST(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def min_node(self):
        while self.left:
            self = self.left
        print("Node with smallest value: ",self.value)
    
    def max_node(self):
        while self.right:
            self = self.right
        print("Node with largest value: ",self.value)

    def inorder_print(self,start,traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal += (str(start.value)+" - ")
            traversal = self.inorder_print(start.right,traversal)
        return traversal

    def postorder_print(self,start,traversal):
        """Left -> Right ->Root"""
        if start:
            traversal = self.postorder_print(start.left,traversal)
            traversal = self.postorder_print(start.right,traversal)
            traversal += (str(start.value)+" - ")
        return traversal

    def preorder_print(self,start,traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.value)+" - ")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal

#               6
#              /  \
#             4    7
#            / \    \
#           2   5    8
#          / \
#         1   3

# main
tree = BST(6)
tree.left = BST(4)
tree.right = BST(7)
tree.left.left = BST(2)
tree.left.right = BST(5)
tree.right.right = BST(8)
tree.left.left.left = BST(1)
tree.left.left.right = BST(3)
print("Preorder(N,L,R):",tree.preorder_print(tree,""))
print("Inorder(L,N,R): ",tree.inorder_print(tree,""))
print("Postorder(L,R,N): ",tree.postorder_print(tree,""))

tree.max_node()
tree.min_node()

