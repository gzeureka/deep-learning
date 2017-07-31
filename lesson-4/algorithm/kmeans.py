"""KMeans 算法实现"""
import numpy as np


def kMeans(dataSet, k, distOp, centOp):
    """KMeans 算法实现"""
    # 获取质点
    centroids = centOp(dataSet, k)
    # 第一维长度是样本数量
    dataCount = np.shape(dataSet)[0]
    # 记录每个记录分配情况
    # 第一个元素记录分配簇索引
    # 第二个元素记录和簇质点的距离
    clusterResult = np.mat(np.zeros((dataCount, 2)))

    while True:
        # 根据质点进行聚类
        # 聚类是否改变
        clusterChanged = clusterData(centroids, clusterResult, dataCount, dataSet, distOp, k)

        # 如果前一轮聚类没有变化则停止聚类过程
        if not clusterChanged:
            break

        # 根据聚类结果重置质点
        resetCentroids(centroids, clusterResult, dataSet, k)

    return centroids, clusterResult


def clusterData(centroids, clusterResult, dataCount, dataSet, distOp, k):
    """根据质点聚类数据"""
    clusterChanged = False
    # 遍历样本
    for datumIndex in range(dataCount):
        # 取出一个样本
        datum = dataSet[datumIndex, :]
        # 查找和样本距离最小的质点，得到最小距离和质点索引
        minDist, minIndex = findMinCent(datum, centroids, k, distOp)

        # 如果聚类结果发生改变则需要下一轮聚类
        if clusterResult[datumIndex, 0] != minIndex:
            clusterChanged = True

        # 记录聚类结果
        clusterResult[datumIndex, :] = minIndex, minDist ** 2
    return clusterChanged


def findMinCent(datum, centroids, k, distOp):
    """获取距离最小的质点"""
    minDist = np.inf
    minIndex = -1

    # 遍历所有质点
    for centroidIndex in range(k):
        centroid = centroids[centroidIndex, :]
        # 计算质点和当前样本距离
        dist = distOp(datum, centroid)

        # 比较设置最小质点
        if dist < minDist:
            minDist = dist
            minIndex = centroidIndex

    return minDist, minIndex


def randCent(dataSet, k):
    """随机生成质点"""
    # 获取每个样本的特征维度
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k, n)))

    # 遍历每一个维度
    for j in range(n):
        # 获取某个维度的最小值
        minJ = min(dataSet[:, j])
        # 获取某个维度的最大值并计算最大值和最小值之间的范围
        # 这里我之前多打了一个符号，应该是j不是-j
        rangeJ = float(max(dataSet[:, j]) - minJ)
        # -> 改成
        # rangeJ = float(max(dataSet[:, j]) - minJ)

        # 为每一个质点生成一个随机数
        # 并生成质点矩阵
        # 质点中的数值是 p = min + range * r
        # range * r确保不会越界
        centroids[:, j] = minJ + rangeJ * np.random.rand(k, 1)

    return centroids


def resetCentroids(centroids, clusterResult, dataSet, k):
    """根据聚类结果重置质点"""
    for centIndex in range(k):
        # 生成一个映射表
        # 如果clusterResult中对应样本聚类编号为centIndex则映射表中为1，否则为0
        clusterMap = clusterResult[:, 0].A == centIndex
        # 根据映射表获取属于某个质点聚类的样本索引
        clusterPointIndexes = np.nonzero(clusterMap)[0]
        # 获取聚类样本点
        clusterPoints = dataSet[clusterPointIndexes]

        # 将质点重置为聚类样本的均值
        # 0标表示按列求均值
        centroids[centIndex, :] = np.mean(clusterPoints, axis=0)
