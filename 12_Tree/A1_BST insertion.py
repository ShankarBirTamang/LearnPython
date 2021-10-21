
class BST(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,item):
        if self.value is None:
            self.value = item
            print(self.value," is inserted .")
            return
        if self.value == item:
            print(self.value," is already inserted.")
            return
        if item < self.value :
            print(item," is less than ",self.value)
            if self.left:
                print("Left child present.")
                self.left.insert(item)
            else:
                print("Left child not present.")
                self.left = BST(item)
                print("Created Left child with value: ", item)
                print()
        else:
            print(item," is greater than ",self.value)
            if self.right:
                print("Right child present.")
                self.right.insert(item)
            else:
                print("Right child not present.")
                self.right = BST(item)
                print("Created right child with value: ",item)
                print()
 
tree = BST(None)
list1 = list(map(int,input("Enter the values to be inserted in the BST: ").split()))
for i in list1:
    tree.insert(i)