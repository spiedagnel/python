from DataStructures.BSTNode import BSTNode

class BST(object):

    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        if not self.rootNode:
            self.rootNode = BSTNode(data)
        else:
            self.rootNode.insert(data)

    def remove(self, data):
        if self.rootNode:
            if self.rootNode.data == data:
                tempNode = BSTNode(data)
                tempNode.leftChild = self.rootNode
                self.rootNode.remove(data. tempNode)
                self.rootNode = tempNode.leftChild
            else:
                self.rootNode.remove(data, None)

    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMax()

    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin()

    def traverseInOrder(self):
        if self.rootNode:
            self.rootNode.traverseInOrder()
