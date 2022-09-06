# -*- encoding:utf-8 -*-

import re

with open('sdf.txt', 'r', encoding='utf-8') as f:
    content_l = f.readlines()
    content_s = ''.join(content_l)
    # print(content_s)
pattern = r'''target="_blank" href="(.*?)">(.*?)</a></li>'''
url_title_list = re.findall(pattern, content_s)
# print(url_title_list)

# https://news.zhibo8.cc/nba/2022-07-18/62d549901e046.htm

# for url_title in url_title_list:
#     # print(url_title)
#     # print('https:' + url_title[0], url_title[1])
#     print({'https:' + url_title[0]: url_title[1]})

print([{'https:' + url_title[0]: url_title[1]} for url_title in url_title_list])