# -*- coding: utf-8 -*-
import os
import jieba.analyse as jiebays
def getTag(fileLocation, k) :
    with open(fileLocation) as f :
        txt = f.read()
        # 重点 ----- 在 ----- 这里
        tags = jiebays.extract_tags(txt, topK = k)
        return (" ".join(tags)).split()

if __name__ == '__main__' :
    n = int(input('输入关键字的个数 : '))
    while(n > 5 or n < 0) :
        n = int(input('输入数字应大于零并且小于等于5 : '))
    path = './article/'
    for fileName in os.listdir(path) :
        tagList = getTag(path + fileName, n)
        print (fileName + ' : ')
        for i in range(n) :
            print ('\t#' + str(i + 1) + ':', tagList[i])
        print()
    input('any key to continue...')

# 资料
#https://www.zybuluo.com/ArrowLLL/note/713763
