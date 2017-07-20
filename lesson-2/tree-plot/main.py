from tree import TreeNode, DecisionTree
from treeplot import TreePlot


# 主函数
def main():
    # age：年龄，<30或者>=30
    # beautiful：是否漂亮，yes或者no
    # temperament：性格、脾气，good或者bad
    rootNode = TreeNode(label='age', children={
        '<30': TreeNode(label='beautiful', children={
            'yes': TreeNode(label='temperament', children={
                'good': TreeNode(label='accept'),
                'bad': TreeNode(label='deny')
            }),
            'no': TreeNode(label='deny')
        }),
        '>=30': TreeNode(label='deny')
    })

    tree = DecisionTree(root=rootNode)
    treePlot = TreePlot()
    treePlot.plotTree(tree)

    # 测试数据
    testData = [{
        'age': '>=30'
    }, {
        'age': '<30',
        'beautiful': 'yes',
        'temperament': 'good'
    },  {
        'age': '<30',
        'beautiful': 'yes',
        'temperament': 'bad'
    }, {
        'age': '<30',
        'beautiful': 'no'
    }]

    # 预测结果
    result = tree.predict(testData)
    print(result)

# 如果模块名称是__main__（使用python执行该模块）
# 则执行main函数
if __name__ == '__main__':
    main()
