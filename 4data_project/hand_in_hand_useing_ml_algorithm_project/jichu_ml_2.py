#手写数字识别问题
# 数据读入
from sklearn.datasets import load_digits
digits=load_digits()
print(digits.data.shape)

# 数据集分割
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)

# 数据规模查看
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

# 数据标准化处理
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
X_train1=ss.fit_transform(X_train)
X_test1=ss.transform(X_test)

# 线性支持向量机模型
from sklearn.svm import LinearSVC
lsvc=LinearSVC()
lsvc.fit(X_train1, y_train)
y_predict=lsvc.predict(X_test1)

# 模型性能评价
print("LSVC的准确度：", lsvc.score(X_test1, y_test))
from sklearn.metrics import classification_report
print(classification_report(y_test, y_predict, target_names=digits.target_names.astype(str)))












# 文档：
# http://scikit-learn.org/stable/modules/classes.html