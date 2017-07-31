class TsvDataSetReader(object):
    """Tab分隔符数据文件读取类"""
    def __init__(self):
        pass

    def loadDataSet(self, fileName, attrType=None):
        """装载数据集"""
        # 打开文件，定义编码
        dataFile = open(fileName, 'r', encoding='utf-8')
        lines = dataFile.readlines()

        # 循环推导式，解析每一行，生成行数组
        matrix = [self.parseLine(line, attrType=attrType) for line in lines]
        # 关闭文件
        dataFile.close()

        return matrix

    def parseLine(self, line, attrType=None):
        """解析行，生成列数组"""
        # 根据制表符分割数据
        # 字符串函数
        words = line.strip().split('\t')
        # 判断None要用is
        if attrType is None:
            return words

        # 循环推导式，将字符串数组转换成对应类型数组
        return [attrType(word) for word in words]
