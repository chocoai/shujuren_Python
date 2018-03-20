# -*- coding:utf-8 -*-
__author__='wangluqing360@163.com'

# 1 删除低方差的变量
# from sklearn.feature_selection import VarianceThreshold
# X=[[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
# print(X)
# sel=VarianceThreshold(threshold=(.8*(1-.8)))
# X1=sel.fit_transform(X)
# print(X1)

# 2 单变量特征选择 filter方法
# 验证单变量与目标变量的独立关系
# from sklearn.datasets import load_iris
# from sklearn.feature_selection import SelectKBest
# from sklearn.feature_selection import chi2
# iris = load_iris()
# X, y = iris.data, iris.target
# print(X.shape)
# print(y.shape)
# print(X[:2,])
# X_new = SelectKBest(chi2, k=2).fit_transform(X,y)
# print(X_new.shape)
# print(X_new[:2,])

# 3 递归特征消除 wrapper方法
# from sklearn.datasets import load_digits
# from sklearn.feature_selection import RFE
# from sklearn.svm import SVC
# import matplotlib.pyplot as plt
#
# digits = load_digits()
# X = digits.images.reshape((len(digits.images), -1))
# y = digits.target
#
# svc = SVC(kernel="linear", C=1)
# rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
# rfe.fit(X, y)
# ranking = rfe.ranking_.reshape(digits.images[0].shape)
#
# plt.matshow(ranking, cmap=plt.cm.Blues)
# plt.colorbar()
# plt.title("Ranking of pixels with RFE")
# plt.show()

# 4 L1-based feature selection Embedded方法
# from sklearn.datasets import load_iris
# from sklearn.svm import LinearSVC
# from sklearn.feature_selection import SelectFromModel
#
# iris = load_iris()
# X, y = iris.data, iris.target
# print(X.shape)
# print(X[:1,])
# lsvc = LinearSVC(C=0.01, penalty='l1', dual=False).fit(X,y)
# model = SelectFromModel(lsvc, prefit=True)
# X_new = model.transform(X)
# print(X_new.shape)
# print(X_new[:1,])

# 5 Tree-based feature selection  Embedded方法
from sklearn.datasets import load_iris
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
iris = load_iris()
X, y = iris.data, iris.target
print(X.shape)
print(X[:1,])
clf = ExtraTreesClassifier()
clf = clf.fit(X,y)
print(clf.feature_importances_)
model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)
print(X_new.shape)
print(X_new[:1,])


