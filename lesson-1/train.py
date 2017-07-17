from sklearn import datasets
from sklearn import svm
from sklearn.externals import joblib

print('Loading data ...')
digits = datasets.load_digits()

print('Create SVM classfier')
clf = svm.SVC(gamma=0.001, C=100)

print('Training ...')
trainData = digits.data[:-6]
trainLabels = digits.target[:-6]

clf.fit(trainData, trainLabels)
print('Finish training')

print('Saving model ...')
joblib.dump(clf, 'model.dat')