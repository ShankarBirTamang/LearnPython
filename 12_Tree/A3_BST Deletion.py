class BST(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def delete(self,item):
        if self.value is None:
            print("Tree is Empty.")
            return
        if item<self.value:
            print(item," is less than ",self.value)
            if self.left:
                print("Left child present")
                self.left = self.left.delete(item)
            else:
                print(item," is not present.")
        elif item > self.value:
            print(item," is greater than ",self.value)
            if self.right:
                print("Right child present")
                self.right = self.right.delete(item)
            else:
                print(item, " is not present.")
        else:
            print(self.value, " is gonna be deleted.")
            # Deleting nodes with 0 or 1 child
            if self.left is None:
                print("No left child")
                temp = self.right
                print(self.value," is deleted.")
                self = None
                return temp
            if self.right is None:
                print("No right child")
                temp = self.left
                print(self.value," is deleted.")
                self = None
                return temp
            # Deleting nodes with 2 child
            # Smallest nodes of right subtree or Largest nodes of left subtree takes place
            # To find and replace with smallest nodes of right subtree
            print("Left and right child detected")
            node = self.right
            while node.left:
                node = node.left
            print(self.value ," is replaced with ",node.value)
            self.value = node.value
            self.right = self.right.delete(node.value)
            print()
        return self


            # Alternatively:
            # # To find and replace with largest node of left subtree
            # node = self.left
            # while node.right:
            #     node = node.right
            #     self.value = node.value
            #     self.left = self.left.delete(node.value)

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

list1= list(map(int,input("Enter the items to be deleted: ").split()))
for i in list1:
    print("Deletion operation started for item: ",i)
    tree.delete(i)
    print()


print("Preorder(N,L,R):",tree.preorder_print(tree,""))
print("Inorder(L,N,R): ",tree.inorder_print(tree,""))
print("Postorder(L,R,N): ",tree.postorder_print(tree,""))

