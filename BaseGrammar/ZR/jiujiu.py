
# #
# print(123, end='==')
# print(456)
#
# # 旧的字符串格式化
# print("小明今年{}岁了".format(18))
#
# print('{}今年{}岁了...'.format('小宝子', 29))
#
# print('{name}今年{age}岁...'.format(age=30, name='大包子'))
#
# # 新的字符串格式化
# n1 = 1
# n2 = 9
# print(f'{n1} * {n2} = {n1 * n2}')
#
# name = '大宝子'
# age = 32
# print(f'{name}今年{age}岁...')


# for i in range(1, 6):
#    print(i)

# for i in range(10):
# #     print(i)
# # for i in range(0, 10, 2):
# #     print(i)
#
# for i in range(1, 6, 2):
#     print('* ' * i)
#
# for i in range(5, 0, -2):
#     print('* ' * i)
#
# n = 5
# for i in range(1, 6, 2):
#     print(' ' * (5 - i) + i * '*')
#
# n = 5
# for i in range(1, 6, 2):
#     print(' ' * (5 - i) + i * ' *')
#
# n = 5
# for i in range(5, 0, -2):
#     print(' ' * (5 - i) + i * '*')
#
# n = 5
# for i in range(5, 0, -2):
#     print(' ' * (5 - i) + i * ' *')




# for i in range(1, 10):
#     for j in range(1, i+1):
#         # print(f'{j} * {i} = {i * j}', end=' ')
#         print(f'{i * j} / {j} = {i}', end=' ')
#     print()

#九九除法表
# for i in range(9, 0, -1):
#     for j in range(i, 0, -1):
#         # print(f'{j} * {i} = {i * j}', end=' ')
#         print(f'{i * j} / {j} = {i}', end=' ')
#     print()

# 字符串反转 切片  注意与range的区别
# s = 'hello world'
# print(s[1: 5: 1])
# print(s[-1: -6: -1])
# s = 'python'
# # print(s[-1: -7: -1])
# print(s[: : -1])

# 列表反转
# l = [1, 2, 3]
# print(l[: : -1])

# 字典生成式,一般不用
# d = {'name': '小红', 'age': 16, 'height': 198}
# print(d)
# k_list = ['name', 'age', 'height']
# v_list = ['小红', 16, 198]
# print({k_list[i]: v_list[i] for i in range(len(k_list))})

# 字典的遍历
# d = {'name': '小红', 'age': 16, 'height': 198}
# d.clear()   #清空字典
# # print(help(d))
# # print(d['ad'])
#
# print(d.get('name'))       #字典里没有所需键，不报错且可以有个默认值
# print(d.get('ad', '北京市朝阳区138号'))
# print(len(d))

# print(d.items())    #键值对整体返回，用于遍历键值对
# for k, v in d.items():
#     print(f'{k}: {v}')
#
# print(d.keys())  #返回键组成的列表
# # print(type(d.keys()))
#
# print(d.values()) #返回值组成的列表
# # print(d.pop('name')) #根据k移除元素，并返回移除元素对应的值
# d.pop('name')
# print(d)
#
# d1 = {'name': '小明'}  #字典的合并
# d2 = {'age': 31}
# d1.update(d2)
# print(d1)
# print(d2)
# print(d.update())

# l1 = [1, 2, 3]
# print(id(l1))
#
# # l2 = [1, 2, 3]
# # print(id(l2))
#
# l3 = l1
# del l1
# print(id(l3))
#


# d1 = {'classone': 81}
# d2 = {'classtwo': 93}
# d1.update(d2)
# # print(d1)
#


# def g_s(s=None):
#     if s >= 90:
#         print('优秀')
#     elif s >= 80:
#         print('良好')
#     elif s >= 60:
#         print('及格')
#     else:
#         print('你怎么的睡的着的！')
#
#
# if __name__ == '__main__':
#     s = 30
#     g_s(s)


#第一种方法
# def list_merge(l1, l2=[]):
#     l3 = l1 + l2
#     return l3
#
# if __name__ == '__main__':
#     l1 = [1, 2, 3]
#     l2 = ['a', 'b', 'c']
#     print(list_merge(l1, l2))
#
# #第二种方法
# def ll_merge(l1, l2):
#     l1.extend(l2)
#     return l1
#
# if __name__ == '__main__':
#     l1 = [1, 2, 3]
#     l2 = ['a', 'b', 'c']
#     print(ll_merge(l1, l2))
#     print(l1)

