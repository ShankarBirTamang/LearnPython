# Calculate the size of binary tree
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


class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def size(self):
        if self.root is None:
            return 0
        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size+=1
                stack.push(node.right)
        return size
    
    # Alternative method
    def size_(self,node):
        if node is None:
            return 0
        return 1+(self.size_(node.left))+(self.size_(node.right))


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

print("Size of tree: ",tree.size())
print("Size of tree: ",tree.size_(tree.root))