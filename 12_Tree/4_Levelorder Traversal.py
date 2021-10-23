# BREADTH FIRST SEARCH --> LEVEL ODER TRAVERSAL
# Here , we will visit all the nodes present at the same level one by one from left to right
# and then move to next level to visit all the nodes of that level.

# Implementation:
# We will use queue data structure(FIFO) where after visiting a node, we put its left and right 
# children to queue sequentially.

class Queue(object):
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items)==0
    
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

    def levelorder_print(self,start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue)>0:
            traversal += str(queue.peek())+" - "
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
    
    # Alternative method
    def levelorder(self,start):
        result=[]
        level = []
        queue = [start]
        while len(queue)>0 and start is not None:
            for node in queue:
                if node.left :
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            for i in range(len(queue)):
                result.append(queue[i].value)
                # print(result)
            queue = level
            level = []
        return result

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

print("Level order traversal(string): ",tree.levelorder_print(tree.root))
print("Level order(list): ",tree.levelorder(tree.root))
