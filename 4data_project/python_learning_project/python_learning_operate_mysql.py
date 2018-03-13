# # python3操作mysql
#
# # import pymysql
# # #打开数据库连接
# # db=pymysql.connect("localhost", "testuser", "test123", "TESTDB")
# # #使用cursor()方法创建一个游标对象
# # cursor=db.cursor()
# # #使用execute()方法执行SQL语句
# # cursor.execute("SELECT VERSION()")
# # #使用fetchone()方法获取单条数据
# # data=cursor.fetchone()
# # print("Database version:%s" %data)
# # #关闭数据库连接
# # db.close()
#
# # 创建数据库表
# # import pymysql
# # db=pymysql.connect("localhost", "testuser", "test123", "TESTDB")
# # cursor=db.cursor()
# # # 如果表存在则删除
# # cursor.execute("drop table if exists employee")
# # # 使用预处理语句创建表
# # sql="""
# # create table emplo
# # """
#
# # import pymysql
# #
# # # 查询数据库中的数据
# # # 第一步：打开数据库连接
# # db=pymysql.connect(host='192.168.1.21', user='root', password='123456', database='wlq_data', charset='utf8')
# # # 第二步：获取操作游标
# # cur=db.cursor()
# # # 第三步：查询数据
# # sql="""
# # select
# # projectid,
# # id,
# # typecode,
# # type,
# # name,
# # location
# # from gaode_poi_result
# # limit 0, 10
# # """
# # try:
# #     cur.execute(sql)
# #     results=cur.fetchall()
# #     print(results)
# #     print("projectid", "id", "typecode", "name", "location")
# #     # 遍历结果
# #     for row in results:
# #         projectid=row[0],
# #         id=row[1],
# #         typecode=row[2]
# #         name=row[3]
# #         location=row[4]
# #         print(projectid, id, typecode, name, location)
# # except Exception as e:
# #     raise  e
# # finally:
# #     cur.close()
# #     db.close()
#
#
# # 把数据插入到数据库表中
# # import pymysql
# # db=pymysql.connect(
# #     host="192.168.1.21",
# #     user="root",
# #     password="123456",
# #     database="wlq_data",
# #     charset="utf8"
# # )
# # cur=db.cursor()
# # cur.execute("select * from emp")
# # results=cur.fetchall()
# # print(results)
#
# # 插入记录
# # sql_inser1="""
# # insert into emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) values(10000, 'A', 'B', 1000, '2016-07-08', 2000, 400, 60)
# # """
# #
# # try:
# #     cur.execute(sql_inser1)
# #     db.commit()
# # except Exception as e:
# #     db.rollback()
# #
# # cur.execute("select * from emp")
# # results1 = cur.fetchall()
# # print(results1)
#
#
#
# # 更新操作
# # 更新的sql语句
# sql_update="update emp set ename='%s' where empno = %d"
# try:
#     cur.execute(sql_update %("AA", 1234))
#     # 数据提交
#     db.commit()
# except Exception as e:
#     db.rollback()
#
# cur.execute("select * from emp")
# results2 = cur.fetchall()
# print(results2)
#
# # 删除操作
# # 删除的sql语句
# sql_delete="delete from emp where empno = %d"
# try:
#     cur.execute(sql_delete %(10000))
#     # 数据提交
#     db.commit()
# except Exception as e:
#     db.rollback()
#
# cur.execute("select * from emp")
# results3 = cur.fetchall()
# print(results3)
#
#
#
# # sql_insert = """insert into user(id,username,password) values(4,'liu','1234')"""
# #
# # try:
# #     cur.execute(sql_insert)
# #     # 提交
# #     db.commit()
# # except Exception as e:
# #     # 错误回滚
# #     db.rollback()
# # finally:
# #     db.close()
#
#     # 创建表和数据的脚本
# # CREATE TABLE emp
# # (empno smallint(4) not null primary key,
# #  ename varchar(10),
# #  job varchar(9),
# #  mgr smallint(4),
# #  hiredate date,
# #  sal float(7, 2),
# #  comm float(7, 2),
# #  deptno tinyint(2)
# # ) engine=innodb charset=utf8;
# #
# # INSERT INTO emp VALUES (7369, '员工SMITH',  'CLERK',     7902, '1980-12-17',  800, NULL, 20);
# # INSERT INTO emp VALUES (7499, '员工ALLEN',  'SALESMAN',  7698, '1981-02-20', 1600,  300, 30);
# # INSERT INTO emp VALUES (7521, '员工WARD',   'SALESMAN',  7698, '1981-02-22', 1250,  500, 30);
#
# # conn2 = pymysql.connect(
# #     host='192.168.1.21',
# #     user='root',
# #     password='123456',
# #     database='wlq_data',
# #     charset='utf8'
# # )
#
# # def save_info():
# #     try:
# #         with conn2.cursor() as cursor2:
# #             for str in list1:
# #                 sql="insert into xiangmu_location_poi1 (id, name, type, typecode, address, location, pname, cityname, adname, projectid) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s')" %(str[0],str[1],str[2],str[3],str[4],str[5],str[6],str[7],str[8],str[9])
# #                 cursor2.execute(sql)
# #         conn2.commit()
# #     except:
# #         print('error2')


# python3 操作mysql
# pymysql与pandas结合
import pandas as pd
import pymysql
db=pymysql.connect(
    host="192.168.1.21",
    user="root",
    password="123456",
    db="wlq_data",
    charset="utf8"
)

cursor=db.cursor()
# print(db)
# print(cursor)
#
# cursor.execute("select version()")
# data=cursor.fetchone()
# print(data)
# cursor.close()
# db.close()


# 创建数据库表
# cursor.execute("drop table if exists test")
# sql_create="""
# create table test(
# first_name char(20) not null,
# last_name char(20),
# age int,
# sex char(1),
# income float
# )
# """
# cursor.execute(sql_create)
# cursor.close()
# db.close()

# 数据库表中插入数据
# sql_insert="""
# insert into test(first_name, last_name, age, sex, income) values('Mac', 'Month', 40, 'M', 1000)
# """
#
# try:
#     cursor.execute(sql_insert)
#     db.commit()
# except:
#     db.rollback()
# cursor.close()
# db.close()

# 数据库表中查询操作
sql_query="""
select * from test
"""
try:
    cursor.execute(sql_query)
    results=cursor.fetchall()
    print(results)
    df=pd.DataFrame(list(results), columns=['fname', 'lname', 'age', 'sex', 'income'])
    print(df)
    for row in results:
        fname=row[0]
        lname=row[1]
        age=row[2]
        sex=row[3]
        income=row[4]
        print("fname=%s, lname=%s, age=%d, sex=%s, income=%d" %(fname, lname, age, sex, income))
except:
    print("不能获取数据")

cursor.close()
db.close()

# 数据库更新操作
# sql_update="""
# update test set age=age+1 where sex="M"
# """
# try:
#     cursor.execute(sql_update)
#     db.commit()
# except:
#     db.rollback()
# cursor.close()
# db.close()

# 数据库删除操作
# sql_delete="""
# delete from test where age > 30
# """
# try:
#     cursor.execute(sql_delete)
#     db.commit()
# except:
#     db.rollback()
# cursor.close()
# db.close()



