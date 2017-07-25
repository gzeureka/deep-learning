class TreeNode(object):
    def __init__(self, label, **kwargs):
        # lable为节点标签
        self.label = label
        # children为边标签和孩子节点的字典
        self.children = kwargs.get('children', {})

    def isLeaf(self):
        return len(self.children) == 0

    def getHeight(self):
        # 如果是叶子结点，高度为1
        if self.isLeaf():
            return 1

        # 如果是非叶子节点，高度为子树最大高度+1
        return 1 + max([child.getHeight() for child in self.children.values()])

    def getWidth(self):
        # 如果是叶子结点，宽度为1
        if self.isLeaf():
            return 1

        # 如果是非叶子结点，高度为子树最大宽度
        return sum([child.getWidth() for child in self.children.values()])


class Tree(object):
    def __init__(self, **kwargs):
        self.root = kwargs.get('root', None)

    def getHeight(self):
        if self.root is None:
            return 0

        return self.root.getHeight()

    def getWidth(self):
        if self.root is None:
            return 0

        return self.root.getWidth()
