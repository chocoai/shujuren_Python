import pandas as pd

# df1=pd.read_csv("data_output/28081_1.txt", sep="\t")
# print(df1)

# import os
# os.remove("data_output/28081_1.txt")
#
# import shutil

import os
files=os.listdir("data_output_location/")
print(files)
for i in files:
    print(i)
    os.remove("data_output_location/"+i)
    os.remove(i)


# 资料：
# http://www.cnblogs.com/feeland/p/4463682.html

