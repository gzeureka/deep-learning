from sklearn import datasets
from sklearn.externals import joblib
import matplotlib.pyplot as plt

print('Loading model ...')
clf = joblib.load('model.dat')

print('Loading data ...')
digits = datasets.load_digits()

originLabels = digits.target[-6:]
originImages = digits.images[-6:]

for index in range(len(originLabels)):
    label = originLabels[index]
    image = originImages[index]

    plt.subplot(2, 6, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title('Orig %i: ' % label)

print('Predicting ...')
testData = digits.data[-6:]
testLabels = clf.predict(testData)
testImages = digits.images[-6:]

for index in range(len(testLabels)):
    label = testLabels[index]
    image = testImages[index]

    plt.subplot(2, 6, index + 7)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title('Pred %i: ' % label)

plt.show()