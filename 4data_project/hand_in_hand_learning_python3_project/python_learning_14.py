# Python与正则表达式

# import re
#
# phone = "2004-959-559 # 这是一个电话号码"
#
# # 删除注释
# num = re.sub(r'#.*$', "", phone)
# print("电话号码 : ", num)
#
# # 移除非数字的内容
# num = re.sub(r'\D', "", phone)
# print("电话号码 : ", num)


# import re
# pattern=re.compile(r'\d+')
# result1=pattern.findall("项目123品牌456")
# print(result1)

# pattern1=re.compile(r'\w\d')
# result2=pattern.findall("项目123品牌456")
# print(result2)

# import re
# project=["广州正佳广场", "广州天河城", "广州正佳", "广州太古汇"]
# list1=[]
# pattern=re.compile(r"正佳")
# for i in project:
#     result2=re.search(pattern, i)
#     if result2 is not None:
#         list1.append(i)
# print(list1)

# import pandas as pd
# foo=pd.DataFrame({'a' : [1,2,3,4], 'b' : ['广州正佳广场', '广州天河城', '广州正佳东门', '广州正佳南门']})
# print(foo)
# print(foo.b.str.contains("正佳"))
# print(foo[foo.b.str.contains("正佳")])
# print(foo[foo.b.str.contains("正佳|天河")])

# def regex_function(x):
# print(foo['b'].apply())

# import re
# a='xy123'
# b=re.findall('x...', a)
# print(b)

# import re
# secret_code = '<name>天河城</name><address>广州市天河城</address>'
# c1 = re.findall('(?:>).*?(?=<)',secret_code)
# print(c1)
# c2 = re.findall('(?:>)(.*?)(?=<)',secret_code)
# print(c2)

import pandas as pd
df = pd.DataFrame({'id':[1,2], 'location':['113.2,25.3','123.6,24.8']})
print(df)

def split_str(x):
    return x.split(",")
str1=df.location.apply(split_str)
str1=list(str1)
df1=pd.DataFrame(str1, columns=["lng","lat"])
print(df1)
# 按着索引进行拼接
df2=df.join(df1)
print(df2)

















