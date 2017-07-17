from sklearn import datasets
from sklearn import svm

print('Loading data ...')
digits = datasets.load_digits()

print('Create SVM classfier')
clf = svm.SVC(gamma=0.001, C=100)

print('Train data')
trainData = digits.data[:-1]
trainLabels = digits.target[:-1]

clf.fit(trainData, trainLabels)
print('Finish training')

testData = digits.data[-1:]
testLabels = clf.predict(testData)

print('Result: ', testLabels)
