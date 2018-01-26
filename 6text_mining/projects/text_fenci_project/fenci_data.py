# Python结巴分词库测试
# import jieba.posseg as pseg
# words=pseg.cut("购物中心和品牌")
# for key in words:
#     print(key.word, key.flag)

# 分词权重tf-idf
# import jieba
# import jieba.posseg as pseg
# import os
# import sys
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.feature_extraction.text import CountVectorizer
#
#
#
# if __name__ == "__main__":
# 	corpus=["我 来到 北京 清华大学",#第一类文本切词后的结果，词之间以空格隔开
# 		"他 来到 了 网易 杭研 大厦",#第二类文本的切词结果
# 		"小明 硕士 毕业 与 中国 科学院",#第三类文本的切词结果
# 		"我 爱 北京 天安门"]#第四类文本的切词结果
# 	vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
# 	transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
# 	tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
# 	word=vectorizer.get_feature_names()#获取词袋模型中的所有词语
# 	weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
# 	for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
# 		print(u"-------这里输出第",i,u"类文本的词语tf-idf权重------")
# 		for j in range(len(word)):
# 			print(word[j],weight[i][j])
import pandas as pd
# columns = ['c1','c2','c3','c4','c5','c6','c7','c8','class']
# url="http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# raw_data=pd.read_csv(url, header=None, names=columns)
raw_data=pd.read_csv("data/pima_indians_diabetes.csv")
print(raw_data.shape)
# print(raw_data.head(2))
# raw_data.to_csv('data/pima_indians_diabetes.csv', index=False)
# raw_data.to_excel('data/pima_indians_diabetes.xlsx', index=False)
# print(raw_data.columns)

# 数据分割
# 特征矩阵X和目标变量y
X=raw_data[['c1','c2','c3','c4','c5','c6','c7','c8']]
y=raw_data['class']

# 特征工程
# 特征的重要性量化
# from sklearn.ensemble import ExtraTreesClassifier
# model = ExtraTreesClassifier()
# model.fit(X,y)
# print(model.feature_importances_)

# 特征最佳自己搜寻
# from sklearn.feature_selection import RFE
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression()
# rfe=RFE(model,3)
# rfe=rfe.fit(X,y)
# print(rfe.support_)
# print(rfe.ranking_)

# 算法与模型
# 逻辑回归算法
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
model = LogisticRegression()
model.fit(X,y)
print(model)
# 逻辑回归模型预测应用
expected=y
predicted=model.predict(X)
# 模型结果评价
# 混淆矩阵
print(metrics.confusion_matrix(expected,predicted))
print(metrics.classification_report(expected, predicted))
# 结论：
# 逻辑回归算法的准确率是0.77

#朴素贝斯算法
# from sklearn.naive_bayes import GaussianNB
# from sklearn import metrics
# model=GaussianNB()
# model.fit(X,y)
# print(model)
# expected=y
# predicted=model.predict(X)
# print(metrics.confusion_matrix(expected,predicted))
# print(metrics.classification_report(expected,predicted))
# 结论：
# 朴素贝叶斯算法的准确率是0.76

#KNN算法
# from sklearn import metrics
# from sklearn.neighbors import KNeighborsClassifier
# model=KNeighborsClassifier()
# model.fit(X,y)
# print(model)
# expected=y
# predicted=model.predict(X)
# print(metrics.confusion_matrix(expected,predicted))
# print(metrics.classification_report(expected,predicted))
# 结论：
# KNN算法的准确率是0.80

#决策树算法
# from sklearn.tree import DecisionTreeClassifier
# from sklearn import metrics
# model=DecisionTreeClassifier()
# model.fit(X,y)
# print(model)
# expected=y
# predicted=model.predict(X)
# print(metrics.confusion_matrix(expected,predicted))
# print(metrics.classification_report(expected,predicted))
#结论：
#决策树算法的准确率是100%

# 支持向量机算法
from sklearn.svm import SVC
from sklearn import metrics
model=SVC()
model.fit(X,y)
expected=y
predicted=model.predict(X)
print(metrics.confusion_matrix(expected,predicted))
print(metrics.classification_report(expected,predicted))
# 结论：
# 支持向量机的准确率是100%

# 最佳参数选择
# import numpy as np
# from sklearn.linear_model import Ridge
# from sklearn.model_selection import GridSearchCV
# alphas=np.array([1,0.1,0.01,0.001,0.0001,0])
# model=Ridge()
# grid=GridSearchCV(estimator=model,param_grid=dict(alpha=alphas))
# grid.fit(X,y)
# print(grid)
# print(grid.best_params_)
# print(grid.best_score_)
# print(grid.best_estimator_.alpha)

# 或者随机地给超参数初始化
# from scipy.stats import uniform as sp_rand
# from sklearn.linear_model import Ridge
# from sklearn.model_selection import RandomizedSearchCV
# param_grid={'alpha':sp_rand()}
# model=Ridge()
# rsearch=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100)
# rsearch.fit(X,y)
# print(rsearch)
# print(rsearch.best_score_)
# print(rsearch.best_estimator_.alpha)





