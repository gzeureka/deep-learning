from sklearn import datasets
from sklearn.externals import joblib

print('Loading model ...')
clf = joblib.load('model.dat')

print('Loading data ...')
digits = datasets.load_digits()

print('Predicting ...')
testData = digits.data[-1:]
testLabels = clf.predict(testData)

print('Result: ', testLabels)