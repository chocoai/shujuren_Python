import os
import pandas as pd

dirlist=[]
dflist=[]


# for dirpath, dirname, filename in os.walk("data_output"):
#     for i in filename:
#         dirlist.append(os.path.join(dirpath, i))
#
# print(dirlist)
# for index in dirlist:
#     dflist.append(pd.read_csv(i, ))

def concat_data(path, name):
    for dirpath, dirname, filename in os.walk(path):
        for i in filename:
            dirlist.append(os.path.join(dirpath, i))
    for file in dirlist:
        dflist.append(pd.read_csv(file, sep="\t"))
    #数据集合并
    mydf=pd.concat(dflist)
    #去掉重复的行
    mydf1=mydf.drop_duplicates()
    mydf1.to_excel('data_output_location/'+str(name)+".xlsx", index=None)
    return

# concat_data("data_output", "监测的30个城市door信息")

def main():
    # concat_data("data_output/", "监测的30个城市door信息")
    concat_data("data_output_location/", "监测的30个城市door信息")

if __name__=='__main__':
    main()