'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/3/8 14:16 
'''


from DAO.DataBaseConfig import ForDBs
import pandas as pd
from Tools import constants


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
        df = pd.read_sql(sql, tt.conn)
        # df.columns = [str(i).upper() for i in df.columns]
        # print(df.columns)
        return df
    except:
        return None


if __name__ == '__main__':
    # sql = "select U_ID,U_NAME,C_TIME from basic_info limit 100;"
    sql = "select * from user;"
    print(query_to_df(sql))