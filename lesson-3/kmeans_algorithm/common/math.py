import numpy as np


def eulerDistance(vA, vB):
    """计算两个点的欧拉距离""" # 开方((x1-x2)^2 + (y1-y2)^2)   # numpy 的功能 , np -> numpy   #sqrt 开方、sum 求和、power指数。
    return np.sqrt(np.sum(np.power(vA - vB, 2)))
