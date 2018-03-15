# 数据去重操作
from pandas import DataFrame

data=DataFrame({'k':[1,1,2,2]})
print(data)

# 判断是否有重复的行
IsDuplicated=data.duplicated()
print(IsDuplicated)
print(type(IsDuplicated))

# 删除重复的行
data1=data.drop_duplicates()
print(data1)


