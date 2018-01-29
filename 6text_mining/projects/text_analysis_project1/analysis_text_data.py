import jieba

# 构建停用词函数
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

# 句子分词处理
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('stopWords/1893（utf8）.txt')
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

# 文本数据输入
inputs = open('input/环境监测与环境影响评价（摘要utf8).txt', 'r', encoding='utf-8')
outputs = open('fenci_result.txt', 'w',encoding='utf-8')

for line in inputs:
    line_seg = seg_sentence(line)
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()

# 资料
# https://github.com/xiaoyichao/-python-
