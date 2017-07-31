"""Apriori算法实现"""
# TODO：补充实现关联规则提取


def apriori(transactions, supportThreshold):
    """Apriori实现"""
    # 将每一个事务转换成集合，提高检索效率
    transactionSets = [set(transaction) for transaction in transactions]
    # 生成1项集
    itemSets = createItemSets(transactions)
    # 计算1项集支持度并筛选符合要求的项集
    filteredItemSets, supports = filterBySupport(transactionSets, itemSets, supportThreshold)
    # 保存符合要求的1项集
    itemSetsList = [filteredItemSets]

    # 如果前一次筛选的项集为空则停止循环
    while len(filteredItemSets) > 0:
        # 将k-1项集合并生成k项集
        itemSets = combineItemSets(itemSets)
        # 筛选符合要求的k项集
        filteredItemSets, newSupports = filterBySupport(
            transactionSets, itemSets, supportThreshold)

        # 保存新项集的支持度
        supports.update(newSupports)
        # 保存符合要求的k项集
        itemSetsList.append(filteredItemSets)

    return itemSetsList, supports


def createItemSets(transactions):
    """根据事务创建1项集"""
    itemSets = []

    # 遍历所有事务
    for transaction in transactions:
        # 遍历事务中项目并构造项集
        for item in transaction:
            itemSet = [item]

            if itemSet not in itemSets:
                itemSets.append(itemSet)

    # 排序并返回每一个项集的frozenset
    # frozenset是不可变集合，可以作为字典的key
    itemSets.sort()
    return [frozenset(itemSet) for itemSet in itemSets]


def filterBySupport(transactions, itemSets, threshold):
    """计算项集支持度，并根据支持度阈值筛选满足要求的项集"""
    itemSetCounts = {}

    # 遍历所有事务
    for transaction in transactions:
        # 遍历项集并计算项集在事务中的出现次数
        for itemSet in itemSets:
            if itemSet.issubset(transaction):
                # 如果项集没有出现过则返回0
                itemSetCount = itemSetCounts.get(itemSet, 0)
                itemSetCounts[itemSet] = itemSetCount + 1

    filteredItems = []
    supports = {}
    transactionCount = len(transactions)

    # 遍历所有的项集计数
    for itemSet, itemSetCount in itemSetCounts.items():
        # 计算支持度
        support = itemSetCount / transactionCount
        # 根据阈值筛选项集
        if support >= threshold:
            filteredItems.append(itemSet)
        # 保存支持度
        supports[itemSet] = support

    return filteredItems, supports


def combineItemSets(itemSets):
    """将k-1项集合并成k项集"""
    newItemSets = []
    itemSetsCount = len(itemSets)

    # 遍历提取两个项集
    for itemSet1Index in range(itemSetsCount):
        for itemSet2Index in range(itemSet1Index + 1, itemSetsCount):
            itemSet1 = itemSets[itemSet1Index]
            itemSet2 = itemSets[itemSet2Index]

            # 分别计算两个项集的差集
            diff1 = itemSet1 - itemSet2
            diff2 = itemSet2 - itemSet1

            # 如果两个项集各有一个项目不同，其他项目相同则组合成一个新项集
            if len(diff1) == 1 and len(diff2) == 1:
                newItemSet = itemSet1 | itemSet2
                if newItemSet not in newItemSets:
                    newItemSets.append(newItemSet)

    return newItemSets
