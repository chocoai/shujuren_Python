# -*- coding:utf-8 -*-
__author__='wangluqing360@163.com'
__web__='http://shujuren.org'

# 导入Python库
import pymysql
import logging

class MySQLCommand(object):
    def __init__(self, host, port, user, password, db, table):
        self.host=host
        self.port=port
        self.user=user
        self.passowrd=password
        self.db=db
        self.table=table

    def connectMySQL(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.passowrd,
                db=self.db,
                charset='utf8'

            )
            self.cursor=self.conn.cursor()
        except:
            print('connect mysql error.')

    def queryMySQL(self):
        sql="select * from" + self.table
        try:
            self.cursor.execute(sql)
            row=self.cursor.fetchone()
            print(row)
        except:
            print(sql + ' execute failed')

    def insertMySQL(self, id, name, sex):
        sql="insert into" + self.table + "values(" + id + "," + name + "," + sex + ")"
        try:
            self.cursor.execute(sql)
        except:
            print("insert failed")

    def updateMySQL(self, name, sex):
        sql="update" + self.table + "set sex=" + sex + "where name=" + name
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def closeMySQL(self):
        self.cursor.close()
        self.conn.close()















# #资料：
# # http://blog.csdn.net/qq_37176126/article/details/72824106
# # encoding:utf8
# import pymysql
#
#
# ##查询
# def select():
#     conn = pymysql.connect(user='root', passwd='123456',
#                            host='192.168.1.21', database='wlq_data', charset='utf8')
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM emp")
#     for r in cur:
#         print("row_number:", (cur.rownumber))
#         print("empno:" + str(r[0]) + " ename:" + str(r[1]) )
#     cur.close()
#     conn.close()
#
# select()
#
#
# # ##插入
# # def insert(name, pwd):
# #     conn = pymysql.connect(user='root', passwd='你的密码',
# #                            host='localhost', db='test', charset='utf8')
# #     cur = conn.cursor()
# #     sql = "INSERT INTO user (Name,Password) VALUES ('" + name + "','" + pwd + "')"
# #     print(sql)
# #     sta = cur.execute(sql)
# #     if sta == 1:
# #         print('Done')
# #     else:
# #         print('Failed')
# #     conn.commit()
# #     cur.close()
# #     conn.close()
# #
# #
# # ##更新
# # def update(name, pwd):
# #     conn = pymysql.connect(user='root', passwd='你的密码',
# #                            host='localhost', db='test', charset='utf8')
# #     cur = conn.cursor()
# #     sql = "UPDATE USER SET PASSWORD='" + pwd + "' WHERE NAME='" + name + "'""'"
# #     print(sql)
# #     sta = cur.execute(sql)
# #     if sta == 1:
# #         print('Done')
# #     else:
# #         print('Failed')
# #     conn.commit()
# #     cur.close()
# #     conn.close()
# #
# #
# # ##删除
# # def delete(name):
# #     conn = pymysql.connect(user='root', passwd='你的密码',
# #                            host='localhost', db='test', charset='utf8')
# #     cur = conn.cursor()
# #     sql = "DELETE FROM USER WHERE Name='" + name + "'"
# #     print(sql)
# #     sta = cur.execute(sql)
# #     if sta == 1:
# #         print('Done')
# #     else:
# #         print('Failed')
# #     conn.commit()
# #     cur.close()
# #     conn.close()
# #
# #     ##调用函数进行操作即可