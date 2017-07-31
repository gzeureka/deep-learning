import numpy as np


def eulerDistance(vA, vB):
    """计算两个点的欧拉距离"""
    return np.sqrt(np.sum(np.power(vA - vB, 2)))
