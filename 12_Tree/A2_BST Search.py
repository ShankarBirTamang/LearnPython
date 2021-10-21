

class BST(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def search(self,item):
        if self.value == item:
            print(item, " is found. ")
            return
        elif item < self.value:
            if self.left:
                self.left.search(item)
            else:
                print(item," is not found.")
        else:
            if self.right:
                self.right.search(item)
            else:
                print(item," is not found ")

#               1
#              /  \
#             2    3
#            / \    \
#           4   5    6
#          / \
#         7   8

# main
tree = BST(1)
tree.left = BST(2)
tree.right = BST(3)
tree.left.left = BST(4)
tree.left.right = BST(5)
tree.right.right = BST(6)
tree.left.left.left = BST(7)
tree.left.left.right = BST(8)

tree.search(6)        
tree.search(9)        