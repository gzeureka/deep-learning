import matplotlib.pyplot as plt

ARROW_ARGS = dict(arrowstyle='<-')
DECISION_NODE = dict(boxstyle='sawtooth', fc='#cab3f0')
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
