from binary_tree import BinaryTree

tree = BinaryTree()

tree.insertNumber(4)
tree.insertNumber(2)
tree.insertNumber(3)
tree.insertNumber(1)
tree.insertNumber(10)
tree.insertNumber(6)
tree.insertNumber(11)
tree.insertNumber(5)
tree.insertNumber(7)
tree.insertNumber(12)


tree.printInorder()
tree.removeNode(10)
print('post remove')
tree.printInorder()