

import re


sss = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="renderer" content="webkit" />
    <title>斗罗大陆最新章节_斗罗大陆无弹窗全文阅读_唐家三少_顶点小说</title>
    <link href="https://www.x23us.us/0_80/" rel="canonical" />
    <meta name="keywords" content="斗罗大陆,斗罗大陆最新章节,斗罗大陆全文阅读,斗罗大陆TXT下载,唐家三少" />
    <meta name="description" content="斗罗大陆最新章节正文 第二百三十六章 大结局，最后一个条件（全书完）由网友提供，《斗罗大陆》情节跌宕起伏、扣人心弦，是一本情节与文笔俱佳的玄幻小说，斗罗大陆主要讲述了：&nbsp;&nbsp;&nbsp;&nbsp;将会在本周日，斗罗大6结束的同时开始上传更新，麻烦大家先收藏、推荐一下，谢谢。<br/>&nbsp;&nbsp;&nbsp;&nbsp;阴阳冕书号：1436o15<br/>&nbsp;&nbsp;&nbsp;&nbsp;下面的直通车也可以直接点过去。<br/>&nbsp;&nbsp;&nbsp;&nbsp;【小三出品，必属精品，全新设定，酬谢书友】<br/>&nbsp;&nbsp;&nbsp;&nbsp;抢购实体书，尽享五重惊喜好礼<br/>"/>
    <meta name="mobile-agent" content="format=html5;url=https://m.x23us.us/book/80/">
    <link rel="alternate" media="only screen and (max-width:960px)" href="https://m.x23us.us/book/80/ ">
    <meta name="applicable-device" content="pc">
    <meta http-equiv="Cache-Control" content="no-transform" />
    <meta http-equiv="Cache-Control" content="no-siteapp" />
    <!--必填-->
    <meta property="og:type" content="novel" />
    <meta property="og:title" content="斗罗大陆" />
    <meta property="og:description" content="&nbsp;&nbsp;&nbsp;&nbsp;将会在本周日，斗罗大6结束的同时开始上传更新，麻烦大家先收藏、推荐一下，谢谢。<br/>&nbsp;&nbsp;&nbsp;&nbsp;阴阳冕书号：1436o15<br/>&nbsp;&nbsp;&nbsp;&nbsp;下面的直通车也可以直接点过去。<br/>&nbsp;&nbsp;&nbsp;&nbsp;【小三出品，必属精品，全新设定，酬谢书友】<br/>&nbsp;&nbsp;&nbsp;&nbsp;抢购实体书，尽享五重惊喜好礼<br/>"
    />
    <meta property="og:image" content="https://www.x23us.us/files/article/image/0/80/80s.jpg"/>
    <meta property="og:novel:category" content="玄幻小说" />
    <meta property="og:novel:author" content="唐家三少" />
    <meta property="og:novel:book_name" content="斗罗大陆" />
    <meta property="og:novel:read_url" content="https://www.x23us.us/0_80/" />
    <!--选填-->
    <meta property="og:url" content="https://www.x23us.us/0_80/" />
    <meta property="og:novel:status" content="已完结" />
    <meta property="og:novel:author_link" content="https://www.x23us.us/modules/article/authorarticle.php?author=唐家三少"
    />
    <meta property="og:novel:update_time" content='1990-01-01 12:00:00' />
    <meta property="og:novel:latest_chapter_name" content="第二百三十六章 大结局，最后一个条件（全书完）" />
    <meta property="og:novel:latest_chapter_url" content="https://www.x23us.us/0_80/46874.html" />
    <link rel="stylesheet" type="text/css" href="/biquge/css/common.css" />
    <link rel="stylesheet" type="text/css" href="/biquge/css/list.css" />
    <script type="text/javascript" src="/biquge/js/jquery-1.8.2.js"></script>
<script src="/js/pc_pf.js"></script>
    <script type="text/javascript" src="/biquge/js/common.js"></script>
    <script>
        Go("https://m.x23us.us/book/80/");
    </script>
</head>

<body>
    <div id="wrapper">
            <div class="ywtop">
    <div class="ywtop_con"><script>HeaderFav(); BDShare.html(); Login();</script></div>
  </div>
  <div class="header">
    <div class="header_logo"><a href="/"> 顶点小说</a></div>
    <div class="header_search"><script type="text/javascript">SearchBox();</script></div>
    <div class="userpanel"><script>Contact();</script></div>
  </div>
  <div class="nav">
    <ul>
      <li><a href="/" title=" 顶点小说">首页</a></li>
      <li><a href="https://www.x23us.us/xuanhuanxiaoshuo/" title="玄幻小说">玄幻小说</a></li>
      <li><a href="https://www.x23us.us/xiuzhenxiaoshuo/" title="修真小说">修真小说</a></li>
      <li><a href="https://www.x23us.us/dushixiaoshuo/" title="都市小说">都市小说</a></li>
      <li><a href="https://www.x23us.us/chuanyuexiaoshuo/" title="穿越小说">穿越小说</a></li>
      <li><a href="https://www.x23us.us/wangyouxiaoshuo/" title="网游小说">网游小说</a></li>
      <li><a href="https://www.x23us.us/kehuanxiaoshuo/" title="科幻小说">科幻小说</a></li>
      <li><a href="https://www.x23us.us/wanben/" title="完本小说">完本小说</a></li>
      <li><a href="https://www.x23us.us/paihangbang/" title="小说排行榜单">排行榜单</a></li>
      <li><a rel="nofollow" href="https://www.x23us.us/modules/article/bookcase.php">我的书架</a></li>
    </ul>
  </div><div id="center_tip"><b>最新网址：www.x23us.us</b></div>
    </div>
<script>list1();</script>
    <div class="box_con">
        <div class="con_top">
            <div class="fr">
                <a target="_blank" href="https://m.x23us.us/book/80/" title="手机阅读《斗罗大陆》">手机阅读《斗罗大陆》</a>、
                <a rel="nofollow" href="javascript:void(0);" onclick="report('斗罗大陆')" class="red errorlink">催更报错</a>
            </div>
            <a href="https://www.x23us.us">顶点小说</a> &gt; 玄幻小说 &gt; 斗罗大陆        </div>
        <div id="maininfo">
            <div id="fmimg">
                <img width="120px" height="180px" onerror="src='/modules/article/images/nocover.jpg'" src="https://www.x23us.us/files/article/image/0/80/80s.jpg"
                    alt="斗罗大陆" />
                <span class="b"></span>
            </div>
            <div id="info">
                <h1>斗罗大陆</h1>
                <p>作者：
                    <a href="/modules/article/authorarticle.php?author=唐家三少"
                        target="_blank">唐家三少</a>
                </p>
                <p>
                    动作：
                    <font color="red"><B>已完结</B></font>，
                    <a href="javascript:;" onclick="vote('80');" rel="nofollow">投票推荐</a>，
                    <a href="javascript:;" onclick="addbookcase('80');">加入书架</a>，
                    <a href="#footer" rel="nofollow">直达底部</a>
                </p>
                <p>更新时间：1990-01-01 12:00:00&nbsp;[共918万字]
                    <p>最新：
                        <a href="46874.html" title="第二百三十六章 大结局，最后一个条件（全书完）">第二百三十六章 大结局，最后一个条件（全书完）</a>
                    </p>
                    <div class="clear"></div>
                    <div id="intro">
                        &nbsp;&nbsp;&nbsp;&nbsp;将会在本周日，斗罗大6结束的同时开始上传更新，麻烦大家先收藏、推荐一下，谢谢。<br/>&nbsp;&nbsp;&nbsp;&nbsp;阴阳冕书号：1436o15<br/>&nbsp;&nbsp;&nbsp;&nbsp;下面的直通车也可以直接点过去。<br/>&nbsp;&nbsp;&nbsp;&nbsp;【小三出品，必属精品，全新设定，酬谢书友】<br/>&nbsp;&nbsp;&nbsp;&nbsp;抢购实体书，尽享五重惊喜好礼<br/>                    </div>
            </div>
            <div class="clear"></div>
            <div class="tjlist">推荐阅读：
                    
  <a href='https://www.x23us.us/60_60471/' target='_blank' title="炎帝诀">炎帝诀</a>、

  <a href='https://www.x23us.us/3_3212/' target='_blank' title="一世独尊">一世独尊</a>、

  <a href='https://www.x23us.us/58_58180/' target='_blank' title="都市极品医神">都市极品医神</a>、

  <a href='https://www.x23us.us/28_28945/' target='_blank' title="终极斗罗">终极斗罗</a>、

  <a href='https://www.x23us.us/3_3546/' target='_blank' title="我从凡间来">我从凡间来</a>、

  <a href='https://www.x23us.us/1_1349/' target='_blank' title="百炼飞升录">百炼飞升录</a>、

  <a href='https://www.x23us.us/90_90928/' target='_blank' title="横推从拔刀开始">横推从拔刀开始</a>、

  <a href='https://www.x23us.us/3_3244/' target='_blank' title="元尊">元尊</a>、

  <a href='https://www.x23us.us/83_83367/' target='_blank' title="我有一个熟练度面板">我有一个熟练度面板</a>、

            </div>
        </div>
    </div>
