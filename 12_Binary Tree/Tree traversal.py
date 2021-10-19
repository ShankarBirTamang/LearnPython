# Preorder traversal
# Inorder traversal
# Postorder traversal
# Level order traversal
# Reverse Level order traversal

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



class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
    
    def print_tree(self,traversal_type):
        if traversal_type == "preorder" :
            return self.preorder_print(tree.root,"")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root,"")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root,"")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverseorder":
            return self.reverseorder_print(tree.root)
        else:
            print(str(traversal_type), " is not supported.")
            return False

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

print("Preorder: ",tree.print_tree("preorder"))
print("inorder: ",tree.print_tree("inorder"))
print("Postorder: ",tree.print_tree("postorder"))
print("Levelorder: ",tree.print_tree("levelorder"))
print("Reverse order: ",tree.print_tree("reverseorder"))


