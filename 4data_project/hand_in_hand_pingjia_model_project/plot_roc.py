# -*- coding:utf-8 -*-
__author__='wangluqing360@163.com'

import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import roc_curve
from sklearn.metrics import auc

iris = datasets.load_iris()
X = iris.data
y = iris.target
print(y)
y1 = label_binarize(y, classes=[0, 1, 2])
print(y1)
print(y1.shape)
n_classes = y1.shape[1]
print(n_classes)

# 特征扩充
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
print(n_samples)
print(n_features)
X1 = np.c_[X, random_state.randn(n_samples, 20 * n_features)]
print(X.shape)
print(X1.shape)

# 数据分割
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=.5, random_state=0)
classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True, random_state=random_state))
y_score = classifier.fit(X1_train, y1_train).decision_function(X1_test)

# 计算每一种类型对应的ROC曲线和ROC面积
fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y1_test[:,i], y_score[:,i])
    roc_auc[i] = auc(fpr[i],tpr[i])

fpr["micro"], tpr["micro"], _ = roc_curve(y1_test.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

plt.figure()
lw = 2
plt.plot(fpr[2], tpr[2], color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[2])
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()

# 资料：
# http://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#sphx-glr-auto-examples-model-selection-plot-roc-py





