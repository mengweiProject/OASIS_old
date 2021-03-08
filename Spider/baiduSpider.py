'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/3/8 12:11

百度搜索页爬虫代码示例
'''


import requests
import re


def spider(url):
    """
    获取百度搜索结果页面，解析出url地址
    :param url:
    :return:
    """
    regUrl = r"data-click=[\s\S]*?href\s+=(.*?)\s+target[\s\S]*?em>(.*?)<\/h3"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    # 模拟请求
    res = requests.get(url=url, headers=headers)
    res.encoding = "utf-8"
    # print(res.text)
    html = res.text
    urlList = re.findall(regUrl, html)
    # print(len(urlList))
    for i in range(len(urlList)):
        print("url: ", urlList[i][0])
        print("title: ", re.sub(r"<.*?>", "", urlList[i][1]), end="\n\n")


if __name__ == '__main__':
    # url = "https://www.baidu.com"
    # 输入想要搜索的内容
    # searchInfo = "美女图片"
    searchInfo = "python requests示例"
    url = "https://www.baidu.com/s?ie=utf-8&wd={}".format(searchInfo)
    spider(url)