class AVLNode(object):

    def __init__(self, data, parentNode):
        self.data = data
        self.parentNode = parentNode
        self.rightChild = None
        self.leftChild = None
        self.balance = 0

    def insert(self, data, parentNode):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = AVLNode(data, parentNode)
            else:
                self.leftChild.insert(data, parentNode)
        else:
            if not self.rightChild:
                self.rightChild = AVLNode(data, parentNode)
            else:
                self.rightChild.insert(data, parentNode)
        return parentNode


    def getMin(self):
        if self.leftChild is None:
            return self.data
        else:
            return self.leftChild.getMin()

    def getMax(self):
        if self.rightChild is None:
            return self.data
        else:
            return self.rightChild.getMax()

    def traverseInOrder(self):
        if self.leftChild is not None:
            self.leftChild.traverseInOrder()
        print(self.data)

        if self.rightChild is not None:
            self.rightChild.traverseInOrder()