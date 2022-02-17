'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/2/16 17:38 
'''


from DAO import mysqlHelper


def add_blog_dao(title, author, content):
    """
    新增blog
    :param title:
    :param content:
    :param author:
    :return:
    """
    sql = f"insert into blog (title, author, content) values('{title}', '{author}', '{content}');"
    print(sql)
    return mysqlHelper.do_execute(sql)