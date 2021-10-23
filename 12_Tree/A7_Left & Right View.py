
class BST(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def right_view(self,start): 
        result = []
        level = []
        queue = [start]
        while len(queue)>0 and start is not None :
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            result.append(node.value)
            queue = level
            level = []
        return result  
    
    def left_view(self,start):
        result=[]
        level = []
        queue = [start]
        while len(queue)>0 and start is not None:
            for node in queue:
                if node.left :
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            result.append(queue[0].value)
            # to check the value of queue at each level
            # for i in range(len(queue)):
            #     print(queue[i].value,end = " ")
            # print()
            queue = level
            level = []
        return result



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

print("Right view of binary tree: ",tree.right_view(tree))
print("Left view of binary tree: ",tree.left_view(tree))