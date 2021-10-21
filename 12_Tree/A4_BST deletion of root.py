# This program can delete the root node when it has only one subtree too.

class BST(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def delete(self,item,rvalue):
        if self.value is None:
            print("Tree is Empty.")
            return
        if item<self.value:
            print(item," is less than ",self.value)
            if self.left:
                print("Left child present")
                self.left = self.left.delete(item,rvalue)
            else:
                print(item," is not present.")
        elif item > self.value:
            print(item," is greater than ",self.value)
            if self.right:
                print("Right child present")
                self.right = self.right.delete(item,rvalue)
            else:
                print(item, " is not present.")
        else:
            print(self.value, " is gonna be deleted.")
            # Deleting nodes with 0 or 1 child
            if self.left is None:
                print("No left child")
                temp = self.right
                if item == rvalue:
                    self.value = temp.value
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                print(self.value," is deleted.")
                self = None
                return temp
            if self.right is None:
                print("No right child")
                temp = self.left
                if item == rvalue:
                    self.value = temp.value
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
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
            self.right = self.right.delete(node.value,rvalue)
            print()
        return self

    def preorder_print(self,start,traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.value)+" - ")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal

    
def count(node):
    if node is None:
        return 0
    return 1+(count(node.left))+count(node.right)

# main
root = BST(6)
# root.right = BST(8)
root.left = BST(2)

print("Number of nodes: ",count(root))
print()
if count(root)>1:
    root.delete(6,root.value)
else:
    print("Can't perform deletion")

print("Preorder(N,L,R):",root.preorder_print(root,""))
