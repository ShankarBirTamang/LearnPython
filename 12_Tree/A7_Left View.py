
class BST(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def left_view(self,start,level,traversal):
        
        if start :  
            maxlevel = 0
            if level>=maxlevel:
                print("Node: ",start.value)
                print("maxlevel:",maxlevel,"\tlevel: ",level)
                maxlevel = level
                print("maxlevel:",maxlevel,"\tlevel: ",level)
                print()
                traversal+= str(start.value)+"-"
                traversal=self.left_view(start.left,level+1,traversal)
                traversal=self.left_view(start.right,level+1,traversal)
            else:
                print("maxlevel:",maxlevel,"\tlevel: ",level)
                print()
            
        return traversal



#  at each level only one left most node is viewed.

#               8           --> level 1
#              /  \
#             4    9        --> level 2
#            / \    \
#           2   5    10      --> level 3
#          / \   \
#         1   3   6
#                  \
#                   7

# main
tree = BST(8)
tree.left = BST(4)
tree.right = BST(9)
tree.left.left = BST(2)
tree.left.right = BST(5)
tree.right.right = BST(10)
tree.left.left.left = BST(1)
tree.left.left.right = BST(3)
tree.left.right.right = BST(6)
tree.left.right.right.right = BST(7)

print(tree.left_view(tree,0,""))