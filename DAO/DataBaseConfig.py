'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/3/8 8:36 
'''


import pandas as pd
import pymysql
# import constants
from Tools import constants

class ForDBs:
    def __init__(self):
        self.conn = pymysql.connect(
            host='114.116.25.129',
            port=49164,
            user='root',
            password='123456',
            database='oasisDB',
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    def sql(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as E:
            try:
                # TODO 添加日志
                with open('wrongToDBs.txt', 'a') as f:
                    f.write("""{}, {}""".format(E,sql) + '\n')
            except:
                print(E, sql)
            self.conn.rollback()


