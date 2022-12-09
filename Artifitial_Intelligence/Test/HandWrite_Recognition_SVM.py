import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn
import mnist_loader

print('Python: {}'.format(sys.version))
print('scipy: {}'.format(scipy.__version__))
print('numpy: {}'.format(numpy.__version__))
print('matplotlib: {}'.format(matplotlib.__version__))
print('pandas: {}'.format(pandas.__version__))
print('sklearn: {}'.format(sklearn.__version__))

from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

validation_size = 0.20
seed = 7
number_of_data = 2000
# Load Dataset
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
training_data = list(training_data)
for i in range(number_of_data):
    temp = numpy.reshape((training_data[i][0]), (1, 784))
    if i is 0:
        X = temp
    else:
        X = numpy.concatenate([X, temp], 0)
Y = []
for i in range(number_of_data):
    for j in range(10):
        if training_data[i][1][j][0] == 1.0:
            Y.append(j)
Y = numpy.array(Y)

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size = validation_size, random_state = seed)

seed = 7
scoring = 'accuracy'

results = []
names = []

name = 'SVM'
model = SVC()

kfold = model_selection.KFold(n_splits=3, shuffle=True, random_state = seed)
cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
results.append(cv_results)
names.append(name)
msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
print(msg)

model.fit(X_train, Y_train)
predictions = model.predict(X_validation)
print(name)
print(accuracy_score(Y_validation, predictions))
print(classification_report(Y_validation, predictions))