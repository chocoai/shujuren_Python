import os
import jieba
import jieba.posseg as pseg
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
# 设置文本数据存放路径
path = './article/'
# 文本数据标题列表和文本分词列表
titlelist, wordslist = [], []
for fileName in os.listdir(path) :
    titlelist.append(''.join(fileName[:-4].split()))
    with open(path + fileName) as f :
        text = f.read()
        text = ''.join(text.split())
        seg_list = jieba.cut(text)
        wordslist.append(' '.join(seg_list))
vec = CountVectorizer()
wordFrequence = vec.fit_transform(wordslist)
words = vec.get_feature_names()
trans = TfidfTransformer()
tfidf = trans.fit_transform(wordFrequence)
wordsWeight = tfidf.toarray()
n = int(input('输入关键字的个数 : '))
while(n > 5 or n < 0) :
    n = int(input('输入数字应大于零并且小于等于5 : '))
for (title, weight) in zip(titlelist, wordsWeight) :
    print (title, ' : ')
    loc = np.argsort(-weight)
    for i in range(n) :
        print('\t#' + str(i + 1) + ':', words[loc[i]])
    print()
input('any key to continue...')