<script>list2();</script>
    <div class="box_con">
        <div id="list">
            <dl>
    <dt>《斗罗大陆》 正文</dt>
    
    
            <dd><a href='/0_80/46124.html'>小三书友团体－“唐门”正式成立。</a></dd>
            <dd><a href='/0_80/46125.html'>不论是骂番茄还是替番茄辩解的，请离开这里</a></dd>
            <dd><a href='/0_80/46126.html'>上架感言</a></dd>
            <dd><a href='/0_80/46127.html'>已出场人物列表</a></dd>
        
    
    
            <dd><a href='/0_80/46128.html'>推荐一本好书给大家</a></dd>
            <dd><a href='/0_80/46129.html'>关于小舞的身高问题，我再解释一下。</a></dd>
            <dd><a href='/0_80/46130.html'>加精大会马上开始，12点05到12点45</a></dd>
            <dd><a href='/0_80/46131.html'>推荐一款不错的网页游戏</a></dd>
        
    
    
            <dd><a href='/0_80/46132.html'>加精大会暂停一次</a></dd>
            <dd><a href='/0_80/46133.html'>加精大会暂停</a></dd>
            <dd><a href='/0_80/46134.html'>今晚加精大会，顺便推荐一本书</a></dd>
            <dd><a href='/0_80/46135.html'>加精大会暂停一段时间，特此通知</a></dd>
        
    
    
            <dd><a href='/0_80/46136.html'>老婆生了，糖糖公主六斤六两，平安降生</a></dd>
            <dd><a href='/0_80/46137.html'>关于大家的质疑，小三解释两句。</a></dd>
            <dd><a href='/0_80/46138.html'>在成千上万书友的支持下，终于获得了第一</a></dd>
            <dd><a href='/0_80/46139.html'>小三自己的家，欢迎大家去看看</a></dd>
        
    
    
            <dd><a href='/0_80/46140.html'>汶川地震一周年，让我们为死难的同胞默哀</a></dd>
            <dd><a href='/0_80/46141.html'>恩，我强调一下，一夫一妻</a></dd>
            <dd><a href='/0_80/46142.html'>宣传一下小三的个人网站</a></dd>
            <dd><a href='/0_80/46143.html'>隆重推荐《剑侠世界》盛大版</a></dd>
        
    
    
            <dd><a href='/0_80/46144.html'>天青牛蟒也写书……</a></dd>
            <dd><a href='/0_80/46145.html'>推荐一本朋友的书</a></dd>
            <dd><a href='/0_80/46146.html'>推荐一本朋友的新书，欢迎大家支持</a></dd>
            <dd><a href='/0_80/46147.html'>『史莱克七怪』资料汇总</a></dd>
        
    
    
            <dd><a href='/0_80/46148.html'>斗罗即将收官，求推荐票</a></dd>
            <dd><a href='/0_80/46149.html'>无语了，不得不澄清</a></dd>
            <dd><a href='/0_80/46150.html'>新书《阴阳冕》预告</a></dd>
            <dd><a href='/0_80/46151.html'>新书天珠变已经注册，28号正式上传</a></dd>
        
    
    
            <dd><a href='/0_80/46152.html'>新书《天珠变》已经开始更新</a></dd>
            <dd><a href='/0_80/46153.html'>新书《神印王座》已开始上传。</a></dd>
            <dd><a href='/0_80/46154.html'>观看火爆视频访谈</a></dd>
            <dd><a href='/0_80/46155.html'>引子 穿越的</a></dd>
        
    
    
            <dd><a href='/0_80/46156.html'>第一章 ，异界唐三（一）</a></dd>
            <dd><a href='/0_80/46157.html'>第一章 ，异界唐三（二）</a></dd>
            <dd><a href='/0_80/46159.html'>第一章 ，异界唐三（三）</a></dd>
            <dd><a href='/0_80/46160.html'>第一章 ，异界唐三（四）</a></dd>
        
    
    
            <dd><a href='/0_80/46161.html'>第二章 废武魂与先天满魂力（一）</a></dd>
            <dd><a href='/0_80/46162.html'>第二章 废武魂与先天满魂力（二）</a></dd>
            <dd><a href='/0_80/46163.html'>第二章 废武魂与先天满魂力（三）</a></dd>
            <dd><a href='/0_80/46164.html'>第二章 废武魂与先天满魂力（四）</a></dd>
        
    
    
            <dd><a href='/0_80/46165.html'>第三章 双生武魂(一)</a></dd>
            <dd><a href='/0_80/46166.html'>第三章 双生武魂(二)</a></dd>
            <dd><a href='/0_80/46167.html'>第三章 双生武魂(三)</a></dd>
            <dd><a href='/0_80/46168.html'>第三章 双生武魂(四)</a></dd>
        
    
    
            <dd><a href='/0_80/46169.html'>第三章 双生武魂(五)</a></dd>
            <dd><a href='/0_80/46170.html'>第四章 异界唐三的第一件暗器（一）</a></dd>
            <dd><a href='/0_80/46171.html'>第四章 异界唐三的第一件暗器（二）</a></dd>
            <dd><a href='/0_80/46172.html'>第四章 异界唐三的第一件暗器(三)</a></dd>
        
    
    
            <dd><a href='/0_80/46173.html'>第四章 异界唐三的第一件暗器(四)</a></dd>
            <dd><a href='/0_80/46174.html'>第四章 异界唐三的第一件暗器(五)</a></dd>
            <dd><a href='/0_80/46175.html'>第五章 大师？师傅？（一）</a></dd>
            <dd><a href='/0_80/46176.html'>第五章 大师？师傅？（二）</a></dd>
        
    
    
            <dd><a href='/0_80/46177.html'>第五章 大师？师傅？（三）</a></dd>
            <dd><a href='/0_80/46178.html'>第五章 大师？师傅？（四）</a></dd>
            <dd><a href='/0_80/46179.html'>第六章 我叫小舞，跳舞的舞（一）</a></dd>
            <dd><a href='/0_80/46180.html'>第六章 我叫小舞，跳舞的舞（二）</a></dd>
        
    
    
            <dd><a href='/0_80/46181.html'>第六章 我叫小舞，跳舞的舞（三）</a></dd>
            <dd><a href='/0_80/46182.html'>第六章 我叫小舞，跳舞的舞（四）</a></dd>
            <dd><a href='/0_80/46183.html'>第六章 我叫小舞，跳舞的舞（五）</a></dd>
            <dd><a href='/0_80/46184.html'>第七章 小舞，你还要啊？(一)</a></dd>
        
    
    
            <dd><a href='/0_80/46185.html'>第七章 小舞，你还要啊？(二)</a></dd>
            <dd><a href='/0_80/46186.html'>第七章 小舞，你还要啊？(三)</a></dd>
            <dd><a href='/0_80/46187.html'>第七章 小舞，你还要啊？(四)</a></dd>
            <dd><a href='/0_80/46188.html'>第七章 小舞，你还要啊？(五)</a></dd>
        
    
    
            <dd><a href='/0_80/46189.html'>第八章 魂导器，二十四桥明月夜（一）</a></dd>
            <dd><a href='/0_80/46190.html'>第八章 魂导器，二十四桥明月夜(二)</a></dd>
            <dd><a href='/0_80/46191.html'>第八章 魂导器，二十四桥明月夜(三)</a></dd>
            <dd><a href='/0_80/46192.html'>第八章 魂导器，二十四桥明月夜(四)</a></dd>
        
    
    
            <dd><a href='/0_80/46193.html'>第八章 魂导器，二十四桥明月夜(五)</a></dd>
            <dd><a href='/0_80/46194.html'>第九章 蓝银草的第一魂环（一）</a></dd>
            <dd><a href='/0_80/46195.html'>第九章 蓝银草的第一魂环（二）</a></dd>
            <dd><a href='/0_80/46196.html'>第九章 蓝银草的第一魂环（三）</a></dd>
        
    
    
            <dd><a href='/0_80/46197.html'>第九章 蓝银草的第一魂环（四）</a></dd>
            <dd><a href='/0_80/46198.html'>第九章 蓝银草的第一魂环（五）</a></dd>
            <dd><a href='/0_80/46199.html'>第十章 第一魂环技能(一)</a></dd>
            <dd><a href='/0_80/46200.html'>第十章 第一魂环技能(二)</a></dd>
        
    
    
            <dd><a href='/0_80/46201.html'>第十章 第一魂环技能(三)</a></dd>
            <dd><a href='/0_80/46202.html'>第十章 第一魂环技能(四)</a></dd>
            <dd><a href='/0_80/46203.html'>第十章 第一魂环技能(五)</a></dd>
            <dd><a href='/0_80/46204.html'>第十一章 小舞，原来你真的是个兔子(一)</a></dd>
        
    
    
            <dd><a href='/0_80/46205.html'>第十一章 小舞原来你真的是个兔子(二)</a></dd>
            <dd><a href='/0_80/46206.html'>第十一章 小舞原来你真的是个兔子(三)</a></dd>
            <dd><a href='/0_80/46207.html'>第十一章 小舞原来你真的是个兔子(四)</a></dd>
            <dd><a href='/0_80/46208.html'>第十二章 乱披风锤法(一)</a></dd>
        
    
    
            <dd><a href='/0_80/46209.html'>第十二章 乱披风锤法(二)</a></dd>
            <dd><a href='/0_80/46210.html'>第十二章 乱披风锤法(三)</a></dd>
            <dd><a href='/0_80/46212.html'>第十二章 乱披风锤法(四)</a></dd>
            <dd><a href='/0_80/46213.html'>第十二章 乱披风锤法(五)</a></dd>
        
    
    
            <dd><a href='/0_80/46214.html'>第十三章 父亲的留言(一)</a></dd>
            <dd><a href='/0_80/46215.html'>第十三章 父亲的留言(二)</a></dd>
            <dd><a href='/0_80/46216.html'>第十三章 父亲的留言(三)</a></dd>
            <dd><a href='/0_80/46217.html'>第十三章 父亲的留言(四)</a></dd>
        
    
    
            <dd><a href='/0_80/46218.html'>第十四章 邪眸白虎戴沐白(一)</a></dd>
            <dd><a href='/0_80/46219.html'>第十四章 邪眸白虎戴沐白(二)</a></dd>
            <dd><a href='/0_80/46220.html'>第十四章 邪眸白虎戴沐白(三)</a></dd>
            <dd><a href='/0_80/46221.html'>第十四章 邪眸白虎戴沐白(四)</a></dd>
        
    
    
            <dd><a href='/0_80/46222.html'>第十四章 邪眸白虎戴沐白(五)</a></dd>
            <dd><a href='/0_80/46223.html'>第十四章 邪眸白虎戴沐白(六)</a></dd>
            <dd><a href='/0_80/46224.html'>第十五章 千年魂环之技，白虎金刚变(一)</a></dd>
            <dd><a href='/0_80/46225.html'>第十五章 千年魂环之技，白虎金刚变(二)</a></dd>
        
    
    
            <dd><a href='/0_80/46226.html'>第十五章 千年魂环之技，白虎金刚变(三)</a></dd>
            <dd><a href='/0_80/46227.html'>第十五章 千年魂环之技，白虎金刚变(四)</a></dd>
            <dd><a href='/0_80/46228.html'>第十五章 千年魂环之技，白虎金刚变(五)</a></dd>
            <dd><a href='/0_80/46229.html'>第十六章 板晶发金龙须针（一）</a></dd>
        
    
    
            <dd><a href='/0_80/46230.html'>第十六章 板晶发金龙须针（二）</a></dd>
            <dd><a href='/0_80/46231.html'>第十六章 板晶发金龙须针（三）</a></dd>
            <dd><a href='/0_80/46232.html'>第十六章 板晶发金龙须针（四）</a></dd>
            <dd><a href='/0_80/46233.html'>第十六章 板晶发金龙须针（五）</a></dd>
        
    
    
            <dd><a href='/0_80/46234.html'>第十七章 只收怪物的学院(一)</a></dd>
            <dd><a href='/0_80/46235.html'>第十七章 只收怪物的学院(二)</a></dd>
            <dd><a href='/0_80/46236.html'>第十七章 只收怪物的学院(三)</a></dd>
            <dd><a href='/0_80/46237.html'>第十七章 只收怪物的学院(四)</a></dd>
        
    
    
            <dd><a href='/0_80/46238.html'>第十七章 只收怪物的学院(五)</a></dd>
            <dd><a href='/0_80/46239.html'>第十八章 不动明王赵无极(一)</a></dd>
            <dd><a href='/0_80/46240.html'>第十八章 不动明王赵无极(二)</a></dd>
            <dd><a href='/0_80/46241.html'>第十八章 不动明王赵无极(三)</a></dd>
        
    
    
            <dd><a href='/0_80/46242.html'>第十八章 不动明王赵无极(四)</a></dd>
            <dd><a href='/0_80/46243.html'>第十八章 不动明王赵无极(五)</a></dd>
            <dd><a href='/0_80/46244.html'>第十九章 唐三的暗器(一)</a></dd>
            <dd><a href='/0_80/46245.html'>第十九章 唐三的暗器(二)</a></dd>
        
    
    
            <dd><a href='/0_80/46246.html'>第十九章 唐三的暗器(三)</a></dd>
            <dd><a href='/0_80/46247.html'>第十九章 唐三的暗器(四)</a></dd>
            <dd><a href='/0_80/46248.html'>第十九章 唐三的暗器(五)</a></dd>
            <dd><a href='/0_80/46249.html'>第二十章 奥斯卡的大香肠和小腊肠(一)</a></dd>
        
    
    
            <dd><a href='/0_80/46250.html'>第二十章 奥斯卡的大香肠和小腊肠(二)</a></dd>
            <dd><a href='/0_80/46251.html'>第二十章 奥斯卡的大香肠和小腊肠(三)</a></dd>
            <dd><a href='/0_80/46252.html'>第二十章 奥斯卡的大香肠和小腊肠(四)</a></dd>
            <dd><a href='/0_80/46253.html'>第二十章 奥斯卡的大香肠和小腊肠(五)</a></dd>
        
    
    
            <dd><a href='/0_80/46254.html'>第二十一章 邪火凤凰(一)</a></dd>
            <dd><a href='/0_80/46255.html'>第二十一章 邪火凤凰(二)</a></dd>
            <dd><a href='/0_80/46256.html'>第二十一章 邪火凤凰(三)</a></dd>
            <dd><a href='/0_80/46257.html'>第二十一章 邪火凤凰(四)</a></dd>
        
    
    
            <dd><a href='/0_80/46258.html'>第二十二章 四眼猫鹰弗兰德(一)</a></dd>
            <dd><a href='/0_80/46259.html'>第二十二章 四眼猫鹰弗兰德(二)</a></dd>
            <dd><a href='/0_80/46260.html'>第二十二章 四眼猫鹰弗兰德(三)</a></dd>
            <dd><a href='/0_80/46261.html'>第二十二章 四眼猫鹰弗兰德(四)</a></dd>
        
    
    
            <dd><a href='/0_80/46262.html'>第二十二章 四眼猫鹰弗兰德(五)</a></dd>
            <dd><a href='/0_80/46263.html'>第二十三章 魔女本色(一)</a></dd>
            <dd><a href='/0_80/46264.html'>第二十三章 魔女本色(二)</a></dd>
            <dd><a href='/0_80/46265.html'>第二十三章 魔女本色(三)</a></dd>
        
    
    
            <dd><a href='/0_80/46266.html'>第二十三章 魔女本色(四)</a></dd>
            <dd><a href='/0_80/46267.html'>第二十三章 魔女本色(五)</a></dd>
            <dd><a href='/0_80/46268.html'>第二十四章 三五组合的成立(一)</a></dd>
            <dd><a href='/0_80/46269.html'>第二十四章 三五组合的成立(二)</a></dd>
        
    
    
            <dd><a href='/0_80/46270.html'>第二十四章 三五组合的成立(三)</a></dd>
            <dd><a href='/0_80/46272.html'>第二十四章 三五组合的成立(四)</a></dd>
            <dd><a href='/0_80/46273.html'>第二十四章 三五组合的成立(五)</a></dd>
            <dd><a href='/0_80/46274.html'>第一百一十六章 器武魂的威力（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46275.html'>第一百一十七章 器武魂的威力（中）</a></dd>
            <dd><a href='/0_80/46276.html'>第一百一十八章 器武魂的威力（下）</a></dd>
            <dd><a href='/0_80/46277.html'>第一百一十九章 星斗大森林（上）</a></dd>
            <dd><a href='/0_80/46278.html'>第一百二十章 星斗大森林（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46279.html'>第一百二十一章 星斗大森林（下）</a></dd>
            <dd><a href='/0_80/46280.html'>第一百二十二章 不敢惹事是庸才（上）</a></dd>
            <dd><a href='/0_80/46281.html'>第一百二十三章 不敢惹事是庸才（中）</a></dd>
            <dd><a href='/0_80/46282.html'>第一百二十四章 不敢惹事是庸才（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46283.html'>第一百二十五章 千年凤尾鸡冠蛇（上）</a></dd>
            <dd><a href='/0_80/46284.html'>第一百二十六章 千年凤尾鸡冠蛇（中）</a></dd>
            <dd><a href='/0_80/46285.html'>第一百二十七章 千年凤尾鸡冠蛇（下）</a></dd>
            <dd><a href='/0_80/46286.html'>第一百二十八章 盖世龙蛇（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46287.html'>第一百二十九章 盖世龙蛇（中）</a></dd>
            <dd><a href='/0_80/46288.html'>第一百三十章 盖世龙蛇（下）</a></dd>
            <dd><a href='/0_80/46289.html'>第一百三十一章 奥斯卡的第三魂环（上）</a></dd>
            <dd><a href='/0_80/46290.html'>第一百三十二章 奥斯卡的第三魂环（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46291.html'>第一百三十三章 奥斯卡的第三魂环（下）</a></dd>
            <dd><a href='/0_80/46292.html'>第一百三十四章 森林之王，泰坦巨猿（上）</a></dd>
            <dd><a href='/0_80/46293.html'>第一百三十五章 森林之王，泰坦巨猿（中）</a></dd>
            <dd><a href='/0_80/46294.html'>第一百三十六章 森林之王，泰坦巨猿（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46295.html'>第一百三十七章 邪恶的杀戮者，人面魔蛛（上）</a></dd>
            <dd><a href='/0_80/46296.html'>第一百三十八章 邪恶的杀戮者，人面魔蛛（中）</a></dd>
            <dd><a href='/0_80/46297.html'>第一百三十九章 邪恶的杀戮者，人面魔蛛（下）</a></dd>
            <dd><a href='/0_80/46298.html'>第一百四十章 孟依然也用暗器？（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46299.html'>第一百四十一章 孟依然也用暗器？（中）</a></dd>
            <dd><a href='/0_80/46300.html'>第一百四十二章 孟依然也用暗器？（下）</a></dd>
            <dd><a href='/0_80/46301.html'>第一百四十三章 超过极限的人面魔蛛魂环（上）</a></dd>
            <dd><a href='/0_80/46302.html'>第一百四十四章 超过极限的人面魔蛛魂环（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46303.html'>第一百四十五章 超过极限的人面魔蛛魂环（下）</a></dd>
            <dd><a href='/0_80/46304.html'>第一百四十六章 唐三强横的第三魂环（上）</a></dd>
            <dd><a href='/0_80/46306.html'>第一百四十七章 唐三强横的第三魂环（中）</a></dd>
            <dd><a href='/0_80/46307.html'>第一百四十八章 唐三强横的第三魂环（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46308.html'>第一百四十九章 大师到来（上）</a></dd>
            <dd><a href='/0_80/46309.html'>第一百五十章 大师到来（中）</a></dd>
            <dd><a href='/0_80/46310.html'>第一百五十一章 大师到来（下）</a></dd>
            <dd><a href='/0_80/46311.html'>第一百五十二章 蓝银草进化后的威力（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46312.html'>第一百五十三章 蓝银草进化后的威力（中）</a></dd>
            <dd><a href='/0_80/46313.html'>第一百五十四章 蓝银草进化后的威力（下）</a></dd>
            <dd><a href='/0_80/46314.html'>第一百五十五章 外附魂骨(上)</a></dd>
            <dd><a href='/0_80/46315.html'>第一百五十六章 外附魂骨(中)</a></dd>
        
    
    
            <dd><a href='/0_80/46316.html'>第一百五十七章 外附魂骨(下)</a></dd>
            <dd><a href='/0_80/46317.html'>第一百五十八章 “铁”匠铺（上）</a></dd>
            <dd><a href='/0_80/46318.html'>第一百五十九章 “铁”匠铺（中）</a></dd>
            <dd><a href='/0_80/46319.html'>第一百六十章 “铁”匠铺（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46320.html'>第一百六十一章 特训第一阶段开始（上）</a></dd>
            <dd><a href='/0_80/46321.html'>第一百六十二章 特训第一阶段开始（中）</a></dd>
            <dd><a href='/0_80/46322.html'>第一百六十三章 特训第一阶段开始（下）</a></dd>
            <dd><a href='/0_80/46323.html'>第一百六十四章 不抛弃，不放弃（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46324.html'>第一百六十五章 不抛弃，不放弃（中）</a></dd>
            <dd><a href='/0_80/46325.html'>第一百六十六章 不抛弃，不放弃（下）</a></dd>
            <dd><a href='/0_80/46326.html'>第一百六十七章 大师是魔鬼（上）</a></dd>
            <dd><a href='/0_80/46327.html'>第一百六十八章 大师是魔鬼（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46328.html'>第一百六十九章 大师是魔鬼（下）</a></dd>
            <dd><a href='/0_80/46329.html'>第一百七十章 猥琐怪叔叔，不乐(上)</a></dd>
            <dd><a href='/0_80/46330.html'>第一百七十一章 猥琐怪叔叔，不乐(中)</a></dd>
            <dd><a href='/0_80/46331.html'>第一百七十二章 猥琐怪叔叔，不乐(下)</a></dd>
        
    
    
            <dd><a href='/0_80/46332.html'>第一百七十三章 大师教学的第二阶段(上)</a></dd>
            <dd><a href='/0_80/46333.html'>第一百七十四章 大师教学的第二阶段(中)</a></dd>
            <dd><a href='/0_80/46334.html'>第一百七十五章 大师教学的第二阶段(下)</a></dd>
            <dd><a href='/0_80/46335.html'>第一百七十六章 强横的对手，狂战队（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46336.html'>第一百七十七章 强横的对手，狂战队（中）</a></dd>
            <dd><a href='/0_80/46337.html'>第一百七十八章 强横的对手，狂战队（下）</a></dd>
            <dd><a href='/0_80/46339.html'>第一百七十九章 控制系魂师的强势（上）</a></dd>
            <dd><a href='/0_80/46340.html'>第一百八十章 控制系魂师的强势（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46341.html'>第一百八十一章 控制系魂师的强势（下）</a></dd>
            <dd><a href='/0_80/46342.html'>第一百八十二章 蜘蛛王者的威压（上）</a></dd>
            <dd><a href='/0_80/46343.html'>第一百八十三章 蜘蛛王者的威压（中）</a></dd>
            <dd><a href='/0_80/46344.html'>第一百八十四章 蜘蛛王者的威压（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46345.html'>第一百八十五章 皇斗战队(上)</a></dd>
            <dd><a href='/0_80/46346.html'>第一百八十六章 皇斗战队(中)</a></dd>
            <dd><a href='/0_80/46347.html'>第一百八十七章 皇斗战队(下)</a></dd>
            <dd><a href='/0_80/46348.html'>第一百八十八章 七怪战皇斗（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46349.html'>第一百八十九章 七怪战皇斗（中）</a></dd>
            <dd><a href='/0_80/46350.html'>第一百九十章 七怪战皇斗（下）</a></dd>
            <dd><a href='/0_80/46351.html'>第一百九十一章 碧磷紫毒（上）</a></dd>
            <dd><a href='/0_80/46352.html'>第一百九十二章 碧磷紫毒（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46353.html'>第一百九十三章 碧磷紫毒（下）</a></dd>
            <dd><a href='/0_80/46354.html'>第一百九十四章 武魂融合技之幽冥白虎（上）</a></dd>
            <dd><a href='/0_80/46355.html'>第一百九十五章 武魂融合技之幽冥白虎（中）</a></dd>
            <dd><a href='/0_80/46356.html'>第一百九十六章 武魂融合技之幽冥白虎（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46357.html'>第一百九十七章 八蛛矛，定胜负（上）</a></dd>
            <dd><a href='/0_80/46358.html'>第一百九十八章 八蛛矛，定胜负（中）</a></dd>
            <dd><a href='/0_80/46359.html'>第一百九十九章 八蛛矛，定胜负（下）</a></dd>
            <dd><a href='/0_80/46360.html'>第二百章 史莱克，金斗魂级战队（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46361.html'>第二百零一章 史莱克，金斗魂级战队（中）</a></dd>
            <dd><a href='/0_80/46362.html'>第二百零二章 史莱克，金斗魂级战队（下）</a></dd>
            <dd><a href='/0_80/46364.html'>第二百零三章 借鸡生蛋？（上）</a></dd>
            <dd><a href='/0_80/46365.html'>第二百零四章 借鸡生蛋？（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46366.html'>第二百零五章 借鸡生蛋？（下）</a></dd>
            <dd><a href='/0_80/46367.html'>第二百零六章 飞天神爪（上）</a></dd>
            <dd><a href='/0_80/46368.html'>第二百零七章 飞天神爪（中）</a></dd>
            <dd><a href='/0_80/46369.html'>第二百零八章 飞天神爪（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46370.html'>第二百零九章 越阶挑战（上）</a></dd>
            <dd><a href='/0_80/46371.html'>第二百一十章 越阶挑战（中）</a></dd>
            <dd><a href='/0_80/46372.html'>第二百一十一章 越阶挑战（下）</a></dd>
            <dd><a href='/0_80/46373.html'>第二百一十二章 凶神战队（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46374.html'>第二百一十三章 凶神战队（中）</a></dd>
            <dd><a href='/0_80/46375.html'>第二百一十四章 凶神战队（下）</a></dd>
            <dd><a href='/0_80/46376.html'>第二百一十五章 天斗皇家学院(上)</a></dd>
            <dd><a href='/0_80/46377.html'>第二百一十六章 天斗皇家学院(中)</a></dd>
        
    
    
            <dd><a href='/0_80/46378.html'>第二百一十七章 天斗皇家学院(下）</a></dd>
            <dd><a href='/0_80/46379.html'>第二百一十八章 贯通，第一脉（上）</a></dd>
            <dd><a href='/0_80/46380.html'>第二百一十九章 贯通，第一脉（中）</a></dd>
            <dd><a href='/0_80/46381.html'>第二百二十章 贯通，第一脉（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46382.html'>第二百二十一章 封号斗罗，封号：毒（上）</a></dd>
            <dd><a href='/0_80/46383.html'>第二百二十二章 封号斗罗，封号：毒（中）</a></dd>
            <dd><a href='/0_80/46384.html'>第二百二十三章 封号斗罗，封号：毒（下）</a></dd>
            <dd><a href='/0_80/46385.html'>第二百二十四章 黄金铁三角的最后一角(上)</a></dd>
        
    
    
            <dd><a href='/0_80/46386.html'>第二百二十五章 黄金铁三角的最后一角(中)</a></dd>
            <dd><a href='/0_80/46387.html'>第二百二十六章 黄金铁三角的最后一角(下)</a></dd>
            <dd><a href='/0_80/46389.html'>第二百二十七章 黄金铁三角的往事（上）</a></dd>
            <dd><a href='/0_80/46390.html'>第二百二十八章 黄金铁三角的往事（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46391.html'>第二百二十九章 黄金铁三角的往事（下）</a></dd>
            <dd><a href='/0_80/46392.html'>第二百三十章 冰火两仪眼(上)</a></dd>
            <dd><a href='/0_80/46393.html'>第二百三十一章 冰火两仪眼(中)</a></dd>
            <dd><a href='/0_80/46394.html'>第二百三十二章 冰火两仪眼(下)</a></dd>
        
    
    
            <dd><a href='/0_80/46395.html'>第二百三十三章 冰火炼金身（上）</a></dd>
            <dd><a href='/0_80/46396.html'>第二百三十四章 冰火炼金身（中）</a></dd>
            <dd><a href='/0_80/46397.html'>第二百三十五章 冰火炼金身（下）</a></dd>
            <dd><a href='/0_80/46398.html'>第二百三十六章 黄金圣龙VS碧磷蛇皇（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46399.html'>第二百三十七章 黄金圣龙VS碧磷蛇皇（中）</a></dd>
            <dd><a href='/0_80/46400.html'>第二百三十八章 黄金圣龙VS碧磷蛇皇（下）</a></dd>
            <dd><a href='/0_80/46401.html'>第二百三十九章 幽香绮罗仙品（上）</a></dd>
            <dd><a href='/0_80/46402.html'>第二百四十章 幽香绮罗仙品（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46403.html'>第二百四十一章 幽香绮罗仙品（下）</a></dd>
            <dd><a href='/0_80/46404.html'>第二百四十二章 水火不侵，百毒辟易（上）</a></dd>
            <dd><a href='/0_80/46405.html'>第二百四十三章 水火不侵，百毒辟易（中）</a></dd>
            <dd><a href='/0_80/46406.html'>第二百四十四章 水火不侵，百毒辟易（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46407.html'>第二百四十五章 如意百宝囊与子母追魂夺命胆（上）</a></dd>
            <dd><a href='/0_80/46408.html'>第二百四十六章 如意百宝囊与子母追魂夺命胆（中）</a></dd>
            <dd><a href='/0_80/46409.html'>第二百四十七章 如意百宝囊与子母追魂夺命胆（下）</a></dd>
            <dd><a href='/0_80/46411.html'>第二百四十八章 小舞：发誓不要离开我（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46412.html'>第二百四十九章 小舞：发誓不要离开我（中）</a></dd>
            <dd><a href='/0_80/46413.html'>第二百五十章 小舞：发誓不要离开我（下）</a></dd>
            <dd><a href='/0_80/46414.html'>第二百五十一章 绝世仙品配七怪（上）</a></dd>
            <dd><a href='/0_80/46415.html'>第二百五十二章 绝世仙品配七怪（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46416.html'>第二百五十三章 绝世仙品配七怪（下）</a></dd>
            <dd><a href='/0_80/46417.html'>第二百五十四章 冰清玉洁唐三少（上）</a></dd>
            <dd><a href='/0_80/46418.html'>第二百五十五章 冰清玉洁唐三少（中）</a></dd>
            <dd><a href='/0_80/46419.html'>第二百五十六章 冰清玉洁唐三少（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46420.html'>第二百五十七章 豁然贯通（上）</a></dd>
            <dd><a href='/0_80/46421.html'>第二百五十八章 豁然贯通（中）</a></dd>
            <dd><a href='/0_80/46422.html'>第二百五十九章 豁然贯通（下）</a></dd>
            <dd><a href='/0_80/46423.html'>第二百六十章 天斗拍卖场（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46424.html'>第二百六十一章 天斗拍卖场（中）</a></dd>
            <dd><a href='/0_80/46425.html'>第二百六十二章 天斗拍卖场（下）</a></dd>
            <dd><a href='/0_80/46426.html'>第二百六十三章 极端纯力量魂师（上）</a></dd>
            <dd><a href='/0_80/46427.html'>第二百六十四章 极端纯力量魂师（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46428.html'>第二百六十五章 极端纯力量魂师（下）</a></dd>
            <dd><a href='/0_80/46429.html'>第二百六十六章 七宝琉璃宗（上）</a></dd>
            <dd><a href='/0_80/46431.html'>第二百六十七章 七宝琉璃宗（中）</a></dd>
            <dd><a href='/0_80/46432.html'>第二百六十八章 七宝琉璃宗（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46433.html'>第二百六十九章 七宝琉璃宗的惊讶(上)</a></dd>
            <dd><a href='/0_80/46434.html'>第二百七十章 七宝琉璃宗的惊讶(中)</a></dd>
            <dd><a href='/0_80/46435.html'>第二百七十一章 七宝琉璃宗的惊讶(下)</a></dd>
            <dd><a href='/0_80/46436.html'>第二百七十二章 大力神，爷爷真的来了（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46437.html'>第二百七十三章 大力神，爷爷真的来了（中）</a></dd>
            <dd><a href='/0_80/46438.html'>第二百七十四章 大力神，爷爷真的来了（下）</a></dd>
            <dd><a href='/0_80/46439.html'>第二百七十五章 唐三左手，昊天锤（上）</a></dd>
            <dd><a href='/0_80/46441.html'>第二百七十六章 唐三左手，昊天锤（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46442.html'>第二百七十七章 唐三左手，昊天锤（下）</a></dd>
            <dd><a href='/0_80/46443.html'>第二百七十八章 身世之谜与昊天斗罗（上）</a></dd>
            <dd><a href='/0_80/46444.html'>第二百七十九章 身世之谜与昊天斗罗（中）</a></dd>
            <dd><a href='/0_80/46445.html'>第二百八十章 身世之谜与昊天斗罗（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46446.html'>第二百八十一章 双生武魂的奥秘（上）</a></dd>
            <dd><a href='/0_80/46447.html'>第二百八十二章 双生武魂的奥秘（中）</a></dd>
            <dd><a href='/0_80/46448.html'>第二百八十三章 双生武魂的奥秘（下）</a></dd>
            <dd><a href='/0_80/46449.html'>第二百八十四章 小舞：哥，替我梳头（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46450.html'>第二百八十五章 小舞：哥，替我梳头（中）</a></dd>
            <dd><a href='/0_80/46451.html'>第二百八十六章 小舞：哥，替我梳头（下）</a></dd>
            <dd><a href='/0_80/46452.html'>第二百八十七章 赤龙脚下的大地之王（上）</a></dd>
            <dd><a href='/0_80/46453.html'>第二百八十八章 赤龙脚下的大地之王（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46454.html'>第二百八十九章 赤龙脚下的大地之王（下）</a></dd>
            <dd><a href='/0_80/46455.html'>第二百九十章 ‘大地之王’与‘粉红娘娘’（上）</a></dd>
            <dd><a href='/0_80/46456.html'>第二百九十一章 ‘大地之王’与‘粉红娘娘’（中）</a></dd>
            <dd><a href='/0_80/46457.html'>第二百九十二章 ‘大地之王’与‘粉红娘娘’（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46458.html'>第二百九十三章 胖子的第四魂技，凤凰啸天击（上）</a></dd>
            <dd><a href='/0_80/46459.html'>第二百九十四章 胖子的第四魂技，凤凰啸天击（中）</a></dd>
            <dd><a href='/0_80/46460.html'>第二百九十五章 胖子的第四魂技，凤凰啸天击（下）</a></dd>
            <dd><a href='/0_80/46461.html'>第二百九十六章 幽香引魂兽（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46462.html'>第二百九十七章 幽香引魂兽（中）</a></dd>
            <dd><a href='/0_80/46464.html'>第二百九十八章 幽香引魂兽（下）</a></dd>
            <dd><a href='/0_80/46465.html'>第二百九十九章 千年麟甲兽与万年魔蛛(上)</a></dd>
            <dd><a href='/0_80/46466.html'>第三百章 千年麟甲兽与万年魔蛛(中)</a></dd>
        
    
    
            <dd><a href='/0_80/46467.html'>第三百零一章 千年麟甲兽与万年魔蛛(下)</a></dd>
            <dd><a href='/0_80/46468.html'>第三百零二章 万年地穴魔蛛(上)</a></dd>
            <dd><a href='/0_80/46469.html'>第三百零三章 万年地穴魔蛛(中)</a></dd>
            <dd><a href='/0_80/46470.html'>第三百零四章 万年地穴魔蛛(下)</a></dd>
        
    
    
            <dd><a href='/0_80/46471.html'>第三百零五章 吞噬，八蛛矛(上)</a></dd>
            <dd><a href='/0_80/46472.html'>第三百零六章 吞噬，八蛛矛(中)</a></dd>
            <dd><a href='/0_80/46473.html'>第三百零七章 吞噬，八蛛矛(下)</a></dd>
            <dd><a href='/0_80/46474.html'>第三百零八章 唐三的第四魂技(上)</a></dd>
        
    
    
            <dd><a href='/0_80/46476.html'>第三百零九章 唐三的第四魂技(中)</a></dd>
            <dd><a href='/0_80/46477.html'>第三百一十章 唐三的第四魂技(下)</a></dd>
            <dd><a href='/0_80/46478.html'>第三百一十一章 全大陆高级魂师学院精英大赛(上)</a></dd>
            <dd><a href='/0_80/46479.html'>第三百一十二章 全大陆高级魂师学院精英大赛(中)</a></dd>
        
    
    
            <dd><a href='/0_80/46480.html'>第三百一十三章 全大陆高级魂师学院精英大赛(下)</a></dd>
            <dd><a href='/0_80/46481.html'>第三百一十四章 预选赛第一场，开战(上)</a></dd>
            <dd><a href='/0_80/46482.html'>第三百一十五章 预选赛第一场，开战(中)</a></dd>
            <dd><a href='/0_80/46483.html'>第三百一十六章 预选赛第一场，开战（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46484.html'>第三百一十七章 一分钟的完胜（上）</a></dd>
            <dd><a href='/0_80/46485.html'>第三百一十八章 一分钟的完胜（中）</a></dd>
            <dd><a href='/0_80/46486.html'>第三百一十九章 一分钟的完胜（下）</a></dd>
            <dd><a href='/0_80/46487.html'>第三百二十章 唐昊退隐的原因(上)</a></dd>
        
    
    
            <dd><a href='/0_80/46488.html'>第三百二十一章 唐昊退隐的原因(中)</a></dd>
            <dd><a href='/0_80/46489.html'>第三百二十二章 唐昊退隐的原因(下)</a></dd>
            <dd><a href='/0_80/46490.html'>第三百二十三章 分心控制之三窍御之心(上)</a></dd>
            <dd><a href='/0_80/46491.html'>第三百二十四章 分心控制之三窍御之心(中)</a></dd>
        
    
    
            <dd><a href='/0_80/46492.html'>第三百二十五章 分心控制之三窍御之心(下)</a></dd>
            <dd><a href='/0_80/46493.html'>第三百二十六章 唐三的新战术，宇宙天空流(上)</a></dd>
            <dd><a href='/0_80/46494.html'>第三百二十七章 唐三的新战术，宇宙天空流(中)</a></dd>
            <dd><a href='/0_80/46495.html'>第三百二十八章 唐三的新战术，宇宙天空流(下)</a></dd>
        
    
    
            <dd><a href='/0_80/46496.html'>第三百二十九章 极限团控与恐怖的幽冥白虎(上)</a></dd>
            <dd><a href='/0_80/46497.html'>第三百三十章 极限团控与恐怖的幽冥白虎(中)</a></dd>
            <dd><a href='/0_80/46498.html'>第三百三十一章 极限团控与恐怖的幽冥白虎(下)</a></dd>
            <dd><a href='/0_80/46500.html'>第三百三十二章 魂师界的极限流与均衡流（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46501.html'>第三百三十三章 魂师界的极限流与均衡流（中）</a></dd>
            <dd><a href='/0_80/46502.html'>第三百三十四章 魂师界的极限流与均衡流（下）</a></dd>
            <dd><a href='/0_80/46503.html'>第三百三十五章 追魂夺命阎王帖（上）</a></dd>
            <dd><a href='/0_80/46504.html'>第三百三十六章 追魂夺命阎王帖（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46505.html'>第三百三十七章 追魂夺命阎王帖（下）</a></dd>
            <dd><a href='/0_80/46506.html'>第三百三十八章 又是一块魂骨（上）</a></dd>
            <dd><a href='/0_80/46507.html'>第三百三十九章 又是一块魂骨（中）</a></dd>
            <dd><a href='/0_80/46508.html'>第三百四十章 又是一块魂骨（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46509.html'>第三百四十一章 史莱克学院VS炽火学院（上）</a></dd>
            <dd><a href='/0_80/46510.html'>第三百四十二章 史莱克学院VS炽火学院（中）</a></dd>
            <dd><a href='/0_80/46511.html'>第三百四十三章 史莱克学院VS炽火学院（下）</a></dd>
            <dd><a href='/0_80/46512.html'>第三百四十四章 火免，蓝银草（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46513.html'>第三百四十五章 火免，蓝银草（中）</a></dd>
            <dd><a href='/0_80/46514.html'>第三百四十六章 火免，蓝银草（下）</a></dd>
            <dd><a href='/0_80/46515.html'>第三百四十七章 隐藏的奥秘，七宝石武魂（上）</a></dd>
            <dd><a href='/0_80/46516.html'>第三百四十八章 隐藏的奥秘，七宝石武魂（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46518.html'>第三百四十九章 隐藏的奥秘，七宝石武魂（下）</a></dd>
            <dd><a href='/0_80/46519.html'>第三百五十章 七位一体融合技（上）</a></dd>
            <dd><a href='/0_80/46520.html'>第三百五十一章 七位一体融合技（中）</a></dd>
            <dd><a href='/0_80/46521.html'>第三百五十二章 七位一体融合技（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46522.html'>第三百五十三章 一唱一和（上）</a></dd>
            <dd><a href='/0_80/46523.html'>第三百五十四章 一唱一和（中）</a></dd>
            <dd><a href='/0_80/46524.html'>第三百五十五章 一唱一和（下）</a></dd>
            <dd><a href='/0_80/46525.html'>第三百五十六章 武魂融合技，冰雪飘零（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46526.html'>第三百五十七章 武魂融合技，冰雪飘零（中）</a></dd>
            <dd><a href='/0_80/46527.html'>第三百五十八章 武魂融合技，冰雪飘零（下）</a></dd>
            <dd><a href='/0_80/46528.html'>第三百五十九章 冰雪飘零冰凤凰（上）</a></dd>
            <dd><a href='/0_80/46529.html'>第三百六十章 冰雪飘零冰凤凰（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46530.html'>第三百六十一章 冰雪飘零冰凤凰（下）</a></dd>
            <dd><a href='/0_80/46531.html'>第三百六十二章 真是普通的蓝银草么？（上）</a></dd>
            <dd><a href='/0_80/46532.html'>第三百六十三章 真是普通的蓝银草么？（中）</a></dd>
            <dd><a href='/0_80/46533.html'>第三百六十四章 真是普通的蓝银草么？（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46534.html'>第三百六十五章 豁然贯通（上）</a></dd>
            <dd><a href='/0_80/46535.html'>第三百六十六章 豁然贯通（中）</a></dd>
            <dd><a href='/0_80/46536.html'>第三百六十七章 豁然贯通（下）</a></dd>
            <dd><a href='/0_80/46537.html'>第三百六十八章 被算计的柳二龙（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46538.html'>第三百六十九章 被算计的柳二龙（中）</a></dd>
            <dd><a href='/0_80/46539.html'>第三百七十章 被算计的柳二龙（下）</a></dd>
            <dd><a href='/0_80/46540.html'>第三百七十一章 花中之王、君临群芳（上）</a></dd>
            <dd><a href='/0_80/46542.html'>第三百七十二章 花中之王、君临群芳（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46543.html'>第三百七十三章 花中之王、君临群芳（下）</a></dd>
            <dd><a href='/0_80/46544.html'>第三百七十四章 魂技与唐门绝学的融合（上）</a></dd>
            <dd><a href='/0_80/46545.html'>第三百七十五章 魂技与唐门绝学的融合（中）</a></dd>
            <dd><a href='/0_80/46546.html'>第三百七十六章 魂技与唐门绝学的融合（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46547.html'>第三百七十七章 唐三VS火舞（上）</a></dd>
            <dd><a href='/0_80/46548.html'>第三百七十八章 唐三VS火舞（中）</a></dd>
            <dd><a href='/0_80/46549.html'>第三百七十九章 唐三VS火舞（下）</a></dd>
            <dd><a href='/0_80/46550.html'>第三百八十章 凤凰的狂野（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46551.html'>第三百八十一章 凤凰的狂野（中）</a></dd>
            <dd><a href='/0_80/46552.html'>第三百八十二章 凤凰的狂野（下）</a></dd>
            <dd><a href='/0_80/46553.html'>第三百八十三章 火舞与小舞的吻(上)</a></dd>
            <dd><a href='/0_80/46554.html'>第三百八十四章 火舞与小舞的吻(中)</a></dd>
        
    
    
            <dd><a href='/0_80/46555.html'>第三百八十五章 火舞与小舞的吻(下)</a></dd>
            <dd><a href='/0_80/46556.html'>第三百八十六章 运筹帷幄，大师（上）</a></dd>
            <dd><a href='/0_80/46557.html'>第三百八十七章 运筹帷幄，大师（中）</a></dd>
            <dd><a href='/0_80/46558.html'>第三百八十八章 运筹帷幄，大师（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46559.html'>第三百八十九章 奇茸通天，虎破龙（上）</a></dd>
            <dd><a href='/0_80/46560.html'>第三百九十章 奇茸通天，虎破龙（中）</a></dd>
            <dd><a href='/0_80/46561.html'>第三百九十一章 奇茸通天，虎破龙（下）</a></dd>
            <dd><a href='/0_80/46562.html'>第三百九十二章 昊天锤，乱披风（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46563.html'>第三百九十三章 昊天锤，乱披风（中）</a></dd>
            <dd><a href='/0_80/46564.html'>第三百九十四章 昊天锤，乱披风（下）</a></dd>
            <dd><a href='/0_80/46565.html'>第三百九十五章 总决赛，武魂城(上)</a></dd>
            <dd><a href='/0_80/46566.html'>第三百九十六章 总决赛，武魂城(中)</a></dd>
        
    
    
            <dd><a href='/0_80/46567.html'>第三百九十七章 总决赛，武魂城(下)</a></dd>
            <dd><a href='/0_80/46569.html'>第三百九十八章 一个爱花的封号斗罗（上）</a></dd>
            <dd><a href='/0_80/46570.html'>第三百九十九章 一个爱花的封号斗罗（中）</a></dd>
            <dd><a href='/0_80/46571.html'>第四百章 一个爱花的封号斗罗（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46572.html'>第四百零一章 四个封号斗罗（上）</a></dd>
            <dd><a href='/0_80/46573.html'>第四百零二章 四个封号斗罗（中）</a></dd>
            <dd><a href='/0_80/46574.html'>第四百零三章 四个封号斗罗（下）</a></dd>
            <dd><a href='/0_80/46575.html'>第四百零四章 教皇比比东（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46576.html'>第四百零五章 教皇比比东（中）</a></dd>
            <dd><a href='/0_80/46577.html'>第四百零六章 教皇比比东（下）</a></dd>
            <dd><a href='/0_80/46578.html'>第四百零七章 星罗皇家学院战队（上）</a></dd>
            <dd><a href='/0_80/46579.html'>第四百零八章 星罗皇家学院战队（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46580.html'>第四百零九章 星罗皇家学院战队（下）</a></dd>
            <dd><a href='/0_80/46581.html'>第四百一十章 万年魂技的变异技能（上）</a></dd>
            <dd><a href='/0_80/46582.html'>第四百一十一章 万年魂技的变异技能（中）</a></dd>
            <dd><a href='/0_80/46583.html'>第四百一十二章 万年魂技的变异技能（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46584.html'>第四百一十三章 幽冥白虎的身世（上）</a></dd>
            <dd><a href='/0_80/46585.html'>第四百一十四章 幽冥白虎的身世（中）</a></dd>
            <dd><a href='/0_80/46587.html'>第四百一十五章 幽冥白虎的身世（下）</a></dd>
            <dd><a href='/0_80/46588.html'>第四百一十六章 震惊，七怪融合技（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46589.html'>第四百一十七章 震惊，七怪融合技（中）</a></dd>
            <dd><a href='/0_80/46590.html'>第四百一十八章 震惊，七怪融合技（下）</a></dd>
            <dd><a href='/0_80/46591.html'>第四百一十九章 器魂真身，暗金昊天锤（上）</a></dd>
            <dd><a href='/0_80/46592.html'>第四百二十章 器魂真身，暗金昊天锤（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46593.html'>第四百二十一章 器魂真身，暗金昊天锤（下）</a></dd>
            <dd><a href='/0_80/46594.html'>第四百二十二章 史莱克七怪完整的实力（上）</a></dd>
            <dd><a href='/0_80/46595.html'>第四百二十三章 史莱克七怪完整的实力（中）</a></dd>
            <dd><a href='/0_80/46596.html'>第四百二十四章 史莱克七怪完整的实力（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46597.html'>第四百二十五章 唐门第十，蝠翼轮回（上）</a></dd>
            <dd><a href='/0_80/46598.html'>第四百二十六章 唐门第十，蝠翼轮回（中）</a></dd>
            <dd><a href='/0_80/46599.html'>第四百二十七章 唐门第十，蝠翼轮回（下）</a></dd>
            <dd><a href='/0_80/46600.html'>第四百二十八章 小舞不是人（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46601.html'>第四百二十九章 小舞不是人（中）</a></dd>
            <dd><a href='/0_80/46602.html'>第四百三十章 小舞不是人（下）</a></dd>
            <dd><a href='/0_80/46603.html'>第四百三十一章 昊天扬威，新的开始（上）</a></dd>
            <dd><a href='/0_80/46604.html'>第四百三十二章 昊天扬威，新的开始（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46605.html'>第四百三十三章 昊天扬威，新的开始（下）</a></dd>
            <dd><a href='/0_80/46607.html'>第四百三十四章 智慧头骨之技，紫极神光（上）</a></dd>
            <dd><a href='/0_80/46608.html'>第四百三十五章 智慧头骨之技，紫极神光（中）</a></dd>
            <dd><a href='/0_80/46609.html'>第四百三十六章 智慧头骨之技，紫极神光（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46610.html'>第四百三十七章 八十一锤（上）</a></dd>
            <dd><a href='/0_80/46611.html'>第四百三十八章 八十一锤（中）</a></dd>
            <dd><a href='/0_80/46612.html'>第四百三十九章 八十一锤（下）</a></dd>
            <dd><a href='/0_80/46613.html'>第四百四十章 锤法大成，杀戮之气（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46614.html'>第四百四十一章 锤法大成，杀戮之气（中）</a></dd>
            <dd><a href='/0_80/46615.html'>第四百四十二章 锤法大成，杀戮之气（下）</a></dd>
            <dd><a href='/0_80/46616.html'>第四百四十三章 唐三武魂的真面目，蓝银皇（上）</a></dd>
            <dd><a href='/0_80/46617.html'>第四百四十四章 唐三武魂的真面目，蓝银皇（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46618.html'>第四百四十五章 唐三武魂的真面目，蓝银皇（下）</a></dd>
            <dd><a href='/0_80/46619.html'>第四百四十六章 杀戮之都（上）</a></dd>
            <dd><a href='/0_80/46620.html'>第四百四十七章 杀戮之都（中）</a></dd>
            <dd><a href='/0_80/46621.html'>第四百四十八章 杀戮之都（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46622.html'>第四百四十九章 地狱杀戮场（上）</a></dd>
            <dd><a href='/0_80/46623.html'>第四百五十章 地狱杀戮场（中）</a></dd>
            <dd><a href='/0_80/46624.html'>第四百五十一章 地狱杀戮场（下）</a></dd>
            <dd><a href='/0_80/46625.html'>第四百五十二章 杀戮之王（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46626.html'>第四百五十三章 杀戮之王（中）</a></dd>
            <dd><a href='/0_80/46627.html'>第四百五十四章 杀戮之王（下）</a></dd>
            <dd><a href='/0_80/46628.html'>第四百五十五章 血的祭奠，地狱路（上）</a></dd>
            <dd><a href='/0_80/46629.html'>第四百五十六章 血的祭奠，地狱路（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46630.html'>第四百五十七章 血的祭奠，地狱路（下）</a></dd>
            <dd><a href='/0_80/46631.html'>第四百五十八章 暗金三头蝙蝠王（上）</a></dd>
            <dd><a href='/0_80/46632.html'>第四百五十九章 暗金三头蝙蝠王（中）</a></dd>
            <dd><a href='/0_80/46633.html'>第四百六十章 暗金三头蝙蝠王（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46635.html'>第四百六十一章 十首烈阳蛇（上）</a></dd>
            <dd><a href='/0_80/46636.html'>第四百六十二章 十首烈阳蛇（中）</a></dd>
            <dd><a href='/0_80/46637.html'>第四百六十三章 十首烈阳蛇（下）</a></dd>
            <dd><a href='/0_80/46638.html'>第四百六十四章 蓝银领域与杀神领域（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46639.html'>第四百六十五章 蓝银领域与杀神领域（中）</a></dd>
            <dd><a href='/0_80/46640.html'>第四百六十六章 蓝银领域与杀神领域（下）</a></dd>
            <dd><a href='/0_80/46641.html'>第四百六十七章 月轩、姑姑（上）</a></dd>
            <dd><a href='/0_80/46642.html'>第四百六十八章 月轩、姑姑（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46643.html'>第四百六十九章 月轩、姑姑（下）</a></dd>
            <dd><a href='/0_80/46644.html'>第四百七十章 铅华洗尽，圆融如意（上）</a></dd>
            <dd><a href='/0_80/46645.html'>第四百七十一章 铅华洗尽，圆融如意（中）</a></dd>
            <dd><a href='/0_80/46646.html'>第四百七十二章 铅华洗尽，圆融如意（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46647.html'>第四百七十三章 唐三的母亲，十万年蓝银皇（上）</a></dd>
            <dd><a href='/0_80/46648.html'>第四百七十四章 唐三的母亲，十万年蓝银皇（中）</a></dd>
            <dd><a href='/0_80/46649.html'>第四百七十五章 唐三的母亲，十万年蓝银皇（下）</a></dd>
            <dd><a href='/0_80/46650.html'>第四百七十六章 母亲的遗物，蓝银皇右腿骨（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46651.html'>第四百七十七章 母亲的遗物，蓝银皇右腿骨（中）</a></dd>
            <dd><a href='/0_80/46652.html'>第四百七十八章 母亲的遗物，蓝银皇右腿骨（下）</a></dd>
            <dd><a href='/0_80/46653.html'>第四百七十九章 回归昊天宗（上）</a></dd>
            <dd><a href='/0_80/46654.html'>第四百八十章 回归昊天宗（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46655.html'>第四百八十一章 回归昊天宗（下）</a></dd>
            <dd><a href='/0_80/46656.html'>第四百八十二章 啸天斗罗（上）</a></dd>
            <dd><a href='/0_80/46657.html'>第四百八十三章 啸天斗罗（中）</a></dd>
            <dd><a href='/0_80/46658.html'>第四百八十四章 啸天斗罗（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46659.html'>第四百八十五章 蓝银皇的霸道控制力（上）</a></dd>
            <dd><a href='/0_80/46661.html'>第四百八十六章 蓝银皇的霸道控制力（中）</a></dd>
            <dd><a href='/0_80/46662.html'>第四百八十七章 蓝银皇的霸道控制力（下）</a></dd>
            <dd><a href='/0_80/46663.html'>第四百八十八章 第五魂技，蓝银霸王枪（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46664.html'>第四百八十九章 第五魂技，蓝银霸王枪（中）</a></dd>
            <dd><a href='/0_80/46665.html'>第四百九十章 第五魂技，蓝银霸王枪（下）</a></dd>
            <dd><a href='/0_80/46666.html'>第四百九十一章 虚空鬼影迷踪（上）</a></dd>
            <dd><a href='/0_80/46667.html'>第四百九十二章 虚空鬼影迷踪（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46668.html'>第四百九十三章 虚空鬼影迷踪（下）</a></dd>
            <dd><a href='/0_80/46669.html'>第四百九十四章 史莱克，再聚首（上）</a></dd>
            <dd><a href='/0_80/46670.html'>第四百九十五章 史莱克，再聚首（中）</a></dd>
            <dd><a href='/0_80/46671.html'>第四百九十六章 史莱克，再聚首（下）</a></dd>
        
    
    
            <dd><a href='/0_80/46672.html'>第四百九十七章 五年来的变化（上）</a></dd>
            <dd><a href='/0_80/46673.html'>第四百九十八章 五年来的变化（中）</a></dd>
            <dd><a href='/0_80/46674.html'>第四百九十九章 五年来的变化（下）</a></dd>
            <dd><a href='/0_80/46675.html'>第五百章 奥斯卡的第六魂环（上）</a></dd>
        
    
    
            <dd><a href='/0_80/46676.html'>第五百零一章 奥斯卡的第六魂环（中）</a></dd>
            <dd><a href='/0_80/46677.html'>第五百零二章 奥斯卡的第六魂环（下）</a></dd>
            <dd><a href='/0_80/46678.html'>第五百零三章 蓝银领域真正的威力（上）</a></dd>
            <dd><a href='/0_80/46679.html'>第五百零四章 蓝银领域真正的威力（中）</a></dd>
        
    
    
            <dd><a href='/0_80/46680.html'>第五百零五章 蓝银领域真正的威力（下）</a></dd>
            <dd><a href='/0_80/46681.html'>第五百零六章 魂斗罗级别的碰撞</a></dd>
            <dd><a href='/0_80/46682.html'>第五百零七章 猎魂，灭门</a></dd>
            <dd><a href='/0_80/46683.html'>第五百零八章 再遇胡列娜</a></dd>
        
    
    
            <dd><a href='/0_80/46684.html'>第五百零九章 成功潜伏</a></dd>
            <dd><a href='/0_80/46686.html'>第五百一十章 小舞，我的爱人，终再相见</a></dd>
            <dd><a href='/0_80/46687.html'>第五百一十一章 森林死战</a></dd>
            <dd><a href='/0_80/46688.html'>第五百一十二章 同样的命运，唐三的十万年魂环</a></dd>
        
    
    
            <dd><a href='/0_80/46689.html'>第五百一十三章 复活的希望</a></dd>
            <dd><a href='/0_80/46690.html'>第五百一十四章 进化，八蛛矛</a></dd>
            <dd><a href='/0_80/46691.html'>第五百一十五章 皇室秘辛</a></dd>
            <dd><a href='/0_80/46692.html'>第五百一十六章 八蛛矛进化铠甲的缘由</a></dd>
        
    
    
            <dd><a href='/0_80/46693.html'>第五百一十七章 奥斯卡归来，复制镜像肠</a></dd>
            <dd><a href='/0_80/46694.html'>第五百一十八章 奥斯卡，宁荣荣</a></dd>
            <dd><a href='/0_80/46695.html'>第五百一十九章 唐门，力之一族</a></dd>
            <dd><a href='/0_80/46696.html'>第五百二十章 单属性四大宗族</a></dd>
        
    
    
            <dd><a href='/0_80/46697.html'>第五百二十一章 猥琐三贱客</a></dd>
            <dd><a href='/0_80/46698.html'>第五百二十二章 御之一族</a></dd>
            <dd><a href='/0_80/46700.html'>第五百二十三章 对阵，与板甲巨犀比防御</a></dd>
            <dd><a href='/0_80/46701.html'>第五百二十四章 破防，乱披风之威</a></dd>
        
    
    
            <dd><a href='/0_80/46702.html'>第五百二十五章 御之一族入唐门</a></dd>
            <dd><a href='/0_80/46703.html'>第五百二十六章 鬼影迷踪斗纯敏</a></dd>
            <dd><a href='/0_80/46704.html'>第五百二十七章 唐三的第六魂技，小舞现身</a></dd>
            <dd><a href='/0_80/46705.html'>第五百二十八章 水晶血龙参</a></dd>
        
    
    
            <dd><a href='/0_80/46706.html'>第五百二十九章 唐三VS杨无敌</a></dd>
            <dd><a href='/0_80/46707.html'>第五百三十章 唐三第六魂技：虚无、爆杀八段摔</a></dd>
            <dd><a href='/0_80/46708.html'>第五百三十一章 复活，小舞，二分之一</a></dd>
            <dd><a href='/0_80/46709.html'>第五百三十二章 五年的差距，一挑三</a></dd>
        
    
    
            <dd><a href='/0_80/46710.html'>第五百三十三章 四元素学院的来意</a></dd>
            <dd><a href='/0_80/46711.html'>第五百三十四章 金属之都庚辛城</a></dd>
            <dd><a href='/0_80/46712.html'>第五百三十五章 神匠楼高</a></dd>
            <dd><a href='/0_80/46713.html'>第五百三十六章 真的滚出去了</a></dd>
        
    
    
            <dd><a href='/0_80/46715.html'>第五百三十七章 寒心铁精与深海沉银</a></dd>
            <dd><a href='/0_80/46716.html'>第五百三十八章 月黑风高杀人夜</a></dd>
            <dd><a href='/0_80/46717.html'>第五百三十九掌 神器，八宝如意软甲</a></dd>
            <dd><a href='/0_80/46718.html'>第五百四十章 唐门五堂</a></dd>
        
    
    
            <dd><a href='/0_80/46719.html'>第五百四十一章 宫闱，惊变，敌影现</a></dd>
            <dd><a href='/0_80/46720.html'>第五百四十二章 刺豚、蛇矛、破魂枪</a></dd>
            <dd><a href='/0_80/46721.html'>第五百四十三章 杀神领域VS天使领域</a></dd>
            <dd><a href='/0_80/46722.html'>第五百四十四章 自创魂技，乱披风之舞</a></dd>
        
    
    
            <dd><a href='/0_80/46723.html'>第五百四十五章 小舞，复活，四分之一</a></dd>
            <dd><a href='/0_80/46724.html'>第五百四十六章 六块，魂骨，天使神装</a></dd>
            <dd><a href='/0_80/46725.html'>第五百四十七章 九十九级的封号斗罗</a></dd>
            <dd><a href='/0_80/46726.html'>第五百四十八章 魔鬼岛？海神岛？</a></dd>
        
    
    
            <dd><a href='/0_80/46727.html'>第五百四十九章 三位绝世斗罗的来历</a></dd>
            <dd><a href='/0_80/46728.html'>第五百五十章 唐三和小舞的幸福，订婚</a></dd>
            <dd><a href='/0_80/46729.html'>第五百五十一章 重聚，史莱克七怪</a></dd>
            <dd><a href='/0_80/46731.html'>第五百五十二章 镇国之宝赠唐三，瀚海乾坤罩</a></dd>
        
    
    
            <dd><a href='/0_80/46732.html'>第五百五十三章 瀚海乾坤罩</a></dd>
            <dd><a href='/0_80/46733.html'>第五百五十四章 暗影猎手</a></dd>
            <dd><a href='/0_80/46734.html'>第五百五十五章 唐门第四，一千零一夜</a></dd>
            <dd><a href='/0_80/46735.html'>第五百五十六章 嗜血狂化之飓风右腿</a></dd>
        
    
    
            <dd><a href='/0_80/46736.html'>第五百五十七章 瀚海大斗魂场</a></dd>
            <dd><a href='/0_80/46737.html'>第五百五十八章 不要崇拜哥，哥只是个传说</a></dd>
            <dd><a href='/0_80/46738.html'>第五百五十九章 海上旖旎</a></dd>
            <dd><a href='/0_80/46739.html'>第五百六十章 魔鲸海域</a></dd>
        
    
    
            <dd><a href='/0_80/46740.html'>第五百六十一章 超级十万年，海中霸主</a></dd>
            <dd><a href='/0_80/46741.html'>第五百六十二章 险死还生、塞翁失马</a></dd>
            <dd><a href='/0_80/46742.html'>第五百六十三章 神医拜师</a></dd>
            <dd><a href='/0_80/46743.html'>第五百六十四章 火辣辣的紫珍珠</a></dd>
        
    
    
            <dd><a href='/0_80/46744.html'>第五百六十五章</a></dd>
            <dd><a href='/0_80/46746.html'>第五百六十六章 供奉海神的海神岛</a></dd>
            <dd><a href='/0_80/46747.html'>第五百六十七章 避水乾坤罩</a></dd>
            <dd><a href='/0_80/46748.html'>第五百六十八章 海马圣柱，黑级六考</a></dd>
        
    
    
            <dd><a href='/0_80/46749.html'>第五百六十九章 顶级七考与黄级一考</a></dd>
            <dd><a href='/0_80/46750.html'>第五百七十章 海神九考，三叉戟烙印</a></dd>
            <dd><a href='/0_80/46751.html'>第五百七十一章 海神之光</a></dd>
            <dd><a href='/0_80/46752.html'>第五百七十二章 海神之光的奥秘</a></dd>
        
    
    
            <dd><a href='/0_80/46753.html'>第五百七十三章 神赐魂环</a></dd>
            <dd><a href='/0_80/46754.html'>第五百七十四章 天使与罗刹</a></dd>
            <dd><a href='/0_80/46755.html'>第五百七十五章 十万年，唐三的第七魂环</a></dd>
            <dd><a href='/0_80/46756.html'>第五百七十六章 穿越，海神之光</a></dd>
        
    
    
            <dd><a href='/0_80/46757.html'>第五百七十七章 穿越，双倍，海神之光</a></dd>
            <dd><a href='/0_80/46758.html'>第五百七十八章 唐三的底牌，进化的杀神领域之技</a></dd>
            <dd><a href='/0_80/46759.html'>第五百七十九章 奥斯卡猥琐的第七魂技</a></dd>
            <dd><a href='/0_80/46760.html'>第五百八十章 十万年，魔魂大白鲨之王</a></dd>
        
    
    
            <dd><a href='/0_80/46761.html'>第五百八十一章 莽撞的魔魂大白鲨之王</a></dd>
            <dd><a href='/0_80/46763.html'>第五百八十二章 邪火凤凰的武魂真身</a></dd>
            <dd><a href='/0_80/46764.html'>第五百八十三章 七首火凤凰</a></dd>
            <dd><a href='/0_80/46765.html'>第五百八十四章 凤凰领域</a></dd>
        
    
    
            <dd><a href='/0_80/46766.html'>第五百八十五章 第三考，潮汐炼体</a></dd>
            <dd><a href='/0_80/46767.html'>第五百八十六章 紫极魔瞳的最终境界，浩瀚</a></dd>
            <dd><a href='/0_80/46768.html'>第五百八十七章 第四考，鲨鲸之战</a></dd>
            <dd><a href='/0_80/46769.html'>第五百八十八章 巧杀邪魔虎鲸</a></dd>
        
    
    
            <dd><a href='/0_80/46770.html'>第五百八十九章 唐三的第八魂环</a></dd>
            <dd><a href='/0_80/46771.html'>第五百九十章 十万年邪魔左腿骨</a></dd>
            <dd><a href='/0_80/46772.html'>第五百九十一章 第五考，挑战，封号斗罗</a></dd>
            <dd><a href='/0_80/46773.html'>第五百九十二章 海马圣柱之战</a></dd>
        
    
    
            <dd><a href='/0_80/46774.html'>第五百九十三章 控制！邪眸白虎VS海之矛</a></dd>
            <dd><a href='/0_80/46776.html'>第五百九十四章 再现，小舞献祭的时刻</a></dd>
            <dd><a href='/0_80/46777.html'>第五百九十五章 挑战，海星圣柱</a></dd>
            <dd><a href='/0_80/46778.html'>第五百九十六章 海魔女，人鱼公主？</a></dd>
        
    
    
            <dd><a href='/0_80/46779.html'>第五百九十七章 进化十万年，唐三的第五魂环</a></dd>
            <dd><a href='/0_80/46780.html'>第五百九十八章 海龙斗罗</a></dd>
            <dd><a href='/0_80/46781.html'>第五百九十九章 控鹤擒龙，昊天飞锤</a></dd>
            <dd><a href='/0_80/46782.html'>第六百章 第六考，海神斗罗的攻击</a></dd>
        
    
    
            <dd><a href='/0_80/46783.html'>第六百零一章 海神斗罗，无限接近于神的实力</a></dd>
            <dd><a href='/0_80/46784.html'>第六百零二章 借势过关，冲破，第六考</a></dd>
            <dd><a href='/0_80/46785.html'>第六百零三章 海神神诋，成神之路</a></dd>
            <dd><a href='/0_80/46786.html'>第六百零四章 拔出，神器，海神的三叉戟</a></dd>
        
    
    
            <dd><a href='/0_80/46787.html'>第六百零五章 海神三叉戟，重十万八千斤</a></dd>
            <dd><a href='/0_80/46788.html'>第六百零六章 四年来的收获与分别</a></dd>
            <dd><a href='/0_80/46789.html'>第六百零七章 武魂帝国</a></dd>
            <dd><a href='/0_80/46791.html'>第六百零八章 海神三叉戟之威</a></dd>
        
    
    
            <dd><a href='/0_80/46792.html'>第六百零九章 再现，杀戮之王</a></dd>
            <dd><a href='/0_80/46793.html'>第六百一十章 杀戮之王？曾祖？</a></dd>
            <dd><a href='/0_80/46794.html'>第六百一十一章 两大神兽的危机</a></dd>
            <dd><a href='/0_80/46795.html'>第六百一十二章 唐三与比比东的第一次交手</a></dd>
        
    
    
            <dd><a href='/0_80/46796.html'>第六百一十三章 海神的技能，黄金十三戟</a></dd>
            <dd><a href='/0_80/46797.html'>第六百一十四章 献祭！森林之王，唐三九环</a></dd>
            <dd><a href='/0_80/46798.html'>第六百一十五章 复活之地，落日森林</a></dd>
            <dd><a href='/0_80/46799.html'>第六百一十六章 复活吧，我的爱人</a></dd>
        
    
    
            <dd><a href='/0_80/46800.html'>第六百一十七章 蓝银领域之终极进化，海纳百川</a></dd>
            <dd><a href='/0_80/46801.html'>第六百一十八章 送上门来的大礼</a></dd>
            <dd><a href='/0_80/46802.html'>第六百一十九章 铁汉柔情</a></dd>
            <dd><a href='/0_80/46803.html'>第六百二十章 重返昊天宗</a></dd>
        
    
    
            <dd><a href='/0_80/46804.html'>第六百二十一章 泰坦苍穹破与天青迟钝神爪</a></dd>
            <dd><a href='/0_80/46805.html'>第六百二十二章 宗门首席，昊天令</a></dd>
            <dd><a href='/0_80/46806.html'>第六百二十三章 神匠遗物，绝世暗器</a></dd>
            <dd><a href='/0_80/46807.html'>第六百二十四章 唐家军，九十三级，帝师</a></dd>
        
    
    
            <dd><a href='/0_80/46808.html'>第六百二十五章 天斗大军</a></dd>
            <dd><a href='/0_80/46809.html'>第六百二十六章 七怪，守护，补给线</a></dd>
            <dd><a href='/0_80/46811.html'>第六百二十七章 唐三的第九魂技</a></dd>
            <dd><a href='/0_80/46812.html'>第六百二十八章 天青寂灭雷霆</a></dd>
        
    
    
            <dd><a href='/0_80/46813.html'>第六百二十九章 再战比比东，唐家军初显威</a></dd>
            <dd><a href='/0_80/46814.html'>第六百三十章 紫极魔瞳之修罗魔光</a></dd>
            <dd><a href='/0_80/46815.html'>第六百三十一章 计定总攻</a></dd>
            <dd><a href='/0_80/46816.html'>第六百三十二章 一个人的战场</a></dd>
        
    
    
            <dd><a href='/0_80/46817.html'>第六百三十三章 唐门绝顶，佛怒唐莲</a></dd>
            <dd><a href='/0_80/46818.html'>第六百三十四章 六大供奉，巅峰斗罗</a></dd>
            <dd><a href='/0_80/46819.html'>第六百三十五章 击溃，九十六级的供奉兄弟</a></dd>
            <dd><a href='/0_80/46820.html'>第六百三十六章 真正的昊天锤，完全状态的昊天斗罗</a></dd>
        
    
    
            <dd><a href='/0_80/46821.html'>第六百三十七章 昊天宗神技，大须弥锤</a></dd>
            <dd><a href='/0_80/46822.html'>第六百三十八章 天使第九考，传承神诋</a></dd>
            <dd><a href='/0_80/46823.html'>第六百三十九章 邪神附体之暗魔邪神虎</a></dd>
            <dd><a href='/0_80/46824.html'>第六百四十章 聪明绝顶的超级魂兽</a></dd>
        
    
    
            <dd><a href='/0_80/46825.html'>第六百四十一章 返老还童之战，昊天锤第四魂环</a></dd>
            <dd><a href='/0_80/46826.html'>第六百四十二章 神级进化，八蛛矛</a></dd>
            <dd><a href='/0_80/46827.html'>第六百四十三章 九万年！千钧蚁皇三兄弟</a></dd>
            <dd><a href='/0_80/46828.html'>第六百四十四章 昆虫魂兽的克星，神级八蛛矛</a></dd>
        
    
    
            <dd><a href='/0_80/46829.html'>第六百四十五章 宁为玉碎，不为瓦全</a></dd>
            <dd><a href='/0_80/46830.html'>第六百四十六章 神级天使第一战</a></dd>
            <dd><a href='/0_80/46832.html'>第六百四十七章 第十魂环，神级魂环</a></dd>
            <dd><a href='/0_80/46833.html'>第六百四十八章 大须弥锤之奥义：炸环</a></dd>
        
    
    
            <dd><a href='/0_80/46834.html'>第六百四十九章 绝对压制，大须弥昊天锤</a></dd>
            <dd><a href='/0_80/46835.html'>第六百五十章 唐门第一，观音有泪</a></dd>
            <dd><a href='/0_80/46836.html'>第六百五十一章 太阳圣剑</a></dd>
            <dd><a href='/0_80/46837.html'>第六百五十二章 大地中的神级追杀</a></dd>
        
    
    
            <dd><a href='/0_80/46838.html'>第六百五十三章 海神降临</a></dd>
            <dd><a href='/0_80/46839.html'>第六百五十四章 目标，深海魔鲸王</a></dd>
            <dd><a href='/0_80/46840.html'>第六百五十五章 战斗吧！深海魔鲸王</a></dd>
            <dd><a href='/0_80/46841.html'>第六百五十六章 一线之差的神，百万年魂兽</a></dd>
        
    
    
            <dd><a href='/0_80/46842.html'>第六百五十七章 唐三VS深海魔鲸王</a></dd>
            <dd><a href='/0_80/46843.html'>第六百五十八章 灭杀魔鲸王，变异的杀神领域</a></dd>
            <dd><a href='/0_80/46844.html'>第六百五十九章 百万年魂环与百万年魂骨</a></dd>
            <dd><a href='/0_80/46845.html'>第六百六十章 深海魔鲸王脑袋里的宝贝</a></dd>
        
    
    
            <dd><a href='/0_80/46846.html'>第六百六十一章 两个传承选择，海神还是修罗神？</a></dd>
            <dd><a href='/0_80/46847.html'>第六百六十二章 传承开始，献祭，海神斗罗</a></dd>
            <dd><a href='/0_80/46848.html'>第六百六十三章 海神与修罗神</a></dd>
            <dd><a href='/0_80/46850.html'>第六百六十四章 魂骨剥离，海神八翼</a></dd>
        
    
    
            <dd><a href='/0_80/46851.html'>第六百六十五章 爱之一字，心灵感应的救赎</a></dd>
            <dd><a href='/0_80/46852.html'>第六百六十六章 海神神装</a></dd>
            <dd><a href='/0_80/46853.html'>第六百六十七章 海神唐三</a></dd>
            <dd><a href='/0_80/46854.html'>第六百六十八章 海神VS天使神</a></dd>
        
    
    
            <dd><a href='/0_80/46855.html'>第六百六十九章 碧波、海神、无尽蔚蓝</a></dd>
            <dd><a href='/0_80/46856.html'>第六百七十章 食神与九彩神女</a></dd>
            <dd><a href='/0_80/46857.html'>第六百七十一章 七怪封号与复苏的修罗神之力</a></dd>
            <dd><a href='/0_80/46858.html'>第六百七十二章 小舞的选择，魔剑入体</a></dd>
        
    
    
            <dd><a href='/0_80/46859.html'>第六百七十三章 嘉陵关，双神降临</a></dd>
            <dd><a href='/0_80/46860.html'>第六百七十四章 绝世双神，决战万米之上</a></dd>
            <dd><a href='/0_80/46861.html'>第六百七十五章 超级版融合技，幽冥白虎</a></dd>
            <dd><a href='/0_80/46862.html'>第六百七十六章 六怪发威，兵临城下</a></dd>
        
    
    
            <dd><a href='/0_80/46863.html'>第六百七十七章 九宝无敌神光</a></dd>
            <dd><a href='/0_80/46864.html'>第六百七十八章 满城尽是绿幽幽</a></dd>
            <dd><a href='/0_80/46865.html'>第六百七十九章 太阳天使</a></dd>
            <dd><a href='/0_80/46866.html'>第六百八十章 罗刹神现</a></dd>
        
    
    
            <dd><a href='/0_80/46868.html'>第六百八十一章 天使与罗刹</a></dd>
            <dd><a href='/0_80/46869.html'>第六百八十二章 海神陨落</a></dd>
            <dd><a href='/0_80/46870.html'>第六百八十三章 完美融合之复活神光</a></dd>
            <dd><a href='/0_80/46871.html'>第六百八十四章 神魂归位，海神归来</a></dd>
        
    
    
            <dd><a href='/0_80/46872.html'>第六百八十五章 最终决战</a></dd>
            <dd><a href='/0_80/46873.html'>第六百八十六章 完美融合之双神战双神</a></dd>
            <dd><a href='/0_80/46874.html'>第二百三十六章 大结局，最后一个条件（全书完）</a></dd>
            
        
    
            </dl>
        </div>
    </div>
<script>list3();</script>
    <div class="footer" id="footer">
        <div class="footer_cont">
            <p>本站推荐：
                    
  <a href='https://www.x23us.us/131_131460/' target='_blank' title="大燕出家人">大燕出家人</a>、

  <a href='https://www.x23us.us/131_131424/' target='_blank' title="全民武魂：我以神文横推此世">全民武魂：我以神文横推此世</a>、

  <a href='https://www.x23us.us/131_131434/' target='_blank' title="诡秘之妖">诡秘之妖</a>、

  <a href='https://www.x23us.us/131_131441/' target='_blank' title="临姜纪">临姜纪</a>、

  <a href='https://www.x23us.us/131_131417/' target='_blank' title="女儿上节目谴责我，武神身份曝光">女儿上节目谴责我，武神身份曝光</a>、

  <a href='https://www.x23us.us/131_131409/' target='_blank' title="玄幻三国：开局桃园四结义">玄幻三国：开局桃园四结义</a>、

  <a href='https://www.x23us.us/131_131439/' target='_blank' title="无勉传说">无勉传说</a>、

  <a href='https://www.x23us.us/131_131445/' target='_blank' title="九指剑尊">九指剑尊</a>、

  <a href='https://www.x23us.us/131_131425/' target='_blank' title="猪人的野望">猪人的野望</a>、

            </p>
            <p>《斗罗大陆》所有内容均来自互联网或网友上传，顶点小说只为原作者唐家三少的小说进行宣传。欢迎各位书友支持唐家三少并收藏《斗罗大陆》最新章节。</p>
            <script type="text/javascript">
                FooterTip();
            </script>
        </div>
    </div>
    <script>
        bd_push();
        addvisit("80");
        BDShare.js();
    </script>
</body>
</html>
"""

# pattern = r"""<dd><a href='/0_80/\d+.html'>(第.*?)</a></dd>"""
#
# title_list = re.findall(pattern, sss)
# print(title_list)
# for title in title_list:
#     print(title)

# https://www.x23us.us/0_80/46345.html
# https://www.x23us.us/0_80/46359.html

url_pattern = r"""<a href='(/0_80/\d+.html)'>"""

url_list = re.findall(url_pattern, sss)
for url in url_list:
    print('https://www.x23us.us' + url)