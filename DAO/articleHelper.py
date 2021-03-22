'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/3/8 14:12

文章的增删改查
'''


from DAO import mysqlHelper


def articleAdd(title="无标题", author="佚名", language="NULL"):
    sql = "INSERT INTO article_list(title, author, language) VALUES('{}', '{}', '{}');".format(title, author, language)
    return mysqlHelper.do_execute(sql)



if __name__ == '__main__':
    print(articleAdd("python3基础教程", "奥斯特洛夫斯基", ""))