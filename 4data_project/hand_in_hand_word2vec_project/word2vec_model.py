#-*- coding:utf-8 -*-

import os
import logging
from gensim import models
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

train_dir = "./data"

# file_path = "case.txt"
# train_dir = "./data"

class MySEntences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for filename in os.listdir(self.dirname):
            file_path = self.dirname + "/" + filename
            for line in open(file_path, encoding='utf-8'):
                words = line.split(" ")
                result_word = []
                for word in words:
                    if word and word != "\n":
                        result_word.append(word)

sentences = MySEntences(train_dir)

# 建立word2vec模型
model = models.Word2Vec(sentences, workers=20, min_count=5, size=200)
# 保存模型
model.save("./word2vec_model")


# class MySentences(object):
#     def __init__(self, dirname):
#         self.dirname = dirname
#
#     def __iter__(self):
#         # 遍历对应目录下所有文件
#         for filename in os.listdir(self.dirname):
#             file_path = self.dirname + "/" + filename
#             for line in open(file_path):
#                 # 以空格进行分割词语
#                 words = line.split(" ")
#                 result_word = []
#                 for word in words:
#                     if word and word != '\n':
#                         result_word.append(word)
#                 yield result_word

# sentences = MySentences(train_dir)
