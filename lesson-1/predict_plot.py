from sklearn import datasets
from sklearn.externals import joblib
import matplotlib.pyplot as plt

print('Loading model ...')
clf = joblib.load('model.dat')

print('Loading data ...')
digits = datasets.load_digits()

originLabels = digits.target[-4:]
originImages = digits.images[-4:]

for index in range(len(originLabels)):
    label = originLabels[index]
    image = originImages[index]

    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title('Original %i: ' % label)

print('Predicting ...')
testData = digits.data[-4:]
testLabels = clf.predict(testData)
testImages = digits.images[-4:]

for index in range(len(testLabels)):
    label = testLabels[index]
    image = testImages[index]

    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title('Prediction %i: ' % label)

plt.show()