#-*- coding:utf-8 -*-
__author__='wangluqing360@163.com'
__web__='http://shujuren.org'

import os

class FileCommand(object):
    def __init__(self, pathname):
        self.pathname=pathname

    # 创建文件
    def createFile(self, filename):
        fn=self.pathname+str(filename).strip()
        if not os.path.isfile(fn):
            open(fn, mode='w', encoding='utf-8').close()

    # 获取文件的大小
    def getFileSize(self, filename):
        k_size=round(os.stat(filename).st_size / 1024, 1)
        if k_size > 1024:
            m_size = round(k_size / 1024, 1)
            if m_size > 1024:
                return str(round(m_size / 1024, 1)) + 'G'
            else:
                return str(m_size) + 'M'
        else:
            return str(k_size) + 'K'

    # 列出目录下所有文件夹和文件
    def listPath(self):
        for root, dirs, files in os.walk(self.pathname):
            print(root)
            for dir in dirs:
                print('\t', dir)
            for file in files:
                print('\t', file, '\t', self.getFileSize(root+'\\'+file))

    def readFile(self, filename):
        fn=self.pathname+str(filename).strip()
        f=open(fn, 'r', encoding='utf-8')
        result=list()
        for line in f.readlines():
            line=line.strip()
            if not len(line) or line.startswith('#'):
                continue
            result.append(line)
        result.sort()
        print(result)
        f.close()

    # 删除文件
    def delectFile(self, filename):
        fn=self.pathname + str(filename).strip()
        if os.path.isfile(fn):
            os.remove(fn)
            if(not os.path.isfile(fn)):
                print('*Tips: File: ', fn, ' has been deleted.')
        else:
            print('*Tips: File ', fn, ' not found')

# 用户交互操作函数
def selectOperation():
    print('\n*1.罗列所有文件夹和文件')
    print('*2 创建文件')
    print('*3 删除文件')
    print('*4 读取文件')
    print('*5 退出')

    s=input('*请输入操作码：')
    return s

if __name__ == "__main__":
    pathname=input('请输入文件夹名：')
    myfile=FileCommand(pathname)
    while True:
        selectNum=selectOperation()
        if selectNum == '1':
            myfile.listPath()
        elif selectNum == '2':
            fn=input('请输入文件名：')
            myfile.createFile(fn)
        elif selectNum == '3':
            fn=input('请输入文件名：')
            myfile.delectFile(fn)
        elif selectNum == '4':
            fn=input('请输入文件名：')
            myfile.readFile(fn)
        elif selectNum == '5':
            break;

