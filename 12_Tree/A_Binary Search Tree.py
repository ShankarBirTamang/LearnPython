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

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __len__(self):
        return self.size()

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
            left = start.left
            right = start.right
            start.right = left
            start.left = right
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

    def reverseorder_print(self,start):
            if start is None:
                return
            
            queue = Queue()
            stack = Stack()
            queue.enqueue(start)

            traversal = ""
            while len(queue)>0:
                node = queue.dequeue()
                stack.push(node)
                if node.right:
                    queue.enqueue(node.right)
                if node.left:
                    queue.enqueue(node.left)
            while len(stack)>0:
                node= stack.pop()
                traversal += str(node.value)+" - "
            return traversal

    def min_node(self):
        while self.left:
            self = self.left
        print("Node with smallest value: ",self.value)
    
    def max_node(self):
        while self.right:
            self = self.right
        print("Node with largest value: ",self.value)

    def delete(self,item,rvalue):
            if self.value is None:
                print("Tree is Empty.")
                return
            if item<self.value:
                if self.left:
                    self.left = self.left.delete(item,rvalue)
                else:
                    print(item," is not present.")
            elif item > self.value:
                if self.right:
                    self.right = self.right.delete(item,rvalue)
                else:
                    print(item, " is not present.")
            else:
                # Deleting nodes with 0 or 1 child
                if self.left is None:
                    temp = self.right
                    # if the item is root value 
                    if item == rvalue:
                        self.value = temp.value
                        self.left = temp.left
                        self.right = temp.right
                        temp = None
                        return
                    self = None
                    return temp
                if self.right is None:
                    print("No right child")
                    temp = self.left
                    # if the item is root value
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

    def height(self,node):
            if node is None:
                return -1
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            return 1+max(left_height,right_height)

    def count(self,node):
        if node is None:
            return 0
        return 1+(self.count(node.left))+self.count(node.right)

tree = BST(None)
print("Binary Search Tree created with an empty node.")
print("Enter any no. (1 to 5): ")
print("1.INSERTION\n2.SEARCH\n3.DELETION\n4.PREORDER TRAVERSAL\n5.INORDER TRAVERSAL")
print("\n6.POST ORDER TRAVERSAL\n7.LEVEL ORDER TRAVERSAL\n8.REVERSE ORDER TRAVERSAL")
print("\n9.HEIGHT\n10.SIZE\n11.MAXIMUM\n12.MINIMUM\n13.INVERT BST")
num = int(input())
myswitch = {
	1: "ONE",
	2: "TWO",
	3: "THREE",
	4: "FOUR",
	5: "FIVE"
}
myswitch.get(num)
list1 = list(map(int,input("Enter the values to be inserted in the BST: ").split()))
for i in list1:
    tree.insert(i)

print("Pre order(N,L,R): ",tree.preorder_print(tree,""))
print("In order(L,N,R): ",tree.inorder_print(tree,""))
print("Post order(L,R,N): ",tree.postorder_print(tree,""))
print("Level order: ",tree.levelorder_print(tree))
print("Reverse Order: ",tree.reverseorder_print(tree))
tree.invert_BST(tree)
print("Levelorder after Inverted: ",tree.levelorder_print(tree))

num = int(input("Enter the item to be searched: "))
tree.search(num)

tree.min_node()
tree.max_node()

list2= list(map(int,input("Enter the items to be deleted: ").split()))
for i in list2:
    print("Deletion operation started for item: ",i)
    if tree.count(tree)>1:
        tree.delete(i,tree.value)
    else:
        print("Can't perform deletion.")
    print()

print("Height of tree:",tree.height(tree))
print("Total no of nodes: ",tree.count(tree))