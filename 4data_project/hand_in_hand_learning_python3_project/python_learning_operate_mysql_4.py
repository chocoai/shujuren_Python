#python3 pymysql pandas
#1 pandas 读取数据库的表
# import pandas as pd
# import pymysql
#
# db=pymysql.connect(
#     host="192.168.1.21",
#     user="root",
#     password="123456",
#     db="wlq_data"
# )
#
# df=pd.read_sql("select * from test", con=db)
# print(df)
# db.close()

import pandas as pd
import pymysql
from sqlalchemy import create_engine

engine=create_engine("mysql+pymysql://root:123456@192.168.1.21:3306/wlq_data")
df=pd.read_sql_query("select * from test", engine)
print(df)

# 从mysql数据库里面使用pandas把数据导入到pd.dataframe
# import pandas as pd
# import pymysql
# import sqlalchemy
# from sqlalchemy import create_engine
#
# # 1. 用sqlalchemy构建数据库链接engine
# connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)  #1
# engine = create_engine(connect_info)
# # sql 命令
# sql_cmd = "SELECT * FROM table"
# df = pd.read_sql(sql=sql_cmd, con=engine)
#
# # 2. 用DBAPI构建数据库链接engine
# con = pymysql.connect(host=localhost, user=username, password=password, database=dbname, charset='utf8', use_unicode=True)
# df = pd.read_sql(sql_cmd, con)

# 把pands的df数据存放到mysql的表里面
data=[["John", "AB", 30, "F", 3000], ["ABC", "AB", 40, "M", 3000]]
columns1=["first_name", "last_name", "age", "sex", "income"]
df1=pd.DataFrame(data, columns=columns1)
print(df1)
df1.to_sql(
    name="test",
    con=engine,
    if_exists="append",
    index=False
)

# 把写入的数据进行读取
df2=pd.read_sql("select * from test", con=engine)
print(df2)

# 资料：
# https://www.cnblogs.com/arkenstone/p/6271923.html


