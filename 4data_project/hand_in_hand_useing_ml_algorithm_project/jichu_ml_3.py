#朴素贝叶斯算法
# 20类新闻文本数据分类
# 数据读入
from sklearn.datasets import fetch_20newsgroups
news=fetch_20newsgroups(subset="all")
# print(len(news.data))

# 数据集分割
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25, random_state=33)

# 文本数据向量化
from sklearn.feature_extraction.text import CountVectorizer
vec=CountVectorizer()
X_train1=vec.fit_transform(X_train)
X_test1=vec.transform(X_test)
