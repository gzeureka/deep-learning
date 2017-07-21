class TreeNode(object):
    def __init__(self, label, children={}):
        print('Construct tree node')

        self.label = label
        self.children = children

    def isLeaf(self):
        return len(self.children) == 0

    def getHeight(self):
        if self.isLeaf():
            return 1

        return 1 + max([child.getHeight() for child in self.children.values()])

    def getWidth(self):
        if self.isLeaf():
            return 1

        return sum([child.getWidth() for child in self.children.values()])

class Tree(object):
    def __init__(self, rootNode):
        self.rootNode = rootNode

    def getHeight(self):
        if self.rootNode is None:
            return 0

        return self.rootNode.getHeight()

    def getWidth(self):
        if self.rootNode is None:
            return 0

        return self.rootNode.getWidth()
