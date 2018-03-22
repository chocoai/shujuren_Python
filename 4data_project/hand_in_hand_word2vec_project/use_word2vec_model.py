#-*- coding:utf-8 -*-
from gensim import models
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = models.Word2Vec.load("./word2vec_model")
print("\n女人 + 丈夫 - 男人:")
result = model.most_similar(positive=['女人', '丈夫'], negative=['男人'], topn=1)
print(result[0][0], result[0][1])

print("\n抢夺和抢劫相近程度:")
print(model.similarity("抢夺", "抢劫"))

print("\n抢劫的近义词")
reuslt = model.most_similar(['抢劫'])
for value in result:
    print(value[0], value[1])

print("\n找出投资、抢劫、强奸、盗窃中,哪个词不是一组的:")
result = model.doesnt_match(['投资', '抢劫', '强奸', '盗窃'])
print(result)

