"""FP-Growth算法实现"""
# TODO: 实现挖掘频繁项集

from common.tree import TreeNode, Tree


class FpTreeNode(TreeNode):
    """FPTree节点实现，继承自TreeNode"""
    def __init__(self, name, count, parent):
        # 生成label并调用基类初始化方法
        label = '{name}: {count}'.format(name=name, count=count)
        super(FpTreeNode, self).__init__(label=label)

        # 项目名称
        self.name = name
        # 项目计数
        self.count = count
        # 父节点
        self.parent = parent
        # 下一节点（连接相同项目的节点）
        self.nextNode = None

    def addCount(self, count):
        """增加计数"""
        self.count += count
        # 重新生成标签
        self.label = '{name}: {count}'.format(name=self.name, count=self.count)


class FpTree(Tree):
    """FPTree树实现，继承自Tree"""
    def __init__(self, transactions, supportThreshold):
        # 调用基类初始化方法
        # 初始化根节点（名称为root）
        super(FpTree, self).__init__(root=FpTreeNode(name='root', count=0, parent=None))

        # 支持度阈值
        self.supportThreshold = supportThreshold
        # 符合要求的项目
        self.items = []
        # 项目频数
        self.itemCounts = {}
        # 头指针表
        self.headerTable = {}

        # 创建树
        self.createTree(transactions)

    def createTree(self, transactions):
        """创建FP树"""
        # 筛选满足支持度阈值的项目
        self.items, self.itemCounts, transactions = self.filterItemsBySupport(transactions)
        # 排序事务中的项目
        self.sortTransactions(transactions)

        # 遍历事务，更新FP树
        for transaction in transactions:
            self.updateTree(transaction, self.root)

    def filterItemsBySupport(self, transactions):
        """根据支持度筛选项目并处理事务，将不符合要求的项目从事务中删除"""
        transactionSets = [set(transaction) for transaction in transactions]
        itemCounts = {}

        # 遍历所有事务
        for transaction in transactionSets:
            # 遍历事务中的项并计算项集在事务中的出现次数
            for item in transaction:
                itemCount = itemCounts.get(item, 0)
                itemCounts[item] = itemCount + 1

        filteredItems = []
        transactionCount = len(transactions)

        # 遍历所有的项集计数
        for item, itemCount in itemCounts.items():
            # 计算支持度
            support = itemCount / transactionCount
            # 根据阈值筛选项集
            if support >= self.supportThreshold:
                # 如果符合阈值要求则保留项目
                filteredItems.append({
                    'name': item,
                    'count': itemCount
                })
            else:
                # 如果不符合阈值要求则将事务中的对应项目删除掉
                for transaction in transactionSets:
                    if item in transaction:
                        transaction.remove(item)

        # 将处理过的事务转换回列表
        filteredTransactions = [list(transaction) for transaction in transactionSets]
        return filteredItems, itemCounts, filteredTransactions

    def sortTransactions(self, transactions):
        """将事务内的项目排序"""
        for transaction in transactions:
            # 根据项目技术倒序排序
            transaction.sort(key=lambda itemName: self.itemCounts[itemName], reverse=True)

    def updateTree(self, items, treeNode):
        """根据事务剩余项目更新FP树"""
        # 如果事务中没有项目就直接返回
        if len(items) == 0:
            return

        # 取事务项目列表中剩余的第一个项目
        item = items[0]
        # 如果该项目不是当前节点的子节点
        if item not in treeNode.children:
            # 创建孩子节点
            childNode = FpTreeNode(name=item, count=0, parent=treeNode)
            # 插入孩子节点
            treeNode.children[item] = childNode
            # 更新头指针表
            self.updateHeaderTable(item, childNode)

        # 将对应的孩子节点技术加1
        childNode = treeNode.children[item]
        childNode.addCount(1)

        # 递归处理事务项目列表中的后续项目
        self.updateTree(items[1:], childNode)

    def updateHeaderTable(self, item, childNode):
        """更新头指针表"""
        # 如果头指针表中不存在该项目则将孩子节点插入
        if item not in self.headerTable:
            self.headerTable[item] = childNode
        else:
            # 否则将孩子节点放到节点链表的最后
            currentNode = self.headerTable[item]
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode

            currentNode.nextNode = childNode