# def test(a, b):
#     a += b
#     return a
#
# if __name__ == '__main__':
#     a, b = 11, 22
#     print(test(a, b))
#     print(a)
#
# def test2(d):
#     d['name'] = '小红'
#
# if __name__ == '__main__':
#     d = {'name': '小明', 'age': 31}
#     test2(d)
#     print(d)

#
# l = [1, 2, 3, 'a', 'b', 'c']
# l[3] = 'aaa'
# print(l)
# # #排序
# l2 = [1, 3, 5, 7, 8, 6, 4]
# print(sorted(l2, reverse=True))
# print(sorted(l2, reverse=False))
# print(l2)


# d = {'name': '小明', 'age': 31}
# print(len(d))


# s = {1, 2, 3, 3}
# # s[0] = 2
# print(s)




# 列表的赋值，浅拷贝，深拷贝
# 1. 列表的赋值
# l1 = [1, 2, 3]
#
# l2 = l1
#
# l1[0] = 111
# print(l1)
# print(l2)

# # 2.1 列表的浅拷贝（浅复制）
# l3 = [1, 2, 3]
#
# l4 = l3.copy()
#
# l3[1] = 222
# print(l3)
# print(l4)
#
# # 2.2 列表的浅拷贝：浅拷贝，拷贝的是最外层!!!
# l5 = [1, 2, 3, [4, 5]]
#
# l6 = l5.copy()
#
# l5[3][0] = 444
# print(l5)
# print(l6)


# 3. 深拷贝：拷贝的是每一层，从最内层到最外层
# l7 = [1, 2, 3, [4, 5]]
#
# import copy
#
# l8 = copy.deepcopy(l7)
# l7[0] = '你好'
# l7[3][0] = 444
#
# print(l7)
# print(l8)
#
#join只用于字符串拼接
# l1 = ['a', 'b', 'c']
# print('-'.join(l1))
#
# l1 = [1, 'a', 'b', 'c']
# print('-'.join([str(i) for i in l1]))

#
# s = 'today is tuesday, today is very hot!'
# print(s.split(' '))
# s = 'gct78b-v8-cty8ct78b-v8-ticct78b-v8-98igvhuct78b-v8-f8ygct78b-v8-78b-v8-g7t9fyvct78b-v8-t769ivct78b-vvg7yf8ivct78b-v8-08-'
# print(s.split('-'))
#

#位置参数要在默认值参数之前
def emo(a, b, c, d=4, e=5):
    pass

#接受多个位置参数，形成一个元组
# def asdf(*args):
#     print(args)
#     print(type(args))
#     for arg in args:
#         print(arg)

#通过key value形式传参，形成一个字典
# def qwer(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# if __name__ == '__main__':
    # # a = 123
    # emo(1, 2, 3, e=6, d=7)
    # asdf(1, 2, 3, 4)
    # qwer(a=3, b=2, c=3)

# try:
#     # n = 1
#     # s = '2'
#     # m = s + n
#     # print(m)
#     l = [1, 2, 3]
#     print(l[4])
# except Exception as e:
#     print(e)
#     print('代码出错请检查逻辑')
# print(123)
#
# try:
#     n = 1
#     s = '2'
#     m = s + n
#     print(m)
# except:
#     print('代码出错请检查逻辑')
# finally:
#     print('无论如何都会执行这一步！')

#占位
# for i in range(100):
#     if i % 2 == 0:
#         pass
#     else:
#         print(i, end=' ')


# for i in range(100):
#     if i % 2 != 0:
#        print(i)


# # 中断当前程序
# for i in range(100):
#     if i > 50:
#         break
#     print(i, end=' ')
#

#跳过当前循环，直接进行下一个循环
# for i in range(100):
#     if i > 50:
#         continue
#     print(i, end=' ')


