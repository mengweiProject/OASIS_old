'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/3/8 14:12

文章的增删改查
'''


from DAO import mysqlHelper
from Tools import constants as cs


def register(userName, pwd, age, pse, toBeAuthor):
    """

    :param userName:
    :param pwd:
    :param age:
    :param pse:
    :param toBeAuthor:
    :return:
    """
    try:
        query = """SELECT u.* FROM user_info u WHERE u.u_name = '{userName}';""".format(userName=userName)
        result = mysqlHelper.query_to_df(query)
        if result.empty or len(result) == 0:
            print("开始注册流程")
            #TODO
            #考虑用装饰器实现验证
        else:
            return cs.EXISTENCE
        return cs.SUCESS
    except Exception as e:
        print(e)
        return cs.FAILURE


if __name__ == '__main__':
    pass