# encoding:utf8
import pymysql


# 定义一个连接函数
# def exeConn(host, user, passwd, db):
#     global conn, cur
#     conn=pymysql.connect(
#         host=host,
#         user=user,
#         password=passwd,
#         database=db,
#         charset='utf8'
#     )
#     cur=conn.cursor()
#     return conn, cur

# def exeQuery(sql):
#     conn = pymysql.connect(
#         host="192.168.1.21",
#         user="root",
#         password="123456",
#         database="wlq_data",
#         charset='utf8'
#     )
#     cur = conn.cursor()
#     cur.execute(sql)
#     queryResults=cur.fetchall()
#     print(queryResults)
#     for row in queryResults:
#         print("row_number:", (cur.rownumber))
#         print("empno"+str(row[0])+ " ename:" + str(row[1]))
#     cur.close()
#     conn.close()
#
#
# if "__name__" == "__main__":
#     # exeConn("192.168.1.21", "root", "123456", "wlq_data")
#     exeQuery("select * from emp")









# ##查询
# def select():
#     conn = pymysql.connect(user='root', passwd='你的密码',
#                            host='localhost', db='test', charset='utf8')
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM user")
#     for r in cur:
#         print("row_number:", (cur.rownumber))
#         print("id:" + str(r[0]) + " name:" + str(r[1]) + " password:" + str(r[2]))
#     cur.close()
#     conn.close()
#
#
# ##插入
# def insert(name, pwd):
#     conn = pymysql.connect(user='root', passwd='你的密码',
#                            host='localhost', db='test', charset='utf8')
#     cur = conn.cursor()
#     sql = "INSERT INTO user (Name,Password) VALUES ('" + name + "','" + pwd + "')"
#     print(sql)
#     sta = cur.execute(sql)
#     if sta == 1:
#         print('Done')
#     else:
#         print('Failed')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# ##更新
# def update(name, pwd):
#     conn = pymysql.connect(user='root', passwd='你的密码',
#                            host='localhost', db='test', charset='utf8')
#     cur = conn.cursor()
#     sql = "UPDATE USER SET PASSWORD='" + pwd + "' WHERE NAME='" + name + "'""'"
#     print(sql)
#     sta = cur.execute(sql)
#     if sta == 1:
#         print('Done')
#     else:
#         print('Failed')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# ##删除
# def delete(name):
#     conn = pymysql.connect(user='root', passwd='你的密码',
#                            host='localhost', db='test', charset='utf8')
#     cur = conn.cursor()
#     sql = "DELETE FROM USER WHERE Name='" + name + "'"
#     print(sql)
#     sta = cur.execute(sql)
#     if sta == 1:
#         print('Done')
#     else:
#         print('Failed')
#     conn.commit()
#     cur.close()
#     conn.close()
#
# ##调用函数进行操作即可