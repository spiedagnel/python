from DataStructures.AVLTree import AVLTree

tree = AVLTree()

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)

tree.traverseInOrder()

tree = AVLTree()

tree.insert(5)
tree.insert(7)
tree.insert(6)


tree.traverseInOrder()