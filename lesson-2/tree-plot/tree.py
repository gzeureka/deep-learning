class TreeNode(object):
    def __init__(self, label, children={}):
        # lable为节点标签
        self.label = label
        # children为边标签和孩子节点的字典
        self.children = children

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

        # 如果是非叶子结点，高度为子树宽度之和
        return sum([child.getWidth() for child in self.children.values()])


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def getHeight(self):
        if self.root is None:
            return 0

        return self.root.getHeight()

    def getWidth(self):
        if self.root is None:
            return 0

        return self.root.getWidth()


class DecisionTree(Tree):
    def __init__(self, **kwargs):
        # 调用父类初始化方法
        # 新式类鼓励使用这种方式初始化
        super(DecisionTree, self).__init__(**kwargs)

    # 预测一组数据
    def predict(self, items):
        result = [self.predictOne(item) for item in items]

        return result

    # 预测单个数据
    def predictOne(self, item, **kwargs):
        # 如果是叶子节点，说明已经获得了预测的分类标签
        currentNode = kwargs.get('node', self.root)
        if currentNode.isLeaf():
            return currentNode.label

        # 否则说明是决策节点，需要获取特征名称（节点标签）
        featureName = currentNode.label

        # 如果数据项中没有对应特征则抛出异常
        featureValue = item.get(featureName, None)
        if featureValue is None:
            raise KeyError('''Item don't have the key '%s'.''' % featureName)

        # 如果节点没有对应的分支则抛出异常
        nextNode = currentNode.children.get(featureValue, None)
        if nextNode is None:
            raise KeyError('''TreeNode don't have the branch '%s'.''' % featureValue)

        # 递归预测
        return self.predictOne(item, node=nextNode)
