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
        
    def invert_BST(self,start):
        if start:
            left = start.left
            right = start.right
            start.right = left
            start.left = right
            self.invert_BST(start.left)
            self.invert_BST(start.right)

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


#               1
#              /  \
#             2    3
#            / \    \
#           4   5    6
#          / \
#         7   8

# main
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
tree.root.left.left.left = Node(7)
tree.root.left.left.right = Node(8)

print("Level order: ",tree.levelorder_print(tree.root))
tree.invert_BST(tree.root)
print("Level order: ",tree.levelorder_print(tree.root))

