'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2023/3/20 11:12 
'''

import requests
import re
from time import sleep

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

for i in range(1009, 1055):
    res = requests.get(f'https://www.qiuxiangys.com/vodplay/32622-9-{i}.html', headers=headers)


    url_pattern = r'"url":"https:\\/\\/vip\.lz-cdn(\d+)\.com\\/(\d+)\\/(.*?)\\/index\.m3u8"'
    url_part_list = re.findall(url_pattern, res.text)
    cdn, date_str, url_part = '', '', ''
    if len(url_part_list) > 0:
        cdn, date_str, url_part = url_part_list[0]
    # print(f'https://vip.lz-cdn8.com/20220403/{url_part}/1200k/hls/index.m3u8')
    title_pattern = r'海贼王第(\d+)集'
    title_list = re.findall(title_pattern, res.text)
    title = ''
    if len(title_list) > 0:
        title = title_list[0]
    print(f'海贼王{str(title).zfill(5)}', ': ', f'https://vip.lz-cdn{cdn}.com/{date_str}/{url_part}/1200k/hls/index.m3u8')
    # print(res.text)
    sleep(1)
