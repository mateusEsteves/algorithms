class Node:

    def __init__(self, number):
        self.number = number
        self.left = None
        self.right = None
    
    def isLesserThan(self, node):
        return self.number < node.number

    def isGreaterThan(self, node):
        return self.number > node.number

    def hasLeftNode(self):
        return self.left is not None

    def hasRightNode(self):
        return self.right is not None
    
    def insertLeftNode(self, node):
        if (self.hasLeftNode() or self.isLesserThan(node)):
            raise Exception('Could not insert node at the left branch', self.number, node.number)
        
        self.left = node

    def insertRightNode(self, node):
        if (self.hasRightNode() or self.isGreaterThan(node)):
            raise Exception('Could not insert node at the right branch', self.number, node.number)

        self.right = node

    def isLeafNode(self):
        return self.left is None and self.right is None