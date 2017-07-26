import numpy as np

def randCent(dataSet, k):
    # generate cent randomly
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k, n)))

    for j in range(n):
        # retrieve minimum from shape n
        minJ = min(dataSet[:, j])
        # retrieve maximum and use max - min
        rangeJ = float(max(dataSet[:, j]) - minJ)

        # p = min + range * randomNumber
        centroids[:, j] = minJ + rangeJ * np.random.rand(k, 1)

    return centroids

# kmeans algorithm main logic
def kMeans(dataSet, k, distOp, centOp):
    # retrieve centroids
    centroids = centOp(dataSet, k)

    # retrieve sample number of dataSet
    dataCount = np.shape(dataSet)[0]
    clusterResult = np.mat(np.zeros((dataCount, 2)))

    while True:
        clusterChanged = clusterData(centroids, clusterResult, dataCount, dataSet, distOp, k)
        if not clusterChanged:
            break

        # reset cents array for next round of iteration
        resetCentroids(centroids, clusterResult, dataSet, k)

    return centroids, clusterResult

def resetCentroids(centroids, clusterResult, dataSet, k):
    for centIndex in range(k):
        # .A means converting matrix to an array
        clusterMap = clusterResult[:, 0].A == centIndex

        # retrieve index of sample according to clusterMap
        clusterPointIndexes = np.nonzero(clusterMap)[0]

        # get sample cent
        clusterPoints = dataSet[clusterPointIndexes]

        # axis means calculating mean value in column
        centroids[centIndex, :] = np.mean(clusterPoints, axis=0)

def clusterData(centroids, clusterResult, dataCount, dataSet, distOp, k):
    clusterChanged = False
    for datumIndex in range(dataCount):
        # get a sample
        datum = dataSet[datumIndex, :]
        minDist, minIndex = findMinCent(datum, centroids, k, distOp)

        if clusterResult[datumIndex, 0] != minIndex:
            clusterChanged = True

        # record cluster result
        clusterResult[datumIndex, :] = minIndex, minDist ** 2

    return clusterChanged

def findMinCent(datum, centroids, k, distOp):
    minDist = np.inf
    minIndex = -1

    # traverse centroids
    for centroidsIndex in range(k):
        centroid = centroids[centroidsIndex, :]
        # calculate distance between datum and cent in centroids
        dist = distOp(datum, centroid)

        if dist < minDist:
            minDist = dist
            minIndex = centroidsIndex

    return minDist, minIndex