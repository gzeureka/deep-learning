from tree import Tree, TreeNode
# from treeplot import TreePlot, DECISION_NODE, LEAF_NODE
from treeplot import TreePlot

rootNode = TreeNode(label='age', children={
    '<30': TreeNode(label='beautiful', children={
            'yes': TreeNode(label='temperament', children={
                'yes': TreeNode(label='accept'),
                'no': TreeNode(label='deny')
            }),
            'no': TreeNode(label='deny')
        }),
        '>=30': TreeNode(label='deny')
})

tree = Tree(rootNode)

print(tree.getHeight(), tree.getWidth())

treePlot = TreePlot()
# treePlot.plotNode('age', (0.5, 0.8), (0.5, 0.8), DECISION_NODE)
# treePlot.plotText('<30', (0.3, 0.6), (0.5, 0.8))
# treePlot.plotNode('beautiful', (0.3, 0.6), (0.5, 0.8), DECISION_NODE)
# treePlot.plotText('>=30', (0.7, 0.6), (0.5, 0.8))
# treePlot.plotNode('deny', (0.7, 0.6), (0.5, 0.8), LEAF_NODE)
# treePlot.show()
treePlot.plotTree(tree)