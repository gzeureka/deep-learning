class TsvDataSetReader(object):
    """Tab分隔符数据文件读取类"""
    def __init__(self):
        pass

    def loadDataSet(self, fileName, **kwargs):
        """装载数据集"""
        attrType = kwargs.get('attrType', None)
        dataFile = open(fileName, 'r', encoding='utf-8')
        lines = dataFile.readlines()

        # 解析每一行，生成行数组
        matrix = [self.parseLine(line, attrType=attrType) for line in lines]

        return matrix

    def parseLine(self, line, **kwargs):
        """解析行，生成列数组"""
        attrType = kwargs.get('attrType', None)
        # 根据制表符分割数据
        words = line.strip().split('\t')
        if attrType is None:
            return words

        # 将字符串数组转换成对应类型数组
        return [attrType(word) for word in words]
