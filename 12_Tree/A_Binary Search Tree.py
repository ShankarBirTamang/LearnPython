# Binary Search Tree is a special type of binary tree with following properties:

# 1.The left subtree of a node contains only nodes with values lesser than node's value
# 2.The right subtree of a  node contains only nodes with values greater than node's value
# 3.The left and right subtree each must also be a binary search tree.

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)


class BST(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,item):
        if self.value is None:
            self.value = item
            return
        if self.value == item:
            return
        if item < self.value :
            if self.left:
                self.left.insert(item)
            else:
                self.left = BST(item)
        else:
            if self.right:
                self.right.insert(item)
            else:
                self.right = BST(item)
    
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
    
    def invert_BST(self,start):
        if start:
            left = self.left
            right = self.right
            self.right = left
            self.left = right
            self.invert_BST(start.left)
            self.invert_BST(start.right)
        
    def preorder_print(self,start,traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.value)+" - ")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal
   
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

    def levelorder_print(self,start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue)>0:
            traversal += str(queue.peek()) + " - "
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

tree = BST(None)
list1 = list(map(int,input("Enter the values to be inserted in the BST: ").split()))
for i in list1:
    tree.insert(i)

print("Preorder(N,L,R): ",tree.preorder_print(tree,""))
print("Inorder(L,N,R): ",tree.inorder_print(tree,""))
print("Postorder(L,R,N): ",tree.postorder_print(tree,""))
print("Levelorder: ",tree.levelorder_print(tree))
tree.invert_BST(tree)
print("Levelorder after Inverted: ",tree.levelorder_print(tree))

num = int(input("Enter the item to be searched: "))
tree.search(num)
