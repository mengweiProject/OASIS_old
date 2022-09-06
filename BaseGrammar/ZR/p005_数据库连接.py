

import pymysql

#建立连接
conn = pymysql.connect(
            host='114.116.25.129',
            port=49164,
            user='root',
            password='123456',
            database='oasisDB',
            charset='utf8'
        )

#获取游标
cur = conn.cursor()

# sql = '''
# SELECT * FROM emp e
# INNER JOIN
# (SELECT emp.dept_id, MAX(emp.salary) salary FROM emp GROUP BY emp.dept_id) temp
# ON e.dept_id = temp.dept_id AND e.salary = temp.salary;
# '''
# sql = '''
# SELECT * FROM emp WHERE age > 40 AND salary > 6000;
# '''
# sql = '''
# SELECT * FROM kungfu_table;
# '''
#编写sql语句
sql = '''
SELECT k.k_rating, GROUP_CONCAT(k.k_name) FROM kungfu_table k GROUP BY k.k_rating;
'''
#执行sql语句
cur.execute(sql)
#获取执行结果
result = cur.fetchall()
print(result)     # (('A', '打狗棒法,鹰爪功,幻阴指,大力金刚指'), ('B', '铁头功,七伤拳'), ('S', '乾坤大挪移,龙爪手,玄冥神掌,降龙十八掌'), ('S+', '九阳神功,九阴真经,太极,易筋经'))
#关闭游标
cur.close()
#关闭连接
conn.close()

# d1 = {t[1]: [t[0]] + list(t[2:4]) for t in result}  #  {'杨逍': [2, 42, 9500], '金毛狮王': [3, 53, 8000], '张三丰': [4, 101, 20000], '灭绝': [7, 60, 8800], '史火龙': [10, 45, 6700], '史水龙': [16, 45, 6700]}

# for t in result:
#     print(t)
#     d[t[1]] = [t[0]] + list(t[2:4])
# print(d1)

# d2 = {t[1]: t[2] for t in result}
# print(d2)

# d3 = {t[2]: [] for t in result}
# print(d3)
# for i in result:
#     d3[i[2]].append(i[1])
# print(d3)

# print({t[0]: t[1] for t in result})
# print({t[0]: t[1].split(',') for t in result})