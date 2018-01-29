# 对分词处理后的文本进行
import codecs
from gensim import corpora
from gensim.models import LdaModel

train = []

# 获取分词的结果
fp = codecs.open('fenci_result.txt', 'r', encoding='utf-8')
for line in fp:
    line = line.split()
    train.append([w for w in line])

dictionary = corpora.Dictionary(train)
corpus = [dictionary.doc2bow(text) for text in train]
lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5,passes=20)

for topic in lda.print_topics(num_words = 2):
    termNumber = topic[0]
    print(topic[0], ':', sep='')
    listOfTerms = topic[1].split('+')
    for term in listOfTerms:
        listItems = term.split('*')
        print('  ', listItems[1], '(', listItems[0], ')', sep='')

