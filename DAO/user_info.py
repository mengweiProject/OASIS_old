'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/2/15 9:57 
'''

from DAO import mysqlHelper
# from constants import EXISTENCE, NOTEXISTENCE
from Tools import constants


def insert_into_user_info(username, pwd):
    sql = f"INSERT INTO user_info(user_name, pwd) values('{username}', '{pwd}');"
    print(sql)
    return mysqlHelper.do_execute(sql)


def check_user_name(username):
    sql = f"select * from user_info where user_name = '{username}';"
    print(sql)
    df = mysqlHelper.query_to_df(sql)
    print(df)
    if not df.empty and len(df) > 0:
        return constants.EXISTENCE
    return constants.NOTEXISTENCE


def look_for_user_df(username):
    sql = f"select * from user_info where user_name = '{username}';"
    print(sql)
    df = mysqlHelper.query_to_df(sql)
    if not df.empty and len(df) > 0:
        return df
    return None


def login_in(username, pwd):
    sql = f"select * from user_info where user_name = '{username}' and pwd = '{pwd}';"
    print(f'查询sql：{sql}')
    df = mysqlHelper.query_to_df(sql)
    if df is None or df.empty:
        return None
    return df.to_records()


if __name__ == '__main__':
    import sys
    print(sys.path)
    print(len(sys.path))
    sys.path.append('..')
    print(sys.path)
    print(len(sys.path))