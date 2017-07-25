import matplotlib.pyplot as plt

# 箭头样式
ARROW_ARGS = dict(arrowstyle="<-")
# 坐标轴起点
START_AXIS = 0.1
# 坐标轴终点
END_AXIS = 0.9
# 坐标轴有效距离
AXIS_DISTANCE = END_AXIS - START_AXIS
# 决策节点样式
DECISION_NODE = dict(boxstyle='sawtooth', fc='#cab3f0')
# 叶子节点样式
LEAF_NODE = dict(boxstyle='round4', fc='#c8dcc8')

class TreePlot(object):
    def __init__(self):
        self.ax1 = plt.subplot(1, 1, 1, frameon=False)

    def plotNode(self, nodeTxt, centerPt, parentPt, nodeType):
        self.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                          xytext=centerPt, textcoords='axes fraction',
                          va='center', ha='center',
                          bbox=nodeType, arrowprops=ARROW_ARGS)

    def plotText(self, text, centerPt, parentPt):
        x = (parentPt[0] + centerPt[0]) / 2.0
        y = (parentPt[1] + centerPt[1]) / 2.0
        self.ax1.text(x, y, text)

    def show(self):
        plt.show()

    def plotTree(self, tree):
        # 如果决策树为空，什么都不做
        if tree.rootNode is None:
            return

        # 决策树绘制起点（y轴）
        startY = END_AXIS
        # 决策树高度
        treeHeight = tree.getHeight()
        # 计算每个节点之间的距离
        distanceY = AXIS_DISTANCE
        if treeHeight > 1:
            distanceY = AXIS_DISTANCE / (tree.getHeight() - 1)
        # 决策树x轴绘制范围
        startX = START_AXIS
        endX = END_AXIS

        # 绘制根节点
        self.plotTreeNode(tree.rootNode, startX, endX, startY, distanceY)

        plt.show()

    # 递归绘制决策树节点
    def plotTreeNode(self, treeNode, startX, endX, startY, distanceY, **kwargs):
        # 根据是否是叶子节点判断绘制样式
        nodeStyle = LEAF_NODE if treeNode.isLeaf() else DECISION_NODE

        # 当前节点的坐标
        centerPt = ((endX - startX) / 2 + startX, startY)
        # 获取父节点坐标，如果无父节点，说明是根节点，则其父节点为其自身
        parentPt = kwargs.get('parentPt', centerPt)
        edgeLabel = kwargs.get('edgeLabel', None)

        # 绘制当前节点
        self.plotNode(treeNode.label, centerPt, parentPt, nodeStyle)
        # 绘制判定属性值
        if edgeLabel is not None:
            self.plotText(edgeLabel, centerPt, parentPt)

        childrenCount = len(treeNode.children)
        # 如果只有一个子节点，则绘制在正下方，否则需要根据子节点宽度划分区域
        if childrenCount == 1:
            distanceX = 0
            startX = endX = centerPt[0]
        else:
            distanceX = endX - startX
        startY -= distanceY

        # 获取当前节点宽度
        totalWidth = treeNode.getWidth()
        for childEdgeLabel, childNode in treeNode.children.items():
            # 根据叶子结点宽度与当前结点宽度比计算划分区域大小
            childWidth = childNode.getWidth()
            endX = startX + distanceX * childWidth / totalWidth

            # 递归绘制子节点
            self.plotTreeNode(childNode, startX, endX, startY, distanceY,
                              parentPt=centerPt, edgeLabel=childEdgeLabel)
            startX = endX
