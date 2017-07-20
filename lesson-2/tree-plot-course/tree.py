class TreeNode(object):
    def __init__(self, label, children={}):
        print('Construct tree node')

        self.label = label
        self.children = children

    def isLeaf(self):
        return len(self.children) == 0


class Tree(object):
    def __init__(self, rootNode):
        self.rootNode = rootNode
