from node import Node

class BinaryTree:

    def __init__(self):
        self.rootNode = None

    def insertNumber(self, number):
        newNode = Node(number)

        if (self.rootNode is None):
            self.rootNode = newNode
        else:
            self.__insertNode(self.rootNode, newNode)

    def __insertNode(self, rootNode, nodeToInsert):
        if (rootNode.hasLeftNode() and nodeToInsert.isLesserThan(rootNode)):
            self.__insertNode(rootNode.left, nodeToInsert)
        elif (rootNode.hasRightNode() and nodeToInsert.isGreaterThan(rootNode)):
            self.__insertNode(rootNode.right, nodeToInsert)
        elif (nodeToInsert.isLesserThan(rootNode)):
            rootNode.insertLeftNode(nodeToInsert)
        elif (nodeToInsert.isGreaterThan(rootNode)):
            rootNode.insertRightNode(nodeToInsert)

    def findNode(self, number):
        return self.__findNode(self.rootNode, number)

    def __findNode(self, rootNode, number):
        if (number == rootNode.number):
            return rootNode
        elif (number > rootNode.number):
            return self.__findNode(rootNode.right, number)
        elif (number < rootNode.number):
            return self.__findNode(rootNode.left, number)

    def removeNode(self, number):
        return self.__removeNode(self.rootNode, number)

    def __removeNode(self, rootNode, number):
        # no rootNode
        if (rootNode is None):
            return rootNode
        elif (number < rootNode.number):
            rootNode.left = self.__removeNode(rootNode.left, number)
        elif (number > rootNode.number):
            rootNode.right = self.__removeNode(rootNode.right, number)
        else:
            if (not rootNode.hasLeftNode() and not rootNode.hasRightNode()):
                return None

            if (rootNode.hasLeftNode() and rootNode.hasRightNode()):
                minNode = self.__findMinNode(rootNode.right)
                rootNode.number = minNode.number
                rootNode.right = self.__removeNode(rootNode.right, minNode.number)
                return rootNode
            
            if (not rootNode.hasRightNode()):
                leftNode = rootNode.left
                rootNode = None
                return leftNode
            
            if (not rootNode.hasLeftNode()):
                rightNode = rootNode.right
                rootNode = None
                return rightNode
            
    def __findMinNode(self, rootNode):
        if (not rootNode.hasLeftNode()):
            return rootNode
        else:
            return self.__findMinNode(rootNode.left)

    # Left, root, right
    def printInorder(self):
        self.__DFT_Inorder(self.rootNode)

    def __DFT_Inorder(self, rootNode):
        if (rootNode is not None):
            self.__DFT_Inorder(rootNode.left)
            print(rootNode.number)
            self.__DFT_Inorder(rootNode.right)

    # Root, left, right
    def printPreorder(self):
        self.__DFT_Preorder(self.rootNode)

    def __DFT_Preorder(self, rootNode):
        if (rootNode is not None):
            print(rootNode.number)
            self.__DFT_Preorder(rootNode.left)
            self.__DFT_Preorder(rootNode.right)

    # left, right, root
    def printPostorder(self):
        self.__DFT_Postorder(self.rootNode)

    def __DFT_Postorder(self, rootNode):
        if (rootNode is not None):
            self.__DFT_Postorder(rootNode.left)
            self.__DFT_Postorder(rootNode.right)
            print(rootNode.number)

    def printBFT(self):
        self.__BFT_execute(self.rootNode)

    def __BFT_execute(self, rootNode):
        queue = []
        queue.append(rootNode)

        for node in queue:
            print(node.number)

            if (node.hasLeftNode()):
                queue.append(node.left)

            if (node.hasRightNode()):
                queue.append(node.right)