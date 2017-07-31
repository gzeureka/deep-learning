from common.io.tsv import TsvDataSetReader
from algorithm.apriori import apriori

dataReader = TsvDataSetReader()
transactions = dataReader.loadDataSet('aprioriData.txt')

itemSetsList, supports = apriori(transactions, supportThreshold=0.5)

print(transactions)
print(itemSetsList)
print(supports)