#正则
# import re
# sss = """
# <html>
#     <head>
#         <meta charset="utf-8">
#         <!--IE内核浏览器，强制使用用户已安装的最高版本浏览器渲染，有Chrome框架的优先使用Chrome框架-->
#         <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
#         <title>百度翻译-200种语言互译、沟通全世界！</title>
#         <meta name="keywords" content="翻译,在线翻译,百度翻译,词典,英语,">
#         <meta name="description" content="百度翻译提供即时免费200+语言翻译服务，拥有网页和APP产品，百度翻译APP还支持拍照翻译、语音翻译等特色功能，随时随地沟通全世界">
#         <!--强制国内双核浏览器使用Webkit内核渲染页面-->
#         <!--360 6.X 以上可识别-->
#         <meta name="renderer" content="webkit">
#         <!--其他双核可识别-->
#         <meta name="force-rendering" content="webkit">
#         <script src="//passport.baidu.com/passApi/js/uni_login_wrapper.js?cdnversion=202207131650"></script>
#         <script>
#             var _hmt = _hmt || [];
#             (function() {
#               var hm = document.createElement("script");
#               hm.src = "//hm.baidu.com/hm.js?64ecd82404c51e03dc91cb9e8c025574";
#               var s = document.getElementsByTagName("script")[0];
#               s.parentNode.insertBefore(hm, s);
#             })();
#             // https://fanyi-cdn.cdn.bcebos.com/webStatic /static
#         </script>
#                 <link rel="icon" type="image/png" href="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/img/favicon/favicon-32x32.png" sizes="32x32">
#         <link rel="icon" type="image/png" href="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/img/favicon/favicon-16x16.png" sizes="16x16">
#         <link rel="shortcut icon" type="image/x-icon" href="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/img/favicon/favicon.ico">
#         <link rel="bookmark" type="image/x-icon" href="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/img/favicon/favicon.ico">
#         <link rel="stylesheet" href="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/third_party/outdated_browser/outdatedbrowser.css">
#         <script src="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/third_party/outdated_browser/outdatedbrowser.js?__inline"></script>
#     <script defer="defer" src="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/js/runtime.98da937d.js"></script><script defer="defer" src="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/js/vendors.7284d551.js"></script><script defer="defer" src="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/js/index.593d1b08.js"></script><link href="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/css/vendors.4be20abf.css" rel="stylesheet"><link href="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/css/index.bd177a2c.css" rel="stylesheet"></head>
#     <body>
#         <script src="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/third_party/jquery.js"></script>
#         <script src="https://fanyi-cdn.cdn.bcebos.com/webStatic/translation/third_party//polyfill.min.js"></script>
#             <script>
#         window.parisSubId = 'pc_mainPage';
#     </script>
#     <div class="container">
#         <div class="header">
#     <div class="inner">
#         <div class="logo">
#                         <h1>
#                 <a href="/" class="logo-image" title="百度翻译" target="_self">
#                     <img src="https://fanyiapp.cdn.bcebos.com/cms/image/480f948019d284081745a58783076905.png" alt="" width="99" height="31">
#                 </a>
#             </h1>
#         </div>
#         <div class="navigation">
#     <ul>
#
#
#                     <li class="account-wrap wrap-login">
#                 <a href="https://passport.baidu.com/v2/?login" class="account-login account-head">登录<i class="arrow-down"></i></a>
#                 <ol class="account-panel">
#                     <li>
#                         <a href="https://passport.baidu.com/v2/?login" class="account-login">登录</a>
#                     </li>
#                     <li>
#                         <a href="https://passport.baidu.com/v2/?reg" class="account-register">注册</a>
#                     </li>
#                 </ol>
#             </li>
#             </ul>
# </div>
# <div class="browser-edition-tip" style="display:none">
#     <span>抱歉，您正在使用的浏览器未被完全支持，我们强烈推荐您进行浏览器升级。</span>
#     <a href="###">关闭</a>
# </div>
#
# <script type="text/html" id="tpl-user-info">
#     <li class="account-wrap">
#         <a href="http://www.baidu.com/p/{{$data['user_name']}}" class="account-head">{{$data['user_name']}}<i class="arrow-down"></i></a>
#         <ol class="account-panel">
#             <li>
#                 <a href="http://www.baidu.com/p/{{$data['user_name']}}">{{$data['user_name']}}<i class="arrow-down"></i></a>
#             </li>
#             <li><a href="https://passport.baidu.com/">账号设置</a></li>
#             <li><a href="https://passport.baidu.com/?logout" class="account-logout" target="_self">退出</a></li>
#         </ol>
#     </li>
# </script>
#         <div class="download-guide">
#     <ul class="download-guide-ul">
#         <li class="guide-list download-plugin">
#             <span class="list-name">下载中心</span>
#             <div id="header-plugins-container"></div>
#         </li>
#         <li class="guide-list download-app">
#             <a class="list-name app-list-name" href="http://fanyi.baidu.com/appdownload/download.html?tab=app&appchannel=webtitle" target="_blank">APP下载</a>
#             <a class="list-contain app-contain" href="http://fanyi.baidu.com/appdownload/download.html?tab=app&appchannel=webtitle" target="_blank">
#                 <span class="icon-text">超好用的手机词典</span>
#             </a>
#         </li>
#     </ul>
# </div>
#         <div class="manual-trans-info">
#     <div class="entry-trans-info">
#         <a href="https://fanyi-pro.baidu.com/?hmsr=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91&hmpl=%E5%9B%BA%E5%AE%9A%E5%85%A5%E5%8F%A3&hmcu=%E9%A1%B6%E9%83%A8%E6%8C%89%E9%92%AE&hmkw=&hmci=" target="_blank" class="list-name">人工翻译</a>
#         <span class="list-container">
#             <p class="content-text"><span class="content-text-num">13352</span>&nbsp;名专业译员&nbsp;,&nbsp;<span class="content-text-num">2528</span>&nbsp;名母语审校</p>
#             <p class="content-text">为您提供专属「翻译官」</p>
#             <div class="infolist-detail">
#                 <a class="infolist-left" href="https://fanyi-pro.baidu.com/quick?hmsr=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91&hmpl=%E5%9B%BA%E5%AE%9A%E5%85%A5%E5%8F%A3&hmcu=%E9%A1%B6%E9%83%A8%E6%8C%89%E9%92%AE-%E6%97%A5%E5%B8%B8%E5%BF%AB%E8%AF%91&hmkw=&hmci=" target="_blank">
#                     <div class="infolist-detail-title">日常快译</div>
#                     <div>中英/中日互译</div>
#                     <div>在线输入</div>
#                     <div>即时返回</div>
#                     <div class="infolist-detail-tip">适合日常交流用语</div>
#                 </a>
#                 <div>
#                     <a class="infolist-right-card" href="https://fanyi-pro.baidu.com/doc?hmsr=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91&hmpl=%E5%9B%BA%E5%AE%9A%E5%85%A5%E5%8F%A3&hmcu=%E9%A1%B6%E9%83%A8%E6%8C%89%E9%92%AE-%E4%B8%93%E4%B8%9A%E7%BF%BB%E8%AF%91&hmkw=&hmci=" target="_blank">
#                         <div class="infolist-detail-title">专业翻译</div>
#                         <div>20+语种翻译 |  专业审校排版</div>
#                         <div class="infolist-detail-tip">适合专业文档/证件资料</div>
#                     </a>
#                     <a class="infolist-right-card" href="https://fanyi-pro.baidu.com/polish?hmsr=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91&hmpl=%E5%9B%BA%E5%AE%9A%E5%85%A5%E5%8F%A3&hmcu=%E9%A1%B6%E9%83%A8%E6%8C%89%E9%92%AE-%E6%AF%8D%E8%AF%AD%E6%B6%A6%E8%89%B2&hmkw=&hmci=" target="_blank">
#                         <div class="infolist-detail-title">英文母语润色</div>
#                         <div>专业母语润色 | 审校+质检服务</div>
#                         <div class="infolist-detail-tip">适合SCI论文/发表期刊/演讲稿</div>
#                     </a>
#                 </div>
#             </div>
#         </span>
#     </div>
# </div>
#         <div class="trans-machine">
#     <a href="https://fanyi-video.baidu.com/?hmsr=1&hmpl=2&hmcu=4&hmkw=&hmci=" target="_blank" data-stat-id="88">视频翻译</a>
# </div>        <div class="simultaneous-interpretation">
#     <a href="https://tongchuan.baidu.com?fr=fanyi" target="_blank">同传</a>
#     <img src="https://fanyiapp.cdn.bcebos.com/cms/image/34b406bf33df217a5411dd31f19f932b.png" class="icon-new-si">
# </div>        <div data-stat-id="102" class="simultaneous-interpretation">
#     <a href="https://fanyi-api.baidu.com/" target="_blank">翻译 API</a>
# </div>        <div class="simultaneous-interpretation">
#     <a href="https://fanyi-app.baidu.com/static/react-activity/page/ncov-global-2020.html?fr=pctop" target="_blank">抗疫行动</a>
# </div>        <div class="simultaneous-interpretation">
#     <a href="https://fanyi.baidu.com/home" target="_blank">官网</a>
# </div>    </div>
# </div>
#
# <!-- 彩虹条 -->
# <div class="divide-wrap">
#     <div class="colorbar-before"></div>
#     <div class="colorbar-after"></div>
#     <div class="colorbar"></div>
# </div>
#
# <div id="header"></div>        <div class="main main-outer" id="main-outer">
#             <div class="main main-inner">
#                 <div class="inner">
#                     <div class="translate-wrap">
#                         <div class="trans-operation-wrapper clearfix">
#                             <div class="trans-operation clearfix">
#     <a href="javascript:void(0);" class="language-btn select-from-language">
#         <span class="select-inner">
#             <span class="language-selected" data-lang="auto">
#                 自动检测
#             </span>
#             <i class="arrow-down"></i>
#         </span>
#     </a>
#     <a href="javascript:void(0);" class="language-btn-disable from-to-exchange">
#         <span class="exchange-mask">
#
#         </span>
#     </a>
#     <a href="javascript:void(0);" class="language-btn select-to-language">
#         <span class="select-inner">
#             <span class="language-selected" data-lang="zh">
#                 中文(简体)
#             </span>
#             <i class="arrow arrow-down"></i>
#         </span>
#     </a>
#     <a href="javascript:void(0);" class="trans-btn trans-btn-zh" id="translate-button" target="_self"></a>
#     <a href="javascript:" class="manual-trans-btn"></a>
# </div>
#
# <div id="lang-panel-container"></div>                            <div class="doc-trans-operation">
#     <div class="doc-trans-guide-layout"></div>
#     <div class="doc-trans-dir">
#         <div class="doc-lang-pair curr-doc-dir auto">
#             <span class="from-doc-lang">中英互译(默认)</span>
#             <span class="doc-lang-arrow"></span>
#             <span class="to-doc-lang"></span>
#         </div>
#         <div class="doc-lang-select">
#             <div class="doc-lang-pair" data-dir="zh2en">
#                 <span class="from-doc-lang">中文</span>
#                 <span class="doc-lang-arrow"></span>
#                 <span class="to-doc-lang">英语</span>
#             </div>
#             <div class="doc-lang-pair" data-dir="en2zh">
#                 <span class="from-doc-lang">英语</span>
#                 <span class="doc-lang-arrow"></span>
#                 <span class="to-doc-lang">中文</span>
#             </div>
#             <div class="doc-lang-pair" data-dir="zh2jp">
#                 <span class="from-doc-lang">中文</span>
#                 <span class="doc-lang-arrow"></span>
#                 <span class="to-doc-lang">日语</span>
#             </div>
#             <div class="doc-lang-pair" data-dir="jp2zh">
#                 <span class="from-doc-lang">日语</span>
#                 <span class="doc-lang-arrow"></span>
#                 <span class="to-doc-lang">中文</span>
#             </div>
#             <div class="doc-lang-pair" data-dir="zh2kor">
#                 <span class="from-doc-lang">中文</span>
#                 <span class="doc-lang-arrow"></span>
#                 <span class="to-doc-lang">韩语</span>
#             </div>
#             <div class="doc-lang-pair" data-dir="kor2zh">
#                 <span class="from-doc-lang">韩语</span>
#                 <span class="doc-lang-arrow"></span>
#                 <span class="to-doc-lang">中文</span>
#             </div>
#
#
#             <div class="doc-lang-pair selected" data-dir="auto2auto">
#                 <span class="from-doc-lang">中英互译</span>
#             </div>
#             <div class="doc-lang-guide-container">
#                 <span>点击设置语言，与文档翻译方向一致</span>
#                 <a class="know-btn" href="javascript:">知道了</a>
# """

# pattern = r'\D'
#
# all_numbers = re.findall(pattern, sss)
# print(all_numbers)


# import re
#
# s = 'aa abbb1  245560  9453g  sj5eh95 4h45 h450c c ddd'
#
# # pattern = r'\d'
# #
# # s1 = re.sub(pattern, '-', s)
# # print(s1)
#
# # pattern2 = r'\s'
# # s2 = re.sub(pattern2, '+', s1)
# # print(s2)
#
# pattern3 = r'\d+'
# s1 = re.sub(pattern3, '-', s)
# print(s)
# print(s1)



# def emo(w2, cl, dinner, wash):
#     emo = 100
#     if w2 == 1:
#         emo = emo - 20
#     elif cl == 1:
#         emo -= 20
#     elif dinner:
#         emo -= 20
#     elif wash:
#         emo -= 20
#     return emo


def tmp(t):
    if t >= 20 and t <= 30:
        return '温度适宜'
    elif t >= 31 and t <= 35:
        return '温度较高'
    elif t >= 36:
        return '太热了'
    else:
        return '有点凉'






if __name__ == '__main__':
    # print(emo(1, 0, 0, 0))
    # print(1 == True)
    print(tmp(18))
