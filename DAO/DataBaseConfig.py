'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/3/8 8:36 
'''


import pandas as pd
import pymysql
import constants


class ForDBs:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='666666',
            db='data_analysis',
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


tt = ForDBs()


def do_query(sql):
    try:
        return tt.cur.fetchall()
    except:
        return None


def do_execute(sql):
    try:
        tt.cur.execute(sql)
        tt.conn.commit()
        return constants.SUCESS
    except Exception as e:
        return constants.FAILURE


def query_to_df(sql):
    try:
        # ret = do_query(sql)
        df = pd.read_sql(sql, tt.conn)
        df.columns = [str(i).upper() for i in df.columns]
        # print(df.columns)
        return df
    except:
        return None


if __name__ == '__main__':
    sql = "select * from basic_info limit 100;"
    print(query_to_df(sql))