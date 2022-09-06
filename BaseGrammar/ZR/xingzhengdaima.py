# -*- encoding:utf-8 -*-


import re



get_xzdm = '''
<!DOCTYPE html>
<!--STATUS OK-->
<html style="">



<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=Edge" />
<meta name="referrer" content="always" />
<meta name="description" content="行政区划是国家为便于行政管理而分级划分的区域。因此，行政区划亦称行政区域。中华人民共和国的行政区划由省级行政区、地级行政区、县级行政区、乡级行政区组成。具体情况如下：省级行政区：23个省、5个自治区、4个直辖市、2个特别行政区，合计34个省级行政区。地级行政区：293个地级市、7个地区、30个自治州、3个盟，合计333个地级区划。县级行政区：977个市辖区、1303个县、393个县级市、117个自治县、49个旗、3个自治旗、1个特区、1个林区，合计2844个。乡级行政区：8562个街道、20988个镇、8102个乡、966个民族乡、153个苏木、1个民族苏木、2个县辖区，合计38774个。">
<title>中华人民共和国行政区划_百度百科</title>
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
<link rel="icon" sizes="any" mask href="//baikebcs.bdimg.com/cms/static/baike-icon.svg">

<meta name="csrf-token" content="d4b87f38b35a5e84f28e8674b41132db">
<meta itemprop="dateUpdate" content="2022-06-30 13:36:34" />
<meta name="keywords" content="中华人民共和国行政区划, 中华人民共和国行政区划具体区划, 中华人民共和国行政区划区划体制, 中华人民共和国行政区划区划沿革, 中华人民共和国行政区划管理规定">
<link rel="alternate" hreflang="x-default" href="https://baike.baidu.com/item/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734" />
<link rel="alternate" hreflang="zh" href="https://baike.baidu.com/item/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734" />
<link rel="alternate" hreflang="zh-Hans" href="https://baike.baidu.com/item/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734" />
<link rel="alternate" hreflang="zh-Hant" href="https://baike.baidu.hk/item/%E4%B8%AD%E8%8F%AF%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9C%8B%E8%A1%8C%E6%94%BF%E5%8D%80%E5%8A%83/1292734" />
<link rel="canonical" href="https://baike.baidu.com/item/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734" />
<meta name="image" content="https://bkimg.cdn.bcebos.com/smart/71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4-bkimg-process,v_1,rw_1,rh_1,pad_1,color_ffffff?x-bce-process=image/format,f_auto" />
<meta property="og:title" content="中华人民共和国行政区划_百度百科" />
<meta property="og:description" content="行政区划是国家为便于行政管理而分级划分的区域。因此，行政区划亦称行政区域。中华人民共和国的行政区划由省级行政区、地级行政区、县级行政区、乡级行政区组成。具体情况如下：省级行政区：23个省、5个自治区、4个直辖市、2个特别行政区，合计34个省级行政区。地级行政区：293个地级市、7个地区、30个自治州、3个盟，合计333个地级区划。县级行政区：977个市辖区、1303个县、393个县级市、117个自治县、49个旗、3个自治旗、1个特区、1个林区，合计2844个。乡级行政区：8562个街道、20988个镇、8102个乡、966个民族乡、153个苏木、1个民族苏木、2个县辖区，合计38774个。" />
<meta property="og:image" content="https://bkimg.cdn.bcebos.com/smart/71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4-bkimg-process,v_1,rw_1,rh_1,pad_1,color_ffffff?x-bce-process=image/format,f_auto" />
<meta property="og:url" content="https://baike.baidu.com/item/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734" />
<meta property="og:site_name" content="百度百科" />
<meta property="og:type" content="website" />
<style>
        . {
            display: none !important;
        }
    </style>
<script async>
    (function (d, s) {
        const js = d.createElement(s);
        const sc = d.getElementsByTagName(s)[0];

        js.src = 'https://dmpstatic.cdn.bcebos.com/weirwood-sdk/1/bundle.min.js';
        js.onload = function (params) {
            var defaultOptions = {
                common: {
                    buildid: 'wiki-lemma',
                    token: '3e75a217c52341299b3f0273ff6d2e07',
                    ignoreUrls: [
                        // 本地开发屏蔽错误发送
                        'localhost',
                        '127.0.0.1'
                    ]
                },
                error: {
                    collectWindowErrors: true,
                    collectUnhandledRejections: true
                },
                perf: {
                    // 性能数据PV日志会比较大，可以输入 sampleRate 进行采样，控制在 50 W左右
                    sampleRate: 0.019,
                    spa: true,
                    history: true
                }
            };
            /* globals Weirwood */
            Weirwood.init(defaultOptions);
        };
        sc.parentNode.insertBefore(js, sc);
    }(document, 'script'));
</script>

<!--[if lte IE 9]>
<script>
    (function() {
      var e = "abbr,article,aside,audio,canvas,datalist,details,dialog,eventsource,figure,footer,header,hgroup,mark,menu,meter,nav,output,progress,section,time,video".split(","),
        i = e.length;
      while (i--) {
        document.createElement(e[i]);
      }

      window.console = window.console || {};
      var f = ['log', 'info', 'warning', 'error', 'clear'];
      var l = f.length;
      while(l--) {
        window.console[f[l]] = function () {};
      }
    })();
  </script>
<![endif]-->
<link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/pkg/wiki-lemma_b25e69b.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/widget/lib/larkplayer/larkplayer_83ad94d.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/widget/lib/trumbowyg/plugins/colors/trumbowyg.colors_dd0d230.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/widget/lib/trumbowyg/trumbowyg_2e7ad35.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/widget/lib/watermark/watermark_a0a9ace.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/widget/lib/webuploader/webuploader_08d9db4.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-base_68f2f25.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/widget/component/userbar-n/userbar-n_be7e889.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/announcement/announcement_cba33f4.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/label/label_1b0bc0e.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/newSideShare/sideShare_7e089b7.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/video/pageMask/pageMask_ff9a193.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/pkg/wiki-lemma-module_404480a.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/pkg/vender-ui_d4defec.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/pkg/modules-second_11f7a89.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/pkg/components-videoPlayer_a974a96.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/mainContent_47f1933.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaRelation/lemmaRelation_496a30a.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/zhixin/zhixin_3b0d7a5.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/toolButtons-n/toolButtons-n_5841373.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/toolButtons-n/userInfo-n_7e90184.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/searchHeader-n_f9a6e5b.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/ui/index_e753a3d.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/generalAdvert/advertActivity/advertActivity_ed26fc8.css"/><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/generalAdvert/advertBaseInfo/advertBaseInfo_32e601e.css"/>    
</head>

<script>
        var _hmt = _hmt || [];
        (function() {
            var hm = document.createElement("script");
            hm.src = "https://hm.baidu.com/hm.js?55b574651fcae74b0a9f1cf9c8d7c93a";
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(hm, s);
        })();
    </script>

<body class="wiki-lemma neweditor normal">


<div class="header-wrapper pc-header-new">
<div style="display:none;" id="J-vars" data-lemmaid="1292734" data-lemmatitle="中华人民共和国行政区划" data-tk="d4b87f38b35a5e84f28e8674b41132db"></div>
<div class="topbar cmn-clearfix">
<ul class="wgt-userbar wgt-userbar-n" id="j-wgt-userbar">
<li>
<a href="http://www.baidu.com/">百度首页</a>
</li>
</ul>
<div class="separator"></div>
<div class="wiki-common-headTabBar">
<a href="https://www.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://www.baidu.com/s?ie=utf-8&fr=bks0000&wd=">网页</a>
<a href="http://news.baidu.com/" nslog="normal" nslog-type="10600112" data-href="http://news.baidu.com/ns?tn=news&cl=2&rn=20&ct=1&fr=bks0000&ie=utf-8&word=">新闻</a>
<a href="https://tieba.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://tieba.baidu.com/f?ie=utf-8&fr=bks0000&kw=">贴吧</a>
<a href="https://zhidao.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://zhidao.baidu.com/search?pn=0&&rn=10&lm=0&fr=bks0000&word=">知道</a>
<a href="https://pan.baidu.com?from=1027327l" nslog="normal" nslog-type="10600112" data-href="https://pan.baidu.com/disk/home#/search?from=1027327l&key=">网盘</a>
<a href="http://image.baidu.com/" nslog="normal" nslog-type="10600112" data-href="http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=">图片</a>
<a href="http://v.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://www.baidu.com/sf/vsearch?pd=video&tn=vsearch&ie=utf-8&rsv_spt=17&wd=">视频</a>
<a href="http://map.baidu.com/" nslog="normal" nslog-type="10600112" data-href="http://map.baidu.com/m?ie=utf-8&fr=bks0000&word=">地图</a>
<a href="https://wenku.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://wenku.baidu.com/search?lm=0&od=0&ie=utf-8&fr=bks0000&word=">文库</a>
<b class="baike">百科</b>
</div>
</div>
<div class="header">
<div class="layout">
<div class="wgt-searchbar wgt-searchbar-new wgt-searchbar-main cmn-clearfix wgt-searchbar-large">
<div class="logo-container">
<a class="logo cmn-inline-block" title="到百科首页" href="/">
<span class="cmn-baike-logo">
<em class="cmn-icon cmn-icons cmn-icons_logo-bai"></em>
<em class="cmn-icon cmn-icons cmn-icons_logo-du"></em>
<em class="cmn-icon cmn-icons cmn-icons_logo-baike"></em>
</span>
</a>
</div>
<div class="search">
<div class="form">
<form id="searchForm" action="/search/word" method="GET" target="_self">
<input id="query" nslog="normal" nslog-type="10080011" name="word" type="text" autocomplete="off" autocorrect="off" value="中华人民共和国行政区划" /><button id="search" nslog="normal" nslog-type="10080008" type="button">进入词条</button><button id="searchLemma" nslog="normal" nslog-type="10080009" type="button">全站搜索</button><a class="help" href="/help" nslog="normal" nslog-type="10080010" target="_blank">帮助</a>
</form>
<form id="searchLemmaForm" action="/search" method="GET" target="_self">
<input id="searchLemmaQuery" name="word" type="hidden" />
<input name="pn" type="hidden" value="0" />
<input name="rn" type="hidden" value="0" />
<input name="enc" type="hidden" value="utf8" />
</form>
<ul id="suggestion" class="suggestion">
<div class="sug"></div>
<li class="extra">
<span id="clear" style="margin-right:8px;">清除历史记录</span><span id="close" nslog="normal" nslog-type="10080012">关闭</span>
</li>
</ul>
</div></div>
</div>
<div class="declare-wrap" id="J-declare-wrap">
<div class="declare" id="J-declare">声明：百科词条人人可编辑，词条创建和修改均免费，绝不存在官方及代理商付费代编，请勿上当受骗。<a class="declare-details" target="_blank" href="/common/declaration">详情>></a>
<div class="close-btn" id="J-declare-close">
<em class="cmn-icon cmn-icons cmn-icons_close"></em>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="navbar-wrapper">
<div class="wgt-navbar">
<div class="navbar-bg">
<div class="navbar-bg-top">
<div class="navbar-content layout">
<div class="navbar-content-box">
<dl class="index ">
<dt><a href="/">首页</a></dt>
<dd>
<div><a href="/calendar/" target="_blank">历史上的今天</a></div>
<div><a href="/vbaike/" target="_blank">百科冷知识</a></div>
<div><a href="/vbaike#gallary" target="_blank">图解百科</a></div>
</dd>
</dl>
<dl class="second-know ">
<dt>秒懂百科</dt>
<dd>
<div><a href="https://child.baidu.com/" target="_blank">懂啦</a></div>
<div><a href="/item/秒懂本尊答" target="_blank">秒懂本尊答</a></div>
<div><a href="/item/秒懂大师说" target="_blank">秒懂大师说</a></div>
<div><a href="/item/秒懂看瓦特" target="_blank">秒懂看瓦特</a></div>
<div><a href="/item/秒懂五千年" target="_blank">秒懂五千年</a></div>
<div><a href="/item/秒懂全视界" target="_blank">秒懂全视界</a></div>
</dd>
</dl>
<dl class="special ">
<dt>特色百科</dt>
<dd>
<div><a href="/museum" target="_blank">数字博物馆</a></div>
<div><a href="/feiyi?fr=dhlfeiyi" target="_blank">非遗百科</a></div>
<div><a href="/wikicategory/view?categoryName=恐龙大全" target="_blank">恐龙百科</a></div>
<div><a href="/wikicategory/view?categoryName=多肉植物" target="_blank">多肉百科</a></div>
<div><a href="/art" target="_blank">艺术百科</a></div>
<div><a href="/science" target="_blank">科学百科</a></div>
</dd>
</dl>
<dl class="user ">
<dt>用户</dt>
<dd>
<div><a href="/kedou/" target="_blank">蝌蚪团</a></div>
<div><a href="/item/百科热词团队" target="_blank">热词团</a></div>
<div><a href="/campus" target="_blank">百科校园</a></div>
<div><a href="https://baike.baidu.com/talent/home/index" target="_blank">分类达人</a></div>
<div><a href="/task/" target="_blank">百科任务</a></div>
<div><a href="/mall/" target="_blank">百科商城</a></div>
</dd>
</dl>
<dl class="knowledge">
<dt>知识专题</dt>
<dd id="J-knowledge-content">
</dd>
</dl>
<dl class="cooperation ">
<dt>权威合作</dt>
<dd>
<div><a href="/operation/cooperation#joint" target="_blank">合作模式</a></div>
<div><a href="/operation/cooperation#issue" target="_blank">常见问题</a></div>
<div><a href="/operation/cooperation#connection" target="_blank">联系方式</a></div>
</dd>
</dl>
<div class="right-list">
<span class="item appdownload" nslog-type="21040001"><a href="/wapui/subpage/baikeappdownload?sfrom=pc_lemmapage_navigation" target="_blank"><em class="cmn-icon cmn-icons cmn-icons_mobile-phone"></em>下载百科APP</a></span>
<span class="item usercenter"><a href="/usercenter" target="_blank"><em class="cmn-icon cmn-icons cmn-icons_navbar-usercenter"></em>个人中心</a></span>
</div>
</div>
</div>
</div>
</div>
</div>
</div>


<div class="body-wrapper">
<div class="before-content">
</div>
<div class="content-wrapper">
<div class="content">
<div class="main-content J-content">
<div class="top-tool ">
<a class="add-sub-icon top-tool-icon" href="javascript:;" title="添加义项" nslog-type="50000101">
<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_add-subLemma-solid"></em>
</a>
<a href="/divideload/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92" title="拆分词条" target="_blank" class="split-icon top-tool-icon" style="display:none;" nslog-type="50000104">
<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lemma-split"></em>
</a>
<div class="top-collect top-tool-icon" nslog="area" nslog-type="50000102">
<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_star-solid"></em>
<span class="collect-text">收藏</span>
<div class="collect-tip">查看<a href="/uc/favolemma" target="_blank">我的收藏</a></div>
</div>
<a href="javascript:void(0);" id="j-top-vote" class="top-vote top-tool-icon" nslog-type="10060801">
<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_zan-solid"></em>
<span class="vote-count">0</span>
<span class="vote-tip">有用+1</span>
<span class="voted-tip">已投票</span>
</a><div class="bksharebuttonbox top-share">
<a class="top-share-icon top-tool-icon" nslog-type="9067">
<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_share"></em>
<span class="share-count" id="j-topShareCount">0</span>
</a>
<div class="new-top-share" id="top-share">
<ul class="top-share-list">
<li class="top-share-item">
<a class="share-link bds_qzone"  href="javascript:void(0);" nslog-type="10060501">
<em class="cmn-icon cmn-icons cmn-icons_logo-qzone"></em>
</a>
</li>
<li class="top-share-item">
<a class="share-link bds_tsina" href="javascript:void(0);" nslog-type="10060701">
<em class="cmn-icon cmn-icons cmn-icons_logo-sina-weibo"></em>
</a>
</li>
<li class="top-share-item">
<a class="bds_wechat"  href="javascript:void(0);" nslog-type="10060401">
<em class="cmn-icon cmn-icons cmn-icons_logo-wechat"></em>
</a>
</li>
<li class="top-share-item">
<a class="share-link bds_tqq"  href="javascript:void(0);" nslog-type="10060601">
<em class="cmn-icon cmn-icons cmn-icons_logo-qq"></em>
</a>
</li>
</ul>
</div>
</div>
</div>
<div style="width:0;height:0;clear:both"></div><dl class="lemmaWgt-lemmaTitle lemmaWgt-lemmaTitle-">
<dd class="lemmaWgt-lemmaTitle-title J-lemma-title">
<span class="long-title">
<h1 >中华人民共和国行政区划</h1>
</span>
<span class="btn-list">
<a class="cmn-btn-28 cmn-btn-hover-blue audio-play title-audio-play J-title-audio-play" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_voice-play"></em><span class="J-audio-text">播报</span></a>
<a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="lock-lemma" nslog-type="10003105" target="_blank" href="/view/10812319.htm" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
<a href="javascript:;" class="add-video cmn-btn-hover-blue cmn-btn-28 J-add-video-link J-add-video">
<em class="cmn-icon wiki-lemma-icons add-video-icon wiki-lemma-icons_add-video"></em>上传视频</a>
<a href="javascript:;" class="special-edit cmn-btn-hover-blue cmn-btn-28" id="J-special-edit">
<em class="cmn-icon wiki-lemma-icons special-edit-icon wiki-lemma-icons_special-edit"></em>特型编辑</a>
</span>
</dd>
<div class="lemma-desc">中华人民共和国宪法规定的行政区划</div>
</dl>
<div class="promotion-declaration">
</div><div class="lemma-summary" label-module="lemmaSummary">
<div class="para" label-module="para"><span class="ref" data-ctrid="sBMMaaf90O9X"><a target=_blank href="/item/%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/4655526" data-lemmaid="4655526">行政区划</a></span><span class="ref" data-ctrid="sBMMaaf90O9X">是国家为便于行政管理而分级划分的区域。因此</span><sup class="sup--normal" data-sup="2" data-ctrmap=":2,">
[2]</sup><a class="sup-anchor" name="ref_[2]_71418">&nbsp;</a>
<span class="ref" data-ctrid="sBMMaaf90O9X">，行政区划亦称行政区域。</span><sup class="sup--normal" data-sup="7" data-ctrmap="sBMMaaf90O9X:7,">
[7]</sup><a class="sup-anchor" name="ref_[7]_71418">&nbsp;</a>
<a target=_blank href="/item/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD/106554" data-lemmaid="106554">中华人民共和国</a>的行政区划由省级行政区、地级行政区、县级行政区、乡级行政区组成。具体情况如下：</div><div class="para" label-module="para"><b><a target=_blank href="/item/%E7%9C%81%E7%BA%A7%E8%A1%8C%E6%94%BF%E5%8C%BA/4805340" data-lemmaid="4805340">省级行政区</a></b><b>：</b>23个省、5个自治区、4个直辖市、2个特别行政区，合计34个省级行政区。</div><div class="para" label-module="para"><b><a target=_blank href="/item/%E5%9C%B0%E7%BA%A7%E8%A1%8C%E6%94%BF%E5%8C%BA/5628580" data-lemmaid="5628580">地级行政区</a></b><b>：</b>293个地级市、7个地区、30个自治州、3个盟，合计333个地级区划。</div><div class="para" label-module="para"><b><a target=_blank href="/item/%E5%8E%BF%E7%BA%A7%E8%A1%8C%E6%94%BF%E5%8C%BA/1660163" data-lemmaid="1660163">县级行政区</a></b><b>：</b>977个市辖区、1303个县、393个县级市、117个自治县<sup class="sup--normal" data-sup="10" data-ctrmap=":10,">
[10]</sup><a class="sup-anchor" name="ref_[10]_71418">&nbsp;</a>
、49个旗、3个自治旗、1个特区、1个林区，合计2844个。</div><div class="para" label-module="para"><b><a target=_blank href="/item/%E4%B9%A1%E7%BA%A7%E8%A1%8C%E6%94%BF%E5%8C%BA/8466613" data-lemmaid="8466613">乡级行政区</a></b><b>：</b>8562个街道、20988个镇、8102个乡、966个民族乡、153个苏木、1个民族苏木、2个县辖区<sup class="sup--normal" data-sup="10" data-ctrmap=":10,">
[10]</sup><a class="sup-anchor" name="ref_[10]_71418">&nbsp;</a>
，合计38774个。</div>
</div>
<div class="lemmaWgt-promotion-leadPVBtn">
</div><div class="configModuleBanner">
</div><div class="basic-info J-basic-info cmn-clearfix">
<dl class="basicInfo-block basicInfo-left">
<dt class="basicInfo-item name" id="basic-name">中文名</dt>
<dd class="basicInfo-item value">
中华人民共和国行政区划
</dd>
<dt class="basicInfo-item name" id="basic-name">适用国家</dt>
<dd class="basicInfo-item value">
<a target=_blank href="/item/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD/106554" data-lemmaid="106554">中华人民共和国</a>
</dd>
<dt class="basicInfo-item name" id="basic-name">省级行政区</dt>
<dd class="basicInfo-item value">
<a target=_blank href="/item/%E7%9C%81/7317775" data-lemmaid="7317775">省</a>、<a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E5%8C%BA/987423" data-lemmaid="987423">自治区</a>、<a target=_blank href="/item/%E7%9B%B4%E8%BE%96%E5%B8%82/725471" data-lemmaid="725471">直辖市</a><b>、</b><a target=_blank href="/item/%E7%89%B9%E5%88%AB%E8%A1%8C%E6%94%BF%E5%8C%BA/2411153" data-lemmaid="2411153">特别行政区</a> <sup class="sup--normal" data-sup="1" data-ctrmap=":1,">
[1]</sup><a class="sup-anchor" name="ref_[1]_71418">&nbsp;</a>
</dd>
<dt class="basicInfo-item name" id="basic-name">地级行政区</dt>
<dd class="basicInfo-item value">
<a target=_blank href="/item/%E5%9C%B0%E7%BA%A7%E5%B8%82/2089621" data-lemmaid="2089621">地级市</a>、<a target=_blank href="/item/%E5%9C%B0%E5%8C%BA/2089684" data-lemmaid="2089684">地区</a><b>、</b><a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E5%B7%9E/1710336" data-lemmaid="1710336">自治州</a>、<a target=_blank href="/item/%E7%9B%9F/49920" data-lemmaid="49920">盟</a><sup class="sup--normal" data-sup="1" data-ctrmap=":1,">
[1]</sup><a class="sup-anchor" name="ref_[1]_71418">&nbsp;</a>
</dd>
</dl>
<dl class="basicInfo-block basicInfo-right">
<dt class="basicInfo-item name" id="basic-name">县级行政区</dt>
<dd class="basicInfo-item value">
<a target=_blank href="/item/%E5%B8%82%E8%BE%96%E5%8C%BA/10182051" data-lemmaid="10182051">市辖区</a>、<a target=_blank href="/item/%E5%8E%BF%E7%BA%A7%E5%B8%82/1659674" data-lemmaid="1659674">县级市</a>、<a target=_blank href="/item/%E5%8E%BF/34322" data-lemmaid="34322">县</a>、<a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E5%8E%BF/1660044" data-lemmaid="1660044">自治县</a>、<a target=_blank href="/item/%E6%97%97/52264" data-lemmaid="52264">旗</a>、<a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E6%97%97/1660238" data-lemmaid="1660238">自治旗</a>、特区、<a target=_blank href="/item/%E6%9E%97%E5%8C%BA/1872871" data-lemmaid="1872871">林区</a><sup class="sup--normal" data-sup="1" data-ctrmap=":1,">
[1]</sup><a class="sup-anchor" name="ref_[1]_71418">&nbsp;</a>
</dd>
<dt class="basicInfo-item name" id="basic-name">乡级行政区</dt>
<dd class="basicInfo-item value">
<a target=_blank href="/item/%E8%A1%97%E9%81%93/419541" data-lemmaid="419541">街道</a>、<a target=_blank href="/item/%E9%95%87/5922313" data-lemmaid="5922313">镇</a>、<a target=_blank href="/item/%E4%B9%A1/34483" data-lemmaid="34483">乡</a><b>、</b><a target=_blank href="/item/%E6%B0%91%E6%97%8F%E4%B9%A1/4655580" data-lemmaid="4655580">民族乡</a>、<a target=_blank href="/item/%E8%8B%8F%E6%9C%A8/3226" data-lemmaid="3226">苏木</a>、<a target=_blank href="/item/%E6%B0%91%E6%97%8F%E8%8B%8F%E6%9C%A8/23721489" data-lemmaid="23721489">民族苏木</a>、<a target=_blank href="/item/%E5%8E%BF%E8%BE%96%E5%8C%BA/3663105" data-lemmaid="3663105">县辖区</a><sup class="sup--normal" data-sup="1" data-ctrmap=":1,">
[1]</sup><a class="sup-anchor" name="ref_[1]_71418">&nbsp;</a>
</dd>
</dl>
</div>
<div class="related-video-container J-related-video-container" style="display: none">
<div class="related-video-title">
相关视频<div class="view-more J-go-video-feed">查看全部<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_arrow-right"></em></div>
</div>
<div class="second-wrapper">
<div
    class="video-list-container"
    id="J-video-list-container"
    style="
        max-width: 773px;
            "
></div>
</div>
</div><div class="lemmaWgt-lemmaCatalog">
<div class="lemma-catalog">
<h2 class="block-title">目录</h2>
<div class="catalog-list column-3">
<ol>
<li class="level1">
<span class="index">1</span>
<span class="text"><a href="#1">具体区划</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#1_1">华北地区</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#1_2">东北地区</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#1_3">华东地区</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#1_4">华中地区</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#1_5">华南地区</a></span>
</li>
</ol><ol><li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#1_6">西南地区</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#1_7">西北地区</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#1_8">港澳台地区</a></span>
</li>
<li class="level1">
<span class="index">2</span>
<span class="text"><a href="#2">区划体制</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#2_1">省级行政区</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#2_2">地级行政区</a></span>
</li>
</ol><ol><li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#2_3">县级行政区</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#2_4">乡级行政区</a></span>
</li>
<li class="level1">
<span class="index">3</span>
<span class="text"><a href="#3">区划沿革</a></span>
</li>
<li class="level1">
<span class="index">4</span>
<span class="text"><a href="#4">管理规定</a></span>
</li>
</ol>

</div>
</div>
</div>
<div class="anchor-list ">
<a name="1" class="lemma-anchor para-title" ></a>
<a name="sub71418_1" class="lemma-anchor " ></a>
<a name="具体区划" class="lemma-anchor " ></a>
</div><div class="para-title level-2  J-chapter" data-index="1" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>具体区划</h2>
<a class="edit-icon j-edit-link" data-edit-dl="1" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="audio-play part-audio-play J-part-audio-play" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_voice-play"></em>
<span class="J-part-audio-text">播报</span>
</a>
</div>
<div class="anchor-list ">
<a name="1_1" class="lemma-anchor para-title" ></a>
<a name="sub71418_1_1" class="lemma-anchor " ></a>
<a name="华北地区" class="lemma-anchor " ></a>
<a name="1-1" class="lemma-anchor " ></a>
</div><div class="para-title level-3  " data-index="1_1" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>华北地区</h3>
</div>
<div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/a50f4bfbfbedab641589b799f836afc378311eeb?fr=lemma&ct=single" target="_blank"
			title="北京市" 
	 
		style="width:220px;height:215.13812154696px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/a50f4bfbfbedab641589b799f836afc378311eeb?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="北京市"
							style="width:220px;height:215.13812154696px;"
					/>
</a>
<span class="description">
北京市
</span>
</div><b><a target=_blank href="/item/%E5%8C%97%E4%BA%AC%E5%B8%82/126069" data-lemmaid="126069">北京市</a></b><b>（行政代码：110000）</b></div><div class="para" label-module="para">16个县级区划：16个市辖区</div><div class="para" label-module="para">338个乡级区划：157个街道、143个镇、33个乡、5个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/9f2f070828381f30d5c377f0a6014c086f06f095?fr=lemma&ct=single" target="_blank"
			title="天津市" 
	 
		style="width:220px;height:306.25396825397px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/9f2f070828381f30d5c377f0a6014c086f06f095?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="天津市"
							style="width:220px;height:306.25396825397px;"
					/>
</a>
<span class="description">
天津市
</span>
</div><b><a target=_blank href="/item/%E5%A4%A9%E6%B4%A5%E5%B8%82/213824" data-lemmaid="213824">天津市</a></b><b>（行政代码：120000）</b></div><div class="para" label-module="para">16个县级区划：16个市辖区</div><div class="para" label-module="para">248个乡级区划：119个街道、126个镇、2个乡、1个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/5fdf8db1cb134954cbe6123d594e9258d0094aeb?fr=lemma&ct=single" target="_blank"
			title="河北省" 
	 
		style="width:220px;height:312.41260744986px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/5fdf8db1cb134954cbe6123d594e9258d0094aeb?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="河北省"
							style="width:220px;height:312.41260744986px;"
					/>
</a>
<span class="description">
河北省
</span>
</div><b><a target=_blank href="/item/%E6%B2%B3%E5%8C%97%E7%9C%81/153775" data-lemmaid="153775">河北省</a></b><b>（行政代码：130000）</b></div><div class="para" label-module="para">11个地级区划：11个地级市</div><div class="para" label-module="para">167个县级区划：49个市辖区、21个县级市、91个县、6个自治县。</div><div class="para" label-module="para">2255个乡级区划：308个街道、1156个镇、744个乡、46个民族乡、1个县辖区</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/faf2b2119313b07e4245aa5103d7912396dd8ceb?fr=lemma&ct=single" target="_blank"
			title="山西省" 
	 
		style="width:220px;height:345.96774193548px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/faf2b2119313b07e4245aa5103d7912396dd8ceb?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="山西省"
							style="width:220px;height:345.96774193548px;"
					/>
</a>
<span class="description">
山西省
</span>
</div><b><a target=_blank href="/item/%E5%B1%B1%E8%A5%BF%E7%9C%81/365266" data-lemmaid="365266">山西省</a></b><b>（行政代码：140000）</b></div><div class="para" label-module="para">11个地级区划：11个地级市</div><div class="para" label-module="para">117个县级区划：26个市辖区、11个县级市、80个县</div><div class="para" label-module="para">1396个乡级区划：207个街道、577个镇、612个乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/b64543a98226cffc3c7f45ebb6014a90f603ea16?fr=lemma&ct=single" target="_blank"
			title="内蒙古自治区" 
	 
		style="width:220px;height:170.43915521287px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/b64543a98226cffc3c7f45ebb6014a90f603ea16?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="内蒙古自治区"
							style="width:220px;height:170.43915521287px;"
					/>
</a>
<span class="description">
内蒙古自治区
</span>
</div><b><a target=_blank href="/item/%E5%86%85%E8%92%99%E5%8F%A4%E8%87%AA%E6%B2%BB%E5%8C%BA/49872215" data-lemmaid="49872215">内蒙古自治区</a></b><b>（行政代码：150000）</b></div><div class="para" label-module="para">12个地级区划：9个地级市、3个盟</div><div class="para" label-module="para">103个县级区划：23个市辖区、11个县级市、17个县、49个旗、3个自治旗</div><div class="para" label-module="para">1024个乡级区划：246个街道、508个镇、99个乡、17个民族乡、153个苏木、1个民族苏木</div><div class="anchor-list ">
<a name="1_2" class="lemma-anchor para-title" ></a>
<a name="sub71418_1_2" class="lemma-anchor " ></a>
<a name="东北地区" class="lemma-anchor " ></a>
<a name="1-2" class="lemma-anchor " ></a>
</div><div class="para-title level-3  " data-index="1_2" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>东北地区</h3>
</div>
<div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/c2cec3fdfc039245394c1b568894a4c27c1e25ea?fr=lemma&ct=single" target="_blank"
			title="辽宁省" 
	 
		style="width:220px;height:194.29796355841px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/c2cec3fdfc039245394c1b568894a4c27c1e25ea?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="辽宁省"
							style="width:220px;height:194.29796355841px;"
					/>
</a>
<span class="description">
辽宁省
</span>
</div><b><a target=_blank href="/item/%E8%BE%BD%E5%AE%81%E7%9C%81/739981" data-lemmaid="739981">辽宁省</a></b><b>（行政代码：210000）</b></div><div class="para" label-module="para">14个地级区划：14个地级市</div><div class="para" label-module="para">100个县级区划：59个市辖区、16个县级市、17个县、8个自治县</div><div class="para" label-module="para">1355个乡级区划：514个街道、640个镇、147个乡、54个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/8c1001e93901213f27cab4855be736d12e2e95ea?fr=lemma&ct=single" target="_blank"
			title="吉林省" 
	 
		style="width:220px;height:176.49757673667px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/8c1001e93901213f27cab4855be736d12e2e95ea?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="吉林省"
							style="width:220px;height:176.49757673667px;"
					/>
</a>
<span class="description">
吉林省
</span>
</div><b><a target=_blank href="/item/%E5%90%89%E6%9E%97%E7%9C%81/129609" data-lemmaid="129609">吉林省</a></b><b>（行政代码：220000）</b></div><div class="para" label-module="para">9个地级区划：8个地级市、1个自治州</div><div class="para" label-module="para">60个县级区划：21个市辖区、20个县级市、16个县、3个自治县</div><div class="para" label-module="para">937个乡级区划：329个街道、426个镇、154个乡、28个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/0d338744ebf81a4c3f681690d82a6059252da615?fr=lemma&ct=single" target="_blank"
			title="黑龙江省" 
	 
		style="width:220px;height:237.7897574124px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/0d338744ebf81a4c3f681690d82a6059252da615?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="黑龙江省"
							style="width:220px;height:237.7897574124px;"
					/>
</a>
<span class="description">
黑龙江省
</span>
</div><b><a target=_blank href="/item/%E9%BB%91%E9%BE%99%E6%B1%9F%E7%9C%81/129397" data-lemmaid="129397">黑龙江省</a></b><b>（行政代码：230000）</b></div><div class="para" label-module="para">13个地级区划：12个地级市、1个地区</div><div class="para" label-module="para">121个县级区划：54个市辖区、21个县级市、45个县、1个自治县</div><div class="para" label-module="para">1266个乡级区划：364个街道、557个镇、293个乡、52个民族乡</div><div class="anchor-list ">
<a name="1_3" class="lemma-anchor para-title" ></a>
<a name="sub71418_1_3" class="lemma-anchor " ></a>
<a name="华东地区" class="lemma-anchor " ></a>
<a name="1-3" class="lemma-anchor " ></a>
</div><div class="para-title level-3  " data-index="1_3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>华东地区</h3>
</div>
<div class="para" label-module="para"><b><a target=_blank href="/item/%E4%B8%8A%E6%B5%B7%E5%B8%82/127743" data-lemmaid="127743">上海市</a></b><b>（行政代码：310000）</b></div><div class="para" label-module="para">16个县级区划：16个市辖区</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/5bafa40f4bfbfbedbe03cc2677f0f736afc31f14?fr=lemma&ct=single" target="_blank"
			title="上海市" 
	 
		style="width:220px;height:221.99697428139px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/5bafa40f4bfbfbedbe03cc2677f0f736afc31f14?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="上海市"
							style="width:220px;height:221.99697428139px;"
					/>
</a>
<span class="description">
上海市
</span>
</div>215个乡级区划：107个街道、106个镇、2个乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/9f2f070828381f30d5c177f0a6014c086f06f08b?fr=lemma&ct=single" target="_blank"
			title="江苏省" 
	 
		style="width:220px;height:205.81803345573px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/9f2f070828381f30d5c177f0a6014c086f06f08b?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="江苏省"
							style="width:220px;height:205.81803345573px;"
					/>
</a>
<span class="description">
江苏省
</span>
</div><b><a target=_blank href="/item/%E6%B1%9F%E8%8B%8F%E7%9C%81/320938" data-lemmaid="320938">江苏省</a></b><b>（行政代码：320000）</b></div><div class="para" label-module="para">13个地级区划：13个地级市</div><div class="para" label-module="para">96个县级区划：55个市辖区、22个县级市、19个县</div><div class="para" label-module="para">1261个乡级区划：503个街道、718个镇、39个乡、1个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/f11f3a292df5e0fe23e67358536034a85fdf72e9?fr=lemma&ct=single" target="_blank"
			title="浙江省" 
	 
		style="width:220px;height:200.92766427388px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/f11f3a292df5e0fe23e67358536034a85fdf72e9?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="浙江省"
							style="width:220px;height:200.92766427388px;"
					/>
</a>
<span class="description">
浙江省
</span>
</div><b><a target=_blank href="/item/%E6%B5%99%E6%B1%9F%E7%9C%81/190275" data-lemmaid="190275">浙江省</a></b><b>（行政代码：330000）</b></div><div class="para" label-module="para">11个地级区划：11个地级市</div><div class="para" label-module="para">90个县级区划：37个市辖区、20个县级市、32个县、1个自治县</div><div class="para" label-module="para">1360个乡级区划：482个街道、619个镇、245个乡、14个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/b3b7d0a20cf431ad5f2cb9604436acaf2fdd98e9?fr=lemma&ct=single" target="_blank"
			title="安徽省" 
	 
		style="width:220px;height:292.61320240044px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/b3b7d0a20cf431ad5f2cb9604436acaf2fdd98e9?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="安徽省"
							style="width:220px;height:292.61320240044px;"
					/>
</a>
<span class="description">
安徽省
</span>
</div><b><a target=_blank href="/item/%E5%AE%89%E5%BE%BD%E7%9C%81/526353" data-lemmaid="526353">安徽省</a></b><b>（行政代码：340000）</b></div><div class="para" label-module="para">16个地级区划：16个地级市</div><div class="para" label-module="para">105个县级区划：46个市辖区、9个县级市、50个县</div><div class="para" label-module="para">1498个乡级区划：259个街道、968个镇、262个乡、9个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/9c16fdfaaf51f3de076b433d9beef01f3b29798a?fr=lemma&ct=single" target="_blank"
			title="福建省" 
	 
		style="width:220px;height:223.0985915493px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/9c16fdfaaf51f3de076b433d9beef01f3b29798a?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="福建省"
							style="width:220px;height:223.0985915493px;"
					/>
</a>
<span class="description">
福建省
</span>
</div><b><a target=_blank href="/item/%E7%A6%8F%E5%BB%BA%E7%9C%81/122534" data-lemmaid="122534">福建省</a></b><b>（行政代码：350000）</b></div><div class="para" label-module="para">9个地级区划：9个地级市</div><div class="para" label-module="para">85个县级区划：29个市辖区、12个县级市、44个县</div><div class="para" label-module="para">1107个乡级区划：184个街道、653个镇、251个乡、19个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/c75c10385343fbf237f55c7abf7eca8064388f8a?fr=lemma&ct=single" target="_blank"
			title="江西省" 
	 
		style="width:220px;height:286.28277634961px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/c75c10385343fbf237f55c7abf7eca8064388f8a?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="江西省"
							style="width:220px;height:286.28277634961px;"
					/>
</a>
<span class="description">
江西省
</span>
</div><b><a target=_blank href="/item/%E6%B1%9F%E8%A5%BF%E7%9C%81/19438118" data-lemmaid="19438118">江西省</a></b><b>（行政代码：360000）</b></div><div class="para" label-module="para">11个地级区划：11个地级市</div><div class="para" label-module="para">100个县级区划：27个市辖区、11个县级市、62个县</div><div class="para" label-module="para">1563个乡级区划：165个街道、828个镇、562个乡、8个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/bf096b63f6246b600c330c2e4fb30d4c510fd9f9041f?fr=lemma&ct=single" target="_blank"
			title="山东省" 
	 
		style="width:220px;height:160.80717488789px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/bf096b63f6246b600c330c2e4fb30d4c510fd9f9041f?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="山东省"
							style="width:220px;height:160.80717488789px;"
					/>
</a>
<span class="description">
山东省
</span>
</div><b><a target=_blank href="/item/%E5%B1%B1%E4%B8%9C%E7%9C%81/209822" data-lemmaid="209822">山东省</a></b><b>（行政代码：370000）</b></div><div class="para" label-module="para">16个地级区划：16个地级市<sup class="sup--normal" data-sup="12" data-ctrmap=":12,">
[12]</sup><a class="sup-anchor" name="ref_[12]_71418">&nbsp;</a>
</div><div class="para" label-module="para">136个县级区划：58个市辖区、26个县级市、52个县<sup class="sup--normal" data-sup="12" data-ctrmap=":12,">
[12]</sup><a class="sup-anchor" name="ref_[12]_71418">&nbsp;</a>
</div><div class="para" label-module="para">1822个乡级区划：693个街道、1072个镇、57个乡<sup class="sup--normal" data-sup="12" data-ctrmap=":12,">
[12]</sup><a class="sup-anchor" name="ref_[12]_71418">&nbsp;</a>
</div><div class="anchor-list ">
<a name="1_4" class="lemma-anchor para-title" ></a>
<a name="sub71418_1_4" class="lemma-anchor " ></a>
<a name="华中地区" class="lemma-anchor " ></a>
<a name="1-4" class="lemma-anchor " ></a>
</div><div class="para-title level-3  " data-index="1_4" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>华中地区</h3>
</div>
<div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/80cb39dbb6fd52662ef5c64da418972bd5073689?fr=lemma&ct=single" target="_blank"
			title="河南省" 
	 
		style="width:220px;height:205.83138173302px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/80cb39dbb6fd52662ef5c64da418972bd5073689?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="河南省"
							style="width:220px;height:205.83138173302px;"
					/>
</a>
<span class="description">
河南省
</span>
</div><b><a target=_blank href="/item/%E6%B2%B3%E5%8D%97%E7%9C%81/59474" data-lemmaid="59474">河南省</a></b><b>（行政代码：410000）</b></div><div class="para" label-module="para">17个地级区划：17个地级市</div><div class="para" label-module="para">158个县级区划：53个市辖区、22个县级市、83个县</div><div class="para" label-module="para">2451个乡级区划：660个街道、1173个镇、606个乡、12个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/64380cd7912397dd2c21625d5682b2b7d0a2870b?fr=lemma&ct=single" target="_blank"
			title="湖北省" 
	 
		style="width:220px;height:144.87627845596px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/64380cd7912397dd2c21625d5682b2b7d0a2870b?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="湖北省"
							style="width:220px;height:144.87627845596px;"
					/>
</a>
<span class="description">
湖北省
</span>
</div><b><a target=_blank href="/item/%E6%B9%96%E5%8C%97%E7%9C%81/210064" data-lemmaid="210064">湖北省</a></b><b>（行政代码：420000）</b></div><div class="para" label-module="para">13个地级区划：12个地级市，1个自治州</div><div class="para" label-module="para">103个县级区划：39个市辖区、26个县级市、35个县、2个自治县、1个林区</div><div class="para" label-module="para">1249个乡级区划：327个街道、760个镇、152个乡、10个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/2fdda3cc7cd98d109d0af6682e3fb80e7aec9089?fr=lemma&ct=single" target="_blank"
			title="湖南省" 
	 
		style="width:220px;height:257.86046511628px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/2fdda3cc7cd98d109d0af6682e3fb80e7aec9089?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="湖南省"
							style="width:220px;height:257.86046511628px;"
					/>
</a>
<span class="description">
湖南省
</span>
</div><b><a target=_blank href="/item/%E6%B9%96%E5%8D%97%E7%9C%81/293174" data-lemmaid="293174">湖南省</a></b><b>（行政代码：430000）</b></div><div class="para" label-module="para">14个地级区划：13个地级市，1个自治州</div><div class="para" label-module="para">122个县级区划：36个市辖区、18个县级市、61个县、7个自治县</div><div class="para" label-module="para">1937个乡级区划：411个街道、1134个镇、309个乡、83个民族乡</div><div class="anchor-list ">
<a name="1_5" class="lemma-anchor para-title" ></a>
<a name="sub71418_1_5" class="lemma-anchor " ></a>
<a name="华南地区" class="lemma-anchor " ></a>
<a name="1-5" class="lemma-anchor " ></a>
</div><div class="para-title level-3  " data-index="1_5" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>华南地区</h3>
</div>
<div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/cdbf6c81800a19d8bc3e83c352b1958ba61ea9d3e8e8?fr=lemma&ct=single" target="_blank"
			title="广东省" 
	 
		style="width:220px;height:168.79310344828px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/cdbf6c81800a19d8bc3e83c352b1958ba61ea9d3e8e8?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="广东省"
							style="width:220px;height:168.79310344828px;"
					/>
</a>
<span class="description">
广东省
</span>
</div><b><a target=_blank href="/item/%E5%B9%BF%E4%B8%9C%E7%9C%81/132473" data-lemmaid="132473">广东省</a></b><b>（行政代码：440000）</b></div><div class="para" label-module="para">21个地级区划：21个地级市</div><div class="para" label-module="para">122个县级区划：65个市辖区、20个县级市、34个县、3个自治县</div><div class="para" label-module="para">1606个乡级区划：481个街道、1114个镇、4个乡、7个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/9a504fc2d5628535e5ddeae7f1a461c6a7efcf1bc5e8?fr=lemma&ct=single" target="_blank"
			title="广西壮族自治区" 
	 
		style="width:220px;height:173.34482758621px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/9a504fc2d5628535e5ddeae7f1a461c6a7efcf1bc5e8?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="广西壮族自治区"
							style="width:220px;height:173.34482758621px;"
					/>
</a>
<span class="description">
广西壮族自治区
</span>
</div><b><a target=_blank href="/item/%E5%B9%BF%E8%A5%BF%E5%A3%AE%E6%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA/163178" data-lemmaid="163178">广西壮族自治区</a></b><b>（行政代码：450000）</b></div><div class="para" label-module="para">14个地级区划：14个地级市</div><div class="para" label-module="para">111个县级区划：41个市辖区、9个县级市、49个县、12个自治县</div><div class="para" label-module="para">1250个乡级区划：132个街道、806个镇、253个乡、59个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/738b4710b912c8fcc3ce8c0b9d488545d688d53f8be8?fr=lemma&ct=single" target="_blank"
			title="海南省" 
	 
		style="width:220px;height:234.41379310345px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/738b4710b912c8fcc3ce8c0b9d488545d688d53f8be8?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="海南省"
							style="width:220px;height:234.41379310345px;"
					/>
</a>
<span class="description">
海南省
</span>
</div><b><a target=_blank href="/item/%E6%B5%B7%E5%8D%97%E7%9C%81/533000" data-lemmaid="533000">海南省</a></b><b>（行政代码：460000）</b></div><div class="para" label-module="para">4个地级区划：4个地级市</div><div class="para" label-module="para">25个县级区划：10个市辖区、5个县级市、4个县、6个自治县</div><div class="para" label-module="para">218个乡级区划：22个街道、175个镇、21个乡</div><div class="anchor-list ">
<a name="1_6" class="lemma-anchor para-title" ></a>
<a name="sub71418_1_6" class="lemma-anchor " ></a>
<a name="西南地区" class="lemma-anchor " ></a>
<a name="1-6" class="lemma-anchor " ></a>
</div><div class="para-title level-3  " data-index="1_6" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>西南地区</h3>
</div>
<div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/b3b7d0a20cf431ad5f8bb9604436acaf2edd980a?fr=lemma&ct=single" target="_blank"
			title="重庆市" 
	 
		style="width:220px;height:206.98738170347px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/b3b7d0a20cf431ad5f8bb9604436acaf2edd980a?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="重庆市"
							style="width:220px;height:206.98738170347px;"
					/>
</a>
<span class="description">
重庆市
</span>
</div><b><a target=_blank href="/item/%E9%87%8D%E5%BA%86%E5%B8%82/436625" data-lemmaid="436625">重庆市</a></b><b>（行政代码：500000）</b></div><div class="para" label-module="para">县级区划：26个市辖区、8个县、4个自治县</div><div class="para" label-module="para">1030个乡级区划：229个街道、629个镇、158个乡、14个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/5d6034a85edf8db10bf1863d0623dd54574e7488?fr=lemma&ct=single" target="_blank"
			title="四川省" 
	 
		style="width:220px;height:187.83351120598px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/5d6034a85edf8db10bf1863d0623dd54574e7488?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="四川省"
							style="width:220px;height:187.83351120598px;"
					/>
</a>
<span class="description">
四川省
</span>
</div><b><a target=_blank href="/item/%E5%9B%9B%E5%B7%9D%E7%9C%81/15626925" data-lemmaid="15626925">四川省</a></b><b>（行政代码：510000）</b></div><div class="para" label-module="para">21个地级区划：18个地级市，3个自治州</div><div class="para" label-module="para">183个县级区划：55个市辖区、18个县级市、106个县、4个自治县</div><div class="para" label-module="para">3440个乡级区划：449个街道、1926个镇、982个乡、83个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/0d338744ebf81a4c3fed1690d82a6059242da688?fr=lemma&ct=single" target="_blank"
			title="贵州省" 
	 
		style="width:220px;height:192.32558139535px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/0d338744ebf81a4c3fed1690d82a6059242da688?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="贵州省"
							style="width:220px;height:192.32558139535px;"
					/>
</a>
<span class="description">
贵州省
</span>
</div><b><a target=_blank href="/item/%E8%B4%B5%E5%B7%9E%E7%9C%81/20475641" data-lemmaid="20475641">贵州省</a></b><b>（行政代码：520000）</b></div><div class="para" label-module="para">9个地级区划：6个地级市，3个自治州</div><div class="para" label-module="para">88个县级区划：15个市辖区、9个县级市、52个县、11个自治县、1个特区</div><div class="para" label-module="para">1455个乡级区划：303个街道、837个镇、122个乡、193个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/71cf3bc79f3df8dc356375c8c211728b47102809?fr=lemma&ct=single" target="_blank"
			title="云南省" 
	 
		style="width:220px;height:232.2998729352px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/71cf3bc79f3df8dc356375c8c211728b47102809?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="云南省"
							style="width:220px;height:232.2998729352px;"
					/>
</a>
<span class="description">
云南省
</span>
</div><b><a target=_blank href="/item/%E4%BA%91%E5%8D%97%E7%9C%81/18664752" data-lemmaid="18664752">云南省</a></b><b>（行政代码：530000）</b></div><div class="para" label-module="para">16个地级区划：8个地级市，8个自治州</div><div class="para" label-module="para">129个县级区划：17个市辖区、17个县级市、66个县、29个自治县</div><div class="para" label-module="para">1405个乡级区划：186个街道、679个镇、400个乡、140个民族乡（2020.1云南省民政厅）</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/0ff41bd5ad6eddc451da3eeac692a1fd5266d01695c2?fr=lemma&ct=single" target="_blank"
			title="西藏" 
	 
		style="width:220px;height:132.25433526012px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/0ff41bd5ad6eddc451da3eeac692a1fd5266d01695c2?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="西藏"
							style="width:220px;height:132.25433526012px;"
					/>
</a>
<span class="description">
西藏
</span>
</div><b><a target=_blank href="/item/%E8%A5%BF%E8%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA/242417" data-lemmaid="242417">西藏自治区</a></b><b>（行政代码：540000）</b></div><div class="para" label-module="para">7个地级区划：6个地级市，1个地区</div><div class="para" label-module="para">74个县级区划：8个市辖区、66个县</div><div class="para" label-module="para">697个乡级区划：21个街道、142个镇、525个乡、9个民族乡</div><div class="anchor-list ">
<a name="1_7" class="lemma-anchor para-title" ></a>
<a name="sub71418_1_7" class="lemma-anchor " ></a>
<a name="西北地区" class="lemma-anchor " ></a>
<a name="1-7" class="lemma-anchor " ></a>
</div><div class="para-title level-3  " data-index="1_7" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>西北地区</h3>
</div>
<div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/d62a6059252dd42a5cf4fbf20c3b5bb5c8eab8ee?fr=lemma&ct=single" target="_blank"
			title="陕西省" 
	 
		style="width:220px;height:304.52352231604px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/d62a6059252dd42a5cf4fbf20c3b5bb5c8eab8ee?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="陕西省"
							style="width:220px;height:304.52352231604px;"
					/>
</a>
<span class="description">
陕西省
</span>
</div><b><a target=_blank href="/item/%E9%99%95%E8%A5%BF%E7%9C%81/19657132" data-lemmaid="19657132">陕西省</a></b><b>（行政代码：610000）</b></div><div class="para" label-module="para">10个地级区划：10个地级市</div><div class="para" label-module="para">107个县级区划：30个市辖区、6个县级市、71个县</div><div class="para" label-module="para">1312个乡级区划：316个街道、975个镇、21个乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/b21c8701a18b87d6101c5146080828381f30fd09?fr=lemma&ct=single" target="_blank"
			title="甘肃省" 
	 
		style="width:220px;height:172.58750857927px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/b21c8701a18b87d6101c5146080828381f30fd09?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="甘肃省"
							style="width:220px;height:172.58750857927px;"
					/>
</a>
<span class="description">
甘肃省
</span>
</div><b><a target=_blank href="/item/%E7%94%98%E8%82%83%E7%9C%81/684374" data-lemmaid="684374">甘肃省</a></b><b>（行政代码：620000）</b></div><div class="para" label-module="para">14个地级区划：12个地级市，2个自治州</div><div class="para" label-module="para">86个县级区划：17个市辖区、5个县级市、57个县、7个自治县</div><div class="para" label-module="para">1357个乡级区划：128个街道、892个镇、305个乡、32个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/0ff41bd5ad6eddc4a8654ea236dbb6fd536633ed?fr=lemma&ct=single" target="_blank"
			title="青海省" 
	 
		style="width:220px;height:162.62051915946px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/0ff41bd5ad6eddc4a8654ea236dbb6fd536633ed?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="青海省"
							style="width:220px;height:162.62051915946px;"
					/>
</a>
<span class="description">
青海省
</span>
</div><b><a target=_blank href="/item/%E9%9D%92%E6%B5%B7%E7%9C%81/19428913" data-lemmaid="19428913">青海省</a></b><b>（行政代码：630000）</b></div><div class="para" label-module="para">8个地级区划：2个地级市，6个自治州</div><div class="para" label-module="para">44个县级区划：7个市辖区、4个县级市、26个县、7个自治县</div><div class="para" label-module="para">403个乡级区划：37个街道、144个镇、194个乡、28个民族乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/7c1ed21b0ef41bd55a8e12ad5eda81cb38db3d8e?fr=lemma&ct=single" target="_blank"
			title="宁夏回族自治区" 
	 
		style="width:220px;height:346.34482758621px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/7c1ed21b0ef41bd55a8e12ad5eda81cb38db3d8e?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="宁夏回族自治区"
							style="width:220px;height:346.34482758621px;"
					/>
</a>
<span class="description">
宁夏回族自治区
</span>
</div><b><a target=_blank href="/item/%E5%AE%81%E5%A4%8F%E5%9B%9E%E6%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA/11229891" data-lemmaid="11229891">宁夏回族自治区</a></b><b>（行政代码：640000）</b></div><div class="para" label-module="para">5个地级区划：5个地级市</div><div class="para" label-module="para">22个县级区划：9个市辖区、2个县级市、11个县</div><div class="para" label-module="para">240个乡级区划：47个街道、103个镇、90个乡</div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/3c6d55fbb2fb4316349d80232fa4462308f7d3ed?fr=lemma&ct=single" target="_blank"
			title="新疆维吾尔自治区" 
	 
		style="width:220px;height:201.63982430454px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/3c6d55fbb2fb4316349d80232fa4462308f7d3ed?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="新疆维吾尔自治区"
							style="width:220px;height:201.63982430454px;"
					/>
</a>
<span class="description">
新疆维吾尔自治区
</span>
</div><b><a target=_blank href="/item/%E6%96%B0%E7%96%86%E7%BB%B4%E5%90%BE%E5%B0%94%E8%87%AA%E6%B2%BB%E5%8C%BA/906636" data-lemmaid="906636">新疆维吾尔自治区</a></b><b>（行政代码：650000）</b></div><div class="para" label-module="para">14个地级区划：4个地级市，5个地区，5个自治州</div><div class="para" label-module="para">107个县级区划：<span class="ref" data-ctrid="sS73jCK7wVfF">66个县、28个县级市、13个市辖区</span><sup class="sup--normal" data-sup="9" data-ctrmap="sS73jCK7wVfF:9,">
[9]</sup><a class="sup-anchor" name="ref_[9]_71418">&nbsp;</a>
</div><div class="para" label-module="para"><span class="ref" data-ctrid="sS73GDy4Ip9w">1127个乡级区划：478个乡、444个镇、205个街道、1个县辖区</span><sup class="sup--normal" data-sup="9" data-ctrmap="sS73GDy4Ip9w:9,:11,">
[9]</sup><a class="sup-anchor" name="ref_[9]_71418">&nbsp;</a>
<sup class="sup--normal" data-sup="11" data-ctrmap="sS73GDy4Ip9w:9,:11,">
[11]</sup><a class="sup-anchor" name="ref_[11]_71418">&nbsp;</a>
</div><div class="anchor-list ">
<a name="1_8" class="lemma-anchor para-title" ></a>
<a name="sub71418_1_8" class="lemma-anchor " ></a>
<a name="港澳台地区" class="lemma-anchor " ></a>
<a name="1-8" class="lemma-anchor " ></a>
</div><div class="para-title level-3  " data-index="1_8" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>港澳台地区</h3>
</div>
<div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/c83d70cf3bc79f3d1bbd1e69b5a1cd11728b290f?fr=lemma&ct=single" target="_blank"
			title="香港特别行政区" 
	 
		style="width:220px;height:192.7619047619px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/c83d70cf3bc79f3d1bbd1e69b5a1cd11728b290f?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="香港特别行政区"
							style="width:220px;height:192.7619047619px;"
					/>
</a>
<span class="description">
香港特别行政区
</span>
</div><b><a target=_blank href="/item/%E9%A6%99%E6%B8%AF%E7%89%B9%E5%88%AB%E8%A1%8C%E6%94%BF%E5%8C%BA/24510970" data-lemmaid="24510970">香港特别行政区</a></b><b>（行政代码：810000）</b>：</div><div class="para" label-module="para">18个区：东区、南区、北区、中西区、湾仔区、观塘区、大埔区、沙田区、西贡区、荃湾区、屯门区、元朗区、</div><div class="para" label-module="para">葵青区、离岛区、油尖旺区、深水埗区、九龙城区、黄大仙区</div><div class="para" label-module="para"><b>注：根据《中华人民共和国香港特别行政区基本法》的规定，各区只设非政权机构。</b></div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/e7cd7b899e510fb307c48dced633c895d0430c8d?fr=lemma&ct=single" target="_blank"
			title="澳门特别行政区" 
	 
		style="width:220px;height:340.67326732673px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/e7cd7b899e510fb307c48dced633c895d0430c8d?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="澳门特别行政区"
							style="width:220px;height:340.67326732673px;"
					/>
</a>
<span class="description">
澳门特别行政区
</span>
</div><b><a target=_blank href="/item/%E6%BE%B3%E9%97%A8%E7%89%B9%E5%88%AB%E8%A1%8C%E6%94%BF%E5%8C%BA/50041229" data-lemmaid="50041229">澳门特别行政区</a></b><b>（行政代码：820000）</b>：</div><div class="para" label-module="para">7个堂区：大堂区、望德堂区、风顺堂区、嘉模堂区、花地玛堂区、圣安多尼堂区、圣方济各堂区</div><div class="para" label-module="para">1个填海区：路氹城填海区</div><div class="para" label-module="para"><b>注：根据《中华人民共和国澳门特别行政区基本法》的规定，各堂区只设非政权机构。</b></div><div class="para" label-module="para"><div class="lemma-picture J-lemma-picture text-pic layout-right" 
	 
		style="width:220px; float: right;"
	>
<a class="image-link" nslog-type="9317" 
			href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/0/78310a55b319ebc4a9278cc08d26cffc1e17160f?fr=lemma&ct=single" target="_blank"
			title="台湾省" 
	 
		style="width:220px;height:305.33953488372px;"
		>
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://bkimg.cdn.bcebos.com/pic/78310a55b319ebc4a9278cc08d26cffc1e17160f?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto"  alt="台湾省"
							style="width:220px;height:305.33953488372px;"
					/>
</a>
<span class="description">
台湾省
</span>
</div><b><a target=_blank href="/item/%E5%8F%B0%E6%B9%BE%E7%9C%81/761219" data-lemmaid="761219">台湾省</a></b><b>（行政代码：710000）</b>：</div><div class="para" label-module="para">6个地级区划：6个地级市</div><div class="para" label-module="para">14个县级区划：3个县级市、11个县</div><div class="para" label-module="para">1076个乡级区划：170个市辖区、14个县辖市、35个镇、109个乡。</div><div class="anchor-list ">
<a name="2" class="lemma-anchor para-title" ></a>
<a name="sub71418_2" class="lemma-anchor " ></a>
<a name="区划体制" class="lemma-anchor " ></a>
</div><div class="para-title level-2  J-chapter" data-index="2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>区划体制</h2>
<a class="edit-icon j-edit-link" data-edit-dl="2" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="audio-play part-audio-play J-part-audio-play" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_voice-play"></em>
<span class="J-part-audio-text">播报</span>
</a>
</div>
<div class="anchor-list ">
<a name="2_1" class="lemma-anchor para-title" ></a>
<a name="sub71418_2_1" class="lemma-anchor " ></a>
<a name="省级行政区" class="lemma-anchor " ></a>
<a name="2-1" class="lemma-anchor " ></a>
</div><div class="para-title level-3  " data-index="2_1" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>省级行政区</h3>
</div>
<div class="para" label-module="para"><b><a target=_blank href="/item/%E7%9C%81%E7%BA%A7%E8%A1%8C%E6%94%BF%E5%8C%BA">省级行政区</a></b><b>是中央人民政府直接管辖的最高一级地方行政区域，有</b><b><a target=_blank href="/item/%E7%9C%81/7317775" data-lemmaid="7317775">省</a></b><b>、</b><b><a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E5%8C%BA/987423" data-lemmaid="987423">自治区</a></b><b>、</b><b><a target=_blank href="/item/%E7%9B%B4%E8%BE%96%E5%B8%82/725471" data-lemmaid="725471">直辖市</a></b><b>、</b><b><a target=_blank href="/item/%E7%89%B9%E5%88%AB%E8%A1%8C%E6%94%BF%E5%8C%BA">特别行政区</a></b><b>。</b></div><div class="para" label-module="para"><a target=_blank href="/item/%E7%9C%81/7317775" data-lemmaid="7317775">省</a>——中国国家地方一级行政区域，始于元朝，已有六七百年的历史。</div><div class="para" label-module="para"><a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E5%8C%BA">自治区</a>——中国少数民族聚居地方实行民族区域自治而建立的省级行政区域。新中国成立后共建立了5个：内蒙古自治区、新疆维吾尔自治区、广西壮族自治区、宁夏回族自治区、西藏自治区。</div><div class="para" label-module="para"><a target=_blank href="/item/%E7%9B%B4%E8%BE%96%E5%B8%82">直辖市</a>——中央直辖市，由国务院直接管辖，是人口比较集中，在政治、经济、文化等方面具有特别重要地位的大城市。中国共设有4个：北京、天津、上海、重庆。</div><div class="para" label-module="para"><a target=_blank href="/item/%E7%89%B9%E5%88%AB%E8%A1%8C%E6%94%BF%E5%8C%BA">特别行政区</a>——为贯彻“一国两制”的实施，宪法第三十一条专门规定：国家在必要时可以设立特别行政区。特别行政区与省、自治区、直辖市同属直辖于中央人民政府的地方行政区域。中国共设立2个：香港特别行政区、澳门特别行政区。</div><table log-set-param="table_view" data-sort="sortDisabled"><tr></tr></table><div class="anchor-list ">
<a name="2_2" class="lemma-anchor para-title" ></a>
<a name="sub71418_2_2" class="lemma-anchor " ></a>
<a name="地级行政区" class="lemma-anchor " ></a>
<a name="2-2" class="lemma-anchor " ></a>
</div><div class="para-title level-3  " data-index="2_2" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>地级行政区</h3>
</div>
<div class="para" label-module="para"><b><a target=_blank href="/item/%E5%9C%B0%E7%BA%A7%E8%A1%8C%E6%94%BF%E5%8C%BA">地级行政区</a></b><b>是介于省级和县级之间的一级地方行政区域，包括</b><b><a target=_blank href="/item/%E5%9C%B0%E7%BA%A7%E5%B8%82/2089621" data-lemmaid="2089621">地级市</a></b><b>、</b><b><a target=_blank href="/item/%E5%9C%B0%E5%8C%BA/13841496" data-lemmaid="13841496">地区</a></b><b>、</b><b><a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E5%B7%9E/1710336" data-lemmaid="1710336">自治州</a></b><b>、</b><b><a target=_blank href="/item/%E7%9B%9F/13981654" data-lemmaid="13981654">盟</a></b><b>。</b></div><div class="para" label-module="para"><a target=_blank href="/item/%E5%9C%B0%E7%BA%A7%E5%B8%82">地级市</a>——一级政权组织，是中国人口比较集中，政治、经济、文化地位比较重要的城市，下分市辖区、县、自治县、县级市。</div><div class="para" label-module="para"><a target=_blank href="/item/%E5%9C%B0%E5%8C%BA/13841496" data-lemmaid="13841496">地区</a>（1975年前称专区）——省、自治区的派出机构，管理几个县、自治县和市，不是一级地方政权。始设于国民党政府时期，新中国成立后沿用。1975年前称专区、设专员公署；后称地区、设行政公署。</div><div class="para" label-module="para"><a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E5%B7%9E">自治州</a>——中国少数民族聚居地方为实行民族区域自治而建立的介于省级、县级之间的一级行政区域，设自治州人大、自治州人民政府，是一级政权机构，下分县、自治县、市。</div><div class="para" label-module="para"><a target=_blank href="/item/%E7%9B%9F/13981654" data-lemmaid="13981654">盟</a>——内蒙古自治区地级行政区域。原是蒙古族旗会盟组织，设盟人大、盟人民政府，是一级政权机构，包括几个县、旗、市。</div><div class="anchor-list ">
<a name="2_3" class="lemma-anchor para-title" ></a>
<a name="sub71418_2_3" class="lemma-anchor " ></a>
<a name="县级行政区" class="lemma-anchor " ></a>
<a name="2-3" class="lemma-anchor " ></a>
</div><div class="para-title level-3  " data-index="2_3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>县级行政区</h3>
</div>
<div class="para" label-module="para"><a target=_blank href="/item/%E5%8E%BF%E7%BA%A7%E8%A1%8C%E6%94%BF%E5%8C%BA">县级行政区</a>是中国地方二级行政区域，是地方政权的基础，包括<a target=_blank href="/item/%E5%B8%82%E8%BE%96%E5%8C%BA/10182051" data-lemmaid="10182051">市辖区</a>、<a target=_blank href="/item/%E5%8E%BF%E7%BA%A7%E5%B8%82/1659674" data-lemmaid="1659674">县级市</a>、<a target=_blank href="/item/%E5%8E%BF/7258656" data-lemmaid="7258656">县</a>、<a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E5%8E%BF/1660044" data-lemmaid="1660044">自治县</a>、<a target=_blank href="/item/%E6%97%97/9639886" data-lemmaid="9639886">旗</a>、<a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E6%97%97/1660238" data-lemmaid="1660238">自治旗</a>、特区、<a target=_blank href="/item/%E6%9E%97%E5%8C%BA/1872871" data-lemmaid="1872871">林区</a>。</div><div class="para" label-module="para"><a target=_blank href="/item/%E5%B8%82%E8%BE%96%E5%8C%BA">市辖区</a>——市的下一级行政区划，设立区人大、区政府，为城市的基层政权组织，相当于县。下设街道办事处作为区的派出机关。</div><div class="para" label-module="para"><a target=_blank href="/item/%E5%8E%BF%E7%BA%A7%E5%B8%82">县级市</a>——和市辖区、县、自治县等县级行政区平级的县级行政区域，一般由地级行政区代管。</div><div class="para" label-module="para"><a target=_blank href="/item/%E5%8E%BF/7258656" data-lemmaid="7258656">县</a>——始于春秋时代、已有两千多年历史，是中国基础行政区域。下辖乡、镇。</div><div class="para" label-module="para"><a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E5%8E%BF">自治县</a>——少数民族聚居地方实行民族区域自治的县级行政区域。</div><div class="para" label-module="para"><a target=_blank href="/item/%E6%97%97/9639886" data-lemmaid="9639886">旗</a>——少数民族（主要是蒙古族）聚居的县级行政区域，是新中国成立后沿用的原蒙古族等少数民族的民族组织。</div><div class="para" label-module="para"><a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E6%97%97">自治旗</a>——另一些少数民族聚居区实行区域自治的行政区域（相当于自治县，仅在内蒙古自治区内）。</div><div class="para" label-module="para">特区——工矿企业特别集中的县级行政区划（现仅六枝特区）。</div><div class="para" label-module="para"><a target=_blank href="/item/%E6%9E%97%E5%8C%BA/1872871" data-lemmaid="1872871">林区</a>——县级行政区划（现仅<a target=_blank href="/item/%E7%A5%9E%E5%86%9C%E6%9E%B6%E6%9E%97%E5%8C%BA/2884040" data-lemmaid="2884040">神农架林区</a>）。</div><div class="anchor-list ">
<a name="2_4" class="lemma-anchor para-title" ></a>
<a name="sub71418_2_4" class="lemma-anchor " ></a>
<a name="乡级行政区" class="lemma-anchor " ></a>
<a name="2-4" class="lemma-anchor " ></a>
</div><div class="para-title level-3  " data-index="2_4" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>乡级行政区</h3>
</div>
<div class="para" label-module="para"><b><a target=_blank href="/item/%E4%B9%A1%E7%BA%A7%E8%A1%8C%E6%94%BF%E5%8C%BA">乡级行政区</a></b><b>是地方三级行政单位，包括</b><a target=_blank href="/item/%E8%A1%97%E9%81%93/419541" data-lemmaid="419541">街道</a>、<a target=_blank href="/item/%E9%95%87/5922313" data-lemmaid="5922313">镇</a>、乡<b>、</b><a target=_blank href="/item/%E6%B0%91%E6%97%8F%E4%B9%A1/4655580" data-lemmaid="4655580">民族乡</a>、苏木、<a target=_blank href="/item/%E6%B0%91%E6%97%8F%E8%8B%8F%E6%9C%A8/23721489" data-lemmaid="23721489">民族苏木</a>、<a target=_blank href="/item/%E5%8E%BF%E8%BE%96%E5%8C%BA/3663105" data-lemmaid="3663105">县辖区</a>。</div><div class="para" label-module="para"><a target=_blank href="/item/%E9%95%87/5922313" data-lemmaid="5922313">镇</a>——县、自治县管辖的基层行政区域。1955年，国家颁布《关于划分城镇标准的规定》，规定了建镇的主要条件是县及县级以上政权所在地，常住人口在2000人以上、其中非农业居民占50%以上。1984年，国家制定了新的建镇标准，放宽了条件（工商业比较集中的地区可以设镇），并实行镇管村体制。</div><div class="para" label-module="para"><a target=_blank href="/item/%E4%B9%A1/7465369" data-lemmaid="7465369">乡</a>——中国农村的基层行政区域。中华人民共和国成立后，设乡人民政府，受县人民政府领导。1958年，随着农村人民公社化运动的开展，乡政权一度由人民公社行使，乡制撤销。1982年12月全国人大通过的宪法（即“八二宪法”）规定，恢复乡建制，设立乡人大和乡人民政府。乡按居民居住地区设立村民委员会（简称村委会），作为基层群众性自治组织。1983年开始建乡。</div><div class="para" label-module="para"><a target=_blank href="/item/%E6%B0%91%E6%97%8F%E4%B9%A1/4655580" data-lemmaid="4655580">民族乡</a>——少数民族聚居的乡级行政区域。<sup class="sup--normal" data-sup="2" data-ctrmap=":2,">
[2]</sup><a class="sup-anchor" name="ref_[2]_71418">&nbsp;</a>
</div><div class="anchor-list ">
<a name="3" class="lemma-anchor para-title" ></a>
<a name="sub71418_3" class="lemma-anchor " ></a>
<a name="区划沿革" class="lemma-anchor " ></a>
</div><div class="para-title level-2  J-chapter" data-index="3" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>区划沿革</h2>
<a class="edit-icon j-edit-link" data-edit-dl="3" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="audio-play part-audio-play J-part-audio-play" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_voice-play"></em>
<span class="J-part-audio-text">播报</span>
</a>
</div>
<div class="para" label-module="para">1949年<a target=_blank href="/item/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD/106554" data-lemmaid="106554">中华人民共和国</a>成立时，全国分为30省、1自治区、12直辖市、5行署区、1地方、1地区。此后区划多次调整，到1967年，调整为22省、5自治区、3直辖市共计30省级行政区，此后基本固定下来。1988年从<a target=_blank href="/item/%E5%B9%BF%E4%B8%9C%E7%9C%81">广东省</a>析置<a target=_blank href="/item/%E6%B5%B7%E5%8D%97%E5%B2%9B">海南岛</a>、<a target=_blank href="/item/%E5%8D%97%E6%B5%B7%E8%AF%B8%E5%B2%9B">南海诸岛</a>及其海域，成立<a target=_blank href="/item/%E6%B5%B7%E5%8D%97%E7%9C%81">海南省</a>。1997年撤销<a target=_blank href="/item/%E5%9B%9B%E5%B7%9D%E7%9C%81">四川省</a>辖重庆市，设立<a target=_blank href="/item/%E9%87%8D%E5%BA%86/23586" data-lemmaid="23586">重庆</a>直辖市。1997年和1999年香港和澳门回归中国，相继新设2个特别行政区。至此全国共计23省、5自治区、4直辖市和2特别行政区，共计34省级行政区：</div><div class="para" label-module="para">1949年，中华人民共和国行政区划将全国分为<a target=_blank href="/item/%E4%BA%94%E5%A4%A7%E8%A1%8C%E6%94%BF%E5%8C%BA/20727247" data-lemmaid="20727247">五大行政区</a>和一个中央直属行政单位，总共有30省、1自治区、12直辖市、5<a target=_blank href="/item/%E8%A1%8C%E7%BD%B2%E5%8C%BA">行署区</a>、1地方、1地区。</div><div class="para" label-module="para">1950年，撤销<a target=_blank href="/item/%E6%97%85%E5%A4%A7%E8%A1%8C%E7%BD%B2%E5%8C%BA">旅大行署区</a>，设立旅大市，并设立<a target=_blank href="/item/%E4%B8%AD%E5%A4%AE%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8D%8E%E5%8C%97%E4%BA%8B%E5%8A%A1%E9%83%A8">中央人民政府华北事务部</a>，撤销四川省，设立川东、川南、川西、川北4个行署区。</div><div class="para" label-module="para">1952年，撤销中央人民政府华北事务部，设立<a target=_blank href="/item/%E6%94%BF%E5%8A%A1%E9%99%A2%E5%8D%8E%E5%8C%97%E8%A1%8C%E6%94%BF%E5%A7%94%E5%91%98%E4%BC%9A">政务院华北行政委员会</a>。并将原来的大行政区改称为行政委员会。撤销行署区建制，恢复为省。撤销<a target=_blank href="/item/%E5%B9%B3%E5%8E%9F%E7%9C%81">平原省</a>，并入河南、山东二省。撤销<a target=_blank href="/item/%E5%AF%9F%E5%93%88%E5%B0%94%E7%9C%81">察哈尔省</a>，并入河北、山西二省。直辖市南京市改为江苏省辖市。</div><div class="para" label-module="para">1953年，吉林省长春市、<a target=_blank href="/item/%E6%9D%BE%E6%B1%9F%E7%9C%81">松江省</a>哈尔滨市升为直辖市。总计<a target=_blank href="/item/%E5%85%AD%E5%A4%A7%E8%A1%8C%E6%94%BF%E5%8C%BA/20723226" data-lemmaid="20723226">六大行政区</a>，下辖30省、1自治区、14直辖市、1地方、1地区<sup class="sup--normal" data-sup="3" data-ctrmap=":3,">
[3]</sup><a class="sup-anchor" name="ref_[3]_71418">&nbsp;</a>
。</div><div class="para" label-module="para">1954年，撤销6大行政委员会，最高一级的地方行政单位变为省。撤销辽东、辽西二省，恢复辽宁省。撤销松江省，并入黑龙江省。撤销宁夏省，并入<a target=_blank href="/item/%E7%94%98%E8%82%83%E7%9C%81/684374" data-lemmaid="684374">甘肃省</a>；1954年6月，撤销<a target=_blank href="/item/%E7%BB%A5%E8%BF%9C%E7%9C%81">绥远省</a>，并入内蒙古自治区，原绥远省省会<a target=_blank href="/item/%E5%BD%92%E7%BB%A5">归绥</a>市改称呼和浩特市，定为自治区首府。总计26省、1自治区、3直辖市、1地方、1地区。</div><div class="para" label-module="para">1955年7月30日，撤销<a target=_blank href="/item/%E7%83%AD%E6%B2%B3%E7%9C%81">热河省</a>，将其行政区域并入河北省、辽宁省及内蒙古自治区；1955年10月，撤销<a target=_blank href="/item/%E8%A5%BF%E5%BA%B7%E7%9C%81">西康省</a>，将其行政区域并入四川省；1955年10月1日，撤消新疆省，设立新疆维吾尔自治区，自治区首府乌鲁木齐市（原名迪化，1953年改新名），成立<a target=_blank href="/item/%E8%A5%BF%E8%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA%E7%AD%B9%E5%A4%87%E5%A7%94%E5%91%98%E4%BC%9A">西藏自治区筹备委员会</a>，昌都地区划归其管辖。</div><div class="para" label-module="para">1958年3月5日，撤销广西省，设立广西僮族自治区（1965年10月12日，“僮”改为“壮”）。</div><div class="para" label-module="para">1958年10月25日，从甘肃省划出部分区域，正式成立宁夏回族自治区；1958年2月11日，中央直辖的天津市改为河北省省辖市；至此全国分为22省、4自治区、2直辖市、1筹备委员会。</div><div class="para" label-module="para">1965年9月9日，西藏自治区正式成立。</div><div class="para" label-module="para">1967年1月2日，河北省<a target=_blank href="/item/%E5%A4%A9%E6%B4%A5%E5%B8%82/213824" data-lemmaid="213824">天津市</a>重新升为中央直辖市；截至1967年全国分为22省、5自治区、3直辖市。</div><div class="para" label-module="para">1988年4月13日，撤销<a target=_blank href="/item/%E6%B5%B7%E5%8D%97%E8%A1%8C%E6%94%BF%E5%8C%BA">海南行政区</a>，设立海南省。<sup class="sup--normal" data-sup="4" data-ctrmap=":4,">
[4]</sup><a class="sup-anchor" name="ref_[4]_71418">&nbsp;</a>
</div><div class="para" label-module="para">1997年，（1）设立<a target=_blank href="/item/%E9%87%8D%E5%BA%86/23586" data-lemmaid="23586">重庆</a>直辖市，撤销原四川省重庆市。（2）重庆直辖市辖原<a target=_blank href="/item/%E5%9B%9B%E5%B7%9D%E7%9C%81/15626925" data-lemmaid="15626925">四川省</a>的重庆市、万县市、涪陵市、黔江地区所辖行政区域。（3）重庆直辖市设立后，由国务院依据宪法和有关法律的规定，对其管辖的行政区域的建置和划分作相应的调整。（1997年3月14日第八届全国人民代表大会第五次会议通过）。重庆直辖市简称"渝"(国务院1997年4月18日批准)。<sup class="sup--normal" data-sup="8" data-ctrmap=":8,">
[8]</sup><a class="sup-anchor" name="ref_[8]_71418">&nbsp;</a>
</div><div class="para" label-module="para">1997年7月1日，中国恢复对<a target=_blank href="/item/%E9%A6%99%E6%B8%AF/128775" data-lemmaid="128775">香港</a>行使主权，设立香港特别行政区。</div><div class="para" label-module="para">1999年12月20日，中国恢复对<a target=_blank href="/item/%E6%BE%B3%E9%97%A8/24335" data-lemmaid="24335">澳门</a>行使主权，设立澳门特别行政区。</div><div class="para" label-module="para">中国的行政区域基本上划分为三级，即省（自治区、直辖市），县（自治县、市），乡（民族乡、镇）。但在经济比较发达的地区，为促进城乡结合、工农结合，打破条块分割，充分发挥城乡两个方面积极性，实行市管县体制。实行市管县的地方，就是在省、县之间增加一级政区，实行四级制（宪法上尚未认可）。另外，有些自治区下辖自治州、自治州以下有县，也是四级制。这就使中国现行行政区划和地方行政建制层次形成了三级和四级并存的体制。</div><div class="para" label-module="para">新中国成立以来，中国的行政区划根据国家建设需要先后作过多次调整。特别是改革开放以后，省级以下行政区划变化很大：按“整县改市”“以乡建镇”模式设置了大批市、镇；部分地区与市合并，全面试行市管县体制；人民公社在政社分开后恢复为乡、民族乡；撤（县辖）区并乡建镇；恢复、新设民族自治地方。<sup class="sup--normal" data-sup="5" data-ctrmap=":5,">
[5]</sup><a class="sup-anchor" name="ref_[5]_71418">&nbsp;</a>
</div><div class="anchor-list ">
<a name="4" class="lemma-anchor para-title" ></a>
<a name="sub71418_4" class="lemma-anchor " ></a>
<a name="管理规定" class="lemma-anchor " ></a>
</div><div class="para-title level-2  J-chapter" data-index="4" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">中华人民共和国行政区划</span>管理规定</h2>
<a class="edit-icon j-edit-link" data-edit-dl="4" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="audio-play part-audio-play J-part-audio-play" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_voice-play"></em>
<span class="J-part-audio-text">播报</span>
</a>
</div>
<div class="para" label-module="para">根据《<a target=_blank href="/item/%E5%9B%BD%E5%8A%A1%E9%99%A2%E5%85%B3%E4%BA%8E%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92%E7%AE%A1%E7%90%86%E7%9A%84%E8%A7%84%E5%AE%9A">国务院关于行政区划管理的规定</a>》第三条至第八条规定：</div><div class="para" label-module="para">省、自治区、直辖市的设立、撤销、更名，报全国人民代表大会审议决定。</div><div class="para" label-module="para">下列行政区划的变更由国务院审批：</div><div class="para" label-module="para">（一）省、自治区、直辖市的行政区域界线的变更，省、自治区人民政府驻地的迁移；</div><div class="para" label-module="para">（二）自治州、县、自治县、市、市辖区的设立、撤销、更名和隶属关系的变更以及自治州、县、自治县、市人民政府驻地的迁移；</div><div class="para" label-module="para">（三）<a target=_blank href="/item/%E8%87%AA%E6%B2%BB%E5%B7%9E/1710336" data-lemmaid="1710336">自治州</a>、自治县的行政区域界线的变更，县、市的行政区域界线的重大变更；</div><div class="para" label-module="para">（四）凡涉及海岸线、海岛、边疆要地、重要资源地区及特殊情况地区的隶属关系或行政区域界线的变更。</div><div class="para" label-module="para">县、市、市辖区的部分行政区域界线的变更，国务院授权省、自治区、直辖市人民政府审批；批准变更时，同时报送民政部备案。乡、民族乡、镇的设立、撤销、更名和行政区域界线的变更，乡、民族乡、镇人民政府驻地的迁移，由省、自治区、直辖市人民政府审批。</div><div class="para" label-module="para">行政公署、区公所、街道办事处的撤销、更名、驻地迁移，由依法批准设立各该派出机关的人民政府审批。</div><div class="para" label-module="para">变更行政区划向上级人民政府报告的内容应包括：变更的理由、范围，隶属关系，政治经济情况，人口和面积数字，拟变更的行政区域界线地图，以及县级和县级以上人民政府（含行政公署）的报告或意见等。</div><div class="para" label-module="para">各级民政部门分级负责行政区划的管理工作。各级民政部门在承办行政区划变更的工作时，应根据情况分别同民族、人事、财政、外事、城乡建设、地名等有关部门联系洽商；在承办民族自治地方的行政区划变更的工作时，应同民族自治地方的自治机关和有关民族的代表充分协商拟定。各级民政部门，应建立完整的行政区划档案。<sup class="sup--normal" data-sup="6" data-ctrmap=":6,">
[6]</sup><a class="sup-anchor" name="ref_[6]_71418">&nbsp;</a>
</div>
<div id="J-main-content-end-dom"></div>
<div class="go-auth-box J-go-auth-box hidden">
<div class="go-auth-con">
<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_info"></em>
百度百科内容由网友共同编辑，如您发现自己的词条内容不准确或不完善，欢迎使用本人词条编辑服务（免费）参与修正。<a href="/personal/auth/中华人民共和国行政区划/1292734?bk_fr=lemma" target="_blank" nslog-type="10090202">立即前往>></a>
</div>
</div>
<div class="anchor-list ">
<a name="album-list" class="lemma-anchor " ></a>
</div><div class="album-list">
<div class="header">
<a class="more-link" href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734?fr=lemma" target="_blank" nslog-type="10000204">
<span class="title">词条图册</span>
<div class="more">
<span>更多图册</span>
<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_arrow-right arrow-right"></em>
</div>
</a>
</div>
<div class="scroller">
<div class="list">
</div>
</div>
<div class="footer">
</div>
</div>
<dl class="lemma-reference collapse nslog-area log-set-param" data-nslog-type="2" log-set-param="ext_reference">
<dt class="reference-title">参考资料</dt>
<dd class="reference-list-wrap">
<ul class="reference-list">
<li class="reference-item reference-item--type1 " id="reference-[1]-71418-wrap">
<span class="index">1.</span>
<a class="gotop anchor"  name="refIndex_1_71418" id="refIndex_1_71418" title="向上跳转" href="#ref_[1]_71418">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/reference/1292734/f02cnrjpBEiXp4rI-0C_P3LFVmRYJnLArPPYEDTJhwoFimI4J8FkwhiOC_pxSKqBNakMR82qvELFdqXcyAlvshllPNJh4hJo" target="_blank" class="text">中华人民共和国二〇一九年行政区划统计表<span class="linkout">&nbsp;</span></a>
<span class="site">．中华人民共和国民政部</span><span>．2019-12-31</span><span>&#91;引用日期2019-12-31&#93;</span></li><li class="reference-item reference-item--type1 " id="reference-[2]-71418-wrap">
<span class="index">2.</span>
<a class="gotop anchor"  name="refIndex_2_71418" id="refIndex_2_71418" title="向上跳转" href="#ref_[2]_71418">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/reference/1292734/38b7UYu602bBo3niYDp-YfAe7dwFVJPq1ixyIXfm_1XyTFqjIMFbHqec8pTytPVSmOvIG_qi2KLAMjbly6D6ZKMrZhs6KCJtFvMBzdK0RD9SQw" target="_blank" class="text">中国的行政区划——县级以下基层行政单位<span class="linkout">&nbsp;</span></a>
<span class="site">．中央政府门户网站</span><span>．2009年04月17日</span><span>&#91;引用日期2013-12-04&#93;</span></li><li class="reference-item reference-item--type1 " id="reference-[3]-71418-wrap">
<span class="index">3.</span>
<a class="gotop anchor"  name="refIndex_3_71418" id="refIndex_3_71418" title="向上跳转" href="#ref_[3]_71418">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/reference/1292734/59faIP6vaPfhQ_wV9TGplUUh-6mXUcxY89REqWLka8oOKCRYhf5yQBxHvfOA6z0uhZM50m3HYJFk3-e3MhSU_HQ0tuKzl6nhgBZ6PP49sP6Z" target="_blank" class="text">中华人民共和国行政区划（1953年）<span class="linkout">&nbsp;</span></a>
<span class="site">．中国政府网</span><span>．2007-03-23</span><span>&#91;引用日期2018-12-07&#93;</span></li><li class="reference-item reference-item--type1 " id="reference-[4]-71418-wrap">
<span class="index">4.</span>
<a class="gotop anchor"  name="refIndex_4_71418" id="refIndex_4_71418" title="向上跳转" href="#ref_[4]_71418">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/reference/1292734/cee6zj1hphdM6drbM1jsh5wXv76ZCAoMqRr0SLfaeZC1d4d1sbDB-zsT2XE83hxm7jSd6vkojy96jf4oxbJo9WrRMWZsZu7o1Xhh3Vlu6AqR" target="_blank" class="text">关于设立海南省的决定<span class="linkout">&nbsp;</span></a>
<span class="site">．中央政府门户网站</span><span>．2008-04-10</span><span>&#91;引用日期2021-02-06&#93;</span></li><li class="reference-item reference-item--type1 " id="reference-[5]-71418-wrap">
<span class="index">5.</span>
<a class="gotop anchor"  name="refIndex_5_71418" id="refIndex_5_71418" title="向上跳转" href="#ref_[5]_71418">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/reference/1292734/c2823wXoI39A1Qz1Eamwh5apjRa-iggzRwOCJIBcjGlwlclamyHf1IDUhvIS0KIMxVvfNYKi2sw_4mCaKDEU1e084Yqjg1zvMQf8HmrhNhGuGJjozw" target="_blank" class="text">中华人民共和国行政区划<span class="linkout">&nbsp;</span></a>
<span class="site">．中国政府网</span><span>．2005-06-15</span><span>&#91;引用日期2020-09-26&#93;</span></li><li class="reference-item reference-item--type1 " id="reference-[6]-71418-wrap">
<span class="index">6.</span>
<a class="gotop anchor"  name="refIndex_6_71418" id="refIndex_6_71418" title="向上跳转" href="#ref_[6]_71418">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/reference/1292734/c44dh-tS100Pnk51xRz6sh2TwqUpc9FYt6u4kVCcjfYiVEynqQkMTBQj4XRsE4xijgRV2zdJ8m3U3I5wpPsIhFlKrLbzlRA7W4NOe_edqI6zyg" target="_blank" class="text">国务院关于行政区划管理的规定<span class="linkout">&nbsp;</span></a>
<span class="site">．中央政府门户网站</span><span>．2009年03月30</span><span>&#91;引用日期2013-12-05&#93;</span></li><li class="reference-item reference-item--type1 " id="reference-[7]-71418-wrap">
<span class="index">7.</span>
<a class="gotop anchor"  name="refIndex_7_71418" id="refIndex_7_71418" title="向上跳转" href="#ref_[7]_71418">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/reference/1292734/3484RwZbnUxfAgn_o2N8JNVAjt-OTpyhseIsEbS5YekHU0PXb3wtG704L5UdjUrvq7b_VlqdCgcVXBjkjMgIjTwhh9wGu-XFBgREppQDjr4" target="_blank" class="text">中华人民共和国行政区划<span class="linkout">&nbsp;</span></a>
<span class="site">．中国政府网</span><span>&#91;引用日期2021-06-30&#93;</span></li><li class="reference-item reference-item--type1 " id="reference-[8]-71418-wrap">
<span class="index">8.</span>
<a class="gotop anchor"  name="refIndex_8_71418" id="refIndex_8_71418" title="向上跳转" href="#ref_[8]_71418">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/reference/1292734/6cfcnAG-K9zOl6tLvymthE3rysJ8Fgi2614WyBKi64em5J6a5ZwkLWd92AzE-PX7bd_3_iGpEnEB2pT-FmmSsdT1LREXMJfIFc77Tlzm26Lc" target="_blank" class="text">中华人民共和国行政区划（1997年）<span class="linkout">&nbsp;</span></a>
<span class="site">．中华人民共和国中央人民政府</span><span>&#91;引用日期2021-12-02&#93;</span></li><li class="reference-item reference-item--type1 " id="reference-[9]-71418-wrap">
<span class="index">9.</span>
<a class="gotop anchor"  name="refIndex_9_71418" id="refIndex_9_71418" title="向上跳转" href="#ref_[9]_71418">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/reference/1292734/f804kTZh_tJvgv_oiIq0oNpmJLzpTUsAMJBa7knxO0ouc3WyQkKck21Uwj5v7VNkZTaRD91K__F_22z_2EcBK4J2gX7LLPDYuImLg0duMzd6BQsyqHR_dUencITLPuJXSDu2D4x1BhQr2K5pXbm4wQ0zUQ" target="_blank" class="text">新疆维吾尔自治区概况<span class="linkout">&nbsp;</span></a>
<span class="site">．新疆维吾尔自治区</span><span>&#91;引用日期2021-12-20&#93;</span></li><li class="reference-item reference-item--type1 " id="reference-[10]-71418-wrap">
<span class="index">10.</span>
<a class="gotop anchor"  name="refIndex_10_71418" id="refIndex_10_71418" title="向上跳转" href="#ref_[10]_71418">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/reference/1292734/4644RM3c4-e-XJ83HkRJ3TSHkXRRtTs46cUKHzW_kwbUDv2tbVrKkxRpTV3e5GMaI_uKvzekWHSnc7qcXi0sGXJUF1yONFXz" target="_blank" class="text">中华人民共和国行政区划统计表<span class="linkout">&nbsp;</span></a>
<span class="site">．中华人民共和国民政部</span><span>&#91;引用日期2022-02-22&#93;</span></li><li class="reference-item reference-item--type1 more" id="reference-[11]-71418-wrap">
<span class="index">11.</span>
<a class="gotop anchor"  name="refIndex_11_71418" id="refIndex_11_71418" title="向上跳转" href="#ref_[11]_71418">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/reference/1292734/f04d6hWVYFOJGkEeiMsZeRnnOZi2wypD3A9z3Ksaj8IC0Hj3-28-KoBCHfgBZPVUtcWRW7XYlZnjiKB0Efub1Xmhgu9eT3Dt" target="_blank" class="text">中华人民共和国行政区划统计表<span class="linkout">&nbsp;</span></a>
<span class="site">．中华人民共和国民政部</span><span>&#91;引用日期2022-02-22&#93;</span></li><li class="reference-item reference-item--type1 more" id="reference-[12]-71418-wrap">
<span class="index">12.</span>
<a class="gotop anchor"  name="refIndex_12_71418" id="refIndex_12_71418" title="向上跳转" href="#ref_[12]_71418">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/reference/1292734/c30c4m5HBZdqVj5DU52mTuREKg0GbKq_CtQ5-ftqG6xG5lv__nKGyL8CepaHW5JGmr8p-FN62C9yn_2W61TE3Wn_KuBRdW5eRn11RuMpow" target="_blank" class="text">山东省人民政府 山东省行政区划<span class="linkout">&nbsp;</span></a>
<span class="site">．山东省人民政府</span><span>&#91;引用日期2022-03-08&#93;</span></li></ul>
</dd>
<dd class="toggle">
<span class="text expand-text">展开全部</span>
<span class="text collapse-text">收起</span>
<em class="toggle-arrow"></em>
</dd>
</dl>
</div>
<div class="side-content">
<div class="summary-pic">
<a nslog-type="10002401"
                    href="/pic/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734/1/71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4?fr=lemma&amp;ct=single" target="_blank"
	            >
<img src="https://bkimg.cdn.bcebos.com/pic/71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4?x-bce-process=image/resize,m_lfit,w_536,limit_1/format,f_jpg"
                alt="中华人民共和国行政区划" />
<button class="picAlbumBtn"><em></em><span>图集</span></button>
<div>中华人民共和国行政区划的概述图（3张）</div>
</a>
</div>
<div class="lemmaWgt-promotion-vbaike">
<div class="promotion_title">V百科<a href="/vbaike#gallary" target="_blank">往期回顾</a></div>
<div class="promotion_viewport">
<dl>
</dl>
<div class="promotion_viewport_pager"></div>
</div>
</div><div class="lemmaWgt-promotion-rightPreciseAd" data-lemmaId="1292734" data-lemmaTitle="中华人民共和国行政区划"></div><div class="lemmaWgt-sideRecommend">
<a name="zhixinWrap" class="qnAnchor"></a>
<div class="zhixin-box" id="zhixinWrap" data-source="" data-newLemmaId="1292734">
</div>
<form id="zhixinErrorForm" class="hidden" action="https://sp2.baidu.com/-uV1bjeh1BF3odCf/index.php/feedback/zx/baikeJC" target="zhixinSubErr" method="post">
<input class="js-url" name="fb_html_url" type="hidden" />
<input class="js-query" name="fb_query" type="hidden" />
<input class="js-title" name="fb_card_title" type="hidden" />
<input class="js-content" name="fb_content" type="hidden" />
<input class="js-souceId" name="fb_source_id" type="hidden" />
</form>
<iframe id="zhixinSubErr" name="zhixinSubErr" style="display:none" frameborder="0"></iframe>
</div>
<div class="lemmaWgt-promotion-slide">
<div class="promotion_viewport">
<dl>
</dl>
<div class="promotion_viewport_pager"></div>
</div>
</div><div class="lemmaWgt-promotion-rightBigAd">
</div><dl class="side-box lemma-statistics">
<dt class="title">词条统计</dt>
<dd class="description ">
<ul>
<li>浏览次数：<span id="j-lemmaStatistics-pv"></span>次</li>
<li>编辑次数：150次<a href="/historylist/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/1292734" class="nslog:1021" target="_blank">历史版本</a></li>
<li>
<span class="latest-title">最近更新：</span>
<span class="latest-content">
<a id="j-lemmaStatistics-name" class="show-userCard" data-uid="538413540" data-uk="oaUiA_vqDRAEzrwzgYVuhw" title="查看此用户资料" target="_blank" href="/usercenter/userpage?uk=oaUiA_vqDRAEzrwzgYVuhw&from=lemma"
                    nslog-type="1022">GRDaRcy</a>
<span class="j-modified-time" style="display:none">（2022-06-30）</span>
</span>
</li>
</ul>
</dd>
</dl>
<div class="side-catalog" style="visibility:hidden">
<div class="side-bar">
</div>
<div class="catalog-scroller">
<dl class="catalog-list">
<dt class="catalog-title level1 active">
<a href="#1" class="title-link">
<span class="text">
<span class="title-index">1</span>
<span class="title-link" nslog-type="10002802">具体区划</span>
</span>
</a>
</dt>
<dd class="catalog-title level2">
<a href="#1_1" class="title-link">
<span class="text">
<em class="pointer"></em>
<span class="title-link" nslog-type="10002802">华北地区</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#1_2" class="title-link">
<span class="text">
<em class="pointer"></em>
<span class="title-link" nslog-type="10002802">东北地区</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#1_3" class="title-link">
<span class="text">
<em class="pointer"></em>
<span class="title-link" nslog-type="10002802">华东地区</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#1_4" class="title-link">
<span class="text">
<em class="pointer"></em>
<span class="title-link" nslog-type="10002802">华中地区</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#1_5" class="title-link">
<span class="text">
<em class="pointer"></em>
<span class="title-link" nslog-type="10002802">华南地区</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#1_6" class="title-link">
<span class="text">
<em class="pointer"></em>
<span class="title-link" nslog-type="10002802">西南地区</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#1_7" class="title-link">
<span class="text">
<em class="pointer"></em>
<span class="title-link" nslog-type="10002802">西北地区</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#1_8" class="title-link">
<span class="text">
<em class="pointer"></em>
<span class="title-link" nslog-type="10002802">港澳台地区</span>
</span>
</a>
</dd>
<dt class="catalog-title level1 ">
<a href="#2" class="title-link">
<span class="text">
<span class="title-index">2</span>
<span class="title-link" nslog-type="10002802">区划体制</span>
</span>
</a>
</dt>
<dd class="catalog-title level2">
<a href="#2_1" class="title-link">
<span class="text">
<em class="pointer"></em>
<span class="title-link" nslog-type="10002802">省级行政区</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#2_2" class="title-link">
<span class="text">
<em class="pointer"></em>
<span class="title-link" nslog-type="10002802">地级行政区</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#2_3" class="title-link">
<span class="text">
<em class="pointer"></em>
<span class="title-link" nslog-type="10002802">县级行政区</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#2_4" class="title-link">
<span class="text">
<em class="pointer"></em>
<span class="title-link" nslog-type="10002802">乡级行政区</span>
</span>
</a>
</dd>
<dt class="catalog-title level1 ">
<a href="#3" class="title-link">
<span class="text">
<span class="title-index">3</span>
<span class="title-link" nslog-type="10002802">区划沿革</span>
</span>
</a>
</dt>
<dt class="catalog-title level1 ">
<a href="#4" class="title-link">
<span class="text">
<span class="title-index">4</span>
<span class="title-link" nslog-type="10002802">管理规定</span>
</span>
</a>
</dt>
<a class="arrow" href="javascript:void(0);"></a>
</dl>
</div>
<div class="right-wrap">
<a class="go-up disable" href="javascript:void(0);">
<div class="up-triangle"></div>
</a>
<a class="go-down" href="javascript:void(0);">
<div class="down-triangle"></div>
</a>
</div>
<div class="bottom-wrap">
<a class="gotop-button" href="javascript:void(0);" nslog-type="10002804"></a>
</div>
</div>
<div id="side_box_fengchao" class="fengchao side-box" nslog="area" nslog-type="10000902">
</div>
<div id="side_box_unionAd" class="unionAd">
<div class="union-content"></div>
</div>
<div id="J-side-box-yitiao" class="side-box yitiao-box">
<div class="recommend-title">为您推荐<span class="recommend-flag">广告</span></div>
<div class="recommend-content"></div>
</div>
</div>
</div>
</div>
<div class="after-content">
<div class="bottom-recommend-wrapper"></div>
<div class="fc-guess-like new" id="fc_guess_like_new">
<span class="logo-du">
<em class="cmn-icon cmn-icons cmn-icons_logo-du"></em>
</span>
<h6>搜索发现</h6>
<ul class="cmn-clearfix">
</ul>
</div>
</div>
</div>


<div class="wgt-footer-main">
<div class="content">
<dl class="fresh">
<dt><em class="cmn-icon cmn-icons cmn-icons_footer-fresh"></em>新手上路</dt>
<dd>
<div><a target="_blank" href="/usercenter/tasks#guide">成长任务</a></div>
<div><a target="_blank" href="/help#main01">编辑入门</a></div>
<div><a target="_blank" href="/help#main06">编辑规则</a></div>
<div><a target="_blank" href="/item/%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91%EF%BC%9A%E6%9C%AC%E4%BA%BA%E8%AF%8D%E6%9D%A1%E7%BC%96%E8%BE%91%E6%9C%8D%E5%8A%A1/22442459?bk_fr=pcFooter">本人编辑</a><img src="https://bkssl.bdimg.com/static/wiki-common/widget/component/footer/img/new-icon_e35348d.png" class="new-icon" alt="new"></div>
</dd>
</dl>
<dl class="question">
<dt><em class="cmn-icon cmn-icons cmn-icons_footer-question"></em>我有疑问</dt>
<dd>
<div><a id="J-bk-feedback-query" data-lemma="中华人民共和国行政区划" href="javascript:void(0);" nslog-type="10070001" data-type="feedback">内容质疑</a></div>
<div><a class="J-bk-online-service" target="_blank" href="http://zhiqiu.baidu.com/baike/passport/html/baikechat.html" nslog-type="10000003">在线客服</a></div>
<div><a target="_blank" href="http://tieba.baidu.com/f?ie=utf-8&fr=bks0000&kw=%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91">官方贴吧</a></div>
<div><a id="J-bk-feedback-main" href="javascript:void(0);">意见反馈</a></div>
</dd>
</dl>
<dl class="suggestion">
<dt><em class="cmn-icon cmn-icons cmn-icons_footer-suggestion"></em>投诉建议</dt>
<dd>
<div><a target="_blank" href="http://help.baidu.com/newadd?prod_id=10&category=1">举报不良信息</a></div>
<div><a target="_blank" href="http://help.baidu.com/newadd?prod_id=10&category=2">未通过词条申诉</a></div>
<div><a target="_blank" href="http://help.baidu.com/newadd?prod_id=10&category=6">投诉侵权信息</a></div>
<div><a target="_blank" href="http://help.baidu.com/newadd?prod_id=10&category=5">封禁查询与解封</a></div>
</dd>
</dl>
</div>
<div class="copyright">©2022&nbsp;Baidu&nbsp;<a href="http://www.baidu.com/duty/" target="_blank">使用百度前必读</a>&nbsp;|&nbsp;<a href="http://help.baidu.com/question?prod_en=baike&class=89&id=1637" target="_blank">百科协议</a>&nbsp;|&nbsp;<a href="http://help.baidu.com/question?prod_id=10&class=690&id=1001779" target="_blank">隐私政策</a>&nbsp;|&nbsp;<a href="/operation/cooperation" target="_blank">百度百科合作平台</a>&nbsp;|&nbsp;<span>京ICP证030173号&nbsp;</span><img class="copyright-img" width="13" height="16" src="https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/copy_rignt_24.png"></div>
<p class="recordcode"><a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11000002000001" target="_blank"><i class="icon-police"></i>京公网安备11000002000001号</a></p>
</div>


<div class="lemmaWgt-searchHeader">
<div class="layout cmn-clearfix">
<div class="wgt-searchbar wgt-searchbar-new wgt-searchbar-simple cmn-clearfix ">
<div class="logo-container">
<a class="logo cmn-inline-block" title="到百科首页" href="/">
<span class="cmn-baike-logo">
<em class="cmn-icon cmn-icons cmn-icons_logo-bai"></em>
<em class="cmn-icon cmn-icons cmn-icons_logo-du"></em>
<em class="cmn-icon cmn-icons cmn-icons_logo-baike"></em>
</span>
</a>
</div>
<div class="search">
<div class="form">
<form id="searchForm" action="/search/word" method="GET" target="_self">
<input id="query" nslog="normal" nslog-type="10080015" name="word" type="text" autocomplete="off" autocorrect="off" value="中华人民共和国行政区划" /><button id="search" nslog="normal" nslog-type="10080013" type="button">进入词条</button>
</form>
<form id="searchLemmaForm" action="/search" method="GET" target="_self">
<input id="searchLemmaQuery" name="word" type="hidden" />
<input name="pn" type="hidden" value="0" />
<input name="rn" type="hidden" value="0" />
<input name="enc" type="hidden" value="utf8" />
</form>
<ul id="suggestion" class="suggestion">
<div class="sug"></div>
<li class="extra">
<span id="clear" style="margin-right:8px;">清除历史记录</span><span id="close" nslog="normal" nslog-type="10080016">关闭</span>
</li>
</ul>
</div>
</div>
</div>
<div class="tool-buttons">
<a class="toolButtons-audio button audio-play header-audio-play J-header-audio-play" javascript=":;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_voice-play"></em><span class="J-audio-text">播报</span></a>
<a class="toolButtons-edit button j-edit-link" href="javascript:;" nslog-type="10010001"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-hollow"></em>编辑</a>
<a class="toolButtons-collect button" href="javascript:;" nslog-type="10010002"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_star-hollow"></em><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_star-solid"></em>收藏</a>
<a class="toolButtons-vote button top-vote" href="javascript:;" nslog-type="10010003"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_zan-hollow"></em><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_zan-solid"></em><span class="j-tool-btn-vote-num">赞</span></a>
</div>
<div class="user-info">
<a class="user-link unlogin" href="javascript:;" nslog-type="10010008" target="_blank">登录</a>
</div>
</div></div>
<div class="new-bdsharebuttonbox new-side-share" id="side-share">
<div class="share-list">
<a id="J-bds_task" class="bds_task" target="_blank" href="https://baike.baidu.com/task" nslog-type="10060902"></a>
<a class="share-link bds_qzone"  href="javascript:void(0);" nslog-type="10060101">
<em class="cmn-icon cmn-icons cmn-icons_logo-qzone"></em>
</a>
<a class="share-link bds_tsina" href="javascript:void(0);" nslog-type="10060301">
<em class="cmn-icon cmn-icons cmn-icons_logo-sina-weibo"></em>
</a>
<a class="bds_wechat"  href="javascript:void(0);" nslog-type="10060001">
<em class="cmn-icon cmn-icons cmn-icons_logo-wechat"></em>
</a>
<a class="share-link bds_tqq"  href="javascript:void(0);" nslog-type="10060201">
<em class="cmn-icon cmn-icons cmn-icons_logo-qq"></em>
</a>
<a id="J-bds_app" class="bds_app"  href="javascript:void(0);" nslog-type="10060901">
<em class="cmn-icon cmn-icons cmn-icons_mobile-phone"></em>
</a>
</div>
<div class="go-top">
<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_up-arrow"></em>
</div>
<div id="J-task-tip" class="task-tip"></div>
<div id="J-app-download" class="app-download hide">
<div class="text">
<h3 class="main">扫码下载百科APP</h3>
<h4 class="sub">领取<b>50</b>财富值奖励</h4>
</div>
<div class="qrcode"></div>
</div>
</div>
<div class="qrcode-wrapper" id="layer" style="display: none">
<div class="bd_weixin_popup_header">
<em class="cmn-icon cmn-icons cmn-icons_close"></em>
<span>分享到微信朋友圈</span>
</div>
<div id="wechat-qrcode-img"></div>
<div class="bd_weixin_popup_footer">打开微信“扫一扫”即可将网页分享至朋友圈</div>
</div>
<div></div><div></div><div id="J-tts" class="tts-wrapper">
<div class="tts-container">
<div class="tts-info">
<div class="image-container">
<div class="image-wrapper">
<img class="image" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/image/avatar_default_a111866.png" alt="">
</div>
<div class="playing-ani"></div>
<div class="loading-ani"></div>
</div>
<div class="title default"></div>
</div>
<div class="tts-voice">
<div class="voice-notice">
<div class="choose-title">选择朗读音色</div>
</div>
<div class="choose-icon left-icon"></div>
<div class="choose-icon right-icon"></div>
<div class="voice-list">
</div>
</div>
<div class="tts-tools">
<a class="icon enable-icon play-icon continue" title="播放/暂停"></a>
<div class="progress-container">
<div class="current-time">00:00</div>
<div class="progress-bar">
<div class="progress-bar-inner"></div>
</div>
<div class="end-time">00:00</div>
</div>
<a class="icon enable-icon voice-icon" title="音色调整"></a>
<div class="volume-container">
<a class="icon enable-icon volume-icon" title="音量调整"></a>
<div class="voice-volume">
<div class="volume-bar">
<div class="volume-point"></div>
<div class="volume-active-bar"></div>
</div>
<a class="icon enable-icon ctrl-icon" title="静音"></a>
</div>
</div>
</div>
<div class="front"></div>
<div class="background-container">
<div class="background"></div>
</div>
<a class="icon enable-icon close-icon" title="关闭"></a>
<audio class="audio-core J-audio-core" id="J-audio-current" preload="auto"></audio>
<audio class="audio-core J-audio-core" id="J-audio-cache" preload="auto"></audio>
</div>
</div>
<script>
        window['__abbaidu_2020_subidgetf'] = function () {
            var subid = 'baike_pc_lemmapage';
            return subid;
        };
        window['__abbaidu_2020_cb'] = function (res) {
            document.cookie = 'BAIKE_SHITONG=' + encodeURIComponent(res) + '; path=/item; max-age=86400';
        }
    </script>
<div class="J-empty empty-tag"></div>

<script>
      if (!window['__abbaidu_2020_subidgetf']) {
        window['__abbaidu_2020_subidgetf'] = function () {
            var subid = 01000000;
            return subid;
        };
      }
    </script>
<script async src="https://dlswbr.baidu.com/heicha/mw/abclite-2020-s.js"></script>

</body><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/js/mod_1fc3215.js"></script>
<script type="text/javascript">require.resourceMap({"res":{"wiki-common:widget/lib/jquery/jquery_1.11.1.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/jquery/jquery_1.11.1_c246440.js","pkg":"wiki-common:p9"},"wiki-common:widget/lib/jquery/jquery.mousewheel.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/jquery/jquery.mousewheel_543643d.js","pkg":"wiki-common:p9"},"wiki-common:widget/lib/jquery/jquery.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/jquery/jquery_2d56800.js","pkg":"wiki-common:p9","deps":["wiki-common:widget/lib/jquery/jquery_1.11.1.js","wiki-common:widget/lib/jquery/jquery.mousewheel.js"]},"wiki-common:widget/util/browser.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/browser_ffd6046.js","pkg":"wiki-common:p9"},"wiki-common:widget/component/psLink/psLink.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/psLink/psLink_3e936ee.js","pkg":"wiki-common:p9","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/browser.js"]},"wiki-common:widget/lib/jsmart/PHPJS.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/jsmart/PHPJS_162b0d3.js","pkg":"wiki-common:p14"},"wiki-common:widget/lib/jsmart/jsmart.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/jsmart/jsmart_d10620c.js","pkg":"wiki-common:p14","deps":["wiki-common:widget/lib/jsmart/PHPJS.js"]},"wiki-common:node_modules/@baidu/clickstream-sdk/lib/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@baidu/clickstream-sdk/lib/index_e4fbbea.js","pkg":"wiki-common:p18"},"wiki-common:packages/utils/clickstream.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/clickstream_66ef8b7.js","pkg":"wiki-common:p18","deps":["wiki-common:node_modules/@baidu/clickstream-sdk/lib/index.js"]},"wiki-common:node_modules/core-js/internals/global.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/global_4ecb0a5.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/fails.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/fails_c9a3ad1.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/descriptors.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/descriptors_f42d72e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/internals/function-bind-native.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/function-bind-native_d5a7ef3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/internals/function-call.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/function-call_d7bbea3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-bind-native.js"]},"wiki-common:node_modules/core-js/internals/object-property-is-enumerable.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-property-is-enumerable_9061a83.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/create-property-descriptor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/create-property-descriptor_4b0c5a5.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/function-uncurry-this.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/function-uncurry-this_6767111.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-bind-native.js"]},"wiki-common:node_modules/core-js/internals/classof-raw.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/classof-raw_12be689.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js"]},"wiki-common:node_modules/core-js/internals/indexed-object.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/indexed-object_247eef6.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/classof-raw.js"]},"wiki-common:node_modules/core-js/internals/require-object-coercible.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/require-object-coercible_6a82ce7.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/internals/to-indexed-object.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/to-indexed-object_c6371be.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/indexed-object.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js"]},"wiki-common:node_modules/core-js/internals/is-callable.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/is-callable_e9fa0e3.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/is-object.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/is-object_1a5b715.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/is-callable.js"]},"wiki-common:node_modules/core-js/internals/get-built-in.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/get-built-in_8017c1d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-callable.js"]},"wiki-common:node_modules/core-js/internals/object-is-prototype-of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-is-prototype-of_290a30a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js"]},"wiki-common:node_modules/core-js/internals/engine-user-agent.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/engine-user-agent_a3fe159.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/get-built-in.js"]},"wiki-common:node_modules/core-js/internals/engine-v8-version.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/engine-v8-version_d8a716b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/engine-user-agent.js"]},"wiki-common:node_modules/core-js/internals/native-symbol.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/native-symbol_4b11559.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/engine-v8-version.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/internals/use-symbol-as-uid.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/use-symbol-as-uid_802912e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/native-symbol.js"]},"wiki-common:node_modules/core-js/internals/is-symbol.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/is-symbol_a7fc903.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js","wiki-common:node_modules/core-js/internals/use-symbol-as-uid.js"]},"wiki-common:node_modules/core-js/internals/try-to-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/try-to-string_2b2663f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/internals/a-callable.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/a-callable_0d0fd2c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/try-to-string.js"]},"wiki-common:node_modules/core-js/internals/get-method.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/get-method_302ebe9.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/a-callable.js"]},"wiki-common:node_modules/core-js/internals/ordinary-to-primitive.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/ordinary-to-primitive_2c9ea70.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/is-object.js"]},"wiki-common:node_modules/core-js/internals/is-pure.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/is-pure_bbe132c.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/set-global.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/set-global_126e098.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/internals/shared-store.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/shared-store_d35cbcb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/set-global.js"]},"wiki-common:node_modules/core-js/internals/shared.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/shared_d1c63c0.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/is-pure.js","wiki-common:node_modules/core-js/internals/shared-store.js"]},"wiki-common:node_modules/core-js/internals/to-object.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/to-object_d4cb8f7.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js"]},"wiki-common:node_modules/core-js/internals/has-own-property.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/has-own-property_9d18b73.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-object.js"]},"wiki-common:node_modules/core-js/internals/uid.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/uid_55f3e14.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js"]},"wiki-common:node_modules/core-js/internals/well-known-symbol.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/well-known-symbol_3c7d07b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/shared.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/uid.js","wiki-common:node_modules/core-js/internals/native-symbol.js","wiki-common:node_modules/core-js/internals/use-symbol-as-uid.js"]},"wiki-common:node_modules/core-js/internals/to-primitive.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/to-primitive_99ab55c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/is-symbol.js","wiki-common:node_modules/core-js/internals/get-method.js","wiki-common:node_modules/core-js/internals/ordinary-to-primitive.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/internals/to-property-key.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/to-property-key_c74a64e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/to-primitive.js","wiki-common:node_modules/core-js/internals/is-symbol.js"]},"wiki-common:node_modules/core-js/internals/document-create-element.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/document-create-element_6c7b4dd.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-object.js"]},"wiki-common:node_modules/core-js/internals/ie8-dom-define.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/ie8-dom-define_8256b6f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/document-create-element.js"]},"wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-get-own-property-descriptor_4bc8c69.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/object-property-is-enumerable.js","wiki-common:node_modules/core-js/internals/create-property-descriptor.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/to-property-key.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/ie8-dom-define.js"]},"wiki-common:node_modules/core-js/internals/v8-prototype-define-bug.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/v8-prototype-define-bug_23d2266.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/internals/an-object.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/an-object_3a21801.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-object.js"]},"wiki-common:node_modules/core-js/internals/object-define-property.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-define-property_103d31b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/ie8-dom-define.js","wiki-common:node_modules/core-js/internals/v8-prototype-define-bug.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/to-property-key.js"]},"wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/create-non-enumerable-property_b507db9.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/create-property-descriptor.js"]},"wiki-common:node_modules/core-js/internals/inspect-source.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/inspect-source_d84f9c3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/shared-store.js"]},"wiki-common:node_modules/core-js/internals/native-weak-map.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/native-weak-map_dae9f8a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/inspect-source.js"]},"wiki-common:node_modules/core-js/internals/shared-key.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/shared-key_4ae712d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/shared.js","wiki-common:node_modules/core-js/internals/uid.js"]},"wiki-common:node_modules/core-js/internals/hidden-keys.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/hidden-keys_a0184a0.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/internal-state.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/internal-state_f893e37.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/native-weak-map.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/shared-store.js","wiki-common:node_modules/core-js/internals/shared-key.js","wiki-common:node_modules/core-js/internals/hidden-keys.js"]},"wiki-common:node_modules/core-js/internals/function-name.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/function-name_1d8645c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/has-own-property.js"]},"wiki-common:node_modules/core-js/internals/redefine.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/redefine_d697e46.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js","wiki-common:node_modules/core-js/internals/set-global.js","wiki-common:node_modules/core-js/internals/inspect-source.js","wiki-common:node_modules/core-js/internals/internal-state.js","wiki-common:node_modules/core-js/internals/function-name.js"]},"wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/to-integer-or-infinity_966539c.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/to-absolute-index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/to-absolute-index_a1f522f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js"]},"wiki-common:node_modules/core-js/internals/to-length.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/to-length_8622770.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js"]},"wiki-common:node_modules/core-js/internals/length-of-array-like.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/length-of-array-like_f7be599.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/to-length.js"]},"wiki-common:node_modules/core-js/internals/array-includes.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-includes_1cfcae8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/to-absolute-index.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js"]},"wiki-common:node_modules/core-js/internals/object-keys-internal.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-keys-internal_42056b8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/array-includes.js","wiki-common:node_modules/core-js/internals/hidden-keys.js"]},"wiki-common:node_modules/core-js/internals/enum-bug-keys.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/enum-bug-keys_58246a6.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/object-get-own-property-names.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-get-own-property-names_68815d0.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/object-keys-internal.js","wiki-common:node_modules/core-js/internals/enum-bug-keys.js"]},"wiki-common:node_modules/core-js/internals/object-get-own-property-symbols.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-get-own-property-symbols_20db60e.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/own-keys.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/own-keys_9bf016c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/object-get-own-property-names.js","wiki-common:node_modules/core-js/internals/object-get-own-property-symbols.js","wiki-common:node_modules/core-js/internals/an-object.js"]},"wiki-common:node_modules/core-js/internals/copy-constructor-properties.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/copy-constructor-properties_94a759e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/own-keys.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js","wiki-common:node_modules/core-js/internals/object-define-property.js"]},"wiki-common:node_modules/core-js/internals/is-forced.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/is-forced_ae7efc4.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/is-callable.js"]},"wiki-common:node_modules/core-js/internals/export.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/export_c37ba4f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/set-global.js","wiki-common:node_modules/core-js/internals/copy-constructor-properties.js","wiki-common:node_modules/core-js/internals/is-forced.js"]},"wiki-common:node_modules/core-js/internals/to-string-tag-support.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/to-string-tag-support_a0d99e1.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/internals/classof.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/classof_358765b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/to-string-tag-support.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/classof-raw.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/internals/to-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/to-string_bb15063.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/classof.js"]},"wiki-common:node_modules/core-js/internals/object-keys.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-keys_1291e72.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/object-keys-internal.js","wiki-common:node_modules/core-js/internals/enum-bug-keys.js"]},"wiki-common:node_modules/core-js/internals/object-define-properties.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-define-properties_9bb10b3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/v8-prototype-define-bug.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/object-keys.js"]},"wiki-common:node_modules/core-js/internals/html.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/html_797f127.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/get-built-in.js"]},"wiki-common:node_modules/core-js/internals/object-create.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-create_4333d7e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/object-define-properties.js","wiki-common:node_modules/core-js/internals/enum-bug-keys.js","wiki-common:node_modules/core-js/internals/hidden-keys.js","wiki-common:node_modules/core-js/internals/html.js","wiki-common:node_modules/core-js/internals/document-create-element.js","wiki-common:node_modules/core-js/internals/shared-key.js"]},"wiki-common:node_modules/core-js/internals/create-property.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/create-property_d1479ae.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/to-property-key.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/create-property-descriptor.js"]},"wiki-common:node_modules/core-js/internals/array-slice-simple.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-slice-simple_19f0dbb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/to-absolute-index.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/create-property.js"]},"wiki-common:node_modules/core-js/internals/object-get-own-property-names-external.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-get-own-property-names-external_3bec914.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/classof-raw.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/object-get-own-property-names.js","wiki-common:node_modules/core-js/internals/array-slice-simple.js"]},"wiki-common:node_modules/core-js/internals/well-known-symbol-wrapped.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/well-known-symbol-wrapped_e578899.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/internals/path.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/path_6015b27.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/internals/define-well-known-symbol.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/define-well-known-symbol_916d420.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/path.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/well-known-symbol-wrapped.js","wiki-common:node_modules/core-js/internals/object-define-property.js"]},"wiki-common:node_modules/core-js/internals/symbol-define-to-primitive.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/symbol-define-to-primitive_8ae90a9.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/redefine.js"]},"wiki-common:node_modules/core-js/internals/set-to-string-tag.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/set-to-string-tag_378ddb8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/internals/function-bind-context.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/function-bind-context_8d5e9e0.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/function-bind-native.js"]},"wiki-common:node_modules/core-js/internals/is-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/is-array_77cf88c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/classof-raw.js"]},"wiki-common:node_modules/core-js/internals/is-constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/is-constructor_8c2febb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/classof.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/inspect-source.js"]},"wiki-common:node_modules/core-js/internals/array-species-constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-species-constructor_2306268.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-array.js","wiki-common:node_modules/core-js/internals/is-constructor.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/internals/array-species-create.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-species-create_f4e34de.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-species-constructor.js"]},"wiki-common:node_modules/core-js/internals/array-iteration.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-iteration_f1290e2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-bind-context.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/indexed-object.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/array-species-create.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.constructor_8b07a7f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/is-pure.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/native-symbol.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/to-property-key.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/create-property-descriptor.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/object-keys.js","wiki-common:node_modules/core-js/internals/object-get-own-property-names.js","wiki-common:node_modules/core-js/internals/object-get-own-property-names-external.js","wiki-common:node_modules/core-js/internals/object-get-own-property-symbols.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/object-define-properties.js","wiki-common:node_modules/core-js/internals/object-property-is-enumerable.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/shared.js","wiki-common:node_modules/core-js/internals/shared-key.js","wiki-common:node_modules/core-js/internals/hidden-keys.js","wiki-common:node_modules/core-js/internals/uid.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/well-known-symbol-wrapped.js","wiki-common:node_modules/core-js/internals/define-well-known-symbol.js","wiki-common:node_modules/core-js/internals/symbol-define-to-primitive.js","wiki-common:node_modules/core-js/internals/set-to-string-tag.js","wiki-common:node_modules/core-js/internals/internal-state.js","wiki-common:node_modules/core-js/internals/array-iteration.js"]},"wiki-common:node_modules/core-js/internals/native-symbol-registry.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/native-symbol-registry_cab6514.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/native-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.for.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.for_51028eb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/shared.js","wiki-common:node_modules/core-js/internals/native-symbol-registry.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.key-for.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.key-for_6a1be3b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/is-symbol.js","wiki-common:node_modules/core-js/internals/try-to-string.js","wiki-common:node_modules/core-js/internals/shared.js","wiki-common:node_modules/core-js/internals/native-symbol-registry.js"]},"wiki-common:node_modules/core-js/internals/function-apply.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/function-apply_adb1077.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-bind-native.js"]},"wiki-common:node_modules/core-js/internals/array-slice.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-slice_08188b2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js"]},"wiki-common:node_modules/core-js/modules/es.json.stringify.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.json.stringify_02b54e2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/function-apply.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/is-array.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/is-symbol.js","wiki-common:node_modules/core-js/internals/array-slice.js","wiki-common:node_modules/core-js/internals/native-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.object.get-own-property-symbols.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.get-own-property-symbols_a84021a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/native-symbol.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/object-get-own-property-symbols.js","wiki-common:node_modules/core-js/internals/to-object.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol_7b96d57.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.symbol.constructor.js","wiki-common:node_modules/core-js/modules/es.symbol.for.js","wiki-common:node_modules/core-js/modules/es.symbol.key-for.js","wiki-common:node_modules/core-js/modules/es.json.stringify.js","wiki-common:node_modules/core-js/modules/es.object.get-own-property-symbols.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.description.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.description_a474d49.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/copy-constructor-properties.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.async-iterator.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.async-iterator_f60ef5b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/define-well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.has-instance.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.has-instance_0a6bde6.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/define-well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.is-concat-spreadable.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.is-concat-spreadable_f0a2600.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/define-well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.iterator.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.iterator_fd67b9a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/define-well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.match.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.match_e3d1f21.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/define-well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.match-all.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.match-all_36d78df.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/define-well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.replace.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.replace_8325b71.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/define-well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.search.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.search_56d37d9.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/define-well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.species.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.species_0da4ea3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/define-well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.split.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.split_89a144a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/define-well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.to-primitive.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.to-primitive_b0b4886.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/define-well-known-symbol.js","wiki-common:node_modules/core-js/internals/symbol-define-to-primitive.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.to-string-tag.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.to-string-tag_b6111bd.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/define-well-known-symbol.js","wiki-common:node_modules/core-js/internals/set-to-string-tag.js"]},"wiki-common:node_modules/core-js/modules/es.symbol.unscopables.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.symbol.unscopables_a89a413.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/define-well-known-symbol.js"]},"wiki-common:node_modules/core-js/internals/a-possible-prototype.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/a-possible-prototype_e82a4e3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-callable.js"]},"wiki-common:node_modules/core-js/internals/object-set-prototype-of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-set-prototype-of_794e95a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/a-possible-prototype.js"]},"wiki-common:node_modules/core-js/internals/proxy-accessor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/proxy-accessor_63131a7.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/object-define-property.js"]},"wiki-common:node_modules/core-js/internals/inherit-if-required.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/inherit-if-required_f752522.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/object-set-prototype-of.js"]},"wiki-common:node_modules/core-js/internals/normalize-string-argument.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/normalize-string-argument_7995a04.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/to-string.js"]},"wiki-common:node_modules/core-js/internals/install-error-cause.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/install-error-cause_06dc15a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js"]},"wiki-common:node_modules/core-js/internals/clear-error-stack.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/clear-error-stack_dbdcf1b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js"]},"wiki-common:node_modules/core-js/internals/error-stack-installable.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/error-stack-installable_2c9666e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/create-property-descriptor.js"]},"wiki-common:node_modules/core-js/internals/wrap-error-constructor-with-cause.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/wrap-error-constructor-with-cause_4b4e11d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js","wiki-common:node_modules/core-js/internals/object-set-prototype-of.js","wiki-common:node_modules/core-js/internals/copy-constructor-properties.js","wiki-common:node_modules/core-js/internals/proxy-accessor.js","wiki-common:node_modules/core-js/internals/inherit-if-required.js","wiki-common:node_modules/core-js/internals/normalize-string-argument.js","wiki-common:node_modules/core-js/internals/install-error-cause.js","wiki-common:node_modules/core-js/internals/clear-error-stack.js","wiki-common:node_modules/core-js/internals/error-stack-installable.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/is-pure.js"]},"wiki-common:node_modules/core-js/modules/es.error.cause.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.error.cause_902fd68.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-apply.js","wiki-common:node_modules/core-js/internals/wrap-error-constructor-with-cause.js"]},"wiki-common:node_modules/core-js/internals/error-to-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/error-to-string_b94eae4.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/normalize-string-argument.js"]},"wiki-common:node_modules/core-js/modules/es.error.to-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.error.to-string_29b1f4b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/error-to-string.js"]},"wiki-common:node_modules/core-js/internals/correct-prototype-getter.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/correct-prototype-getter_f1ad231.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/internals/object-get-prototype-of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-get-prototype-of_0da8a9c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/shared-key.js","wiki-common:node_modules/core-js/internals/correct-prototype-getter.js"]},"wiki-common:node_modules/core-js/internals/iterators.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/iterators_a718121.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/is-array-iterator-method.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/is-array-iterator-method_a7be4c4.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/iterators.js"]},"wiki-common:node_modules/core-js/internals/get-iterator-method.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/get-iterator-method_141cdbe.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/classof.js","wiki-common:node_modules/core-js/internals/get-method.js","wiki-common:node_modules/core-js/internals/iterators.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/internals/get-iterator.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/get-iterator_75d6090.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/try-to-string.js","wiki-common:node_modules/core-js/internals/get-iterator-method.js"]},"wiki-common:node_modules/core-js/internals/iterator-close.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/iterator-close_b87f97c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/get-method.js"]},"wiki-common:node_modules/core-js/internals/iterate.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/iterate_65aef68.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-bind-context.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/try-to-string.js","wiki-common:node_modules/core-js/internals/is-array-iterator-method.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js","wiki-common:node_modules/core-js/internals/get-iterator.js","wiki-common:node_modules/core-js/internals/get-iterator-method.js","wiki-common:node_modules/core-js/internals/iterator-close.js"]},"wiki-common:node_modules/core-js/modules/es.aggregate-error.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.aggregate-error.constructor_206bf29.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js","wiki-common:node_modules/core-js/internals/object-get-prototype-of.js","wiki-common:node_modules/core-js/internals/object-set-prototype-of.js","wiki-common:node_modules/core-js/internals/copy-constructor-properties.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js","wiki-common:node_modules/core-js/internals/create-property-descriptor.js","wiki-common:node_modules/core-js/internals/clear-error-stack.js","wiki-common:node_modules/core-js/internals/install-error-cause.js","wiki-common:node_modules/core-js/internals/iterate.js","wiki-common:node_modules/core-js/internals/normalize-string-argument.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/error-stack-installable.js"]},"wiki-common:node_modules/core-js/modules/es.aggregate-error.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.aggregate-error_585c756.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.aggregate-error.constructor.js"]},"wiki-common:node_modules/core-js/modules/es.aggregate-error.cause.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.aggregate-error.cause_8282393.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/function-apply.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/wrap-error-constructor-with-cause.js"]},"wiki-common:node_modules/core-js/internals/add-to-unscopables.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/add-to-unscopables_41937bb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/object-define-property.js"]},"wiki-common:node_modules/core-js/modules/es.array.at.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.at_7eaf4cb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/internals/array-method-has-species-support.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-method-has-species-support_5885c2e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/engine-v8-version.js"]},"wiki-common:node_modules/core-js/modules/es.array.concat.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.concat_fb588d7.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/is-array.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/create-property.js","wiki-common:node_modules/core-js/internals/array-species-create.js","wiki-common:node_modules/core-js/internals/array-method-has-species-support.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/engine-v8-version.js"]},"wiki-common:node_modules/core-js/internals/array-copy-within.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-copy-within_705304c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/to-absolute-index.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js"]},"wiki-common:node_modules/core-js/modules/es.array.copy-within.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.copy-within_3f83587.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-copy-within.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/internals/array-method-is-strict.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-method-is-strict_cca2d8a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.array.every.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.every_c927f33.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-iteration.js","wiki-common:node_modules/core-js/internals/array-method-is-strict.js"]},"wiki-common:node_modules/core-js/internals/array-fill.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-fill_ca8f6b8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/to-absolute-index.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js"]},"wiki-common:node_modules/core-js/modules/es.array.fill.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.fill_4373737.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-fill.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/modules/es.array.filter.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.filter_4daf99b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-iteration.js","wiki-common:node_modules/core-js/internals/array-method-has-species-support.js"]},"wiki-common:node_modules/core-js/modules/es.array.find.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.find_a9b0f48.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-iteration.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/modules/es.array.find-index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.find-index_e3c9745.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-iteration.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/internals/flatten-into-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/flatten-into-array_2196f5d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-array.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/function-bind-context.js"]},"wiki-common:node_modules/core-js/modules/es.array.flat.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.flat_3e79d5c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/flatten-into-array.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/array-species-create.js"]},"wiki-common:node_modules/core-js/modules/es.array.flat-map.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.flat-map_b03d968.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/flatten-into-array.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/array-species-create.js"]},"wiki-common:node_modules/core-js/internals/array-for-each.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-for-each_28ee895.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-iteration.js","wiki-common:node_modules/core-js/internals/array-method-is-strict.js"]},"wiki-common:node_modules/core-js/modules/es.array.for-each.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.for-each_5ba0f8c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-for-each.js"]},"wiki-common:node_modules/core-js/internals/call-with-safe-iteration-closing.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/call-with-safe-iteration-closing_448385d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/iterator-close.js"]},"wiki-common:node_modules/core-js/internals/array-from.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-from_7cbd1f6.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-bind-context.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/call-with-safe-iteration-closing.js","wiki-common:node_modules/core-js/internals/is-array-iterator-method.js","wiki-common:node_modules/core-js/internals/is-constructor.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/create-property.js","wiki-common:node_modules/core-js/internals/get-iterator.js","wiki-common:node_modules/core-js/internals/get-iterator-method.js"]},"wiki-common:node_modules/core-js/internals/check-correctness-of-iteration.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/check-correctness-of-iteration_f22978b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.array.from.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.from_e5273ae.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-from.js","wiki-common:node_modules/core-js/internals/check-correctness-of-iteration.js"]},"wiki-common:node_modules/core-js/modules/es.array.includes.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.includes_d64a996.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-includes.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/modules/es.array.index-of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.index-of_60ccd5d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/array-includes.js","wiki-common:node_modules/core-js/internals/array-method-is-strict.js"]},"wiki-common:node_modules/core-js/modules/es.array.is-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.is-array_4c2bdb5.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/is-array.js"]},"wiki-common:node_modules/core-js/internals/iterators-core.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/iterators-core_d7cfbb0.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/object-get-prototype-of.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/is-pure.js"]},"wiki-common:node_modules/core-js/internals/create-iterator-constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/create-iterator-constructor_c8f311c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/iterators-core.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/create-property-descriptor.js","wiki-common:node_modules/core-js/internals/set-to-string-tag.js","wiki-common:node_modules/core-js/internals/iterators.js"]},"wiki-common:node_modules/core-js/internals/define-iterator.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/define-iterator_abda047.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/is-pure.js","wiki-common:node_modules/core-js/internals/function-name.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/create-iterator-constructor.js","wiki-common:node_modules/core-js/internals/object-get-prototype-of.js","wiki-common:node_modules/core-js/internals/object-set-prototype-of.js","wiki-common:node_modules/core-js/internals/set-to-string-tag.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/iterators.js","wiki-common:node_modules/core-js/internals/iterators-core.js"]},"wiki-common:node_modules/core-js/modules/es.array.iterator.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.iterator_b3a247c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js","wiki-common:node_modules/core-js/internals/iterators.js","wiki-common:node_modules/core-js/internals/internal-state.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/define-iterator.js","wiki-common:node_modules/core-js/internals/is-pure.js","wiki-common:node_modules/core-js/internals/descriptors.js"]},"wiki-common:node_modules/core-js/modules/es.array.join.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.join_289ff8a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/indexed-object.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/array-method-is-strict.js"]},"wiki-common:node_modules/core-js/internals/array-last-index-of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-last-index-of_4c51a61.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-apply.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/array-method-is-strict.js"]},"wiki-common:node_modules/core-js/modules/es.array.last-index-of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.last-index-of_553ef6a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-last-index-of.js"]},"wiki-common:node_modules/core-js/modules/es.array.map.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.map_5d82dde.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-iteration.js","wiki-common:node_modules/core-js/internals/array-method-has-species-support.js"]},"wiki-common:node_modules/core-js/modules/es.array.of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.of_541d1da.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/is-constructor.js","wiki-common:node_modules/core-js/internals/create-property.js"]},"wiki-common:node_modules/core-js/internals/array-reduce.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-reduce_354a096.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/indexed-object.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js"]},"wiki-common:node_modules/core-js/internals/engine-is-node.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/engine-is-node_5ae8ea0.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/classof-raw.js","wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/modules/es.array.reduce.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.reduce_a35527d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-reduce.js","wiki-common:node_modules/core-js/internals/array-method-is-strict.js","wiki-common:node_modules/core-js/internals/engine-v8-version.js","wiki-common:node_modules/core-js/internals/engine-is-node.js"]},"wiki-common:node_modules/core-js/modules/es.array.reduce-right.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.reduce-right_1e8c08f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-reduce.js","wiki-common:node_modules/core-js/internals/array-method-is-strict.js","wiki-common:node_modules/core-js/internals/engine-v8-version.js","wiki-common:node_modules/core-js/internals/engine-is-node.js"]},"wiki-common:node_modules/core-js/modules/es.array.reverse.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.reverse_80b2bd2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/is-array.js"]},"wiki-common:node_modules/core-js/modules/es.array.slice.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.slice_36a2b20.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-array.js","wiki-common:node_modules/core-js/internals/is-constructor.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/to-absolute-index.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/create-property.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/array-method-has-species-support.js","wiki-common:node_modules/core-js/internals/array-slice.js"]},"wiki-common:node_modules/core-js/modules/es.array.some.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.some_2b5b940.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-iteration.js","wiki-common:node_modules/core-js/internals/array-method-is-strict.js"]},"wiki-common:node_modules/core-js/internals/array-sort.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-sort_7588544.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-slice-simple.js"]},"wiki-common:node_modules/core-js/internals/engine-ff-version.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/engine-ff-version_1772526.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/engine-user-agent.js"]},"wiki-common:node_modules/core-js/internals/engine-is-ie-or-edge.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/engine-is-ie-or-edge_5a7d0d6.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/engine-user-agent.js"]},"wiki-common:node_modules/core-js/internals/engine-webkit-version.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/engine-webkit-version_26986de.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/engine-user-agent.js"]},"wiki-common:node_modules/core-js/modules/es.array.sort.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.sort_9b6201f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/array-sort.js","wiki-common:node_modules/core-js/internals/array-method-is-strict.js","wiki-common:node_modules/core-js/internals/engine-ff-version.js","wiki-common:node_modules/core-js/internals/engine-is-ie-or-edge.js","wiki-common:node_modules/core-js/internals/engine-v8-version.js","wiki-common:node_modules/core-js/internals/engine-webkit-version.js"]},"wiki-common:node_modules/core-js/internals/set-species.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/set-species_07a9cad.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/descriptors.js"]},"wiki-common:node_modules/core-js/modules/es.array.species.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.species_ec8478a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/set-species.js"]},"wiki-common:node_modules/core-js/modules/es.array.splice.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.splice_20cc53f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/to-absolute-index.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/array-species-create.js","wiki-common:node_modules/core-js/internals/create-property.js","wiki-common:node_modules/core-js/internals/array-method-has-species-support.js"]},"wiki-common:node_modules/core-js/modules/es.array.unscopables.flat.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.unscopables.flat_8750094.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/modules/es.array.unscopables.flat-map.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array.unscopables.flat-map_002d7e2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/internals/array-buffer-native.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-buffer-native_647bbfd.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/redefine-all.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/redefine-all_7fbc1e2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/redefine.js"]},"wiki-common:node_modules/core-js/internals/an-instance.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/an-instance_c1b0f35.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js"]},"wiki-common:node_modules/core-js/internals/to-index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/to-index_718c5a0.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/to-length.js"]},"wiki-common:node_modules/core-js/internals/ieee754.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/ieee754_0a1a935.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/internals/array-buffer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-buffer_8bc6639.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/array-buffer-native.js","wiki-common:node_modules/core-js/internals/function-name.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js","wiki-common:node_modules/core-js/internals/redefine-all.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/an-instance.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/to-length.js","wiki-common:node_modules/core-js/internals/to-index.js","wiki-common:node_modules/core-js/internals/ieee754.js","wiki-common:node_modules/core-js/internals/object-get-prototype-of.js","wiki-common:node_modules/core-js/internals/object-set-prototype-of.js","wiki-common:node_modules/core-js/internals/object-get-own-property-names.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/array-fill.js","wiki-common:node_modules/core-js/internals/array-slice-simple.js","wiki-common:node_modules/core-js/internals/set-to-string-tag.js","wiki-common:node_modules/core-js/internals/internal-state.js"]},"wiki-common:node_modules/core-js/modules/es.array-buffer.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array-buffer.constructor_7ebcf23.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/array-buffer.js","wiki-common:node_modules/core-js/internals/set-species.js"]},"wiki-common:node_modules/core-js/internals/array-buffer-view-core.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-buffer-view-core_f57fe3f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-native.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/classof.js","wiki-common:node_modules/core-js/internals/try-to-string.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js","wiki-common:node_modules/core-js/internals/object-get-prototype-of.js","wiki-common:node_modules/core-js/internals/object-set-prototype-of.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/uid.js"]},"wiki-common:node_modules/core-js/modules/es.array-buffer.is-view.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array-buffer.is-view_f42b932.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-buffer-view-core.js"]},"wiki-common:node_modules/core-js/internals/a-constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/a-constructor_285aec3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-constructor.js","wiki-common:node_modules/core-js/internals/try-to-string.js"]},"wiki-common:node_modules/core-js/internals/species-constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/species-constructor_40443da.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/a-constructor.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.array-buffer.slice.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.array-buffer.slice_d647b49.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/array-buffer.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/to-absolute-index.js","wiki-common:node_modules/core-js/internals/to-length.js","wiki-common:node_modules/core-js/internals/species-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.data-view.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.data-view.constructor_3ca1a65.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-buffer.js","wiki-common:node_modules/core-js/internals/array-buffer-native.js"]},"wiki-common:node_modules/core-js/modules/es.data-view.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.data-view_7e4ba08.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.data-view.constructor.js"]},"wiki-common:node_modules/core-js/modules/es.date.get-year.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.date.get-year_7d72a1c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.date.now.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.date.now_9b1764e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js"]},"wiki-common:node_modules/core-js/modules/es.date.set-year.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.date.set-year_7c8ceb4.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js"]},"wiki-common:node_modules/core-js/modules/es.date.to-gmt-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.date.to-gmt-string_8d6189a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js"]},"wiki-common:node_modules/core-js/internals/string-repeat.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/string-repeat_9025252.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js"]},"wiki-common:node_modules/core-js/internals/string-pad.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/string-pad_0b7af37.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-length.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/string-repeat.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js"]},"wiki-common:node_modules/core-js/internals/date-to-iso-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/date-to-iso-string_e236533.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/string-pad.js"]},"wiki-common:node_modules/core-js/modules/es.date.to-iso-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.date.to-iso-string_b7587a5.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/date-to-iso-string.js"]},"wiki-common:node_modules/core-js/modules/es.date.to-json.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.date.to-json_940e22e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/to-primitive.js"]},"wiki-common:node_modules/core-js/internals/date-to-primitive.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/date-to-primitive_a8fbfba.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/ordinary-to-primitive.js"]},"wiki-common:node_modules/core-js/modules/es.date.to-primitive.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.date.to-primitive_0998f20.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/date-to-primitive.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.date.to-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.date.to-string_1eb052c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/redefine.js"]},"wiki-common:node_modules/core-js/modules/es.escape.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.escape_0be797e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-string.js"]},"wiki-common:node_modules/core-js/internals/function-bind.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/function-bind_e13df08.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/array-slice.js","wiki-common:node_modules/core-js/internals/function-bind-native.js"]},"wiki-common:node_modules/core-js/modules/es.function.bind.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.function.bind_50205b8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-bind.js"]},"wiki-common:node_modules/core-js/modules/es.function.has-instance.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.function.has-instance_2092609.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/object-get-prototype-of.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.function.name.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.function.name_bcb5835.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/function-name.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/object-define-property.js"]},"wiki-common:node_modules/core-js/modules/es.global-this.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.global-this_bd06339.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/modules/es.json.to-string-tag.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.json.to-string-tag_6cd48cd.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/set-to-string-tag.js"]},"wiki-common:node_modules/core-js/internals/array-buffer-non-extensible.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-buffer-non-extensible_93b85a0.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/internals/object-is-extensible.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-is-extensible_3f71a7e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/classof-raw.js","wiki-common:node_modules/core-js/internals/array-buffer-non-extensible.js"]},"wiki-common:node_modules/core-js/internals/freezing.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/freezing_5135e5d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/internals/internal-metadata.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/internal-metadata_59b56fa.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/hidden-keys.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/object-get-own-property-names.js","wiki-common:node_modules/core-js/internals/object-get-own-property-names-external.js","wiki-common:node_modules/core-js/internals/object-is-extensible.js","wiki-common:node_modules/core-js/internals/uid.js","wiki-common:node_modules/core-js/internals/freezing.js"]},"wiki-common:node_modules/core-js/internals/collection.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/collection_bdb81fb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/is-forced.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/internal-metadata.js","wiki-common:node_modules/core-js/internals/iterate.js","wiki-common:node_modules/core-js/internals/an-instance.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/check-correctness-of-iteration.js","wiki-common:node_modules/core-js/internals/set-to-string-tag.js","wiki-common:node_modules/core-js/internals/inherit-if-required.js"]},"wiki-common:node_modules/core-js/internals/collection-strong.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/collection-strong_1354220.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/redefine-all.js","wiki-common:node_modules/core-js/internals/function-bind-context.js","wiki-common:node_modules/core-js/internals/an-instance.js","wiki-common:node_modules/core-js/internals/iterate.js","wiki-common:node_modules/core-js/internals/define-iterator.js","wiki-common:node_modules/core-js/internals/set-species.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/internal-metadata.js","wiki-common:node_modules/core-js/internals/internal-state.js"]},"wiki-common:node_modules/core-js/modules/es.map.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.map.constructor_e0dfb7a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/collection.js","wiki-common:node_modules/core-js/internals/collection-strong.js"]},"wiki-common:node_modules/core-js/modules/es.map.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.map_cc48442.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.map.constructor.js"]},"wiki-common:node_modules/core-js/internals/math-log1p.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/math-log1p_2f1cb1d.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/modules/es.math.acosh.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.acosh_123fed5.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/math-log1p.js"]},"wiki-common:node_modules/core-js/modules/es.math.asinh.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.asinh_0d71fce.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js"]},"wiki-common:node_modules/core-js/modules/es.math.atanh.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.atanh_e3ffcb2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js"]},"wiki-common:node_modules/core-js/internals/math-sign.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/math-sign_553fed7.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/modules/es.math.cbrt.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.cbrt_69d888d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/math-sign.js"]},"wiki-common:node_modules/core-js/modules/es.math.clz32.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.clz32_6f2ee25.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js"]},"wiki-common:node_modules/core-js/internals/math-expm1.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/math-expm1_cf6de05.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/modules/es.math.cosh.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.cosh_4dc9057.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/math-expm1.js"]},"wiki-common:node_modules/core-js/modules/es.math.expm1.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.expm1_3781a71.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/math-expm1.js"]},"wiki-common:node_modules/core-js/internals/math-fround.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/math-fround_8da8777.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/math-sign.js"]},"wiki-common:node_modules/core-js/modules/es.math.fround.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.fround_db175e6.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/math-fround.js"]},"wiki-common:node_modules/core-js/modules/es.math.hypot.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.hypot_7b2403c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js"]},"wiki-common:node_modules/core-js/modules/es.math.imul.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.imul_9522f27.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/internals/math-log10.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/math-log10_4255cda.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/modules/es.math.log10.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.log10_18d3164.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/math-log10.js"]},"wiki-common:node_modules/core-js/modules/es.math.log1p.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.log1p_4980e40.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/math-log1p.js"]},"wiki-common:node_modules/core-js/modules/es.math.log2.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.log2_0247c97.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js"]},"wiki-common:node_modules/core-js/modules/es.math.sign.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.sign_3b1a55f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/math-sign.js"]},"wiki-common:node_modules/core-js/modules/es.math.sinh.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.sinh_59b25c7.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/math-expm1.js"]},"wiki-common:node_modules/core-js/modules/es.math.tanh.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.tanh_7aea91e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/math-expm1.js"]},"wiki-common:node_modules/core-js/modules/es.math.to-string-tag.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.to-string-tag_fb4d12b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/set-to-string-tag.js"]},"wiki-common:node_modules/core-js/modules/es.math.trunc.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.math.trunc_c0cfcde.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js"]},"wiki-common:node_modules/core-js/internals/this-number-value.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/this-number-value_3f64485.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js"]},"wiki-common:node_modules/core-js/internals/whitespaces.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/whitespaces_93caf8e.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/string-trim.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/string-trim_b70c4a5.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/whitespaces.js"]},"wiki-common:node_modules/core-js/modules/es.number.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.constructor_cabf404.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/is-forced.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/inherit-if-required.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js","wiki-common:node_modules/core-js/internals/is-symbol.js","wiki-common:node_modules/core-js/internals/to-primitive.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/object-get-own-property-names.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/this-number-value.js","wiki-common:node_modules/core-js/internals/string-trim.js"]},"wiki-common:node_modules/core-js/modules/es.number.epsilon.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.epsilon_f9cb3b2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js"]},"wiki-common:node_modules/core-js/internals/number-is-finite.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/number-is-finite_6906c22.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/modules/es.number.is-finite.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.is-finite_65e41c1.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/number-is-finite.js"]},"wiki-common:node_modules/core-js/internals/is-integral-number.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/is-integral-number_7ef80ab.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/is-object.js"]},"wiki-common:node_modules/core-js/modules/es.number.is-integer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.is-integer_5072aa3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/is-integral-number.js"]},"wiki-common:node_modules/core-js/modules/es.number.is-nan.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.is-nan_b0f92ce.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js"]},"wiki-common:node_modules/core-js/modules/es.number.is-safe-integer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.is-safe-integer_c0c53fc.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/is-integral-number.js"]},"wiki-common:node_modules/core-js/modules/es.number.max-safe-integer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.max-safe-integer_20a1e47.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js"]},"wiki-common:node_modules/core-js/modules/es.number.min-safe-integer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.min-safe-integer_b9aebdb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js"]},"wiki-common:node_modules/core-js/internals/number-parse-float.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/number-parse-float_ea33245.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/string-trim.js","wiki-common:node_modules/core-js/internals/whitespaces.js"]},"wiki-common:node_modules/core-js/modules/es.number.parse-float.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.parse-float_422223d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/number-parse-float.js"]},"wiki-common:node_modules/core-js/internals/number-parse-int.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/number-parse-int_dbde224.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/string-trim.js","wiki-common:node_modules/core-js/internals/whitespaces.js"]},"wiki-common:node_modules/core-js/modules/es.number.parse-int.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.parse-int_b33136d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/number-parse-int.js"]},"wiki-common:node_modules/core-js/modules/es.number.to-exponential.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.to-exponential_575b0d5.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/this-number-value.js","wiki-common:node_modules/core-js/internals/string-repeat.js","wiki-common:node_modules/core-js/internals/math-log10.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.number.to-fixed.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.to-fixed_24a9d02.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/this-number-value.js","wiki-common:node_modules/core-js/internals/string-repeat.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.number.to-precision.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.number.to-precision_f58c6fa.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/this-number-value.js"]},"wiki-common:node_modules/core-js/internals/object-assign.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-assign_f6df448.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/object-keys.js","wiki-common:node_modules/core-js/internals/object-get-own-property-symbols.js","wiki-common:node_modules/core-js/internals/object-property-is-enumerable.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/indexed-object.js"]},"wiki-common:node_modules/core-js/modules/es.object.assign.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.assign_8e2c175.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/object-assign.js"]},"wiki-common:node_modules/core-js/modules/es.object.create.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.create_716d0a4.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/object-create.js"]},"wiki-common:node_modules/core-js/internals/object-prototype-accessors-forced.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-prototype-accessors-forced_4f43488.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/is-pure.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/engine-webkit-version.js"]},"wiki-common:node_modules/core-js/modules/es.object.define-getter.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.define-getter_16421ff.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/object-prototype-accessors-forced.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/object-define-property.js"]},"wiki-common:node_modules/core-js/modules/es.object.define-properties.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.define-properties_3c6cbed.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/object-define-properties.js"]},"wiki-common:node_modules/core-js/modules/es.object.define-property.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.define-property_2979956.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/object-define-property.js"]},"wiki-common:node_modules/core-js/modules/es.object.define-setter.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.define-setter_d2cfda3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/object-prototype-accessors-forced.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/object-define-property.js"]},"wiki-common:node_modules/core-js/internals/object-to-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-to-array_9cbad67.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/object-keys.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/object-property-is-enumerable.js"]},"wiki-common:node_modules/core-js/modules/es.object.entries.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.entries_9db569e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/object-to-array.js"]},"wiki-common:node_modules/core-js/modules/es.object.freeze.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.freeze_6b78812.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/freezing.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/internal-metadata.js"]},"wiki-common:node_modules/core-js/modules/es.object.from-entries.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.from-entries_a25d72e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/iterate.js","wiki-common:node_modules/core-js/internals/create-property.js"]},"wiki-common:node_modules/core-js/modules/es.object.get-own-property-descriptor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.get-own-property-descriptor_8758ac0.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js","wiki-common:node_modules/core-js/internals/descriptors.js"]},"wiki-common:node_modules/core-js/modules/es.object.get-own-property-descriptors.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.get-own-property-descriptors_0a977da.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/own-keys.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js","wiki-common:node_modules/core-js/internals/create-property.js"]},"wiki-common:node_modules/core-js/modules/es.object.get-own-property-names.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.get-own-property-names_006c115.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/object-get-own-property-names-external.js"]},"wiki-common:node_modules/core-js/modules/es.object.get-prototype-of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.get-prototype-of_f57128c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/object-get-prototype-of.js","wiki-common:node_modules/core-js/internals/correct-prototype-getter.js"]},"wiki-common:node_modules/core-js/modules/es.object.has-own.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.has-own_b071277.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/has-own-property.js"]},"wiki-common:node_modules/core-js/internals/same-value.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/same-value_8ca6291.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/modules/es.object.is.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.is_163f91d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/same-value.js"]},"wiki-common:node_modules/core-js/modules/es.object.is-extensible.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.is-extensible_a886f43.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/object-is-extensible.js"]},"wiki-common:node_modules/core-js/modules/es.object.is-frozen.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.is-frozen_35f8330.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/classof-raw.js","wiki-common:node_modules/core-js/internals/array-buffer-non-extensible.js"]},"wiki-common:node_modules/core-js/modules/es.object.is-sealed.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.is-sealed_a36296e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/classof-raw.js","wiki-common:node_modules/core-js/internals/array-buffer-non-extensible.js"]},"wiki-common:node_modules/core-js/modules/es.object.keys.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.keys_bba22e3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/object-keys.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.object.lookup-getter.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.lookup-getter_26bddaf.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/object-prototype-accessors-forced.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/to-property-key.js","wiki-common:node_modules/core-js/internals/object-get-prototype-of.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js"]},"wiki-common:node_modules/core-js/modules/es.object.lookup-setter.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.lookup-setter_78c6d2a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/object-prototype-accessors-forced.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/to-property-key.js","wiki-common:node_modules/core-js/internals/object-get-prototype-of.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js"]},"wiki-common:node_modules/core-js/modules/es.object.prevent-extensions.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.prevent-extensions_07d4834.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/internal-metadata.js","wiki-common:node_modules/core-js/internals/freezing.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.object.seal.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.seal_1f4340e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/internal-metadata.js","wiki-common:node_modules/core-js/internals/freezing.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.object.set-prototype-of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.set-prototype-of_e9d4c69.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/object-set-prototype-of.js"]},"wiki-common:node_modules/core-js/internals/object-to-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/object-to-string_f5972f7.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/to-string-tag-support.js","wiki-common:node_modules/core-js/internals/classof.js"]},"wiki-common:node_modules/core-js/modules/es.object.to-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.to-string_73fa712.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/to-string-tag-support.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/object-to-string.js"]},"wiki-common:node_modules/core-js/modules/es.object.values.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.object.values_9d296d4.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/object-to-array.js"]},"wiki-common:node_modules/core-js/modules/es.parse-float.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.parse-float_303774d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/number-parse-float.js"]},"wiki-common:node_modules/core-js/modules/es.parse-int.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.parse-int_b5a01cb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/number-parse-int.js"]},"wiki-common:node_modules/core-js/internals/validate-arguments-length.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/validate-arguments-length_3730cb4.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/internals/engine-is-ios.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/engine-is-ios_cf9a544.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/engine-user-agent.js"]},"wiki-common:node_modules/core-js/internals/task.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/task_728e735.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-apply.js","wiki-common:node_modules/core-js/internals/function-bind-context.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/html.js","wiki-common:node_modules/core-js/internals/array-slice.js","wiki-common:node_modules/core-js/internals/document-create-element.js","wiki-common:node_modules/core-js/internals/validate-arguments-length.js","wiki-common:node_modules/core-js/internals/engine-is-ios.js","wiki-common:node_modules/core-js/internals/engine-is-node.js"]},"wiki-common:node_modules/core-js/internals/engine-is-ios-pebble.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/engine-is-ios-pebble_30893cc.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/engine-user-agent.js","wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/internals/engine-is-webos-webkit.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/engine-is-webos-webkit_fcccec3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/engine-user-agent.js"]},"wiki-common:node_modules/core-js/internals/microtask.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/microtask_afa463b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-bind-context.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js","wiki-common:node_modules/core-js/internals/task.js","wiki-common:node_modules/core-js/internals/engine-is-ios.js","wiki-common:node_modules/core-js/internals/engine-is-ios-pebble.js","wiki-common:node_modules/core-js/internals/engine-is-webos-webkit.js","wiki-common:node_modules/core-js/internals/engine-is-node.js"]},"wiki-common:node_modules/core-js/internals/host-report-errors.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/host-report-errors_07a9d61.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/internals/perform.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/perform_b62d9a8.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/queue.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/queue_fb81197.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/promise-native-constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/promise-native-constructor_34baeec.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/internals/engine-is-browser.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/engine-is-browser_7b15a51.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/promise-constructor-detection.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/promise-constructor-detection_3259bef.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/promise-native-constructor.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/is-forced.js","wiki-common:node_modules/core-js/internals/inspect-source.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/engine-is-browser.js","wiki-common:node_modules/core-js/internals/is-pure.js","wiki-common:node_modules/core-js/internals/engine-v8-version.js"]},"wiki-common:node_modules/core-js/internals/new-promise-capability.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/new-promise-capability_f6e40a6.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/a-callable.js"]},"wiki-common:node_modules/core-js/modules/es.promise.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.promise.constructor_00b9192.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/is-pure.js","wiki-common:node_modules/core-js/internals/engine-is-node.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/redefine-all.js","wiki-common:node_modules/core-js/internals/object-set-prototype-of.js","wiki-common:node_modules/core-js/internals/set-to-string-tag.js","wiki-common:node_modules/core-js/internals/set-species.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/an-instance.js","wiki-common:node_modules/core-js/internals/species-constructor.js","wiki-common:node_modules/core-js/internals/task.js","wiki-common:node_modules/core-js/internals/microtask.js","wiki-common:node_modules/core-js/internals/host-report-errors.js","wiki-common:node_modules/core-js/internals/perform.js","wiki-common:node_modules/core-js/internals/queue.js","wiki-common:node_modules/core-js/internals/internal-state.js","wiki-common:node_modules/core-js/internals/promise-native-constructor.js","wiki-common:node_modules/core-js/internals/promise-constructor-detection.js","wiki-common:node_modules/core-js/internals/new-promise-capability.js"]},"wiki-common:node_modules/core-js/internals/promise-statics-incorrect-iteration.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/promise-statics-incorrect-iteration_3aacd44.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/promise-native-constructor.js","wiki-common:node_modules/core-js/internals/check-correctness-of-iteration.js","wiki-common:node_modules/core-js/internals/promise-constructor-detection.js"]},"wiki-common:node_modules/core-js/modules/es.promise.all.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.promise.all_682eef7.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/new-promise-capability.js","wiki-common:node_modules/core-js/internals/perform.js","wiki-common:node_modules/core-js/internals/iterate.js","wiki-common:node_modules/core-js/internals/promise-statics-incorrect-iteration.js"]},"wiki-common:node_modules/core-js/modules/es.promise.catch.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.promise.catch_d450806.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/is-pure.js","wiki-common:node_modules/core-js/internals/promise-constructor-detection.js","wiki-common:node_modules/core-js/internals/promise-native-constructor.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/redefine.js"]},"wiki-common:node_modules/core-js/modules/es.promise.race.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.promise.race_3f969d0.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/new-promise-capability.js","wiki-common:node_modules/core-js/internals/perform.js","wiki-common:node_modules/core-js/internals/iterate.js","wiki-common:node_modules/core-js/internals/promise-statics-incorrect-iteration.js"]},"wiki-common:node_modules/core-js/modules/es.promise.reject.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.promise.reject_218ebf8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/new-promise-capability.js","wiki-common:node_modules/core-js/internals/promise-constructor-detection.js"]},"wiki-common:node_modules/core-js/internals/promise-resolve.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/promise-resolve_d47a9d2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/new-promise-capability.js"]},"wiki-common:node_modules/core-js/modules/es.promise.resolve.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.promise.resolve_67d60d6.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/is-pure.js","wiki-common:node_modules/core-js/internals/promise-native-constructor.js","wiki-common:node_modules/core-js/internals/promise-constructor-detection.js","wiki-common:node_modules/core-js/internals/promise-resolve.js"]},"wiki-common:node_modules/core-js/modules/es.promise.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.promise_d269b96.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.promise.constructor.js","wiki-common:node_modules/core-js/modules/es.promise.all.js","wiki-common:node_modules/core-js/modules/es.promise.catch.js","wiki-common:node_modules/core-js/modules/es.promise.race.js","wiki-common:node_modules/core-js/modules/es.promise.reject.js","wiki-common:node_modules/core-js/modules/es.promise.resolve.js"]},"wiki-common:node_modules/core-js/modules/es.promise.all-settled.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.promise.all-settled_eb2a6a4.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/new-promise-capability.js","wiki-common:node_modules/core-js/internals/perform.js","wiki-common:node_modules/core-js/internals/iterate.js"]},"wiki-common:node_modules/core-js/modules/es.promise.any.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.promise.any_333e5eb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/new-promise-capability.js","wiki-common:node_modules/core-js/internals/perform.js","wiki-common:node_modules/core-js/internals/iterate.js"]},"wiki-common:node_modules/core-js/modules/es.promise.finally.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.promise.finally_3b6d0d3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/is-pure.js","wiki-common:node_modules/core-js/internals/promise-native-constructor.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/species-constructor.js","wiki-common:node_modules/core-js/internals/promise-resolve.js","wiki-common:node_modules/core-js/internals/redefine.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.apply.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.apply_aadc8ad.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-apply.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.construct.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.construct_984ca5c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/function-apply.js","wiki-common:node_modules/core-js/internals/function-bind.js","wiki-common:node_modules/core-js/internals/a-constructor.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.define-property.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.define-property_4753cfb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/to-property-key.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.delete-property.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.delete-property_6177df0.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js"]},"wiki-common:node_modules/core-js/internals/is-data-descriptor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/is-data-descriptor_233b465.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/has-own-property.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.get.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.get_ef09082.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/is-data-descriptor.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js","wiki-common:node_modules/core-js/internals/object-get-prototype-of.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.get-own-property-descriptor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.get-own-property-descriptor_3e8dc76.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.get-prototype-of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.get-prototype-of_f5da21a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/object-get-prototype-of.js","wiki-common:node_modules/core-js/internals/correct-prototype-getter.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.has.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.has_5789edb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.is-extensible.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.is-extensible_34ac7cc.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/object-is-extensible.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.own-keys.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.own-keys_e9b2910.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/own-keys.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.prevent-extensions.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.prevent-extensions_7939841.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/freezing.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.set.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.set_abe8ad1.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/is-data-descriptor.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js","wiki-common:node_modules/core-js/internals/object-get-prototype-of.js","wiki-common:node_modules/core-js/internals/create-property-descriptor.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.set-prototype-of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.set-prototype-of_11e7935.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/a-possible-prototype.js","wiki-common:node_modules/core-js/internals/object-set-prototype-of.js"]},"wiki-common:node_modules/core-js/modules/es.reflect.to-string-tag.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.reflect.to-string-tag_2f890f4.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/set-to-string-tag.js"]},"wiki-common:node_modules/core-js/internals/is-regexp.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/is-regexp_2a72148.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/classof-raw.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/internals/regexp-flags.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/regexp-flags_28abda6.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/an-object.js"]},"wiki-common:node_modules/core-js/internals/regexp-sticky-helpers.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/regexp-sticky-helpers_81cc75c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/internals/regexp-unsupported-dot-all.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/regexp-unsupported-dot-all_e04f6a6.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/internals/regexp-unsupported-ncg.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/regexp-unsupported-ncg_c62f246.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/modules/es.regexp.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.regexp.constructor_ab1e5b8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/is-forced.js","wiki-common:node_modules/core-js/internals/inherit-if-required.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js","wiki-common:node_modules/core-js/internals/object-get-own-property-names.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js","wiki-common:node_modules/core-js/internals/is-regexp.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/regexp-flags.js","wiki-common:node_modules/core-js/internals/regexp-sticky-helpers.js","wiki-common:node_modules/core-js/internals/proxy-accessor.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/internal-state.js","wiki-common:node_modules/core-js/internals/set-species.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/regexp-unsupported-dot-all.js","wiki-common:node_modules/core-js/internals/regexp-unsupported-ncg.js"]},"wiki-common:node_modules/core-js/modules/es.regexp.dot-all.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.regexp.dot-all_6ce6cb9.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/regexp-unsupported-dot-all.js","wiki-common:node_modules/core-js/internals/classof-raw.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/internal-state.js"]},"wiki-common:node_modules/core-js/internals/regexp-exec.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/regexp-exec_cd24282.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/regexp-flags.js","wiki-common:node_modules/core-js/internals/regexp-sticky-helpers.js","wiki-common:node_modules/core-js/internals/shared.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/internal-state.js","wiki-common:node_modules/core-js/internals/regexp-unsupported-dot-all.js","wiki-common:node_modules/core-js/internals/regexp-unsupported-ncg.js"]},"wiki-common:node_modules/core-js/modules/es.regexp.exec.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.regexp.exec_bfcd595.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/regexp-exec.js"]},"wiki-common:node_modules/core-js/modules/es.regexp.flags.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.regexp.flags_591d580.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/regexp-flags.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.regexp.sticky.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.regexp.sticky_2937528.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/regexp-sticky-helpers.js","wiki-common:node_modules/core-js/internals/classof-raw.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/internal-state.js"]},"wiki-common:node_modules/core-js/modules/es.regexp.test.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.regexp.test_13d3408.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.regexp.exec.js","wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/is-object.js"]},"wiki-common:node_modules/core-js/modules/es.regexp.to-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.regexp.to-string_8a4c442.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/function-name.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/regexp-flags.js"]},"wiki-common:node_modules/core-js/modules/es.set.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.set.constructor_a7e07a9.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/collection.js","wiki-common:node_modules/core-js/internals/collection-strong.js"]},"wiki-common:node_modules/core-js/modules/es.set.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.set_cd62625.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.set.constructor.js"]},"wiki-common:node_modules/core-js/modules/es.string.at-alternative.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.at-alternative_fef035b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/internals/string-multibyte.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/string-multibyte_898ff36.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js"]},"wiki-common:node_modules/core-js/modules/es.string.code-point-at.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.code-point-at_d603a13.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/string-multibyte.js"]},"wiki-common:node_modules/core-js/internals/not-a-regexp.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/not-a-regexp_c51ddb8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/is-regexp.js"]},"wiki-common:node_modules/core-js/internals/correct-is-regexp-logic.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/correct-is-regexp-logic_8d46d48.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.string.ends-with.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.ends-with_5acb64e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js","wiki-common:node_modules/core-js/internals/to-length.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/not-a-regexp.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/correct-is-regexp-logic.js","wiki-common:node_modules/core-js/internals/is-pure.js"]},"wiki-common:node_modules/core-js/modules/es.string.from-code-point.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.from-code-point_669311a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-absolute-index.js"]},"wiki-common:node_modules/core-js/modules/es.string.includes.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.includes_c1968b5.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/not-a-regexp.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/correct-is-regexp-logic.js"]},"wiki-common:node_modules/core-js/modules/es.string.iterator.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.iterator_5d98cfa.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/string-multibyte.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/internal-state.js","wiki-common:node_modules/core-js/internals/define-iterator.js"]},"wiki-common:node_modules/core-js/internals/fix-regexp-well-known-symbol-logic.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/fix-regexp-well-known-symbol-logic_85a7f24.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.regexp.exec.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/regexp-exec.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js"]},"wiki-common:node_modules/core-js/internals/advance-string-index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/advance-string-index_5cdfa0c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/string-multibyte.js"]},"wiki-common:node_modules/core-js/internals/regexp-exec-abstract.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/regexp-exec-abstract_ecc753f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/classof-raw.js","wiki-common:node_modules/core-js/internals/regexp-exec.js"]},"wiki-common:node_modules/core-js/modules/es.string.match.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.match_63cea63.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/fix-regexp-well-known-symbol-logic.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/to-length.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/get-method.js","wiki-common:node_modules/core-js/internals/advance-string-index.js","wiki-common:node_modules/core-js/internals/regexp-exec-abstract.js"]},"wiki-common:node_modules/core-js/modules/es.string.match-all.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.match-all_e7b5f11.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/create-iterator-constructor.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/to-length.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/classof-raw.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js","wiki-common:node_modules/core-js/internals/is-regexp.js","wiki-common:node_modules/core-js/internals/regexp-flags.js","wiki-common:node_modules/core-js/internals/get-method.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/species-constructor.js","wiki-common:node_modules/core-js/internals/advance-string-index.js","wiki-common:node_modules/core-js/internals/regexp-exec-abstract.js","wiki-common:node_modules/core-js/internals/internal-state.js","wiki-common:node_modules/core-js/internals/is-pure.js"]},"wiki-common:node_modules/core-js/internals/string-pad-webkit-bug.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/string-pad-webkit-bug_758f39b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/engine-user-agent.js"]},"wiki-common:node_modules/core-js/modules/es.string.pad-end.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.pad-end_58d0a7b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/string-pad.js","wiki-common:node_modules/core-js/internals/string-pad-webkit-bug.js"]},"wiki-common:node_modules/core-js/modules/es.string.pad-start.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.pad-start_fc6041c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/string-pad.js","wiki-common:node_modules/core-js/internals/string-pad-webkit-bug.js"]},"wiki-common:node_modules/core-js/modules/es.string.raw.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.raw_bd3810d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js"]},"wiki-common:node_modules/core-js/modules/es.string.repeat.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.repeat_1e6645f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/string-repeat.js"]},"wiki-common:node_modules/core-js/internals/get-substitution.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/get-substitution_6e270c4.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-object.js"]},"wiki-common:node_modules/core-js/modules/es.string.replace.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.replace_f925a44.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-apply.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fix-regexp-well-known-symbol-logic.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/to-length.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/advance-string-index.js","wiki-common:node_modules/core-js/internals/get-method.js","wiki-common:node_modules/core-js/internals/get-substitution.js","wiki-common:node_modules/core-js/internals/regexp-exec-abstract.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.string.replace-all.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.replace-all_94955b3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/is-regexp.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/get-method.js","wiki-common:node_modules/core-js/internals/regexp-flags.js","wiki-common:node_modules/core-js/internals/get-substitution.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/is-pure.js"]},"wiki-common:node_modules/core-js/modules/es.string.search.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.search_58253cc.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/fix-regexp-well-known-symbol-logic.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/same-value.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/get-method.js","wiki-common:node_modules/core-js/internals/regexp-exec-abstract.js"]},"wiki-common:node_modules/core-js/modules/es.string.split.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.split_07a5dad.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-apply.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fix-regexp-well-known-symbol-logic.js","wiki-common:node_modules/core-js/internals/is-regexp.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/species-constructor.js","wiki-common:node_modules/core-js/internals/advance-string-index.js","wiki-common:node_modules/core-js/internals/to-length.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/get-method.js","wiki-common:node_modules/core-js/internals/array-slice-simple.js","wiki-common:node_modules/core-js/internals/regexp-exec-abstract.js","wiki-common:node_modules/core-js/internals/regexp-exec.js","wiki-common:node_modules/core-js/internals/regexp-sticky-helpers.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.string.starts-with.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.starts-with_8a8b99d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js","wiki-common:node_modules/core-js/internals/to-length.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/not-a-regexp.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/correct-is-regexp-logic.js","wiki-common:node_modules/core-js/internals/is-pure.js"]},"wiki-common:node_modules/core-js/modules/es.string.substr.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.substr_a358f06.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js","wiki-common:node_modules/core-js/internals/to-string.js"]},"wiki-common:node_modules/core-js/internals/string-trim-forced.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/string-trim-forced_c2bc762.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-name.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/whitespaces.js"]},"wiki-common:node_modules/core-js/modules/es.string.trim.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.trim_2958379.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/string-trim.js","wiki-common:node_modules/core-js/internals/string-trim-forced.js"]},"wiki-common:node_modules/core-js/internals/string-trim-end.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/string-trim-end_3d26931.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/string-trim.js","wiki-common:node_modules/core-js/internals/string-trim-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.trim-right.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.trim-right_40c1834.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/string-trim-end.js"]},"wiki-common:node_modules/core-js/modules/es.string.trim-end.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.trim-end_45fbb43.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.string.trim-right.js","wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/string-trim-end.js"]},"wiki-common:node_modules/core-js/internals/string-trim-start.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/string-trim-start_cf240d2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/string-trim.js","wiki-common:node_modules/core-js/internals/string-trim-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.trim-left.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.trim-left_3da0f76.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/string-trim-start.js"]},"wiki-common:node_modules/core-js/modules/es.string.trim-start.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.trim-start_5e74826.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.string.trim-left.js","wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/string-trim-start.js"]},"wiki-common:node_modules/core-js/internals/create-html.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/create-html_b685575.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/require-object-coercible.js","wiki-common:node_modules/core-js/internals/to-string.js"]},"wiki-common:node_modules/core-js/internals/string-html-forced.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/string-html-forced_abac593.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.string.anchor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.anchor_eaaec1d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.big.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.big_c79f406.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.blink.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.blink_a813d78.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.bold.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.bold_7a397d8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.fixed.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.fixed_8fe925f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.fontcolor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.fontcolor_14ef388.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.fontsize.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.fontsize_2be9445.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.italics.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.italics_55ea20e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.link.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.link_56b27b2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.small.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.small_87f2e23.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.strike.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.strike_cf8d376.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.sub.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.sub_e40429a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/modules/es.string.sup.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.string.sup_7de6ca5.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/create-html.js","wiki-common:node_modules/core-js/internals/string-html-forced.js"]},"wiki-common:node_modules/core-js/internals/typed-array-constructors-require-wrappers.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/typed-array-constructors-require-wrappers_c3918c7.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/check-correctness-of-iteration.js","wiki-common:node_modules/core-js/internals/array-buffer-view-core.js"]},"wiki-common:node_modules/core-js/internals/to-positive-integer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/to-positive-integer_09dd640.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js"]},"wiki-common:node_modules/core-js/internals/to-offset.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/to-offset_9f10cd9.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/to-positive-integer.js"]},"wiki-common:node_modules/core-js/internals/typed-array-from.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/typed-array-from_d7f04e5.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-bind-context.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/a-constructor.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/get-iterator.js","wiki-common:node_modules/core-js/internals/get-iterator-method.js","wiki-common:node_modules/core-js/internals/is-array-iterator-method.js","wiki-common:node_modules/core-js/internals/array-buffer-view-core.js"]},"wiki-common:node_modules/core-js/internals/typed-array-constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/typed-array-constructor_f5be60d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/typed-array-constructors-require-wrappers.js","wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-buffer.js","wiki-common:node_modules/core-js/internals/an-instance.js","wiki-common:node_modules/core-js/internals/create-property-descriptor.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js","wiki-common:node_modules/core-js/internals/is-integral-number.js","wiki-common:node_modules/core-js/internals/to-length.js","wiki-common:node_modules/core-js/internals/to-index.js","wiki-common:node_modules/core-js/internals/to-offset.js","wiki-common:node_modules/core-js/internals/to-property-key.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/classof.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/is-symbol.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/object-is-prototype-of.js","wiki-common:node_modules/core-js/internals/object-set-prototype-of.js","wiki-common:node_modules/core-js/internals/object-get-own-property-names.js","wiki-common:node_modules/core-js/internals/typed-array-from.js","wiki-common:node_modules/core-js/internals/array-iteration.js","wiki-common:node_modules/core-js/internals/set-species.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/object-get-own-property-descriptor.js","wiki-common:node_modules/core-js/internals/internal-state.js","wiki-common:node_modules/core-js/internals/inherit-if-required.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.float32-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.float32-array_6b15318.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/typed-array-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.float64-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.float64-array_aa51933.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/typed-array-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.int8-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.int8-array_2acbfa8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/typed-array-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.int16-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.int16-array_99245c2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/typed-array-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.int32-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.int32-array_c81f443.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/typed-array-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.uint8-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.uint8-array_f8e0a27.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/typed-array-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.uint8-clamped-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.uint8-clamped-array_449065b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/typed-array-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.uint16-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.uint16-array_d38d132.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/typed-array-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.uint32-array.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.uint32-array_25a078d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/typed-array-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.at.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.at_fb72b18.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.copy-within.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.copy-within_d9bbbab.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-copy-within.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.every.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.every_1e414d0.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-iteration.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.fill.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.fill_051f744.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/array-fill.js"]},"wiki-common:node_modules/core-js/internals/array-from-constructor-and-list.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-from-constructor-and-list_0c04e2f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/length-of-array-like.js"]},"wiki-common:node_modules/core-js/internals/typed-array-species-constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/typed-array-species-constructor_d643896.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/species-constructor.js"]},"wiki-common:node_modules/core-js/internals/typed-array-from-species-and-list.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/typed-array-from-species-and-list_d9898fa.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-from-constructor-and-list.js","wiki-common:node_modules/core-js/internals/typed-array-species-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.filter.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.filter_3391645.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-iteration.js","wiki-common:node_modules/core-js/internals/typed-array-from-species-and-list.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.find.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.find_3b57b64.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-iteration.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.find-index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.find-index_363f7c9.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-iteration.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.for-each.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.for-each_1d5b0e1.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-iteration.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.from.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.from_2e452d4.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/typed-array-constructors-require-wrappers.js","wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/typed-array-from.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.includes.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.includes_ae1366e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-includes.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.index-of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.index-of_00ccae1.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-includes.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.iterator.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.iterator_e9e8383.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/modules/es.array.iterator.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.join.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.join_764be1e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.last-index-of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.last-index-of_a50f663.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/function-apply.js","wiki-common:node_modules/core-js/internals/array-last-index-of.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.map.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.map_95ec947.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-iteration.js","wiki-common:node_modules/core-js/internals/typed-array-species-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.of.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.of_04ddf20.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/typed-array-constructors-require-wrappers.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.reduce.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.reduce_c38aa95.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-reduce.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.reduce-right.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.reduce-right_26913c2.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-reduce.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.reverse.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.reverse_d812ecf.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.set.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.set_08dfeaa.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/to-offset.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/fails.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.slice.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.slice_ca2df3e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/typed-array-species-constructor.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/array-slice.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.some.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.some_ec4fb9a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-iteration.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.sort.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.sort_7516e9a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/array-sort.js","wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/engine-ff-version.js","wiki-common:node_modules/core-js/internals/engine-is-ie-or-edge.js","wiki-common:node_modules/core-js/internals/engine-v8-version.js","wiki-common:node_modules/core-js/internals/engine-webkit-version.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.subarray.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.subarray_da2138f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/to-length.js","wiki-common:node_modules/core-js/internals/to-absolute-index.js","wiki-common:node_modules/core-js/internals/typed-array-species-constructor.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.to-locale-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.to-locale-string_f839a78.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-apply.js","wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/array-slice.js"]},"wiki-common:node_modules/core-js/modules/es.typed-array.to-string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.typed-array.to-string_09d5807.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js"]},"wiki-common:node_modules/core-js/modules/es.unescape.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.unescape_776392d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/to-string.js"]},"wiki-common:node_modules/core-js/internals/collection-weak.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/collection-weak_93cbcd9.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/redefine-all.js","wiki-common:node_modules/core-js/internals/internal-metadata.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/an-instance.js","wiki-common:node_modules/core-js/internals/iterate.js","wiki-common:node_modules/core-js/internals/array-iteration.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/internal-state.js"]},"wiki-common:node_modules/core-js/modules/es.weak-map.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.weak-map.constructor_622b1b3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/redefine-all.js","wiki-common:node_modules/core-js/internals/internal-metadata.js","wiki-common:node_modules/core-js/internals/collection.js","wiki-common:node_modules/core-js/internals/collection-weak.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/object-is-extensible.js","wiki-common:node_modules/core-js/internals/internal-state.js","wiki-common:node_modules/core-js/internals/native-weak-map.js"]},"wiki-common:node_modules/core-js/modules/es.weak-map.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.weak-map_c5da40e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.weak-map.constructor.js"]},"wiki-common:node_modules/core-js/modules/es.weak-set.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.weak-set.constructor_3bc85b3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/collection.js","wiki-common:node_modules/core-js/internals/collection-weak.js"]},"wiki-common:node_modules/core-js/modules/es.weak-set.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/es.weak-set_0212f8f.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.weak-set.constructor.js"]},"wiki-common:node_modules/core-js/internals/base64-map.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/base64-map_8f34520.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/modules/web.atob.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.atob_d7a083d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/validate-arguments-length.js","wiki-common:node_modules/core-js/internals/base64-map.js"]},"wiki-common:node_modules/core-js/modules/web.btoa.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.btoa_61fe3eb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/validate-arguments-length.js","wiki-common:node_modules/core-js/internals/base64-map.js"]},"wiki-common:node_modules/core-js/internals/dom-iterables.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/dom-iterables_a616e4c.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/internals/dom-token-list-prototype.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/dom-token-list-prototype_f51fc85.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/document-create-element.js"]},"wiki-common:node_modules/core-js/modules/web.dom-collections.for-each.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.dom-collections.for-each_d4008c8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/dom-iterables.js","wiki-common:node_modules/core-js/internals/dom-token-list-prototype.js","wiki-common:node_modules/core-js/internals/array-for-each.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js"]},"wiki-common:node_modules/core-js/modules/web.dom-collections.iterator.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.dom-collections.iterator_73338d4.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/dom-iterables.js","wiki-common:node_modules/core-js/internals/dom-token-list-prototype.js","wiki-common:node_modules/core-js/modules/es.array.iterator.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js"]},"wiki-common:node_modules/core-js/internals/try-node-require.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/try-node-require_a9fa3b8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/engine-is-node.js"]},"wiki-common:node_modules/core-js/internals/dom-exception-constants.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/dom-exception-constants_8266d3b.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/core-js/modules/web.dom-exception.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.dom-exception.constructor_88b35f5.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/try-node-require.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/create-property-descriptor.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/object-define-properties.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/an-instance.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/error-to-string.js","wiki-common:node_modules/core-js/internals/normalize-string-argument.js","wiki-common:node_modules/core-js/internals/dom-exception-constants.js","wiki-common:node_modules/core-js/internals/clear-error-stack.js","wiki-common:node_modules/core-js/internals/internal-state.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/is-pure.js"]},"wiki-common:node_modules/core-js/modules/web.dom-exception.stack.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.dom-exception.stack_0fbebdb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/create-property-descriptor.js","wiki-common:node_modules/core-js/internals/object-define-property.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/an-instance.js","wiki-common:node_modules/core-js/internals/inherit-if-required.js","wiki-common:node_modules/core-js/internals/normalize-string-argument.js","wiki-common:node_modules/core-js/internals/dom-exception-constants.js","wiki-common:node_modules/core-js/internals/clear-error-stack.js","wiki-common:node_modules/core-js/internals/is-pure.js"]},"wiki-common:node_modules/core-js/modules/web.dom-exception.to-string-tag.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.dom-exception.to-string-tag_665bc09.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/set-to-string-tag.js"]},"wiki-common:node_modules/core-js/modules/web.clear-immediate.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.clear-immediate_55436cf.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/task.js"]},"wiki-common:node_modules/core-js/modules/web.set-immediate.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.set-immediate_caa179e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/task.js"]},"wiki-common:node_modules/core-js/modules/web.immediate.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.immediate_3823c30.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/web.clear-immediate.js","wiki-common:node_modules/core-js/modules/web.set-immediate.js"]},"wiki-common:node_modules/core-js/modules/web.queue-microtask.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.queue-microtask_8af51ed.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/microtask.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/validate-arguments-length.js","wiki-common:node_modules/core-js/internals/engine-is-node.js"]},"wiki-common:node_modules/core-js/modules/web.structured-clone.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.structured-clone_ae409ad.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/is-pure.js","wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/uid.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/is-constructor.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/is-symbol.js","wiki-common:node_modules/core-js/internals/iterate.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/classof.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/create-property.js","wiki-common:node_modules/core-js/internals/create-non-enumerable-property.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/validate-arguments-length.js","wiki-common:node_modules/core-js/internals/regexp-flags.js","wiki-common:node_modules/core-js/internals/error-stack-installable.js"]},"wiki-common:node_modules/core-js/internals/schedulers-fix.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/schedulers-fix_fce46d9.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-apply.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/engine-user-agent.js","wiki-common:node_modules/core-js/internals/array-slice.js","wiki-common:node_modules/core-js/internals/validate-arguments-length.js"]},"wiki-common:node_modules/core-js/modules/web.set-interval.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.set-interval_3a016d1.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/schedulers-fix.js"]},"wiki-common:node_modules/core-js/modules/web.set-timeout.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.set-timeout_9a4888b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/schedulers-fix.js"]},"wiki-common:node_modules/core-js/modules/web.timers.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.timers_bb023c9.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/web.set-interval.js","wiki-common:node_modules/core-js/modules/web.set-timeout.js"]},"wiki-common:node_modules/core-js/internals/native-url.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/native-url_ab347cc.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/fails.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/is-pure.js"]},"wiki-common:node_modules/core-js/internals/string-punycode-to-ascii.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/string-punycode-to-ascii_0e7a9e8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js"]},"wiki-common:node_modules/core-js/modules/web.url-search-params.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.url-search-params.constructor_81f79f7.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.array.iterator.js","wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/function-call.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/native-url.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/redefine-all.js","wiki-common:node_modules/core-js/internals/set-to-string-tag.js","wiki-common:node_modules/core-js/internals/create-iterator-constructor.js","wiki-common:node_modules/core-js/internals/internal-state.js","wiki-common:node_modules/core-js/internals/an-instance.js","wiki-common:node_modules/core-js/internals/is-callable.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/function-bind-context.js","wiki-common:node_modules/core-js/internals/classof.js","wiki-common:node_modules/core-js/internals/an-object.js","wiki-common:node_modules/core-js/internals/is-object.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/create-property-descriptor.js","wiki-common:node_modules/core-js/internals/get-iterator.js","wiki-common:node_modules/core-js/internals/get-iterator-method.js","wiki-common:node_modules/core-js/internals/validate-arguments-length.js","wiki-common:node_modules/core-js/internals/well-known-symbol.js","wiki-common:node_modules/core-js/internals/array-sort.js"]},"wiki-common:node_modules/core-js/modules/web.url.constructor.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.url.constructor_2aeec90.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.string.iterator.js","wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/descriptors.js","wiki-common:node_modules/core-js/internals/native-url.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-bind-context.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/object-define-properties.js","wiki-common:node_modules/core-js/internals/redefine.js","wiki-common:node_modules/core-js/internals/an-instance.js","wiki-common:node_modules/core-js/internals/has-own-property.js","wiki-common:node_modules/core-js/internals/object-assign.js","wiki-common:node_modules/core-js/internals/array-from.js","wiki-common:node_modules/core-js/internals/array-slice-simple.js","wiki-common:node_modules/core-js/internals/string-multibyte.js","wiki-common:node_modules/core-js/internals/string-punycode-to-ascii.js","wiki-common:node_modules/core-js/internals/to-string.js","wiki-common:node_modules/core-js/internals/set-to-string-tag.js","wiki-common:node_modules/core-js/internals/validate-arguments-length.js","wiki-common:node_modules/core-js/modules/web.url-search-params.constructor.js","wiki-common:node_modules/core-js/internals/internal-state.js"]},"wiki-common:node_modules/core-js/modules/web.url.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.url_b2999d8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/web.url.constructor.js"]},"wiki-common:node_modules/core-js/modules/web.url.to-json.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.url.to-json_17ecb28.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/function-call.js"]},"wiki-common:node_modules/core-js/modules/web.url-search-params.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/web.url-search-params_d265c87.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/web.url-search-params.constructor.js"]},"wiki-common:node_modules/core-js/stable/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/stable/index_f14030c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.symbol.js","wiki-common:node_modules/core-js/modules/es.symbol.description.js","wiki-common:node_modules/core-js/modules/es.symbol.async-iterator.js","wiki-common:node_modules/core-js/modules/es.symbol.has-instance.js","wiki-common:node_modules/core-js/modules/es.symbol.is-concat-spreadable.js","wiki-common:node_modules/core-js/modules/es.symbol.iterator.js","wiki-common:node_modules/core-js/modules/es.symbol.match.js","wiki-common:node_modules/core-js/modules/es.symbol.match-all.js","wiki-common:node_modules/core-js/modules/es.symbol.replace.js","wiki-common:node_modules/core-js/modules/es.symbol.search.js","wiki-common:node_modules/core-js/modules/es.symbol.species.js","wiki-common:node_modules/core-js/modules/es.symbol.split.js","wiki-common:node_modules/core-js/modules/es.symbol.to-primitive.js","wiki-common:node_modules/core-js/modules/es.symbol.to-string-tag.js","wiki-common:node_modules/core-js/modules/es.symbol.unscopables.js","wiki-common:node_modules/core-js/modules/es.error.cause.js","wiki-common:node_modules/core-js/modules/es.error.to-string.js","wiki-common:node_modules/core-js/modules/es.aggregate-error.js","wiki-common:node_modules/core-js/modules/es.aggregate-error.cause.js","wiki-common:node_modules/core-js/modules/es.array.at.js","wiki-common:node_modules/core-js/modules/es.array.concat.js","wiki-common:node_modules/core-js/modules/es.array.copy-within.js","wiki-common:node_modules/core-js/modules/es.array.every.js","wiki-common:node_modules/core-js/modules/es.array.fill.js","wiki-common:node_modules/core-js/modules/es.array.filter.js","wiki-common:node_modules/core-js/modules/es.array.find.js","wiki-common:node_modules/core-js/modules/es.array.find-index.js","wiki-common:node_modules/core-js/modules/es.array.flat.js","wiki-common:node_modules/core-js/modules/es.array.flat-map.js","wiki-common:node_modules/core-js/modules/es.array.for-each.js","wiki-common:node_modules/core-js/modules/es.array.from.js","wiki-common:node_modules/core-js/modules/es.array.includes.js","wiki-common:node_modules/core-js/modules/es.array.index-of.js","wiki-common:node_modules/core-js/modules/es.array.is-array.js","wiki-common:node_modules/core-js/modules/es.array.iterator.js","wiki-common:node_modules/core-js/modules/es.array.join.js","wiki-common:node_modules/core-js/modules/es.array.last-index-of.js","wiki-common:node_modules/core-js/modules/es.array.map.js","wiki-common:node_modules/core-js/modules/es.array.of.js","wiki-common:node_modules/core-js/modules/es.array.reduce.js","wiki-common:node_modules/core-js/modules/es.array.reduce-right.js","wiki-common:node_modules/core-js/modules/es.array.reverse.js","wiki-common:node_modules/core-js/modules/es.array.slice.js","wiki-common:node_modules/core-js/modules/es.array.some.js","wiki-common:node_modules/core-js/modules/es.array.sort.js","wiki-common:node_modules/core-js/modules/es.array.species.js","wiki-common:node_modules/core-js/modules/es.array.splice.js","wiki-common:node_modules/core-js/modules/es.array.unscopables.flat.js","wiki-common:node_modules/core-js/modules/es.array.unscopables.flat-map.js","wiki-common:node_modules/core-js/modules/es.array-buffer.constructor.js","wiki-common:node_modules/core-js/modules/es.array-buffer.is-view.js","wiki-common:node_modules/core-js/modules/es.array-buffer.slice.js","wiki-common:node_modules/core-js/modules/es.data-view.js","wiki-common:node_modules/core-js/modules/es.date.get-year.js","wiki-common:node_modules/core-js/modules/es.date.now.js","wiki-common:node_modules/core-js/modules/es.date.set-year.js","wiki-common:node_modules/core-js/modules/es.date.to-gmt-string.js","wiki-common:node_modules/core-js/modules/es.date.to-iso-string.js","wiki-common:node_modules/core-js/modules/es.date.to-json.js","wiki-common:node_modules/core-js/modules/es.date.to-primitive.js","wiki-common:node_modules/core-js/modules/es.date.to-string.js","wiki-common:node_modules/core-js/modules/es.escape.js","wiki-common:node_modules/core-js/modules/es.function.bind.js","wiki-common:node_modules/core-js/modules/es.function.has-instance.js","wiki-common:node_modules/core-js/modules/es.function.name.js","wiki-common:node_modules/core-js/modules/es.global-this.js","wiki-common:node_modules/core-js/modules/es.json.stringify.js","wiki-common:node_modules/core-js/modules/es.json.to-string-tag.js","wiki-common:node_modules/core-js/modules/es.map.js","wiki-common:node_modules/core-js/modules/es.math.acosh.js","wiki-common:node_modules/core-js/modules/es.math.asinh.js","wiki-common:node_modules/core-js/modules/es.math.atanh.js","wiki-common:node_modules/core-js/modules/es.math.cbrt.js","wiki-common:node_modules/core-js/modules/es.math.clz32.js","wiki-common:node_modules/core-js/modules/es.math.cosh.js","wiki-common:node_modules/core-js/modules/es.math.expm1.js","wiki-common:node_modules/core-js/modules/es.math.fround.js","wiki-common:node_modules/core-js/modules/es.math.hypot.js","wiki-common:node_modules/core-js/modules/es.math.imul.js","wiki-common:node_modules/core-js/modules/es.math.log10.js","wiki-common:node_modules/core-js/modules/es.math.log1p.js","wiki-common:node_modules/core-js/modules/es.math.log2.js","wiki-common:node_modules/core-js/modules/es.math.sign.js","wiki-common:node_modules/core-js/modules/es.math.sinh.js","wiki-common:node_modules/core-js/modules/es.math.tanh.js","wiki-common:node_modules/core-js/modules/es.math.to-string-tag.js","wiki-common:node_modules/core-js/modules/es.math.trunc.js","wiki-common:node_modules/core-js/modules/es.number.constructor.js","wiki-common:node_modules/core-js/modules/es.number.epsilon.js","wiki-common:node_modules/core-js/modules/es.number.is-finite.js","wiki-common:node_modules/core-js/modules/es.number.is-integer.js","wiki-common:node_modules/core-js/modules/es.number.is-nan.js","wiki-common:node_modules/core-js/modules/es.number.is-safe-integer.js","wiki-common:node_modules/core-js/modules/es.number.max-safe-integer.js","wiki-common:node_modules/core-js/modules/es.number.min-safe-integer.js","wiki-common:node_modules/core-js/modules/es.number.parse-float.js","wiki-common:node_modules/core-js/modules/es.number.parse-int.js","wiki-common:node_modules/core-js/modules/es.number.to-exponential.js","wiki-common:node_modules/core-js/modules/es.number.to-fixed.js","wiki-common:node_modules/core-js/modules/es.number.to-precision.js","wiki-common:node_modules/core-js/modules/es.object.assign.js","wiki-common:node_modules/core-js/modules/es.object.create.js","wiki-common:node_modules/core-js/modules/es.object.define-getter.js","wiki-common:node_modules/core-js/modules/es.object.define-properties.js","wiki-common:node_modules/core-js/modules/es.object.define-property.js","wiki-common:node_modules/core-js/modules/es.object.define-setter.js","wiki-common:node_modules/core-js/modules/es.object.entries.js","wiki-common:node_modules/core-js/modules/es.object.freeze.js","wiki-common:node_modules/core-js/modules/es.object.from-entries.js","wiki-common:node_modules/core-js/modules/es.object.get-own-property-descriptor.js","wiki-common:node_modules/core-js/modules/es.object.get-own-property-descriptors.js","wiki-common:node_modules/core-js/modules/es.object.get-own-property-names.js","wiki-common:node_modules/core-js/modules/es.object.get-prototype-of.js","wiki-common:node_modules/core-js/modules/es.object.has-own.js","wiki-common:node_modules/core-js/modules/es.object.is.js","wiki-common:node_modules/core-js/modules/es.object.is-extensible.js","wiki-common:node_modules/core-js/modules/es.object.is-frozen.js","wiki-common:node_modules/core-js/modules/es.object.is-sealed.js","wiki-common:node_modules/core-js/modules/es.object.keys.js","wiki-common:node_modules/core-js/modules/es.object.lookup-getter.js","wiki-common:node_modules/core-js/modules/es.object.lookup-setter.js","wiki-common:node_modules/core-js/modules/es.object.prevent-extensions.js","wiki-common:node_modules/core-js/modules/es.object.seal.js","wiki-common:node_modules/core-js/modules/es.object.set-prototype-of.js","wiki-common:node_modules/core-js/modules/es.object.to-string.js","wiki-common:node_modules/core-js/modules/es.object.values.js","wiki-common:node_modules/core-js/modules/es.parse-float.js","wiki-common:node_modules/core-js/modules/es.parse-int.js","wiki-common:node_modules/core-js/modules/es.promise.js","wiki-common:node_modules/core-js/modules/es.promise.all-settled.js","wiki-common:node_modules/core-js/modules/es.promise.any.js","wiki-common:node_modules/core-js/modules/es.promise.finally.js","wiki-common:node_modules/core-js/modules/es.reflect.apply.js","wiki-common:node_modules/core-js/modules/es.reflect.construct.js","wiki-common:node_modules/core-js/modules/es.reflect.define-property.js","wiki-common:node_modules/core-js/modules/es.reflect.delete-property.js","wiki-common:node_modules/core-js/modules/es.reflect.get.js","wiki-common:node_modules/core-js/modules/es.reflect.get-own-property-descriptor.js","wiki-common:node_modules/core-js/modules/es.reflect.get-prototype-of.js","wiki-common:node_modules/core-js/modules/es.reflect.has.js","wiki-common:node_modules/core-js/modules/es.reflect.is-extensible.js","wiki-common:node_modules/core-js/modules/es.reflect.own-keys.js","wiki-common:node_modules/core-js/modules/es.reflect.prevent-extensions.js","wiki-common:node_modules/core-js/modules/es.reflect.set.js","wiki-common:node_modules/core-js/modules/es.reflect.set-prototype-of.js","wiki-common:node_modules/core-js/modules/es.reflect.to-string-tag.js","wiki-common:node_modules/core-js/modules/es.regexp.constructor.js","wiki-common:node_modules/core-js/modules/es.regexp.dot-all.js","wiki-common:node_modules/core-js/modules/es.regexp.exec.js","wiki-common:node_modules/core-js/modules/es.regexp.flags.js","wiki-common:node_modules/core-js/modules/es.regexp.sticky.js","wiki-common:node_modules/core-js/modules/es.regexp.test.js","wiki-common:node_modules/core-js/modules/es.regexp.to-string.js","wiki-common:node_modules/core-js/modules/es.set.js","wiki-common:node_modules/core-js/modules/es.string.at-alternative.js","wiki-common:node_modules/core-js/modules/es.string.code-point-at.js","wiki-common:node_modules/core-js/modules/es.string.ends-with.js","wiki-common:node_modules/core-js/modules/es.string.from-code-point.js","wiki-common:node_modules/core-js/modules/es.string.includes.js","wiki-common:node_modules/core-js/modules/es.string.iterator.js","wiki-common:node_modules/core-js/modules/es.string.match.js","wiki-common:node_modules/core-js/modules/es.string.match-all.js","wiki-common:node_modules/core-js/modules/es.string.pad-end.js","wiki-common:node_modules/core-js/modules/es.string.pad-start.js","wiki-common:node_modules/core-js/modules/es.string.raw.js","wiki-common:node_modules/core-js/modules/es.string.repeat.js","wiki-common:node_modules/core-js/modules/es.string.replace.js","wiki-common:node_modules/core-js/modules/es.string.replace-all.js","wiki-common:node_modules/core-js/modules/es.string.search.js","wiki-common:node_modules/core-js/modules/es.string.split.js","wiki-common:node_modules/core-js/modules/es.string.starts-with.js","wiki-common:node_modules/core-js/modules/es.string.substr.js","wiki-common:node_modules/core-js/modules/es.string.trim.js","wiki-common:node_modules/core-js/modules/es.string.trim-end.js","wiki-common:node_modules/core-js/modules/es.string.trim-start.js","wiki-common:node_modules/core-js/modules/es.string.anchor.js","wiki-common:node_modules/core-js/modules/es.string.big.js","wiki-common:node_modules/core-js/modules/es.string.blink.js","wiki-common:node_modules/core-js/modules/es.string.bold.js","wiki-common:node_modules/core-js/modules/es.string.fixed.js","wiki-common:node_modules/core-js/modules/es.string.fontcolor.js","wiki-common:node_modules/core-js/modules/es.string.fontsize.js","wiki-common:node_modules/core-js/modules/es.string.italics.js","wiki-common:node_modules/core-js/modules/es.string.link.js","wiki-common:node_modules/core-js/modules/es.string.small.js","wiki-common:node_modules/core-js/modules/es.string.strike.js","wiki-common:node_modules/core-js/modules/es.string.sub.js","wiki-common:node_modules/core-js/modules/es.string.sup.js","wiki-common:node_modules/core-js/modules/es.typed-array.float32-array.js","wiki-common:node_modules/core-js/modules/es.typed-array.float64-array.js","wiki-common:node_modules/core-js/modules/es.typed-array.int8-array.js","wiki-common:node_modules/core-js/modules/es.typed-array.int16-array.js","wiki-common:node_modules/core-js/modules/es.typed-array.int32-array.js","wiki-common:node_modules/core-js/modules/es.typed-array.uint8-array.js","wiki-common:node_modules/core-js/modules/es.typed-array.uint8-clamped-array.js","wiki-common:node_modules/core-js/modules/es.typed-array.uint16-array.js","wiki-common:node_modules/core-js/modules/es.typed-array.uint32-array.js","wiki-common:node_modules/core-js/modules/es.typed-array.at.js","wiki-common:node_modules/core-js/modules/es.typed-array.copy-within.js","wiki-common:node_modules/core-js/modules/es.typed-array.every.js","wiki-common:node_modules/core-js/modules/es.typed-array.fill.js","wiki-common:node_modules/core-js/modules/es.typed-array.filter.js","wiki-common:node_modules/core-js/modules/es.typed-array.find.js","wiki-common:node_modules/core-js/modules/es.typed-array.find-index.js","wiki-common:node_modules/core-js/modules/es.typed-array.for-each.js","wiki-common:node_modules/core-js/modules/es.typed-array.from.js","wiki-common:node_modules/core-js/modules/es.typed-array.includes.js","wiki-common:node_modules/core-js/modules/es.typed-array.index-of.js","wiki-common:node_modules/core-js/modules/es.typed-array.iterator.js","wiki-common:node_modules/core-js/modules/es.typed-array.join.js","wiki-common:node_modules/core-js/modules/es.typed-array.last-index-of.js","wiki-common:node_modules/core-js/modules/es.typed-array.map.js","wiki-common:node_modules/core-js/modules/es.typed-array.of.js","wiki-common:node_modules/core-js/modules/es.typed-array.reduce.js","wiki-common:node_modules/core-js/modules/es.typed-array.reduce-right.js","wiki-common:node_modules/core-js/modules/es.typed-array.reverse.js","wiki-common:node_modules/core-js/modules/es.typed-array.set.js","wiki-common:node_modules/core-js/modules/es.typed-array.slice.js","wiki-common:node_modules/core-js/modules/es.typed-array.some.js","wiki-common:node_modules/core-js/modules/es.typed-array.sort.js","wiki-common:node_modules/core-js/modules/es.typed-array.subarray.js","wiki-common:node_modules/core-js/modules/es.typed-array.to-locale-string.js","wiki-common:node_modules/core-js/modules/es.typed-array.to-string.js","wiki-common:node_modules/core-js/modules/es.unescape.js","wiki-common:node_modules/core-js/modules/es.weak-map.js","wiki-common:node_modules/core-js/modules/es.weak-set.js","wiki-common:node_modules/core-js/modules/web.atob.js","wiki-common:node_modules/core-js/modules/web.btoa.js","wiki-common:node_modules/core-js/modules/web.dom-collections.for-each.js","wiki-common:node_modules/core-js/modules/web.dom-collections.iterator.js","wiki-common:node_modules/core-js/modules/web.dom-exception.constructor.js","wiki-common:node_modules/core-js/modules/web.dom-exception.stack.js","wiki-common:node_modules/core-js/modules/web.dom-exception.to-string-tag.js","wiki-common:node_modules/core-js/modules/web.immediate.js","wiki-common:node_modules/core-js/modules/web.queue-microtask.js","wiki-common:node_modules/core-js/modules/web.structured-clone.js","wiki-common:node_modules/core-js/modules/web.timers.js","wiki-common:node_modules/core-js/modules/web.url.js","wiki-common:node_modules/core-js/modules/web.url.to-json.js","wiki-common:node_modules/core-js/modules/web.url-search-params.js","wiki-common:node_modules/core-js/internals/path.js"]},"wiki-common:node_modules/core-js/internals/array-iteration-from-last.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-iteration-from-last_a8e8583.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/function-bind-context.js","wiki-common:node_modules/core-js/internals/indexed-object.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js"]},"wiki-common:node_modules/core-js/modules/esnext.array.find-last.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.array.find-last_d040499.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-iteration-from-last.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/modules/esnext.array.find-last-index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.array.find-last-index_3b808fb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-iteration-from-last.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/modules/esnext.typed-array.find-last.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.typed-array.find-last_432439a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-iteration-from-last.js"]},"wiki-common:node_modules/core-js/modules/esnext.typed-array.find-last-index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.typed-array.find-last-index_7f481bc.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-iteration-from-last.js"]},"wiki-common:node_modules/core-js/proposals/array-find-from-last.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/proposals/array-find-from-last_1a48737.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/esnext.array.find-last.js","wiki-common:node_modules/core-js/modules/esnext.array.find-last-index.js","wiki-common:node_modules/core-js/modules/esnext.typed-array.find-last.js","wiki-common:node_modules/core-js/modules/esnext.typed-array.find-last-index.js"]},"wiki-common:node_modules/core-js/internals/array-group-by.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-group-by_b9eda24.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-bind-context.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/indexed-object.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/to-property-key.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/object-create.js","wiki-common:node_modules/core-js/internals/array-from-constructor-and-list.js"]},"wiki-common:node_modules/core-js/modules/esnext.array.group-by.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.array.group-by_1bc70f5.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/array-group-by.js","wiki-common:node_modules/core-js/internals/array-method-is-strict.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/modules/esnext.array.group-by-to-map.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.array.group-by-to-map_e311a19.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/get-built-in.js","wiki-common:node_modules/core-js/internals/function-bind-context.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/indexed-object.js","wiki-common:node_modules/core-js/internals/to-object.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/array-method-is-strict.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/proposals/array-grouping-stage-3.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/proposals/array-grouping-stage-3_ab9a422.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/esnext.array.group-by.js","wiki-common:node_modules/core-js/modules/esnext.array.group-by-to-map.js"]},"wiki-common:node_modules/core-js/internals/array-to-reversed.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-to-reversed_e471242.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/length-of-array-like.js"]},"wiki-common:node_modules/core-js/modules/esnext.array.to-reversed.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.array.to-reversed_b14c98b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/array-to-reversed.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/internals/entry-virtual.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/entry-virtual_cb99a41.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/modules/esnext.array.to-sorted.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.array.to-sorted_e3652d9.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/array-from-constructor-and-list.js","wiki-common:node_modules/core-js/internals/entry-virtual.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/internals/array-to-spliced.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-to-spliced_ba6ea5a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/to-absolute-index.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js"]},"wiki-common:node_modules/core-js/modules/esnext.array.to-spliced.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.array.to-spliced_4f23504.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js","wiki-common:node_modules/core-js/internals/array-slice.js","wiki-common:node_modules/core-js/internals/array-to-spliced.js","wiki-common:node_modules/core-js/internals/add-to-unscopables.js"]},"wiki-common:node_modules/core-js/internals/array-with.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/internals/array-with_e562ae6.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/length-of-array-like.js","wiki-common:node_modules/core-js/internals/to-integer-or-infinity.js"]},"wiki-common:node_modules/core-js/modules/esnext.array.with.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.array.with_3df2c43.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/export.js","wiki-common:node_modules/core-js/internals/global.js","wiki-common:node_modules/core-js/internals/array-with.js","wiki-common:node_modules/core-js/internals/to-indexed-object.js"]},"wiki-common:node_modules/core-js/modules/esnext.typed-array.to-reversed.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.typed-array.to-reversed_7a495e3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-to-reversed.js","wiki-common:node_modules/core-js/internals/array-buffer-view-core.js"]},"wiki-common:node_modules/core-js/modules/esnext.typed-array.to-sorted.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.typed-array.to-sorted_4676652.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/function-uncurry-this.js","wiki-common:node_modules/core-js/internals/a-callable.js","wiki-common:node_modules/core-js/internals/array-from-constructor-and-list.js"]},"wiki-common:node_modules/core-js/modules/esnext.typed-array.to-spliced.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.typed-array.to-spliced_752d0ac.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-buffer-view-core.js","wiki-common:node_modules/core-js/internals/array-slice.js","wiki-common:node_modules/core-js/internals/array-to-spliced.js"]},"wiki-common:node_modules/core-js/modules/esnext.typed-array.with.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.typed-array.with_d062223.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/internals/array-with.js","wiki-common:node_modules/core-js/internals/array-buffer-view-core.js"]},"wiki-common:node_modules/core-js/proposals/change-array-by-copy.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/proposals/change-array-by-copy_26c7f05.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/esnext.array.to-reversed.js","wiki-common:node_modules/core-js/modules/esnext.array.to-sorted.js","wiki-common:node_modules/core-js/modules/esnext.array.to-spliced.js","wiki-common:node_modules/core-js/modules/esnext.array.with.js","wiki-common:node_modules/core-js/modules/esnext.typed-array.to-reversed.js","wiki-common:node_modules/core-js/modules/esnext.typed-array.to-sorted.js","wiki-common:node_modules/core-js/modules/esnext.typed-array.to-spliced.js","wiki-common:node_modules/core-js/modules/esnext.typed-array.with.js"]},"wiki-common:node_modules/core-js/modules/esnext.object.has-own.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.object.has-own_786392c.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.object.has-own.js"]},"wiki-common:node_modules/core-js/proposals/accessible-object-hasownproperty.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/proposals/accessible-object-hasownproperty_5c56d52.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/esnext.object.has-own.js"]},"wiki-common:node_modules/core-js/modules/esnext.global-this.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.global-this_f97eaa1.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.global-this.js"]},"wiki-common:node_modules/core-js/proposals/global-this.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/proposals/global-this_585a22e.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/esnext.global-this.js","wiki-common:node_modules/core-js/internals/global.js"]},"wiki-common:node_modules/core-js/modules/esnext.promise.all-settled.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.promise.all-settled_cf5536a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.promise.all-settled.js"]},"wiki-common:node_modules/core-js/proposals/promise-all-settled.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/proposals/promise-all-settled_df9d4cb.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/esnext.promise.all-settled.js"]},"wiki-common:node_modules/core-js/modules/esnext.aggregate-error.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.aggregate-error_d1eeb32.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.aggregate-error.js"]},"wiki-common:node_modules/core-js/modules/esnext.promise.any.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.promise.any_892734d.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.promise.any.js"]},"wiki-common:node_modules/core-js/proposals/promise-any.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/proposals/promise-any_1ca9fb0.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/esnext.aggregate-error.js","wiki-common:node_modules/core-js/modules/esnext.promise.any.js"]},"wiki-common:node_modules/core-js/modules/esnext.array.at.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.array.at_d1f8c92.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.array.at.js"]},"wiki-common:node_modules/core-js/modules/esnext.typed-array.at.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.typed-array.at_c4be84b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.typed-array.at.js"]},"wiki-common:node_modules/core-js/proposals/relative-indexing-method.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/proposals/relative-indexing-method_71d83d8.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.string.at-alternative.js","wiki-common:node_modules/core-js/modules/esnext.array.at.js","wiki-common:node_modules/core-js/modules/esnext.typed-array.at.js"]},"wiki-common:node_modules/core-js/modules/esnext.string.match-all.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.string.match-all_74b2190.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.string.match-all.js"]},"wiki-common:node_modules/core-js/proposals/string-match-all.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/proposals/string-match-all_39dde51.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/esnext.string.match-all.js"]},"wiki-common:node_modules/core-js/modules/esnext.string.replace-all.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/modules/esnext.string.replace-all_7b0d883.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/es.string.replace-all.js"]},"wiki-common:node_modules/core-js/proposals/string-replace-all-stage-4.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/proposals/string-replace-all-stage-4_f697755.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/modules/esnext.string.replace-all.js"]},"wiki-common:node_modules/core-js/stage/4.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/stage/4_5125de7.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/proposals/accessible-object-hasownproperty.js","wiki-common:node_modules/core-js/proposals/global-this.js","wiki-common:node_modules/core-js/proposals/promise-all-settled.js","wiki-common:node_modules/core-js/proposals/promise-any.js","wiki-common:node_modules/core-js/proposals/relative-indexing-method.js","wiki-common:node_modules/core-js/proposals/string-match-all.js","wiki-common:node_modules/core-js/proposals/string-replace-all-stage-4.js","wiki-common:node_modules/core-js/internals/path.js"]},"wiki-common:node_modules/core-js/stage/3.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/stage/3_598f3be.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/proposals/array-find-from-last.js","wiki-common:node_modules/core-js/proposals/array-grouping-stage-3.js","wiki-common:node_modules/core-js/proposals/change-array-by-copy.js","wiki-common:node_modules/core-js/stage/4.js"]},"wiki-common:node_modules/core-js/actual/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/core-js/actual/index_8390523.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/stable/index.js","wiki-common:node_modules/core-js/stage/3.js","wiki-common:node_modules/core-js/internals/path.js"]},"wiki-common:node_modules/regenerator-runtime/runtime.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/regenerator-runtime/runtime_1661fc1.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/flexibility/flexibility.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/flexibility/flexibility_feb5519.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/whatwg-fetch/dist/fetch.umd.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/whatwg-fetch/dist/fetch.umd_3a9f477.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/performance-now/lib/performance-now.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/performance-now/lib/performance-now_90d2143.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/raf/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/raf/index_4bea310.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/performance-now/lib/performance-now.js"]},"wiki-common:node_modules/raf/polyfill.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/raf/polyfill_e82ab0b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/raf/index.js"]},"wiki-common:static/js/polyfill.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/js/polyfill_0befe4b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/core-js/actual/index.js","wiki-common:node_modules/regenerator-runtime/runtime.js","wiki-common:node_modules/flexibility/flexibility.js","wiki-common:node_modules/whatwg-fetch/dist/fetch.umd.js","wiki-common:node_modules/raf/polyfill.js"]},"wiki-common:node_modules/object-assign/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/object-assign/index_1f26290.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/interopRequireDefault_bc9f863.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/typeof.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/typeof_3e433aa.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/interopRequireWildcard_e181efc.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/@babel/runtime/helpers/typeof.js"]},"wiki-common:node_modules/@babel/runtime/helpers/defineProperty.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/defineProperty_ca348f8.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/arrayWithHoles.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/arrayWithHoles_2f2f37a.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/iterableToArrayLimit.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/iterableToArrayLimit_88acb0e.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/arrayLikeToArray.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/arrayLikeToArray_d9924a3.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/unsupportedIterableToArray.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/unsupportedIterableToArray_062057b.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/@babel/runtime/helpers/arrayLikeToArray.js"]},"wiki-common:node_modules/@babel/runtime/helpers/nonIterableRest.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/nonIterableRest_bf8b1d8.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/slicedToArray.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/slicedToArray_c02c7ad.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/@babel/runtime/helpers/arrayWithHoles.js","wiki-common:node_modules/@babel/runtime/helpers/iterableToArrayLimit.js","wiki-common:node_modules/@babel/runtime/helpers/unsupportedIterableToArray.js","wiki-common:node_modules/@babel/runtime/helpers/nonIterableRest.js"]},"wiki-common:node_modules/@babel/runtime/helpers/objectWithoutPropertiesLoose.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/objectWithoutPropertiesLoose_bab814a.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/objectWithoutProperties.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/objectWithoutProperties_7e46365.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/@babel/runtime/helpers/objectWithoutPropertiesLoose.js"]},"wiki-common:node_modules/@babel/runtime/helpers/extends.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/extends_ee7a063.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/classCallCheck.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/classCallCheck_f04d157.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/createClass.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/createClass_c2d292c.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/setPrototypeOf.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/setPrototypeOf_2efa141.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/inherits.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/inherits_c5c1490.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/@babel/runtime/helpers/setPrototypeOf.js"]},"wiki-common:node_modules/@babel/runtime/helpers/getPrototypeOf.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/getPrototypeOf_38de542.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/isNativeReflectConstruct.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/isNativeReflectConstruct_589d8d3.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/assertThisInitialized.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/assertThisInitialized_4339fda.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/possibleConstructorReturn.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/possibleConstructorReturn_4af8b61.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/@babel/runtime/helpers/typeof.js","wiki-common:node_modules/@babel/runtime/helpers/assertThisInitialized.js"]},"wiki-common:node_modules/@babel/runtime/helpers/createSuper.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/createSuper_3cf4895.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/@babel/runtime/helpers/getPrototypeOf.js","wiki-common:node_modules/@babel/runtime/helpers/isNativeReflectConstruct.js","wiki-common:node_modules/@babel/runtime/helpers/possibleConstructorReturn.js"]},"wiki-common:node_modules/@babel/runtime/helpers/objectSpread2.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/objectSpread2_8162130.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/@babel/runtime/helpers/defineProperty.js"]},"wiki-common:node_modules/@babel/runtime/helpers/arrayWithoutHoles.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/arrayWithoutHoles_68641f3.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/@babel/runtime/helpers/arrayLikeToArray.js"]},"wiki-common:node_modules/@babel/runtime/helpers/iterableToArray.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/iterableToArray_7040077.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/nonIterableSpread.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/nonIterableSpread_0d095c2.js","pkg":"wiki-common:p0"},"wiki-common:node_modules/@babel/runtime/helpers/toConsumableArray.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@babel/runtime/helpers/toConsumableArray_39e887a.js","pkg":"wiki-common:p0","deps":["wiki-common:node_modules/@babel/runtime/helpers/arrayWithoutHoles.js","wiki-common:node_modules/@babel/runtime/helpers/iterableToArray.js","wiki-common:node_modules/@babel/runtime/helpers/unsupportedIterableToArray.js","wiki-common:node_modules/@babel/runtime/helpers/nonIterableSpread.js"]},"wiki-common:node_modules/dom-walk/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/dom-walk/index_410b499.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/min-document/dom-comment.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/min-document/dom-comment_121ac3e.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/min-document/dom-text.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/min-document/dom-text_90f9883.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/min-document/event/dispatch-event.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/min-document/event/dispatch-event_35a0cbc.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/min-document/event/add-event-listener.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/min-document/event/add-event-listener_d5b82fd.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/min-document/event/remove-event-listener.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/min-document/event/remove-event-listener_dd23c31.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/min-document/serialize.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/min-document/serialize_7856700.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/min-document/dom-element.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/min-document/dom-element_aa58ce1.js","pkg":"wiki-common:p3","deps":["wiki-common:node_modules/dom-walk/index.js","wiki-common:node_modules/min-document/event/dispatch-event.js","wiki-common:node_modules/min-document/event/add-event-listener.js","wiki-common:node_modules/min-document/event/remove-event-listener.js","wiki-common:node_modules/min-document/serialize.js"]},"wiki-common:node_modules/min-document/dom-fragment.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/min-document/dom-fragment_433b27e.js","pkg":"wiki-common:p3","deps":["wiki-common:node_modules/min-document/dom-element.js"]},"wiki-common:node_modules/min-document/event.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/min-document/event_20bd9cb.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/min-document/document.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/min-document/document_bf36d99.js","pkg":"wiki-common:p3","deps":["wiki-common:node_modules/dom-walk/index.js","wiki-common:node_modules/min-document/dom-comment.js","wiki-common:node_modules/min-document/dom-text.js","wiki-common:node_modules/min-document/dom-element.js","wiki-common:node_modules/min-document/dom-fragment.js","wiki-common:node_modules/min-document/event.js","wiki-common:node_modules/min-document/event/dispatch-event.js","wiki-common:node_modules/min-document/event/add-event-listener.js","wiki-common:node_modules/min-document/event/remove-event-listener.js"]},"wiki-common:node_modules/min-document/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/min-document/index_59e6ac9.js","pkg":"wiki-common:p3","deps":["wiki-common:node_modules/min-document/document.js"]},"wiki-common:node_modules/global/document.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/global/document_01f54f6.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/weakmap-polyfill/weakmap-polyfill.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/weakmap-polyfill/weakmap-polyfill_f1f0810.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/global/window.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/global/window_46745f7.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/lodash.includes/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/lodash.includes/index_ec94584.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/array-find/find.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/array-find/find_061e0c6.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/lodash.values/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/lodash.values/index_377a1a2.js","pkg":"wiki-common:p3"},"wiki-common:node_modules/larkplayer/dist/larkplayer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/larkplayer/dist/larkplayer_79c50db.js","pkg":"wiki-common:p3","deps":["wiki-common:node_modules/min-document/index.js","wiki-common:node_modules/global/document.js","wiki-common:node_modules/object-assign/index.js","wiki-common:node_modules/weakmap-polyfill/weakmap-polyfill.js","wiki-common:node_modules/global/window.js","wiki-common:node_modules/lodash.includes/index.js","wiki-common:node_modules/array-find/find.js","wiki-common:node_modules/lodash.values/index.js"]},"wiki-common:node_modules/hls.js/dist/hls.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/hls.js/dist/hls_5871175.js","pkg":"wiki-common:p3"},"wiki-common:widget/lib/clipboard/clipboard.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/clipboard/clipboard_b8cb7b6.js","pkg":"wiki-common:p15"},"wiki-common:widget/lib/kinetic/kinetic.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/kinetic/kinetic_4e978b1.js","pkg":"wiki-common:p15"},"wiki-common:widget/lib/larkplayer/source/player.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/larkplayer/source/player_2bdf02f.js","pkg":"wiki-common:p15"},"wiki-common:widget/lib/larkplayer/larkplayer-hls.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/larkplayer/larkplayer-hls_1fcbc3e.js","pkg":"wiki-common:p15","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/larkplayer/source/player.js","wiki-common:node_modules/hls.js/dist/hls.js"]},"wiki-common:widget/lib/larkplayer/larkplayer-play-continue.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/larkplayer/larkplayer-play-continue_c9ff8ce.js","pkg":"wiki-common:p15","deps":["wiki-common:widget/lib/larkplayer/source/player.js"]},"wiki-common:widget/lib/larkplayer/larkplayer-play-via-second-id.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/larkplayer/larkplayer-play-via-second-id_989e7f0.js","pkg":"wiki-common:p15","deps":["wiki-common:widget/lib/larkplayer/source/player.js","wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/nslog/nslog.js","wiki-common:widget/component/superLogger/superLogger.es.js","wiki-common:widget/tools/clickstream/clickstream.js"]},"wiki-common:widget/lib/larkplayer/larkplayer-playback-rate.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/larkplayer/larkplayer-playback-rate_d9379dc.js","pkg":"wiki-common:p15","deps":["wiki-common:widget/lib/larkplayer/source/player.js","wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/lib/larkplayer/larkplayer-window-player.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/larkplayer/larkplayer-window-player_959ba03.js","pkg":"wiki-common:p15","deps":["wiki-common:widget/lib/larkplayer/source/player.js","wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/lib/larkplayer/source/ui.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/larkplayer/source/ui_7e7c53d.js","pkg":"wiki-common:p15","deps":["wiki-common:widget/lib/larkplayer/source/player.js"]},"wiki-common:widget/lib/larkplayer/larkplayer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/larkplayer/larkplayer_743cb23.js","pkg":"wiki-common:p15","deps":["wiki-common:widget/lib/larkplayer/source/player.js","wiki-common:widget/lib/larkplayer/larkplayer-hls.js","wiki-common:widget/lib/larkplayer/source/ui.js","wiki-common:widget/lib/larkplayer/larkplayer-play-continue.js","wiki-common:widget/lib/larkplayer/larkplayer-play-via-second-id.js","wiki-common:widget/lib/larkplayer/larkplayer-window-player.js","wiki-common:widget/lib/larkplayer/larkplayer-playback-rate.js"]},"wiki-common:widget/lib/promisePolyfill/promise.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/promisePolyfill/promise_346e986.js","pkg":"wiki-common:p15"},"wiki-common:widget/lib/sparkMD5/sparkMD5.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/sparkMD5/sparkMD5_24bf4de.js","pkg":"wiki-common:p15"},"wiki-common:widget/lib/swfObject/swfObject.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/swfObject/swfObject_945a086.js","pkg":"wiki-common:p15"},"wiki-common:widget/lib/trumbowyg/plugins/colors/trumbowyg.colors.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/trumbowyg/plugins/colors/trumbowyg.colors_ad4a7ef.js","pkg":"wiki-common:p15","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/lib/trumbowyg/trumbowyg.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/trumbowyg/trumbowyg_8b6f8f3.js","pkg":"wiki-common:p15","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/lib/watermark/watermark.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/watermark/watermark_e27d63d.js","pkg":"wiki-common:p15"},"wiki-common:widget/lib/webuploader/webuploader.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/webuploader/webuploader_72dcd61.js","pkg":"wiki-common:p15","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/lib/zeroClipboard/zeroClipboard.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/zeroClipboard/zeroClipboard_7ce8c83.js","pkg":"wiki-common:p15","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/util/addStyleSheet.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/addStyleSheet_3ca6753.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/util/tween.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/tween_5edc968.js","pkg":"wiki-common:p11"},"wiki-common:widget/util/safeCall.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/safeCall_71a8de3.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/util/animation.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/animation_858a1a9.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/tween.js","wiki-common:widget/util/safeCall.js"]},"wiki-common:widget/util/number.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/number_66969e3.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/util/timeFormater.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/timeFormater_7a1ee01.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/util/number.js"]},"wiki-common:widget/util/calendar.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/calendar_8a0f5ed.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/timeFormater.js","wiki-common:widget/util/safeCall.js"]},"wiki-common:widget/util/checkCSS.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/checkCSS_af29366.js","pkg":"wiki-common:p11"},"wiki-common:widget/util/clickstreamSdk.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/clickstreamSdk_873b660.js","pkg":"wiki-common:p11","deps":["wiki-common:node_modules/@baidu/clickstream-sdk/lib/index.js"]},"wiki-common:widget/util/color.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/color_e0c44fe.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/number.js"]},"wiki-common:widget/util/cookie.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/cookie_fd98a1a.js","pkg":"wiki-common:p11"},"wiki-common:widget/util/eventEmitter.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/eventEmitter_e3d4d5d.js","pkg":"wiki-common:p11"},"wiki-common:widget/util/feedback.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/feedback_3800112.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/util/getEidByCookie.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/getEidByCookie_0584884.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/util/cookie.js"]},"wiki-common:widget/util/getSrcByUrl.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/getSrcByUrl_32983d7.js","pkg":"wiki-common:p11"},"wiki-common:widget/util/guid.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/guid_5df9a9f.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/lib/sparkMD5/sparkMD5.js","wiki-common:widget/util/cookie.js"]},"wiki-common:widget/util/inSightDetector.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/inSightDetector.es_103b4c0.js","pkg":"wiki-common:p11"},"wiki-common:widget/util/loadXaf.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/loadXaf_37b7950.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/util/safeCall.js","wiki-common:widget/util/cookie.js","wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/util/scrollTo.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/scrollTo_7dabf6c.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/browser.js","wiki-common:widget/util/animation.js"]},"wiki-common:widget/util/scrollToTop.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/scrollToTop_68ae519.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/scrollTo.js","wiki-common:widget/util/browser.js","wiki-common:widget/util/safeCall.js"]},"wiki-common:widget/util/string.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/string_c137f45.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/timeFormater.js"]},"wiki-common:widget/util/themeColor.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/themeColor.es_e84826f.js","pkg":"wiki-common:p11"},"wiki-common:widget/util/url.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/util/url_368604c.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/tools/clickstream/clickstream.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/tools/clickstream/clickstream_7a5bdf2.js","pkg":"wiki-common:p11","deps":["wiki-common:widget/util/clickstreamSdk.js"]},"wiki-common:node_modules/larkplayer-ui/dist/larkplayer-ui.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/larkplayer-ui/dist/larkplayer-ui_d17fc4e.js","deps":["wiki-common:node_modules/larkplayer/dist/larkplayer.js"]},"wiki-common:widget/lib/letvPlayer/letvPlayer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/lib/letvPlayer/letvPlayer_0d7fbb0.js","pkg":"wiki-common:p13"},"wiki-common:widget/ui/bubble/bubble.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/bubble/bubble_a948974.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js"]},"wiki-common:widget/ui/carousel/aniTypes/aniType_dissolve.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/carousel/aniTypes/aniType_dissolve_9416978.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/animation.js","wiki-common:widget/util/checkCSS.js","wiki-common:widget/util/addStyleSheet.js"]},"wiki-common:widget/ui/carousel/aniTypes/aniType_fade.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/carousel/aniTypes/aniType_fade_12be6a3.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/animation.js"]},"wiki-common:widget/ui/carousel/aniTypes/aniType_ripple.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/carousel/aniTypes/aniType_ripple_9fe398d.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/animation.js","wiki-common:widget/util/checkCSS.js"]},"wiki-common:widget/ui/carousel/aniTypes/aniType_scale.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/carousel/aniTypes/aniType_scale_be5032b.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/animation.js","wiki-common:widget/util/checkCSS.js"]},"wiki-common:widget/ui/carousel/aniTypes/aniType_slide.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/carousel/aniTypes/aniType_slide_bf10c5e.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/animation.js"]},"wiki-common:widget/ui/carousel/aniTypes/aniType_wipe.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/carousel/aniTypes/aniType_wipe_ae1fb29.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/animation.js","wiki-common:widget/util/checkCSS.js"]},"wiki-common:widget/ui/carousel/carousel.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/carousel/carousel_3e8f062.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/checkCSS.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/ui/carousel/aniTypes/aniType_slide.js","wiki-common:widget/util/number.js"]},"wiki-common:widget/ui/casecadeControl/casecadeControl.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/casecadeControl/casecadeControl_610fed4.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js"]},"wiki-common:widget/ui/counter/counter.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/counter/counter_3eb6022.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/animation.js","wiki-common:widget/util/number.js","wiki-common:widget/util/checkCSS.js"]},"wiki-common:widget/ui/datePicker/datePicker.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/datePicker/datePicker_0f9abb9.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/ui/bubble/bubble.js","wiki-common:widget/util/timeFormater.js","wiki-common:widget/util/checkCSS.js","wiki-common:widget/util/url.js","wiki-common:widget/util/safeCall.js"]},"wiki-common:widget/ui/overlay/overlay.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/overlay/overlay_494073e.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/animation.js"]},"wiki-common:widget/ui/dialog/windowScroll.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialog/windowScroll_45b6fe6.js","pkg":"wiki-common:p16"},"wiki-common:widget/ui/dialog/dialog.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialog/dialog_b36a239.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/ui/overlay/overlay.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/util/animation.js","wiki-common:widget/util/checkCSS.js","wiki-common:widget/ui/bubble/bubble.js","wiki-common:widget/ui/dialog/windowScroll.js"]},"wiki-common:widget/ui/dialogPlayer/constants.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/constants_5a97307.js","pkg":"wiki-common:p16"},"wiki-common:widget/ui/dialogPlayer/eventful.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/eventful_9516214.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/ui/dialogPlayer/dataManager.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/dataManager_491fcee.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/ui/dialogPlayer/eventful.js","wiki-common:widget/ui/dialogPlayer/constants.js"]},"wiki-common:widget/ui/dialogPlayer/shareBubble/shareBubble.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/shareBubble/shareBubble_77c447c.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/ui/bubble/bubble.js","wiki-common:widget/component/share/share.js","wiki-common:widget/component/share/dep/qrcode.js","wiki-common:widget/ui/dialogPlayer/eventful.js","wiki-common:widget/ui/dialogPlayer/constants.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/dom.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/dom_63133a4.js","pkg":"wiki-common:p16"},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/class.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/class_d5fac88.js","pkg":"wiki-common:p16"},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/helper.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/helper_bedb798.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/class.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/dom.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/default-setting.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/default-setting_45e166c.js","pkg":"wiki-common:p16"},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/event-manager.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/event-manager_ea2f6f1.js","pkg":"wiki-common:p16"},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/guid.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/guid_decc89d.js","pkg":"wiki-common:p16"},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances_66108ca.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/class.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/dom.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/default-setting.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/event-manager.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/guid.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/helper.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/destroy.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/destroy_e35bb20.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/dom.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/helper.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-scroll.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-scroll_d90a2a3.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-geometry.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-geometry_b61f58d.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/class.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/dom.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/helper.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/click-rail.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/click-rail_fd121c6.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/helper.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/drag-scrollbar.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/drag-scrollbar_9f2284c.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/dom.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/helper.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/keyboard.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/keyboard_755e8a3.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/helper.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/dom.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/mouse-wheel.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/mouse-wheel_c7a5a6d.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/native-scroll.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/native-scroll_a39bb7b.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-geometry.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/selection.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/selection_339f387.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/helper.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/touch.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/touch_93a22f8.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/initialize.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/initialize_ecafb67.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/class.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/helper.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/click-rail.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/drag-scrollbar.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/keyboard.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/mouse-wheel.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/native-scroll.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/selection.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/handler/touch.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update_69db2c4.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/dom.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/lib/helper.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/main.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/main_365dfc2.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/destroy.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/initialize.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/update.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/index_87ad452.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/main.js"]},"wiki-common:widget/ui/dialogPlayer/perfectScrollbar.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/perfectScrollbar_7a59ce7.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/util/browser.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/index.js","wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/ui/dialogPlayer/logMap.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/logMap_b08e01e.js","pkg":"wiki-common:p16"},"wiki-common:widget/ui/dialogPlayer/statistical.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/statistical_6e78240.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/nslog/nslog.js","wiki-common:widget/ui/dialogPlayer/logMap.js"]},"wiki-common:widget/ui/dialogPlayer/dialogPlayer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/dialogPlayer_b941a72.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/larkplayer/larkplayer.js","wiki-common:widget/ui/dialog/dialog.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/ui/dialogPlayer/dataManager.js","wiki-common:widget/ui/dialogPlayer/shareBubble/shareBubble.js","wiki-common:widget/ui/dialogPlayer/perfectScrollbar.js","wiki-common:widget/ui/dialogPlayer/constants.js","wiki-common:widget/ui/dialogPlayer/eventful.js","wiki-common:widget/ui/dialogPlayer/statistical.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/adaptor/global.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/adaptor/global_35490aa.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/main.js"]},"wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/adaptor/jquery.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/adaptor/jquery_68f4999.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/main.js","wiki-common:widget/ui/dialogPlayer/third_party/perfect-scrollbar/src/js/plugin/instances.js"]},"wiki-common:widget/ui/flip/flip.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/flip/flip_c6c88f2.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/checkCSS.js","wiki-common:widget/util/animation.js"]},"wiki-common:widget/ui/iqiyiPlayer/iqiyiPlayer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/iqiyiPlayer/iqiyiPlayer_2211bbd.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/swfObject/swfObject.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/guid.js","wiki-common:widget/util/string.js"]},"wiki-common:widget/ui/marquee/marquee.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/marquee/marquee_67512a8.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/animation.js"]},"wiki-common:widget/ui/pager/pagerBase.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/pager/pagerBase_077c16c.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js"]},"wiki-common:widget/ui/pager/horPager/horPager.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/pager/horPager/horPager_d6e3d4f.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/ui/pager/pagerBase.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/util/safeCall.js"]},"wiki-common:widget/ui/picUploader/Jcrop/Jcrop.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/picUploader/Jcrop/Jcrop_aa267d0.js","pkg":"wiki-common:p16"},"wiki-common:widget/ui/picUploader/picUploader.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/picUploader/picUploader_37696a7.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/ui/picUploader/Jcrop/Jcrop.js"]},"wiki-common:widget/ui/pie/pie.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/pie/pie_455c522.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/addStyleSheet.js","wiki-common:widget/util/browser.js","wiki-common:widget/util/color.js"]},"wiki-common:widget/ui/polyline/polyline.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/polyline/polyline_9a3e2d6.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/browser.js","wiki-common:widget/util/color.js","wiki-common:widget/util/animation.js","wiki-common:widget/util/number.js"]},"wiki-common:widget/ui/radar/radar.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/radar/radar_01ce27e.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/browser.js","wiki-common:widget/util/color.js","wiki-common:widget/util/animation.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/number.js"]},"wiki-common:widget/ui/tagsInput/tagsInput.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/tagsInput/tagsInput_075a56d.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/util/safeCall.js"]},"wiki-common:widget/ui/videoAutoPlay/video-ui-plugin.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/videoAutoPlay/video-ui-plugin.es_3e2cdae.js","pkg":"wiki-common:p16","deps":["wiki-common:node_modules/larkplayer/dist/larkplayer.js","wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/ui/videoAutoPlay/videoAutoPlay.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/videoAutoPlay/videoAutoPlay.es_f6c5b2a.js","pkg":"wiki-common:p16","deps":["wiki-common:node_modules/larkplayer/dist/larkplayer.js","wiki-common:node_modules/larkplayer-ui/dist/larkplayer-ui.js","wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/ui/videoAutoPlay/video-ui-plugin.es.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/ui/dialog/dialog.js","wiki-common:widget/tools/clickstream/clickstream.js","wiki-common:widget/util/browser.js"]},"wiki-common:widget/ui/videoPlayer/videoPlayer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/videoPlayer/videoPlayer_254e908.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/ui/iqiyiPlayer/iqiyiPlayer.js","wiki-common:widget/lib/letvPlayer/letvPlayer.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/guid.js","wiki-common:widget/util/timeFormater.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/lib/larkplayer/larkplayer.js"]},"wiki-common:widget/ui/videoDialog/videoDialog.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/ui/videoDialog/videoDialog_ea19733.js","pkg":"wiki-common:p16","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/ui/dialog/dialog.js","wiki-common:widget/ui/videoPlayer/videoPlayer.js","wiki-common:widget/util/guid.js"]},"wiki-common:node_modules/axios/lib/helpers/bind.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/helpers/bind_000c85d.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/axios/lib/utils.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/utils_23f26c4.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/helpers/bind.js"]},"wiki-common:node_modules/axios/lib/helpers/buildURL.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/helpers/buildURL_f3838ab.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js"]},"wiki-common:node_modules/axios/lib/core/InterceptorManager.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/core/InterceptorManager_e0aed1e.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js"]},"wiki-common:node_modules/axios/lib/helpers/normalizeHeaderName.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/helpers/normalizeHeaderName_627bf7b.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js"]},"wiki-common:node_modules/axios/lib/core/enhanceError.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/core/enhanceError_dbf3b27.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/axios/lib/defaults/transitional.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/defaults/transitional_9fa2c6b.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/axios/lib/core/createError.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/core/createError_7e6a27b.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/core/enhanceError.js"]},"wiki-common:node_modules/axios/lib/core/settle.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/core/settle_b63baf0.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/core/createError.js"]},"wiki-common:node_modules/axios/lib/helpers/cookies.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/helpers/cookies_2748410.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js"]},"wiki-common:node_modules/axios/lib/helpers/isAbsoluteURL.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/helpers/isAbsoluteURL_fb7fa82.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/axios/lib/helpers/combineURLs.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/helpers/combineURLs_d735d7d.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/axios/lib/core/buildFullPath.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/core/buildFullPath_d30a37e.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/helpers/isAbsoluteURL.js","wiki-common:node_modules/axios/lib/helpers/combineURLs.js"]},"wiki-common:node_modules/axios/lib/helpers/parseHeaders.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/helpers/parseHeaders_300d333.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js"]},"wiki-common:node_modules/axios/lib/helpers/isURLSameOrigin.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/helpers/isURLSameOrigin_e1e2671.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js"]},"wiki-common:node_modules/axios/lib/cancel/Cancel.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/cancel/Cancel_241a997.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/axios/lib/adapters/xhr.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/adapters/xhr_b3b3557.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js","wiki-common:node_modules/axios/lib/core/settle.js","wiki-common:node_modules/axios/lib/helpers/cookies.js","wiki-common:node_modules/axios/lib/helpers/buildURL.js","wiki-common:node_modules/axios/lib/core/buildFullPath.js","wiki-common:node_modules/axios/lib/helpers/parseHeaders.js","wiki-common:node_modules/axios/lib/helpers/isURLSameOrigin.js","wiki-common:node_modules/axios/lib/core/createError.js","wiki-common:node_modules/axios/lib/defaults/transitional.js","wiki-common:node_modules/axios/lib/cancel/Cancel.js"]},"wiki-common:node_modules/axios/lib/defaults/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/defaults/index_aa6f45c.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js","wiki-common:node_modules/axios/lib/helpers/normalizeHeaderName.js","wiki-common:node_modules/axios/lib/core/enhanceError.js","wiki-common:node_modules/axios/lib/defaults/transitional.js","wiki-common:node_modules/axios/lib/adapters/xhr.js"]},"wiki-common:node_modules/axios/lib/core/transformData.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/core/transformData_30260e6.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js","wiki-common:node_modules/axios/lib/defaults/index.js"]},"wiki-common:node_modules/axios/lib/cancel/isCancel.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/cancel/isCancel_c009671.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/axios/lib/core/dispatchRequest.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/core/dispatchRequest_e460c49.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js","wiki-common:node_modules/axios/lib/core/transformData.js","wiki-common:node_modules/axios/lib/cancel/isCancel.js","wiki-common:node_modules/axios/lib/defaults/index.js","wiki-common:node_modules/axios/lib/cancel/Cancel.js"]},"wiki-common:node_modules/axios/lib/core/mergeConfig.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/core/mergeConfig_1ec3e1d.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js"]},"wiki-common:node_modules/axios/lib/env/data.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/env/data_08dc47a.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/axios/lib/helpers/validator.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/helpers/validator_68e67a4.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/env/data.js"]},"wiki-common:node_modules/axios/lib/core/Axios.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/core/Axios_cd6eb42.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js","wiki-common:node_modules/axios/lib/helpers/buildURL.js","wiki-common:node_modules/axios/lib/core/InterceptorManager.js","wiki-common:node_modules/axios/lib/core/dispatchRequest.js","wiki-common:node_modules/axios/lib/core/mergeConfig.js","wiki-common:node_modules/axios/lib/helpers/validator.js"]},"wiki-common:node_modules/axios/lib/cancel/CancelToken.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/cancel/CancelToken_e6d8cd3.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/cancel/Cancel.js"]},"wiki-common:node_modules/axios/lib/helpers/spread.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/helpers/spread_168c2b3.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/axios/lib/helpers/isAxiosError.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/helpers/isAxiosError_047693f.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js"]},"wiki-common:node_modules/axios/lib/axios.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/lib/axios_719e8d5.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/utils.js","wiki-common:node_modules/axios/lib/helpers/bind.js","wiki-common:node_modules/axios/lib/core/Axios.js","wiki-common:node_modules/axios/lib/core/mergeConfig.js","wiki-common:node_modules/axios/lib/defaults/index.js","wiki-common:node_modules/axios/lib/cancel/Cancel.js","wiki-common:node_modules/axios/lib/cancel/CancelToken.js","wiki-common:node_modules/axios/lib/cancel/isCancel.js","wiki-common:node_modules/axios/lib/env/data.js","wiki-common:node_modules/axios/lib/helpers/spread.js","wiki-common:node_modules/axios/lib/helpers/isAxiosError.js"]},"wiki-common:node_modules/axios/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/axios/index_f14c762.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/axios/lib/axios.js"]},"wiki-common:node_modules/clipboard/dist/clipboard.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/clipboard/dist/clipboard_757f029.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/date-format/lib/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/date-format/lib/index_000ac82.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/eventemitter3/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/eventemitter3/index_0a2d6cc.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/format-duration/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/format-duration/index_b77bcc5.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/strict-uri-encode/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/strict-uri-encode/index_08a94b7.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/decode-uri-component/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/decode-uri-component/index_1f0a68c.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/query-string/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/query-string/index_b674337.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/strict-uri-encode/index.js","wiki-common:node_modules/object-assign/index.js","wiki-common:node_modules/decode-uri-component/index.js"]},"wiki-common:node_modules/qrcode/lib/can-promise.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/can-promise_69d721d.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/qrcode/lib/core/utils.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/utils_e6d19af.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/qrcode/lib/core/error-correction-level.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/error-correction-level_cdba080.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/qrcode/lib/core/bit-buffer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/bit-buffer_28931ed.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/qrcode/lib/core/bit-matrix.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/bit-matrix_e861cbe.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/qrcode/lib/core/alignment-pattern.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/alignment-pattern_2dbf2aa.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/utils.js"]},"wiki-common:node_modules/qrcode/lib/core/finder-pattern.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/finder-pattern_7801d16.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/utils.js"]},"wiki-common:node_modules/qrcode/lib/core/mask-pattern.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/mask-pattern_8fc52ab.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/qrcode/lib/core/error-correction-code.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/error-correction-code_e49366a.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/error-correction-level.js"]},"wiki-common:node_modules/qrcode/lib/core/galois-field.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/galois-field_2df075d.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/qrcode/lib/core/polynomial.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/polynomial_1759123.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/galois-field.js"]},"wiki-common:node_modules/qrcode/lib/core/reed-solomon-encoder.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/reed-solomon-encoder_c909bbb.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/polynomial.js"]},"wiki-common:node_modules/qrcode/lib/core/version-check.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/version-check_1a02725.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/qrcode/lib/core/regex.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/regex_16bf1e4.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/qrcode/lib/core/mode.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/mode_611f4c0.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/version-check.js","wiki-common:node_modules/qrcode/lib/core/regex.js"]},"wiki-common:node_modules/qrcode/lib/core/version.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/version_9b5b7d5.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/utils.js","wiki-common:node_modules/qrcode/lib/core/error-correction-code.js","wiki-common:node_modules/qrcode/lib/core/error-correction-level.js","wiki-common:node_modules/qrcode/lib/core/mode.js","wiki-common:node_modules/qrcode/lib/core/version-check.js"]},"wiki-common:node_modules/qrcode/lib/core/format-info.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/format-info_3302bfa.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/utils.js"]},"wiki-common:node_modules/qrcode/lib/core/numeric-data.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/numeric-data_05f9898.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/mode.js"]},"wiki-common:node_modules/qrcode/lib/core/alphanumeric-data.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/alphanumeric-data_51e601a.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/mode.js"]},"wiki-common:node_modules/encode-utf8/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/encode-utf8/index_9c69731.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/qrcode/lib/core/byte-data.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/byte-data_fe2b95e.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/encode-utf8/index.js","wiki-common:node_modules/qrcode/lib/core/mode.js"]},"wiki-common:node_modules/qrcode/lib/core/kanji-data.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/kanji-data_dd3888f.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/mode.js","wiki-common:node_modules/qrcode/lib/core/utils.js"]},"wiki-common:node_modules/dijkstrajs/dijkstra.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/dijkstrajs/dijkstra_63f8f04.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/qrcode/lib/core/segments.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/segments_9e61e35.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/mode.js","wiki-common:node_modules/qrcode/lib/core/numeric-data.js","wiki-common:node_modules/qrcode/lib/core/alphanumeric-data.js","wiki-common:node_modules/qrcode/lib/core/byte-data.js","wiki-common:node_modules/qrcode/lib/core/kanji-data.js","wiki-common:node_modules/qrcode/lib/core/regex.js","wiki-common:node_modules/qrcode/lib/core/utils.js","wiki-common:node_modules/dijkstrajs/dijkstra.js"]},"wiki-common:node_modules/qrcode/lib/core/qrcode.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/core/qrcode_01758e8.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/core/utils.js","wiki-common:node_modules/qrcode/lib/core/error-correction-level.js","wiki-common:node_modules/qrcode/lib/core/bit-buffer.js","wiki-common:node_modules/qrcode/lib/core/bit-matrix.js","wiki-common:node_modules/qrcode/lib/core/alignment-pattern.js","wiki-common:node_modules/qrcode/lib/core/finder-pattern.js","wiki-common:node_modules/qrcode/lib/core/mask-pattern.js","wiki-common:node_modules/qrcode/lib/core/error-correction-code.js","wiki-common:node_modules/qrcode/lib/core/reed-solomon-encoder.js","wiki-common:node_modules/qrcode/lib/core/version.js","wiki-common:node_modules/qrcode/lib/core/format-info.js","wiki-common:node_modules/qrcode/lib/core/mode.js","wiki-common:node_modules/qrcode/lib/core/segments.js"]},"wiki-common:node_modules/qrcode/lib/renderer/utils.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/renderer/utils_0466d16.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/qrcode/lib/renderer/canvas.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/renderer/canvas_e156f6c.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/renderer/utils.js"]},"wiki-common:node_modules/qrcode/lib/renderer/svg-tag.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/renderer/svg-tag_02276af.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/renderer/utils.js"]},"wiki-common:node_modules/qrcode/lib/browser.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qrcode/lib/browser_47526f1.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/qrcode/lib/can-promise.js","wiki-common:node_modules/qrcode/lib/core/qrcode.js","wiki-common:node_modules/qrcode/lib/renderer/canvas.js","wiki-common:node_modules/qrcode/lib/renderer/svg-tag.js"]},"wiki-common:node_modules/lodash.debounce/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/lodash.debounce/index_16cccf5.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/lodash.get/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/lodash.get/index_75ff6fd.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/lodash.throttle/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/lodash.throttle/index_012b848.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/uuid/dist/rng-browser.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/rng-browser_ddf0af0.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/uuid/dist/regex.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/regex_efcb3ac.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/uuid/dist/validate.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/validate_cb07094.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/uuid/dist/regex.js"]},"wiki-common:node_modules/uuid/dist/stringify.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/stringify_47eeea3.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/uuid/dist/validate.js"]},"wiki-common:node_modules/uuid/dist/v1.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/v1_d736663.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/uuid/dist/rng-browser.js","wiki-common:node_modules/uuid/dist/stringify.js"]},"wiki-common:node_modules/uuid/dist/parse.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/parse_5670e9c.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/uuid/dist/validate.js"]},"wiki-common:node_modules/uuid/dist/v35.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/v35_248abbe.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/uuid/dist/stringify.js","wiki-common:node_modules/uuid/dist/parse.js"]},"wiki-common:node_modules/uuid/dist/md5-browser.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/md5-browser_83b277e.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/uuid/dist/v3.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/v3_cc44fb4.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/uuid/dist/v35.js","wiki-common:node_modules/uuid/dist/md5-browser.js"]},"wiki-common:node_modules/uuid/dist/v4.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/v4_b5ec229.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/uuid/dist/rng-browser.js","wiki-common:node_modules/uuid/dist/stringify.js"]},"wiki-common:node_modules/uuid/dist/sha1-browser.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/sha1-browser_1a81814.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/uuid/dist/v5.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/v5_8816311.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/uuid/dist/v35.js","wiki-common:node_modules/uuid/dist/sha1-browser.js"]},"wiki-common:node_modules/uuid/dist/nil.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/nil_4fed50e.js","pkg":"wiki-common:p2"},"wiki-common:node_modules/uuid/dist/version.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/version_1380662.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/uuid/dist/validate.js"]},"wiki-common:node_modules/uuid/dist/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/uuid/dist/index_e98e454.js","pkg":"wiki-common:p2","deps":["wiki-common:node_modules/uuid/dist/v1.js","wiki-common:node_modules/uuid/dist/v3.js","wiki-common:node_modules/uuid/dist/v4.js","wiki-common:node_modules/uuid/dist/v5.js","wiki-common:node_modules/uuid/dist/nil.js","wiki-common:node_modules/uuid/dist/version.js","wiki-common:node_modules/uuid/dist/validate.js","wiki-common:node_modules/uuid/dist/stringify.js","wiki-common:node_modules/uuid/dist/parse.js"]},"wiki-common:widget/component/nslog/nslog.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/nslog/nslog_4e4ac21.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/component/share/dep/qrcode.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/share/dep/qrcode_51c716b.js","pkg":"wiki-common:p10"},"wiki-common:widget/component/baikeAppPromote/baikeAppPromote.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/baikeAppPromote/baikeAppPromote.es_59b6790.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/util/guid.js","wiki-common:widget/component/nslog/nslog.js","wiki-common:widget/component/share/dep/qrcode.js"]},"wiki-common:widget/component/cmsModuleLoader/cmsModuleLoader.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/cmsModuleLoader/cmsModuleLoader_e8ac5be.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/component/evtMsgManager/event.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/evtMsgManager/event_662db9d.js","pkg":"wiki-common:p10"},"wiki-common:widget/component/evtMsgManager/evtMsgManager.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/evtMsgManager/evtMsgManager.es_c645f73.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/util/eventEmitter.js","wiki-common:widget/component/evtMsgManager/event.js"]},"wiki-common:widget/component/footer/footer_feedback.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/footer/footer_feedback_b663b77.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/component/headTabBar/headTabBar.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/headTabBar/headTabBar_2c4e3a0.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/component/lemmasInput-n/lemmasInput-n.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/lemmasInput-n/lemmasInput-n_a1debe4.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/ui/dialog/dialog.js","wiki-common:widget/ui/tagsInput/tagsInput.js","wiki-common:widget/util/safeCall.js"]},"wiki-common:widget/component/lemmasInput/lemmasInput.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/lemmasInput/lemmasInput_a8a8876.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/string.js","wiki-common:widget/ui/tagsInput/tagsInput.js","wiki-common:widget/ui/dialog/dialog.js"]},"wiki-common:widget/component/picUploader/Jcrop/Jcrop.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/picUploader/Jcrop/Jcrop_6648d3d.js","pkg":"wiki-common:p10"},"wiki-common:widget/component/picUploader/picCropper.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/picUploader/picCropper_3a7343d.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/ui/picUploader/Jcrop/Jcrop.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/util/safeCall.js"]},"wiki-common:widget/component/picUploader/picUploader.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/picUploader/picUploader_f4e22dc.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/util/safeCall.js"]},"wiki-common:widget/component/recruitment/recruitment.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/recruitment/recruitment_24c1a45.js","pkg":"wiki-common:p10"},"wiki-common:widget/component/searchbar-n/searchbar.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/searchbar-n/searchbar_d8eccb1.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/browser.js","wiki-common:widget/util/cookie.js"]},"wiki-common:widget/component/searchbar/searchbar.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/searchbar/searchbar_663d882.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/browser.js"]},"wiki-common:widget/component/share/share.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/share/share_7aa442e.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/component/share/dep/qrcode.js","wiki-common:widget/util/url.js","wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/component/shareBubble/shareBubble.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/shareBubble/shareBubble_9ac7a39.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/ui/bubble/bubble.js","wiki-common:widget/component/share/share.js","wiki-common:widget/component/share/dep/qrcode.js","wiki-common:widget/util/url.js","wiki-common:node_modules/clipboard/dist/clipboard.js","wiki-common:widget/tools/clickstream/clickstream.js"]},"wiki-common:widget/component/superLogger/superLogger.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/superLogger/superLogger.es_7235327.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/component/testElem/testElem.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/testElem/testElem_d3c0ea0.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/util/string.js","wiki-common:widget/component/nslog/nslog.js"]},"wiki-common:widget/component/themeInput/themeInput.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/themeInput/themeInput_c4c8a62.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/ui/tagsInput/tagsInput.js"]},"wiki-common:widget/component/unameFiller/unameFiller.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/unameFiller/unameFiller_d37ebcb.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/ui/dialog/dialog.js"]},"wiki-common:widget/component/uploadImg/uploadImg.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/uploadImg/uploadImg_e0357a1.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/component/urls/getLemmaUrl.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/urls/getLemmaUrl_ec3f27f.js","pkg":"wiki-common:p10"},"wiki-common:widget/component/userLogin/userLogin.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/userLogin/userLogin_8a4807c.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-common:widget/component/userbar-n/userbar-n.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/userbar-n/userbar-n_0a7a442.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/userLogin/userLogin.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/util/browser.js","wiki-common:widget/ui/bubble/bubble.js"]},"wiki-common:widget/component/userCard/userCard.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/userCard/userCard_f6b5d1f.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/ui/bubble/bubble.js"]},"wiki-common:widget/component/userMsg/userMsg.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/widget/component/userMsg/userMsg_21cd452.js","pkg":"wiki-common:p10","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/userLogin/userLogin.js"]},"wiki-common:node_modules/react/cjs/react.production.min.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/react/cjs/react.production.min_874691d.js","pkg":"wiki-common:p1","deps":["wiki-common:node_modules/object-assign/index.js"]},"wiki-common:node_modules/react/cjs/react.development.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/react/cjs/react.development_5e33078.js","pkg":"wiki-common:p1","deps":["wiki-common:node_modules/object-assign/index.js"]},"wiki-common:node_modules/react/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/react/index_8471d1a.js","pkg":"wiki-common:p1","deps":["wiki-common:node_modules/react/cjs/react.production.min.js","wiki-common:node_modules/react/cjs/react.development.js"]},"wiki-common:node_modules/scheduler/cjs/scheduler.production.min.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/scheduler/cjs/scheduler.production.min_e63711c.js","pkg":"wiki-common:p1"},"wiki-common:node_modules/scheduler/cjs/scheduler.development.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/scheduler/cjs/scheduler.development_7aa2a03.js","pkg":"wiki-common:p1"},"wiki-common:node_modules/scheduler/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/scheduler/index_65581d8.js","pkg":"wiki-common:p1","deps":["wiki-common:node_modules/scheduler/cjs/scheduler.production.min.js","wiki-common:node_modules/scheduler/cjs/scheduler.development.js"]},"wiki-common:node_modules/react-dom/cjs/react-dom.production.min.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/react-dom/cjs/react-dom.production.min_6590d53.js","pkg":"wiki-common:p1","deps":["wiki-common:node_modules/react/index.js","wiki-common:node_modules/object-assign/index.js","wiki-common:node_modules/scheduler/index.js"]},"wiki-common:node_modules/scheduler/cjs/scheduler-tracing.production.min.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/scheduler/cjs/scheduler-tracing.production.min_40aff9b.js","pkg":"wiki-common:p1"},"wiki-common:node_modules/scheduler/cjs/scheduler-tracing.development.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/scheduler/cjs/scheduler-tracing.development_e3a4441.js","pkg":"wiki-common:p1"},"wiki-common:node_modules/scheduler/tracing.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/scheduler/tracing_64bff6f.js","pkg":"wiki-common:p1","deps":["wiki-common:node_modules/scheduler/cjs/scheduler-tracing.production.min.js","wiki-common:node_modules/scheduler/cjs/scheduler-tracing.development.js"]},"wiki-common:node_modules/react-dom/cjs/react-dom.development.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/react-dom/cjs/react-dom.development_93f6dcd.js","pkg":"wiki-common:p1","deps":["wiki-common:node_modules/react/index.js","wiki-common:node_modules/object-assign/index.js","wiki-common:node_modules/scheduler/index.js","wiki-common:node_modules/scheduler/tracing.js"]},"wiki-common:node_modules/react-dom/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/react-dom/index_7c4635a.js","pkg":"wiki-common:p1","deps":["wiki-common:node_modules/react-dom/cjs/react-dom.production.min.js","wiki-common:node_modules/react-dom/cjs/react-dom.development.js"]},"wiki-common:node_modules/rc-util/lib/raf.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/raf_9de3127.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/rc-util/lib/Dom/canUseDom.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/Dom/canUseDom_5b1996c.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/rc-util/lib/Portal.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/Portal_f557244.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/react-dom/index.js","wiki-common:node_modules/rc-util/lib/Dom/canUseDom.js"]},"wiki-common:node_modules/rc-util/lib/getScrollBarSize.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/getScrollBarSize_1f9ee89.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/rc-util/lib/setStyle.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/setStyle_110fd08.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/rc-util/lib/switchScrollingEffect.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/switchScrollingEffect_4b20270.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/rc-util/lib/getScrollBarSize.js","wiki-common:node_modules/rc-util/lib/setStyle.js"]},"wiki-common:node_modules/rc-util/lib/Dom/scrollLocker.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/Dom/scrollLocker_84463ca.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/toConsumableArray.js","wiki-common:node_modules/@babel/runtime/helpers/createClass.js","wiki-common:node_modules/@babel/runtime/helpers/classCallCheck.js","wiki-common:node_modules/rc-util/lib/getScrollBarSize.js","wiki-common:node_modules/rc-util/lib/setStyle.js"]},"wiki-common:node_modules/rc-util/lib/PortalWrapper.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/PortalWrapper_3af4e83.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/classCallCheck.js","wiki-common:node_modules/@babel/runtime/helpers/createClass.js","wiki-common:node_modules/@babel/runtime/helpers/inherits.js","wiki-common:node_modules/@babel/runtime/helpers/createSuper.js","wiki-common:node_modules/@babel/runtime/helpers/typeof.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-util/lib/raf.js","wiki-common:node_modules/rc-util/lib/Portal.js","wiki-common:node_modules/rc-util/lib/Dom/canUseDom.js","wiki-common:node_modules/rc-util/lib/switchScrollingEffect.js","wiki-common:node_modules/rc-util/lib/setStyle.js","wiki-common:node_modules/rc-util/lib/Dom/scrollLocker.js"]},"wiki-common:node_modules/classnames/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/classnames/index_0d09d32.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/rc-util/lib/KeyCode.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/KeyCode_7c22ce1.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/rc-util/lib/Dom/contains.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/Dom/contains_60fbfcc.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/rc-util/lib/pickAttrs.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/pickAttrs_3c0c8fc.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/objectSpread2.js"]},"wiki-common:node_modules/rc-util/lib/Dom/findDOMNode.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/Dom/findDOMNode_b8c32ef.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/react-dom/index.js"]},"wiki-common:node_modules/react-is/cjs/react-is.production.min.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/react-is/cjs/react-is.production.min_e0dbae5.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/react-is/cjs/react-is.development.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/react-is/cjs/react-is.development_a84cebf.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/react-is/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/react-is/index_41bb64c.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/react-is/cjs/react-is.production.min.js","wiki-common:node_modules/react-is/cjs/react-is.development.js"]},"wiki-common:node_modules/rc-util/lib/hooks/useMemo.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/hooks/useMemo_9cca5ba.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/react/index.js"]},"wiki-common:node_modules/rc-util/lib/ref.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/ref_fa7d6be.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/typeof.js","wiki-common:node_modules/react-is/index.js","wiki-common:node_modules/rc-util/lib/hooks/useMemo.js"]},"wiki-common:node_modules/rc-motion/lib/util/motion.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-motion/lib/util/motion_3dde0ad.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/typeof.js","wiki-common:node_modules/rc-util/lib/Dom/canUseDom.js"]},"wiki-common:node_modules/rc-motion/lib/interface.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-motion/lib/interface_c50b1ef.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/rc-util/lib/hooks/useState.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/hooks/useState_f4bc02c.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/slicedToArray.js","wiki-common:node_modules/react/index.js"]},"wiki-common:node_modules/rc-motion/lib/hooks/useNextFrame.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-motion/lib/hooks/useNextFrame_ad79687.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-util/lib/raf.js"]},"wiki-common:node_modules/rc-motion/lib/hooks/useIsomorphicLayoutEffect.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-motion/lib/hooks/useIsomorphicLayoutEffect_051130c.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-util/lib/Dom/canUseDom.js"]},"wiki-common:node_modules/rc-motion/lib/hooks/useStepQueue.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-motion/lib/hooks/useStepQueue_1816f46.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/slicedToArray.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-util/lib/hooks/useState.js","wiki-common:node_modules/rc-motion/lib/interface.js","wiki-common:node_modules/rc-motion/lib/hooks/useNextFrame.js","wiki-common:node_modules/rc-motion/lib/hooks/useIsomorphicLayoutEffect.js"]},"wiki-common:node_modules/rc-motion/lib/hooks/useDomMotionEvents.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-motion/lib/hooks/useDomMotionEvents_593b13d.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-motion/lib/util/motion.js"]},"wiki-common:node_modules/rc-motion/lib/hooks/useStatus.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-motion/lib/hooks/useStatus_b352b21.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/objectSpread2.js","wiki-common:node_modules/@babel/runtime/helpers/defineProperty.js","wiki-common:node_modules/@babel/runtime/helpers/slicedToArray.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-util/lib/hooks/useState.js","wiki-common:node_modules/rc-motion/lib/interface.js","wiki-common:node_modules/rc-motion/lib/hooks/useStepQueue.js","wiki-common:node_modules/rc-motion/lib/hooks/useDomMotionEvents.js","wiki-common:node_modules/rc-motion/lib/hooks/useIsomorphicLayoutEffect.js"]},"wiki-common:node_modules/rc-motion/lib/DomWrapper.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-motion/lib/DomWrapper_1f9ec34.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/classCallCheck.js","wiki-common:node_modules/@babel/runtime/helpers/createClass.js","wiki-common:node_modules/@babel/runtime/helpers/inherits.js","wiki-common:node_modules/@babel/runtime/helpers/createSuper.js","wiki-common:node_modules/react/index.js"]},"wiki-common:node_modules/rc-motion/lib/CSSMotion.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-motion/lib/CSSMotion_5baa002.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/defineProperty.js","wiki-common:node_modules/@babel/runtime/helpers/objectSpread2.js","wiki-common:node_modules/@babel/runtime/helpers/slicedToArray.js","wiki-common:node_modules/@babel/runtime/helpers/typeof.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-util/lib/Dom/findDOMNode.js","wiki-common:node_modules/rc-util/lib/ref.js","wiki-common:node_modules/classnames/index.js","wiki-common:node_modules/rc-motion/lib/util/motion.js","wiki-common:node_modules/rc-motion/lib/interface.js","wiki-common:node_modules/rc-motion/lib/hooks/useStatus.js","wiki-common:node_modules/rc-motion/lib/DomWrapper.js","wiki-common:node_modules/rc-motion/lib/hooks/useStepQueue.js"]},"wiki-common:node_modules/rc-motion/lib/util/diff.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-motion/lib/util/diff_72a33c4.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/objectSpread2.js","wiki-common:node_modules/@babel/runtime/helpers/typeof.js"]},"wiki-common:node_modules/rc-motion/lib/CSSMotionList.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-motion/lib/CSSMotionList_2b14baa.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/extends.js","wiki-common:node_modules/@babel/runtime/helpers/objectWithoutProperties.js","wiki-common:node_modules/@babel/runtime/helpers/objectSpread2.js","wiki-common:node_modules/@babel/runtime/helpers/classCallCheck.js","wiki-common:node_modules/@babel/runtime/helpers/createClass.js","wiki-common:node_modules/@babel/runtime/helpers/inherits.js","wiki-common:node_modules/@babel/runtime/helpers/createSuper.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-motion/lib/CSSMotion.js","wiki-common:node_modules/rc-motion/lib/util/motion.js","wiki-common:node_modules/rc-motion/lib/util/diff.js"]},"wiki-common:node_modules/rc-motion/lib/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-motion/lib/index_f0185c3.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/rc-motion/lib/CSSMotion.js","wiki-common:node_modules/rc-motion/lib/CSSMotionList.js"]},"wiki-common:node_modules/rc-dialog/lib/Dialog/Mask.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-dialog/lib/Dialog/Mask_20449f4.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/extends.js","wiki-common:node_modules/@babel/runtime/helpers/objectSpread2.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/classnames/index.js","wiki-common:node_modules/rc-motion/lib/index.js"]},"wiki-common:node_modules/rc-dialog/lib/util.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-dialog/lib/util_4135d27.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/rc-dialog/lib/Dialog/Content/MemoChildren.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-dialog/lib/Dialog/Content/MemoChildren_6b5138d.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/react/index.js"]},"wiki-common:node_modules/rc-dialog/lib/Dialog/Content/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-dialog/lib/Dialog/Content/index_45a521e.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/objectSpread2.js","wiki-common:node_modules/@babel/runtime/helpers/extends.js","wiki-common:node_modules/@babel/runtime/helpers/slicedToArray.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/classnames/index.js","wiki-common:node_modules/rc-motion/lib/index.js","wiki-common:node_modules/rc-dialog/lib/util.js","wiki-common:node_modules/rc-dialog/lib/Dialog/Content/MemoChildren.js"]},"wiki-common:node_modules/rc-dialog/lib/Dialog/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-dialog/lib/Dialog/index_5756171.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/extends.js","wiki-common:node_modules/@babel/runtime/helpers/objectSpread2.js","wiki-common:node_modules/@babel/runtime/helpers/slicedToArray.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/classnames/index.js","wiki-common:node_modules/rc-util/lib/KeyCode.js","wiki-common:node_modules/rc-util/lib/Dom/contains.js","wiki-common:node_modules/rc-util/lib/pickAttrs.js","wiki-common:node_modules/rc-dialog/lib/Dialog/Mask.js","wiki-common:node_modules/rc-dialog/lib/util.js","wiki-common:node_modules/rc-dialog/lib/Dialog/Content/index.js"]},"wiki-common:node_modules/rc-dialog/lib/DialogWrap.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-dialog/lib/DialogWrap_890155e.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/extends.js","wiki-common:node_modules/@babel/runtime/helpers/slicedToArray.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-util/lib/PortalWrapper.js","wiki-common:node_modules/rc-dialog/lib/Dialog/index.js"]},"wiki-common:node_modules/rc-dialog/lib/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-dialog/lib/index_6166b71.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/rc-dialog/lib/DialogWrap.js"]},"wiki-common:node_modules/rc-util/lib/hooks/useMergedState.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/hooks/useMergedState_b0307d1.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/slicedToArray.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-util/lib/hooks/useState.js"]},"wiki-common:node_modules/rc-switch/lib/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-switch/lib/index_35b66bc.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/defineProperty.js","wiki-common:node_modules/@babel/runtime/helpers/slicedToArray.js","wiki-common:node_modules/@babel/runtime/helpers/objectWithoutProperties.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/classnames/index.js","wiki-common:node_modules/rc-util/lib/hooks/useMergedState.js","wiki-common:node_modules/rc-util/lib/KeyCode.js"]},"wiki-common:node_modules/rc-util/lib/Children/toArray.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/Children/toArray_8d82364.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/react-is/index.js"]},"wiki-common:node_modules/rc-util/lib/warning.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/warning_65ef62c.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/resize-observer-polyfill/dist/ResizeObserver.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/resize-observer-polyfill/dist/ResizeObserver_8e89f36.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/rc-resize-observer/lib/utils/observerUtil.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-resize-observer/lib/utils/observerUtil_d1bfc0f.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/resize-observer-polyfill/dist/ResizeObserver.js"]},"wiki-common:node_modules/rc-resize-observer/lib/SingleObserver/DomWrapper.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-resize-observer/lib/SingleObserver/DomWrapper_1d5ff59.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/classCallCheck.js","wiki-common:node_modules/@babel/runtime/helpers/createClass.js","wiki-common:node_modules/@babel/runtime/helpers/inherits.js","wiki-common:node_modules/@babel/runtime/helpers/createSuper.js","wiki-common:node_modules/react/index.js"]},"wiki-common:node_modules/rc-resize-observer/lib/Collection.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-resize-observer/lib/Collection_c8ae6e3.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/react/index.js"]},"wiki-common:node_modules/rc-resize-observer/lib/SingleObserver/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-resize-observer/lib/SingleObserver/index_c48e6e0.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/objectSpread2.js","wiki-common:node_modules/rc-util/lib/ref.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-util/lib/Dom/findDOMNode.js","wiki-common:node_modules/rc-resize-observer/lib/utils/observerUtil.js","wiki-common:node_modules/rc-resize-observer/lib/SingleObserver/DomWrapper.js","wiki-common:node_modules/rc-resize-observer/lib/Collection.js"]},"wiki-common:node_modules/rc-resize-observer/lib/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-resize-observer/lib/index_704f250.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/extends.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-util/lib/Children/toArray.js","wiki-common:node_modules/rc-util/lib/warning.js","wiki-common:node_modules/rc-resize-observer/lib/SingleObserver/index.js","wiki-common:node_modules/rc-resize-observer/lib/Collection.js"]},"wiki-common:node_modules/rc-util/lib/omit.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-util/lib/omit_a79b8ba.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/objectSpread2.js"]},"wiki-common:node_modules/rc-textarea/lib/calculateNodeHeight.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-textarea/lib/calculateNodeHeight_e2f0b42.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/shallowequal/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/shallowequal/index_f611873.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/rc-textarea/lib/ResizableTextArea.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-textarea/lib/ResizableTextArea_d2fa2f8.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/extends.js","wiki-common:node_modules/@babel/runtime/helpers/objectSpread2.js","wiki-common:node_modules/@babel/runtime/helpers/defineProperty.js","wiki-common:node_modules/@babel/runtime/helpers/classCallCheck.js","wiki-common:node_modules/@babel/runtime/helpers/createClass.js","wiki-common:node_modules/@babel/runtime/helpers/inherits.js","wiki-common:node_modules/@babel/runtime/helpers/createSuper.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-resize-observer/lib/index.js","wiki-common:node_modules/rc-util/lib/omit.js","wiki-common:node_modules/classnames/index.js","wiki-common:node_modules/rc-textarea/lib/calculateNodeHeight.js","wiki-common:node_modules/shallowequal/index.js"]},"wiki-common:node_modules/rc-textarea/lib/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/rc-textarea/lib/index_ef03474.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/@babel/runtime/helpers/interopRequireWildcard.js","wiki-common:node_modules/@babel/runtime/helpers/interopRequireDefault.js","wiki-common:node_modules/@babel/runtime/helpers/extends.js","wiki-common:node_modules/@babel/runtime/helpers/classCallCheck.js","wiki-common:node_modules/@babel/runtime/helpers/createClass.js","wiki-common:node_modules/@babel/runtime/helpers/inherits.js","wiki-common:node_modules/@babel/runtime/helpers/createSuper.js","wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-textarea/lib/ResizableTextArea.js"]},"wiki-common:node_modules/react-cool-onclickoutside/dist/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/react-cool-onclickoutside/dist/index_9184201.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:node_modules/reactjs-popup/dist/reactjs-popup.cjs.production.min.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/reactjs-popup/dist/reactjs-popup.cjs.production.min_c21ae86.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/react/index.js","wiki-common:node_modules/react-dom/index.js"]},"wiki-common:node_modules/reactjs-popup/dist/reactjs-popup.cjs.development.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/reactjs-popup/dist/reactjs-popup.cjs.development_038561d.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/react/index.js","wiki-common:node_modules/react-dom/index.js"]},"wiki-common:node_modules/reactjs-popup/dist/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/reactjs-popup/dist/index_b9476a8.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/reactjs-popup/dist/reactjs-popup.cjs.production.min.js","wiki-common:node_modules/reactjs-popup/dist/reactjs-popup.cjs.development.js"]},"wiki-common:node_modules/toggle-selection/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/toggle-selection/index_58176bc.js","pkg":"wiki-common:p4"},"wiki-common:node_modules/copy-to-clipboard/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/copy-to-clipboard/index_8d70cc0.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/toggle-selection/index.js"]},"wiki-common:node_modules/react-copy-to-clipboard/lib/Component.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/react-copy-to-clipboard/lib/Component_10c9405.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/react/index.js","wiki-common:node_modules/copy-to-clipboard/index.js"]},"wiki-common:node_modules/react-copy-to-clipboard/lib/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/react-copy-to-clipboard/lib/index_2bf5018.js","pkg":"wiki-common:p4","deps":["wiki-common:node_modules/react-copy-to-clipboard/lib/Component.js"]},"wiki-common:packages/utils/eventEmitter.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/eventEmitter_2572989.js","pkg":"wiki-common:p24","deps":["wiki-common:node_modules/eventemitter3/index.js"]},"wiki-common:node_modules/has-symbols/shams.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/has-symbols/shams_0b7fc79.js","pkg":"wiki-common:p6"},"wiki-common:node_modules/has-symbols/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/has-symbols/index_d61fd72.js","pkg":"wiki-common:p6","deps":["wiki-common:node_modules/has-symbols/shams.js"]},"wiki-common:node_modules/function-bind/implementation.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/function-bind/implementation_b67595a.js","pkg":"wiki-common:p6"},"wiki-common:node_modules/function-bind/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/function-bind/index_192f91d.js","pkg":"wiki-common:p6","deps":["wiki-common:node_modules/function-bind/implementation.js"]},"wiki-common:node_modules/has/src/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/has/src/index_1aae111.js","pkg":"wiki-common:p6","deps":["wiki-common:node_modules/function-bind/index.js"]},"wiki-common:node_modules/get-intrinsic/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/get-intrinsic/index_19998a5.js","pkg":"wiki-common:p6","deps":["wiki-common:node_modules/has-symbols/index.js","wiki-common:node_modules/function-bind/index.js","wiki-common:node_modules/has/src/index.js"]},"wiki-common:node_modules/call-bind/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/call-bind/index_224e538.js","pkg":"wiki-common:p6","deps":["wiki-common:node_modules/function-bind/index.js","wiki-common:node_modules/get-intrinsic/index.js"]},"wiki-common:node_modules/call-bind/callBound.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/call-bind/callBound_3688e7b.js","pkg":"wiki-common:p6","deps":["wiki-common:node_modules/get-intrinsic/index.js","wiki-common:node_modules/call-bind/index.js"]},"wiki-common:node_modules/object-inspect/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/object-inspect/index_113f1f6.js","pkg":"wiki-common:p6"},"wiki-common:node_modules/side-channel/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/side-channel/index_29c9a4e.js","pkg":"wiki-common:p6","deps":["wiki-common:node_modules/get-intrinsic/index.js","wiki-common:node_modules/call-bind/callBound.js","wiki-common:node_modules/object-inspect/index.js"]},"wiki-common:node_modules/qs/lib/formats.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qs/lib/formats_6636eb3.js","pkg":"wiki-common:p6"},"wiki-common:node_modules/qs/lib/utils.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qs/lib/utils_b710920.js","pkg":"wiki-common:p6","deps":["wiki-common:node_modules/qs/lib/formats.js"]},"wiki-common:node_modules/qs/lib/stringify.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qs/lib/stringify_5f19ff4.js","pkg":"wiki-common:p6","deps":["wiki-common:node_modules/side-channel/index.js","wiki-common:node_modules/qs/lib/utils.js","wiki-common:node_modules/qs/lib/formats.js"]},"wiki-common:node_modules/qs/lib/parse.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qs/lib/parse_c728ba6.js","pkg":"wiki-common:p6","deps":["wiki-common:node_modules/qs/lib/utils.js"]},"wiki-common:node_modules/qs/lib/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/qs/lib/index_5b28743.js","pkg":"wiki-common:p6","deps":["wiki-common:node_modules/qs/lib/stringify.js","wiki-common:node_modules/qs/lib/parse.js","wiki-common:node_modules/qs/lib/formats.js"]},"wiki-common:packages/utils/obj.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/obj_485d42e.js","pkg":"wiki-common:p17","deps":["wiki-common:node_modules/lodash.get/index.js"]},"wiki-common:node_modules/@baiducloud/sdk/dist/baidubce-sdk.bundle.min.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@baiducloud/sdk/dist/baidubce-sdk.bundle.min_73f2256.js","pkg":"wiki-common:p17"},"wiki-common:packages/utils/bosUploader.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/bosUploader_4d24ab4.js","pkg":"wiki-common:p17","deps":["wiki-common:packages/utils/obj.js","wiki-common:node_modules/@baiducloud/sdk/dist/baidubce-sdk.bundle.min.js"]},"wiki-common:packages/utils/fetch.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/fetch_48a3991.js","pkg":"wiki-common:p25","deps":["wiki-common:node_modules/axios/index.js","wiki-common:node_modules/qs/lib/index.js","wiki-common:packages/utils/obj.js"]},"wiki-common:packages/utils/datetime.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/datetime_1e509ea.js","pkg":"wiki-common:p20","deps":["wiki-common:node_modules/date-format/lib/index.js","wiki-common:node_modules/format-duration/index.js"]},"wiki-common:packages/utils/storage.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/storage_090b3d3.js","pkg":"wiki-common:p37"},"wiki-common:packages/utils/dom.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/dom_771ca9f.js","pkg":"wiki-common:p22","deps":["wiki-common:packages/utils/obj.js"]},"wiki-common:packages/components/renderToDom/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/renderToDom/index_3106b8e.js","pkg":"wiki-common:p41","deps":["wiki-common:node_modules/react/index.js","wiki-common:node_modules/react-dom/index.js"]},"wiki-common:packages/components/videoPlayer/common/event.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/common/event_06f2aed.js","pkg":"wiki-common:p43","deps":["wiki-common:packages/utils/eventEmitter.js"]},"wiki-common:packages/components/videoPlayer/common/config.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/common/config_a36b1ed.js","pkg":"wiki-common:p43"},"wiki-common:packages/components/videoPlayer/plugins/HlsPlugin.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/plugins/HlsPlugin_f2a96b9.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/larkplayer/dist/larkplayer.js","wiki-common:node_modules/hls.js/dist/hls.js","wiki-common:packages/components/videoPlayer/common/event.js","wiki-common:packages/components/videoPlayer/common/config.js"]},"wiki-common:packages/components/videoPlayer/plugins/ClassNameManager.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/plugins/ClassNameManager_b5fc7f4.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/larkplayer/dist/larkplayer.js","wiki-common:packages/components/videoPlayer/common/config.js"]},"wiki-common:packages/components/videoPlayer/plugins/ControlsEvent.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/plugins/ControlsEvent_9fc7114.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/larkplayer/dist/larkplayer.js","wiki-common:packages/components/videoPlayer/common/config.js"]},"wiki-common:packages/components/videoPlayer/ui/ProgressBar/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/ProgressBar/index_13ba962.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:node_modules/larkplayer/dist/larkplayer.js","wiki-common:packages/utils/datetime.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/icons/play-radius.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/play-radius_380671d.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/pause.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/pause_90c04bf.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/components/videoPlayer/ui/PlayButton/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/PlayButton/index_e16731f.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/play-next.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/play-next_cb82501.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/components/videoPlayer/common/context.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/common/context_6ed62ef.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/components/videoPlayer/ui/PlayNextButton/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/PlayNextButton/index_80fe9be.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/videoPlayer/common/context.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/icons/volume.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/volume_8a8f6e2.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/mute.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/mute_99b39a0.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/components/videoPlayer/ui/Volume/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Volume/index_4346361.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:node_modules/larkplayer/dist/larkplayer.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/components/videoPlayer/ui/Time/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Time/index_345a184.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/datetime.js"]},"wiki-common:packages/icons/fullscreen.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/fullscreen_5c9c345.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/fullscreen-close.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/fullscreen-close_62be799.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/components/videoPlayer/ui/FullscreenButton/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/FullscreenButton/index_be33fcb.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/icons/check.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/check_f156242.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/components/videoPlayer/ui/PlaybackRate/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/PlaybackRate/index_47c81ad.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/icons/setting.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/setting_f51b22f.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/components/videoPlayer/ui/Setting/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Setting/index_1de67b2.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-switch/lib/index.js","wiki-common:packages/utils/storage.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/components/videoPlayer/ui/ControlBar/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/ControlBar/index_29749ab.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/videoPlayer/ui/ProgressBar/index.jsx","wiki-common:packages/components/videoPlayer/ui/PlayButton/index.jsx","wiki-common:packages/components/videoPlayer/ui/PlayNextButton/index.jsx","wiki-common:packages/components/videoPlayer/ui/Volume/index.jsx","wiki-common:packages/components/videoPlayer/ui/Time/index.jsx","wiki-common:packages/components/videoPlayer/ui/FullscreenButton/index.jsx","wiki-common:packages/components/videoPlayer/ui/PlaybackRate/index.jsx","wiki-common:packages/components/videoPlayer/ui/Setting/index.jsx"]},"wiki-common:packages/components/videoPlayer/ui/Loading/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Loading/index_a326a7c.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/components/videoPlayer/ui/Error/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Error/index_23676a7.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/replay.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/replay_090644d.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/list.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/list_a416a1d.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/components/videoPlayer/ui/Complete/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Complete/index_a1158e8.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/videoPlayer/common/context.js","wiki-common:packages/components/videoPlayer/common/config.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/components/videoPlayer/ui/Tip/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Tip/index_331a6be.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/components/videoPlayer/ui/NextVideo/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/NextVideo/index_34dee8a.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/datetime.js","wiki-common:packages/components/videoPlayer/common/context.js"]},"wiki-common:packages/components/videoPlayer/ui/Mini/MiniPlayButton/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Mini/MiniPlayButton/index_e765c87.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/icons/dialog.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/dialog_de91b6b.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/close-mini.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/close-mini_ad85778.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/components/videoPlayer/ui/Mini/MiniControls/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Mini/MiniControls/index_c4138e5.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/components/videoPlayer/ui/Mini/MiniTitle/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Mini/MiniTitle/index_bfd2d7a.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/videoPlayer/common/context.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/components/videoPlayer/ui/Mini/MiniProgressBar/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Mini/MiniProgressBar/index_fb82124.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/components/videoPlayer/ui/Mini/MiniComplete/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Mini/MiniComplete/index_47c8034.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/videoPlayer/common/context.js","wiki-common:packages/components/videoPlayer/common/config.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/components/videoPlayer/ui/Mini/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/Mini/index_86b506e.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/dom.js","wiki-common:packages/components/videoPlayer/ui/Mini/MiniPlayButton/index.jsx","wiki-common:packages/components/videoPlayer/ui/Mini/MiniControls/index.jsx","wiki-common:packages/components/videoPlayer/ui/Mini/MiniTitle/index.jsx","wiki-common:packages/components/videoPlayer/ui/Mini/MiniProgressBar/index.jsx","wiki-common:packages/components/videoPlayer/ui/Mini/MiniComplete/index.jsx"]},"wiki-common:packages/components/videoPlayer/ui/WaterMark/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/WaterMark/index_523f288.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/videoPlayer/common/event.js"]},"wiki-common:packages/components/videoPlayer/ui/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/ui/index_175d720.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/renderToDom/index.js","wiki-common:packages/components/videoPlayer/ui/ControlBar/index.jsx","wiki-common:packages/components/videoPlayer/ui/Loading/index.jsx","wiki-common:packages/components/videoPlayer/ui/Error/index.jsx","wiki-common:packages/components/videoPlayer/ui/Complete/index.jsx","wiki-common:packages/components/videoPlayer/ui/Tip/index.jsx","wiki-common:packages/components/videoPlayer/ui/NextVideo/index.jsx","wiki-common:packages/components/videoPlayer/ui/Mini/index.jsx","wiki-common:packages/components/videoPlayer/ui/WaterMark/index.jsx","wiki-common:packages/components/videoPlayer/common/event.js","wiki-common:packages/components/videoPlayer/common/context.js"]},"wiki-common:packages/components/videoPlayer/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/videoPlayer/index_332d639.js","pkg":"wiki-common:p43","deps":["wiki-common:node_modules/larkplayer/dist/larkplayer.js","wiki-common:packages/utils/storage.js","wiki-common:packages/components/videoPlayer/plugins/HlsPlugin.js","wiki-common:packages/components/videoPlayer/plugins/ClassNameManager.js","wiki-common:packages/components/videoPlayer/plugins/ControlsEvent.js","wiki-common:packages/components/videoPlayer/common/config.js","wiki-common:packages/components/videoPlayer/common/event.js","wiki-common:packages/components/videoPlayer/ui/index.jsx"]},"wiki-common:packages/utils/jumpLink.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/jumpLink_b1edb61.js","pkg":"wiki-common:p30"},"wiki-common:packages/utils/image.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/image_a5fa80e.js","pkg":"wiki-common:p29"},"wiki-common:packages/utils/logger.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/logger_7e430ee.js","pkg":"wiki-common:p33","deps":["wiki-common:packages/utils/clickstream.js"]},"wiki-common:packages/utils/throttle.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/throttle_e33f855.js","pkg":"wiki-common:p39","deps":["wiki-common:node_modules/lodash.throttle/index.js"]},"wiki-common:modules/globalEvent/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/globalEvent/index_dd8e5af.js","pkg":"wiki-common:p47","deps":["wiki-common:packages/utils/eventEmitter.js"]},"wiki-common:packages/utils/useOnclickOutside.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/useOnclickOutside_9d9de82.js","pkg":"wiki-common:p40","deps":["wiki-common:node_modules/react-cool-onclickoutside/dist/index.js"]},"wiki-common:packages/utils/number.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/number_0f62752.js","pkg":"wiki-common:p34"},"wiki-common:packages/utils/loadScript.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/utils/loadScript_5d0979d.js","pkg":"wiki-common:p31"},"wiki-common:modules/passport/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/passport/index_72cb773.js","pkg":"wiki-common:p49","deps":["wiki-common:packages/utils/fetch.js","wiki-common:packages/utils/obj.js","wiki-common:packages/utils/loadScript.js"]},"wiki-common:modules/feedback/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/feedback/index_c3d324d.js","pkg":"wiki-common:p45","deps":["wiki-common:packages/utils/loadScript.js"]},"wiki-common:packages/components/Dialog/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/Dialog/index_cc83e49.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/rc-dialog/lib/index.js"]},"wiki-common:packages/icons/close.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/close_dbd2921.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/mini.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/mini_db51473.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/dark.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/dark_87c1909.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/light.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/light_99d2226.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/common/context.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/common/context_f341321.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/common/event.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/common/event_9bb855e.js","pkg":"wiki-common:p51","deps":["wiki-common:packages/utils/eventEmitter.js"]},"wiki-common:modules/second/common/service.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/common/service_ce56f9d.js","pkg":"wiki-common:p51","deps":["wiki-common:packages/utils/fetch.js","wiki-common:packages/components/videoPlayer/index.js","wiki-common:packages/utils/jumpLink.js","wiki-common:packages/utils/bosUploader.js","wiki-common:packages/utils/image.js","wiki-common:node_modules/query-string/index.js"]},"wiki-common:modules/second/common/config.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/common/config_a3de749.js","pkg":"wiki-common:p51"},"wiki-common:modules/second/common/logger.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/common/logger_81ed4be.js","pkg":"wiki-common:p51","deps":["wiki-common:widget/component/nslog/nslog.js","wiki-common:packages/utils/logger.js","wiki-common:modules/second/common/service.js","wiki-common:modules/second/common/config.js"]},"wiki-common:modules/second/common/getSecondPlayer.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/common/getSecondPlayer_d70eec4.js","pkg":"wiki-common:p51","deps":["wiki-common:packages/components/videoPlayer/index.js","wiki-common:modules/second/common/service.js","wiki-common:packages/utils/throttle.js","wiki-common:modules/globalEvent/index.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:modules/second/Base/Player/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/Player/index_d90c085.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/common/getSecondPlayer.js","wiki-common:modules/second/common/service.js","wiki-common:modules/second/common/event.js","wiki-common:modules/second/common/context.js","wiki-common:modules/second/common/logger.js","wiki-common:modules/second/common/config.js"]},"wiki-common:packages/icons/emoji.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/emoji_be1fa4f.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:node_modules/@baidu/xbox-emoticon/dist/emoticon.cjs.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/node_modules/@baidu/xbox-emoticon/dist/emoticon.cjs_307056e.js","pkg":"wiki-common:p51"},"wiki-common:modules/second/Comment/CommentInput/EmojiBtn.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentInput/EmojiBtn_c67cb00.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/useOnclickOutside.js","wiki-common:node_modules/@baidu/xbox-emoticon/dist/emoticon.cjs.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:packages/icons/pic.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/pic_e209d90.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Comment/CommentInput/ImageBtn.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentInput/ImageBtn_3169222.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:modules/second/Comment/CommentInput/InputBoxPlaceholder.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentInput/InputBoxPlaceholder_584ed10.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/obj.js"]},"wiki-common:modules/second/Comment/CommentInput/InputBox.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentInput/InputBox_4aefc49.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:node_modules/rc-textarea/lib/index.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:modules/second/Comment/common/context.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/common/context_d9a038c.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Comment/CommentInput/Publisher.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentInput/Publisher_ae8256d.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/common/logger.js","wiki-common:modules/second/Comment/common/context.js"]},"wiki-common:modules/second/Comment/UserAvatar/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/UserAvatar/index_3684179.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/Comment/common/context.js"]},"wiki-common:packages/icons/tip-close.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/tip-close_f0f6679.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Comment/common/config.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/common/config_00c319e.js","pkg":"wiki-common:p51"},"wiki-common:modules/second/Comment/CommentInput/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentInput/index_d64d05e.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/useOnclickOutside.js","wiki-common:modules/second/Comment/CommentInput/EmojiBtn.jsx","wiki-common:modules/second/Comment/CommentInput/ImageBtn.jsx","wiki-common:modules/second/Comment/CommentInput/InputBoxPlaceholder.jsx","wiki-common:modules/second/Comment/CommentInput/InputBox.jsx","wiki-common:modules/second/Comment/CommentInput/Publisher.jsx","wiki-common:modules/second/Comment/UserAvatar/index.jsx","wiki-common:packages/utils/storage.js","wiki-common:modules/second/Comment/common/config.js","wiki-common:modules/second/Comment/common/context.js","wiki-common:modules/second/common/logger.js","wiki-common:modules/second/common/event.js"]},"wiki-common:modules/second/Comment/CommentList/CommentItem/CommentContent.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentList/CommentItem/CommentContent_a0f687c.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:node_modules/@baidu/xbox-emoticon/dist/emoticon.cjs.js"]},"wiki-common:packages/icons/arrow-down.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/arrow-down_979f255.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemReply.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentList/CommentItem/CommentItemReply_d4ee0bc.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/Comment/CommentList/CommentItem/index.jsx","wiki-common:modules/second/Comment/common/context.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemImage.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentList/CommentItem/CommentItemImage_6257ec8.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/components/Popup/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/components/Popup/index_9f7412d.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/reactjs-popup/dist/index.js"]},"wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemInfo/FeedbackBtn.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentList/CommentItem/CommentItemInfo/FeedbackBtn_0d52d4b.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/Comment/common/context.js","wiki-common:packages/components/Popup/index.jsx","wiki-common:modules/second/common/logger.js"]},"wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemInfo/DeleteBtn.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentList/CommentItem/CommentItemInfo/DeleteBtn_cdcfa16.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/useOnclickOutside.js","wiki-common:modules/second/Comment/common/context.js","wiki-common:packages/components/Popup/index.jsx","wiki-common:modules/second/common/logger.js"]},"wiki-common:packages/icons/like.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/like_bc899c6.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/like-o.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/like-o_8b05d60.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemInfo/LikeBtn.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentList/CommentItem/CommentItemInfo/LikeBtn_5a8475a.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/Comment/common/context.js","wiki-common:packages/utils/number.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:packages/icons/reply.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/reply_1b15f38.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/reply-o.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/reply-o_2c28927.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Comment/common/event.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/common/event_0282524.js","pkg":"wiki-common:p51","deps":["wiki-common:packages/utils/eventEmitter.js"]},"wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemInfo/ReplyBtn.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentList/CommentItem/CommentItemInfo/ReplyBtn_34acf1f.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/Comment/common/event.js","wiki-common:modules/second/Comment/common/context.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemInfo/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentList/CommentItem/CommentItemInfo/index_bc11435.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/datetime.js","wiki-common:modules/second/Comment/CommentInput/index.jsx","wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemInfo/FeedbackBtn.jsx","wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemInfo/DeleteBtn.jsx","wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemInfo/LikeBtn.jsx","wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemInfo/ReplyBtn.jsx"]},"wiki-common:modules/second/Comment/CommentList/CommentItem/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentList/CommentItem/index_b0a55ea.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/Comment/UserAvatar/index.jsx","wiki-common:modules/second/Comment/CommentList/CommentItem/CommentContent.jsx","wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemReply.jsx","wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemImage.jsx","wiki-common:modules/second/Comment/CommentList/CommentItem/CommentItemInfo/index.jsx","wiki-common:modules/second/Comment/common/context.js"]},"wiki-common:modules/second/Comment/CommentList/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/CommentList/index_46ff62c.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/Comment/CommentList/CommentItem/index.jsx","wiki-common:modules/second/common/event.js"]},"wiki-common:modules/second/Comment/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Comment/index_4afa5dc.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/renderToDom/index.js","wiki-common:modules/second/Comment/CommentInput/index.jsx","wiki-common:modules/second/Comment/CommentList/index.jsx","wiki-common:modules/second/Comment/common/context.js"]},"wiki-common:modules/second/Base/Comment/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/Comment/index_a658536.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/renderToDom/index.js","wiki-common:modules/second/Comment/index.jsx","wiki-common:modules/passport/index.js","wiki-common:modules/second/common/event.js","wiki-common:modules/second/common/context.js","wiki-common:modules/second/common/config.js","wiki-common:modules/second/common/service.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:packages/icons/album.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/album_9972cb2.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/arrow-right.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/arrow-right_73e6c71.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Base/VideoList/VideoItem.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/VideoList/VideoItem_e0df590.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/datetime.js","wiki-common:packages/utils/number.js","wiki-common:modules/second/common/service.js","wiki-common:modules/second/common/event.js","wiki-common:modules/second/common/context.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:packages/icons/arrow-left.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/arrow-left_7ea583c.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/star.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/star_c59bc9b.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/star-o.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/star-o_1ce00e1.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Base/VideoList/CollectionList/VideoItem.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/VideoList/CollectionList/VideoItem_c048e3e.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/datetime.js","wiki-common:packages/utils/number.js","wiki-common:modules/second/common/service.js","wiki-common:modules/second/common/event.js","wiki-common:modules/second/common/context.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:modules/second/Base/VideoList/CollectionList/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/VideoList/CollectionList/index_b6465cc.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/throttle.js","wiki-common:modules/passport/index.js","wiki-common:modules/second/Base/VideoList/CollectionList/VideoItem.jsx","wiki-common:modules/second/common/service.js","wiki-common:modules/second/common/event.js","wiki-common:modules/second/common/context.js","wiki-common:packages/utils/storage.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:packages/icons/video.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/video_5dfd65b.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Base/VideoList/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/VideoList/index_df1f25b.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/Base/VideoList/VideoItem.jsx","wiki-common:modules/second/Base/VideoList/CollectionList/index.jsx","wiki-common:modules/second/common/config.js","wiki-common:packages/utils/jumpLink.js","wiki-common:packages/utils/throttle.js","wiki-common:modules/second/common/context.js","wiki-common:modules/second/common/event.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:modules/second/Base/Author/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/Author/index_eee06be.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:node_modules/classnames/index.js","wiki-common:modules/second/common/service.js","wiki-common:modules/passport/index.js","wiki-common:modules/second/common/context.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:modules/second/Base/LikeBtn/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/LikeBtn/index_0f19623.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/number.js","wiki-common:modules/second/common/service.js","wiki-common:modules/passport/index.js","wiki-common:modules/second/common/context.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:packages/icons/comment.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/comment_5f57f04.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Base/CommentBtn/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/CommentBtn/index_ea59166.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/number.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:modules/second/Base/CollectBtn/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/CollectBtn/index_8426102.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/common/service.js","wiki-common:modules/passport/index.js","wiki-common:modules/second/common/context.js","wiki-common:packages/utils/storage.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:packages/icons/share.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/share_614cd34.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/weibo.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/weibo_5491a9e.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/copy.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/copy_cf5eb2b.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/qq.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/qq_4a5bcab.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:packages/icons/qq-zone.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/qq-zone_8665d2d.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Base/ShareBtn/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/ShareBtn/index_ca5c35c.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/Popup/index.jsx","wiki-common:node_modules/react-copy-to-clipboard/lib/index.js","wiki-common:modules/second/common/service.js","wiki-common:packages/utils/jumpLink.js","wiki-common:node_modules/qrcode/lib/browser.js","wiki-common:node_modules/query-string/index.js","wiki-common:modules/second/common/context.js","wiki-common:modules/second/common/logger.js"]},"wiki-common:packages/icons/more.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/more_c39d37c.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Base/MoreBtn/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/MoreBtn/index_f442df9.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/feedback/index.js","wiki-common:packages/components/Popup/index.jsx"]},"wiki-common:modules/second/Base/Title/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/Title/index_3107001.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/common/logger.js","wiki-common:modules/second/common/context.js"]},"wiki-common:packages/icons/top.svg":{"url":"https://bkssl.bdimg.com/static/wiki-common/packages/icons/top_84d9b5e.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js"]},"wiki-common:modules/second/Base/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Base/index_7447036.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/utils/throttle.js","wiki-common:modules/second/common/context.js","wiki-common:modules/second/common/event.js","wiki-common:modules/second/common/service.js","wiki-common:modules/second/common/logger.js","wiki-common:modules/second/common/config.js","wiki-common:modules/second/Base/Player/index.jsx","wiki-common:modules/second/Base/Comment/index.jsx","wiki-common:modules/second/Base/VideoList/index.jsx","wiki-common:modules/second/Base/Author/index.jsx","wiki-common:modules/second/Base/LikeBtn/index.jsx","wiki-common:modules/second/Base/CommentBtn/index.jsx","wiki-common:modules/second/Base/CollectBtn/index.jsx","wiki-common:modules/second/Base/ShareBtn/index.jsx","wiki-common:modules/second/Base/MoreBtn/index.jsx","wiki-common:modules/second/Base/Title/index.jsx"]},"wiki-common:modules/second/Modal/index.jsx":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/Modal/index_013973d.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:packages/components/Dialog/index.jsx","wiki-common:modules/second/Base/index.jsx","wiki-common:modules/globalEvent/index.js","wiki-common:modules/second/common/event.js","wiki-common:modules/second/common/logger.js","wiki-common:packages/utils/storage.js","wiki-common:modules/second/common/config.js"]},"wiki-common:modules/second/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-common/modules/second/index_ded4155.js","pkg":"wiki-common:p51","deps":["wiki-common:node_modules/react/index.js","wiki-common:modules/second/Modal/index.jsx","wiki-common:packages/components/renderToDom/index.js"]},"wiki-lemma:widget/tools/bkshare/share.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/bkshare/share_3beba04.js","pkg":"wiki-lemma:p4"},"wiki-lemma:static/tools/bkshare.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/tools/bkshare_a2941a6.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/tools/bkshare/share.js"]},"wiki-lemma:static/tools/durationLog.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/tools/durationLog_8030055.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/nslog/nslog.js"]},"wiki-lemma:static/tools/scriptLazyLoad.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/tools/scriptLazyLoad_eee6f6d.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/tools/announcement/announcement.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/announcement/announcement_f8dd02e.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/util/cookie.js"]},"wiki-lemma:widget/tools/bkclick/bkclick.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/bkclick/bkclick_7e63a7e.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/tools/clickstream/clickstream.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/clickstream/clickstream_80bcccf.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/util/clickstreamSdk.js"]},"wiki-lemma:widget/tools/eid/eid.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/eid/eid.es_1fe5d5c.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/util/getEidByCookie.js","wiki-common:widget/util/url.js"]},"wiki-lemma:widget/tools/inSightDetector/inSightDetector.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/inSightDetector/inSightDetector.es_2167643.js","pkg":"wiki-lemma:p4"},"wiki-lemma:widget/tools/inSightDetector/inSightDetectorIns.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/inSightDetector/inSightDetectorIns.es_73a0531.js","pkg":"wiki-lemma:p4","deps":["wiki-lemma:widget/tools/inSightDetector/inSightDetector.es.js"]},"wiki-lemma:widget/tools/rangeExt/rangeExt.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/rangeExt/rangeExt_798a7db.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/tools/label/label.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/label/label_27e4b3e.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/util/browser.js","wiki-common:widget/ui/bubble/bubble.js","wiki-common:widget/ui/dialog/dialog.js","wiki-lemma:widget/tools/rangeExt/rangeExt.js"]},"wiki-lemma:widget/tools/lazyLoad/lazyLoad.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/lazyLoad/lazyLoad_075e9d1.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/tools/marquee/marquee.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/marquee/marquee_50fd4bd.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/tools/newSideShare/qrcode.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/newSideShare/qrcode_a30d942.js","pkg":"wiki-lemma:p4"},"wiki-lemma:widget/tools/newSideShare/sideShare.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/newSideShare/sideShare_46cc01e.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/tools/newSideShare/taskSideShare.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/newSideShare/taskSideShare_00ad6a5.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/tools/newSideShare/sideShare.js","wiki-lemma:widget/tools/newSideShare/qrcode.js","wiki-common:widget/component/nslog/nslog.js"]},"wiki-lemma:widget/tools/rightCheck/checkUgc.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/rightCheck/checkUgc_0590cb3.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/ui/dialog/dialog.js","wiki-common:widget/component/userLogin/userLogin.js","wiki-common:widget/component/unameFiller/unameFiller.js","wiki-common:widget/component/nslog/nslog.js","wiki-lemma:widget/tools/clickstream/clickstream.js"]},"wiki-lemma:widget/tools/rightCheck/rightCheck.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/rightCheck/rightCheck_6a532d3.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/safeCall.js","wiki-common:widget/component/userLogin/userLogin.js"]},"wiki-lemma:widget/tools/service/service.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/service/service_688d1e2.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/tools/searchHeader/toolButtons-n/toolButtons.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/toolButtons-n/toolButtons_827b876.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/userLogin/userLogin.js","wiki-lemma:widget/tools/service/service.js"]},"wiki-lemma:widget/tools/searchHeader/toolButtons-n/userInfo.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/toolButtons-n/userInfo_fb2faff.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/userLogin/userLogin.js"]},"wiki-lemma:widget/tools/searchHeader/toolButtons/toolButtons.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/toolButtons/toolButtons_3b55e42.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/userLogin/userLogin.js","wiki-lemma:widget/tools/service/service.js"]},"wiki-lemma:widget/tools/searchHeader/toolButtons/userInfo.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/toolButtons/userInfo_0f7cec4.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/userLogin/userLogin.js"]},"wiki-lemma:widget/tools/swiper/swiper.min.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/swiper/swiper.min_4a66e32.js","pkg":"wiki-lemma:p4"},"wiki-lemma:widget/tools/throttle/throttle.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/throttle/throttle.es_b3fd58d.js","pkg":"wiki-lemma:p4"},"wiki-lemma:widget/tools/tool/debounce.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/tool/debounce_9aece8a.js","pkg":"wiki-lemma:p4"},"wiki-lemma:widget/tools/tool/formatPlayNum.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/tool/formatPlayNum_615bcb8.js","pkg":"wiki-lemma:p4"},"wiki-lemma:widget/tools/tool/tool.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/tool/tool_0c386e5.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/tools/video/flashVideo/flashVideo.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/video/flashVideo/flashVideo_808154c.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/swfObject/swfObject.js"]},"wiki-lemma:widget/tools/video/iframeVideo/iframeVideo.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/video/iframeVideo/iframeVideo_6e5b775.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/tools/video/iqiyiVideo/iqiyiVideo.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/video/iqiyiVideo/iqiyiVideo_2bdb190.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/tools/video/flashVideo/flashVideo.js"]},"wiki-lemma:widget/tools/video/pageMask/pageMask.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/video/pageMask/pageMask_f8ef928.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/tools/video/video.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/video/video_c965528.js","pkg":"wiki-lemma:p4","deps":["wiki-lemma:widget/tools/video/iframeVideo/iframeVideo.js","wiki-lemma:widget/tools/video/iqiyiVideo/iqiyiVideo.js","wiki-lemma:widget/tools/video/flashVideo/flashVideo.js"]},"wiki-lemma:widget/basicElement/addSubDialog/addSubDialog.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/basicElement/addSubDialog/addSubDialog.es_896063a.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/ui/dialog/dialog.js","wiki-lemma:widget/tools/rightCheck/checkUgc.js","wiki-lemma:widget/tools/rightCheck/rightCheck.js"]},"wiki-lemma:widget/basicElement/addSub/addSub.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/basicElement/addSub/addSub_c44287b.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/basicElement/addSubDialog/addSubDialog.es.js"]},"wiki-lemma:widget/basicElement/collect/collect.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/basicElement/collect/collect_c780e5b.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/userLogin/userLogin.js","wiki-lemma:widget/tools/service/service.js"]},"wiki-lemma:widget/basicElement/commonModulePager/commonModulePager.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/basicElement/commonModulePager/commonModulePager_3be0385.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/basicElement/editorialStatement/log.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/basicElement/editorialStatement/log.es_3e5688f.js","pkg":"wiki-lemma:p4","deps":["wiki-lemma:widget/tools/clickstream/clickstream.js","wiki-lemma:widget/tools/inSightDetector/inSightDetectorIns.es.js"]},"wiki-lemma:widget/basicElement/editorialStatement/editorialStatement.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/basicElement/editorialStatement/editorialStatement.es_42bc0f7.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-lemma:widget/basicElement/editorialStatement/log.es.js"]},"wiki-lemma:widget/basicElement/modulePager/modulePager.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/basicElement/modulePager/modulePager_22cb06c.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/basicElement/personalIcon/personalIcon.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/basicElement/personalIcon/personalIcon_629c630.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/ui/dialog/dialog.js","wiki-common:widget/component/userLogin/userLogin.js","wiki-common:widget/component/nslog/nslog.js"]},"wiki-lemma:widget/basicElement/slidePager/slidePager.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/basicElement/slidePager/slidePager_ccf6292.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/basicElement/topShare/topShare.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/basicElement/topShare/topShare_6f18a5c.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/component/nslog/nslog.js"]},"wiki-lemma:widget/lemma_content/commonModule/album/album.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/album/album_df5fa75.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/mainContent/albumList/albumList.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/albumList/albumList_bc6a061.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/basicElement/modulePager/modulePager.js","wiki-lemma:widget/lemma_content/commonModule/album/album.js"]},"wiki-lemma:widget/lemma_content/mainContent/basicInfo/basicInfo.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/basicInfo/basicInfo_4f73206.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/mainContent/lemmaReference/lemmaReference.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaReference/lemmaReference_89cf4ec.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/nslog/nslog.js"]},"wiki-lemma:widget/lemma_content/mainContent/lemmaSciencePaper/lemmaSciencePaper.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaSciencePaper/lemmaSciencePaper_329480f.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/component/nslog/nslog.js"]},"wiki-lemma:widget/lemma_content/mainContent/lemmaStatistics/lemmaStatistics.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaStatistics/lemmaStatistics_048479c.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/userCard/userCard.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-lemma:widget/tools/inSightDetector/inSightDetector.es.js","wiki-lemma:widget/tools/clickstream/clickstream.js"]},"wiki-lemma:widget/lemma_content/mainContent/lemmaTitle/lemmaTitle.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaTitle/lemmaTitle_60bcf95.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/mainContent/personalAuth/goAuth.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/personalAuth/goAuth_3090392.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/mainContent/polysemantList/polysemantList.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/polysemantList/polysemantList_66c3502.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/basicElement/addSubDialog/addSubDialog.es.js","wiki-lemma:widget/tools/clickstream/clickstream.js"]},"wiki-lemma:widget/lemma_content/mainContent/sideCatalog/sideCatalog.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/sideCatalog/sideCatalog_74c9f82.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/nslog/nslog.js","wiki-lemma:widget/tools/throttle/throttle.es.js","wiki-lemma:widget/tools/clickstream/clickstream.js"]},"wiki-lemma:widget/lemma_content/mainContent/taskLemmasInfoCard/taskLemmasInfoCard.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/taskLemmasInfoCard/taskLemmasInfoCard_d7e1b14.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js"]},"wiki-lemma:widget/lemma_content/commonModule/album/marquee.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/album/marquee.es_9270e53.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/commonModule/album/albumMarquee.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/album/albumMarquee.es_9917f07.js","pkg":"wiki-lemma:p4","deps":["wiki-lemma:widget/lemma_content/commonModule/album/marquee.es.js","wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/commonModule/cellModule/cellModule.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/cellModule/cellModule_e5ea8f0.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/basicElement/commonModulePager/commonModulePager.js"]},"wiki-lemma:widget/lemma_content/commonModule/horizontalModule/horizontalModule.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/horizontalModule/horizontalModule_ec4cf5c.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/commonModule/map/map.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/map/map_0eec9a6.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/nslog/nslog.js"]},"wiki-lemma:widget/lemma_content/commonModule/music/musicAlbum/musicAlbum.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/music/musicAlbum/musicAlbum_dd02264.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/commonModule/music/musicHot/musicHot.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/music/musicHot/musicHot_94c575f.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/commonModule/musicAlbum/musicAlbumForStar/musicAlbumStarItem.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/musicAlbum/musicAlbumForStar/musicAlbumStarItem.es_becd83a.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/ui/bubble/bubble.js","wiki-common:widget/lib/jsmart/jsmart.js"]},"wiki-lemma:widget/lemma_content/commonModule/musicAlbum/musicAlbumNormal/musicAlbumNormal.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/musicAlbum/musicAlbumNormal/musicAlbumNormal_1ebf9cd.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/commonModule/noticeIcon/noticeIcon.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/noticeIcon/noticeIcon_0b5e785.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/commonModule/publication/bookAd.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/publication/bookAd.es_7cc7dc5.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-lemma:widget/tools/clickstream/clickstream.js","wiki-lemma:widget/tools/inSightDetector/inSightDetectorIns.es.js"]},"wiki-lemma:widget/lemma_content/commonModule/publication/publication.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/publication/publication.es_f1e58b0.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/lemma_content/commonModule/publication/bookAd.es.js","wiki-lemma:widget/tools/clickstream/clickstream.js","wiki-lemma:widget/tools/inSightDetector/inSightDetectorIns.es.js"]},"wiki-lemma:widget/lemma_content/commonModule/series/series.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/series/series_45f4280.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/commonModule/timeAxis/timeAxis.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/commonModule/timeAxis/timeAxis.es_6881c3a.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/tools/clickstream/clickstream.js"]},"wiki-lemma:widget/promotion/baijiahao/baijiahao.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/baijiahao/baijiahao.es_be0e231.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/userLogin/userLogin.js","wiki-common:widget/lib/jsmart/jsmart.js"]},"wiki-lemma:widget/promotion/banner/banner.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/banner/banner_8edad4d.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/component/superLogger/superLogger.es.js","wiki-lemma:widget/tools/clickstream/clickstream.js"]},"wiki-lemma:widget/promotion/bottomRecommend/bottomRecommend.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/bottomRecommend/bottomRecommend.es_39d8991.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/tools/throttle/throttle.es.js","wiki-lemma:widget/tools/clickstream/clickstream.js","wiki-lemma:widget/tools/eid/eid.es.js","wiki-lemma:widget/tools/bkclick/bkclick.js"]},"wiki-lemma:widget/promotion/declaration/declaration.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/declaration/declaration_3f1b3fb.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js"]},"wiki-lemma:widget/promotion/empty/empty.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/empty/empty_f4a2add.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/promotion/fengchao/setAdScrollEvent.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/fengchao/setAdScrollEvent_6e45515.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/tools/throttle/throttle.es.js"]},"wiki-lemma:widget/promotion/fengchao/fengchao.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/fengchao/fengchao.es_87cbe47.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/cookie.js","wiki-common:widget/component/nslog/nslog.js","wiki-common:widget/component/testElem/testElem.js","wiki-lemma:widget/promotion/fengchao/setAdScrollEvent.js","wiki-common:widget/component/superLogger/superLogger.es.js","wiki-lemma:widget/tools/inSightDetector/inSightDetector.es.js","wiki-common:widget/util/getEidByCookie.js"]},"wiki-lemma:widget/promotion/guessLike/guessLike.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/guessLike/guessLike_cc13c9d.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/util/cookie.js","wiki-common:widget/component/nslog/nslog.js","wiki-lemma:widget/tools/bkclick/bkclick.js","wiki-lemma:widget/tools/inSightDetector/inSightDetector.es.js","wiki-common:widget/component/superLogger/superLogger.es.js","wiki-lemma:widget/tools/eid/eid.es.js","wiki-lemma:widget/tools/clickstream/clickstream.js"]},"wiki-lemma:widget/promotion/leadPVBtn/leadPVBtn.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/leadPVBtn/leadPVBtn_83981f3.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/nslog/nslog.js","wiki-common:widget/component/superLogger/superLogger.es.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-lemma:widget/tools/newSideShare/qrcode.js"]},"wiki-lemma:widget/promotion/medicalModal/medicalModal.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/medicalModal/medicalModal_b82d497.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/nslog/nslog.js"]},"wiki-lemma:widget/promotion/relatedBusiness/relatedBusiness.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/relatedBusiness/relatedBusiness_e515428.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/getEidByCookie.js"]},"wiki-lemma:widget/promotion/rightAd/rightAd.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/rightAd/rightAd_3285c8d.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/nslog/nslog.js","wiki-common:widget/util/cookie.js"]},"wiki-lemma:widget/promotion/rightBigAd/rightBigAd.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/rightBigAd/rightBigAd_02b11c7.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/promotion/rightGuessLike/rightGuessLike.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/rightGuessLike/rightGuessLike_b33053e.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/util/cookie.js","wiki-common:widget/component/nslog/nslog.js","wiki-lemma:widget/tools/bkclick/bkclick.js"]},"wiki-lemma:widget/promotion/rightPreciseAd/rightPreciseAd.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/rightPreciseAd/rightPreciseAd_05925e3.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/promotion/rightTashuo/rightTashuo.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/rightTashuo/rightTashuo.es_9eb9261.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/nslog/nslog.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/ui/carousel/carousel.js","wiki-common:widget/ui/pager/horPager/horPager.js","wiki-lemma:widget/tools/inSightDetector/inSightDetector.es.js","wiki-lemma:widget/tools/clickstream/clickstream.js","wiki-common:widget/util/url.js"]},"wiki-lemma:widget/promotion/serviceProduct/serviceProduct.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/serviceProduct/serviceProduct.es_9a2025a.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-lemma:widget/tools/clickstream/clickstream.js","wiki-lemma:widget/tools/throttle/throttle.es.js"]},"wiki-lemma:widget/promotion/slide/slide.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/slide/slide_026efef.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/ui/pager/horPager/horPager.js","wiki-common:widget/ui/carousel/carousel.js"]},"wiki-lemma:widget/promotion/topAd/topAd.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/topAd/topAd_bb7cc8d.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/component/nslog/nslog.js"]},"wiki-lemma:widget/promotion/unionAd/unionAd.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/unionAd/unionAd_44e3477.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/tools/inSightDetector/inSightDetector.es.js","wiki-lemma:widget/tools/bkclick/bkclick.js","wiki-common:widget/component/superLogger/superLogger.es.js","wiki-lemma:widget/promotion/fengchao/setAdScrollEvent.js","wiki-lemma:widget/tools/clickstream/clickstream.js"]},"wiki-lemma:widget/promotion/unionAdFromPs/unionAdFromPs.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/unionAdFromPs/unionAdFromPs_612dac5.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/promotion/vbaike/vbaike.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/promotion/vbaike/vbaike_54249ef.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/ui/pager/horPager/horPager.js","wiki-common:widget/ui/carousel/carousel.js"]},"wiki-lemma:widget/lemma_content/configModule/second/common/constants.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/second/common/constants_2a8f60f.js","pkg":"wiki-lemma:p4"},"wiki-lemma:widget/lemma_content/configModule/second/second.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/second/second_10a32ef.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/lemma_content/configModule/second/common/constants.js","wiki-common:modules/second/index.js","wiki-common:modules/second/common/logger.js","wiki-common:modules/second/common/service.js"]},"wiki-lemma:widget/lemma_content/configModule/second/types/common/videoList/videoList.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/second/types/common/videoList/videoList_9b4ac6c.js","pkg":"wiki-lemma:p4","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:modules/second/common/getSecondPlayer.js","wiki-common:modules/second/index.js","wiki-common:modules/second/common/logger.js","wiki-common:modules/second/common/service.js","wiki-common:widget/ui/marquee/marquee.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:packages/utils/number.js","wiki-lemma:widget/tools/clickstream/clickstream.js"]},"wiki-lemma:node_modules/resize-observer-polyfill/dist/ResizeObserver.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/node_modules/resize-observer-polyfill/dist/ResizeObserver_d7cffe0.js","pkg":"wiki-lemma:p4"},"wiki-lemma:node_modules/lodash.throttle/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/node_modules/lodash.throttle/index_688d1ce.js","pkg":"wiki-lemma:p4"},"wiki-lemma:node_modules/clipboard/dist/clipboard.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/node_modules/clipboard/dist/clipboard_ca9b93e.js","pkg":"wiki-lemma:p4"},"wiki-lemma:widget/lemma_content/mainContent/basicInfo/basicInfoTip/basicInfoTip.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/basicInfo/basicInfoTip/basicInfoTip_9c1ac55.js","deps":["wiki-common:widget/lib/jquery/jquery.js"]},"wiki-lemma:widget/lemma_content/mainContent/lemmaRelation/lemmaInsert.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaRelation/lemmaInsert_5e08533.js","pkg":"wiki-lemma:p5","deps":["wiki-common:widget/component/nslog/nslog.js","wiki-lemma:widget/tools/clickstream/clickstream.js"]},"wiki-lemma:widget/lemma_content/mainContent/lemmaRelation/tangram.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaRelation/tangram_53d0149.js","pkg":"wiki-lemma:p5"},"wiki-lemma:widget/lemma_content/mainContent/lemmaReference/lemmaReferenceTip/lemmaReferenceTip.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaReference/lemmaReferenceTip/lemmaReferenceTip_d59a79a.js","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-common:widget/component/nslog/nslog.js"]},"wiki-lemma:widget/feature/Audio/tools/utils.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/utils.es_cacda34.js"},"wiki-lemma:widget/feature/Audio/tools/pinyin.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/pinyin.es_dc36fb8.js"},"wiki-lemma:widget/feature/Audio/tools/audioHelper.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/audioHelper.es_c00799e.js","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/feature/Audio/tools/utils.es.js","wiki-lemma:widget/feature/Audio/tools/pinyin.es.js"]},"wiki-lemma:widget/feature/Audio/tools/constant.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/constant.es_3eff367.js"},"wiki-lemma:widget/feature/Audio/tools/getSign.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/getSign.es_102e39c.js"},"wiki-lemma:widget/feature/Audio/tools/ttsHelper.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/ttsHelper.es_44c051b.js","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/guid.js","wiki-lemma:widget/feature/Audio/tools/getSign.es.js"]},"wiki-lemma:widget/feature/Audio/tools/event.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/event.es_8db8a45.js"},"wiki-lemma:widget/feature/Audio/ui/index.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/ui/index.es_8adf608.js","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/feature/Audio/tools/audioHelper.es.js","wiki-lemma:widget/feature/Audio/tools/ttsHelper.es.js","wiki-lemma:widget/feature/Audio/tools/constant.es.js","wiki-lemma:widget/feature/Audio/tools/utils.es.js","wiki-lemma:widget/feature/Audio/tools/event.es.js","wiki-common:widget/util/themeColor.es","wiki-common:widget/util/url.js"]},"wiki-lemma:widget/feature/Audio/core/index.es.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/core/index.es_6b825d9.js","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-lemma:widget/feature/Audio/tools/audioHelper.es.js","wiki-common:modules/globalEvent/index.js","wiki-common:widget/util/eventEmitter.js","wiki-lemma:widget/feature/Audio/tools/constant.es.js","wiki-lemma:widget/feature/Audio/tools/utils.es.js","wiki-lemma:widget/feature/Audio/tools/ttsHelper.es.js","wiki-lemma:widget/feature/Audio/tools/event.es.js","wiki-lemma:widget/tools/clickstream/clickstream.js","wiki-lemma:widget/feature/Audio/ui/index.es.js","wiki-common:widget/util/cookie.js"]},"wiki-lemma:widget/feature/generalAdvert/util/qrcode-helper.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/generalAdvert/util/qrcode-helper_452900f.js","deps":["wiki-lemma:widget/tools/newSideShare/qrcode.js"]},"wiki-lemma:widget/feature/generalAdvert/advertActivity/advertActivity.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/generalAdvert/advertActivity/advertActivity_0777a85.js","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/lib/jsmart/jsmart.js","wiki-lemma:widget/tools/newSideShare/qrcode.js","wiki-lemma:widget/tools/clickstream/clickstream.js","wiki-lemma:widget/feature/generalAdvert/util/qrcode-helper.js"]},"wiki-lemma:widget/feature/generalAdvert/advertBaseInfo/advertBaseInfo.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/generalAdvert/advertBaseInfo/advertBaseInfo_c418496.js","deps":["wiki-common:widget/lib/jquery/jquery.js"]}},"pkg":{"wiki-common:p9":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-jquery-ps-link_ada049d.js"},"wiki-common:p14":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-lib-jsmart_3ff2da8.js"},"wiki-common:p18":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-clickstream_a15ec5c.js"},"wiki-common:p0":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/vender-polyfill_dfac3eb.js"},"wiki-common:p3":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/vender-larkplayer_ff2aa2a.js"},"wiki-common:p15":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-lib_6f05759.js"},"wiki-common:p11":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-util_85c7ff2.js"},"wiki-common:p13":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-lib-letv_0ef7211.js"},"wiki-common:p16":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-ui_3292dca.js"},"wiki-common:p2":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/vender-util_f3153ee.js"},"wiki-common:p10":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-component_f33bb11.js"},"wiki-common:p1":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/vender-react_f2ba2fc.js"},"wiki-common:p4":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/vender-ui_d51f2e0.js"},"wiki-common:p24":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-eventEmitter_1ee53b5.js"},"wiki-common:p6":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/vender_74a8c46.js"},"wiki-common:p17":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-bosUploader_81a1865.js"},"wiki-common:p25":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-fetch_77481e7.js"},"wiki-common:p20":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-datetime_1bc7409.js"},"wiki-common:p37":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-storage_f9507ec.js"},"wiki-common:p22":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-dom_136fc97.js"},"wiki-common:p41":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/components-renderToDom_0c8c8ef.js"},"wiki-common:p43":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/components-videoPlayer_2e3622d.js"},"wiki-common:p30":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-jumpLink_8dff541.js"},"wiki-common:p29":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-image_a30b8e7.js"},"wiki-common:p33":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-logger_3b8256e.js"},"wiki-common:p39":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-throttle_537409f.js"},"wiki-common:p47":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/modules-globalEvent_76b7565.js"},"wiki-common:p40":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-useOnclickOutside_54143ea.js"},"wiki-common:p34":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-number_2c0fadf.js"},"wiki-common:p31":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/utils-loadScript_018b896.js"},"wiki-common:p49":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/modules-passport_1f35351.js"},"wiki-common:p45":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/modules-feedback_6597c8b.js"},"wiki-common:p51":{"url":"https://bkssl.bdimg.com/static/wiki-common/pkg/modules-second_0edf23c.js"},"wiki-lemma:p4":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/pkg/wiki-lemma_54fb155.js"},"wiki-lemma:p5":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/pkg/wiki-lemma-module-lemmaRelation_1d29207.js"}}});</script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/vender-polyfill_dfac3eb.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-jquery-ps-link_ada049d.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-component_f33bb11.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-lib-jsmart_3ff2da8.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-lib_6f05759.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/vender-larkplayer_ff2aa2a.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-clickstream_a15ec5c.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-util_85c7ff2.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-ui_3292dca.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/node_modules/larkplayer-ui/dist/larkplayer-ui_d17fc4e.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-lib-letv_0ef7211.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/vender-util_f3153ee.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/pkg/wiki-lemma_54fb155.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/vender-react_f2ba2fc.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/vender-ui_d51f2e0.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/modules-second_0edf23c.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-eventEmitter_1ee53b5.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/vender_74a8c46.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-bosUploader_81a1865.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-fetch_77481e7.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-storage_f9507ec.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/components-videoPlayer_2e3622d.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-datetime_1bc7409.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-dom_136fc97.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/components-renderToDom_0c8c8ef.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-jumpLink_8dff541.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-image_a30b8e7.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-logger_3b8256e.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-throttle_537409f.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/modules-globalEvent_76b7565.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-useOnclickOutside_54143ea.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-number_2c0fadf.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/utils-loadScript_018b896.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/modules-passport_1f35351.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/modules-feedback_6597c8b.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/zhixin/zhixin_f4b3ee1.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/utils.es_cacda34.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/pinyin.es_dc36fb8.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/audioHelper.es_c00799e.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/getSign.es_102e39c.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/ttsHelper.es_44c051b.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/constant.es_3eff367.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/tools/event.es_8db8a45.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/feature/Audio/ui/index.es_8adf608.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/layout/lemma_b8c9ac1.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/layout/layout_76ea466.js"></script>
<script type="text/javascript">!function(){        require.async(['wiki-lemma:widget/tools/clickstream/clickstream']);
    }();
!function(){  var $ = require('wiki-common:widget/lib/jquery/jquery'),
    userbar = require('wiki-common:widget/component/userbar-n/userbar-n');
    
  userbar.buildUserbar($('#j-wgt-userbar'), null);
}();
!function(){  require('wiki-common:widget/component/headTabBar/headTabBar');
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery'),
      initSearchbar = require('wiki-common:widget/component/searchbar-n/searchbar');  
    initSearchbar($('.wgt-searchbar-main'));
  }();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var cookie = require('wiki-common:widget/util/cookie');
    if (!cookie.get('baikedeclare')) {
        $('#J-declare-wrap').css('display', 'block');
    }
    $('#J-declare-close').on('click', function () {
        // 用户关闭后，不再显示，过期时间调整为90天
        cookie.set('baikedeclare', 'showed', {
            expires: 90 * 60 * 60 * 24 * 1000,
            path: '/'
        });
        $('#J-declare-wrap').css('display', 'none');
    });
}();
!function(){var cookie = require('wiki-common:widget/util/cookie');
var $ = require('wiki-common:widget/lib/jquery/jquery');
var clickstream = require('wiki-common:widget/tools/clickstream/clickstream');

var timer = '';
var requestTime= null;
var currentTime= new Date().getTime();
$('.wgt-navbar').on('mouseenter', 'dl', function() {
  clearTimeout(timer);
  timer = setTimeout(function() {
    $('.wgt-navbar').addClass('wgt-navbar-hover');
    clickstream.logActEvent({
      page: 'common',
      act_type: 'hover',
      element: 'navbar-hover'
    });
  }, 300);
}).on('mouseleave', function() {
  clearTimeout(timer);
  $('.wgt-navbar').removeClass('wgt-navbar-hover');
}).on('click', 'a', function() {
  clearTimeout(timer);
  $('.wgt-navbar').removeClass('wgt-navbar-hover');
});
// 30分钟后更新json文件参数，防止浏览器的缓存（仅用当前时间戳会导致带宽压力过大）
if (!cookie.get('zhishiTopicRequestTime') || (currentTime - cookie.get('zhishiTopicRequestTime') > 1800000)) {
  cookie.set('zhishiTopicRequestTime', currentTime);
  requestTime = currentTime;
} else {
  requestTime = cookie.get('zhishiTopicRequestTime');
}
$.getJSON('https://baikebcs.cdn.bcebos.com/cms/pc_index/knowledge_topic_menu.json?time='+ requestTime, function(data) {
    for (var i = 0; i < data.length; i++) {
        $('#J-knowledge-content').append('<div><a href="https://baike.baidu.com/wapui/subpage/knowledgetopic?id=' + data[i].itemId + '" target="_blank">' + data[i].title + '</a></div>')
    }
})
}();
!function(){                var $ = require('wiki-common:widget/lib/jquery/jquery');
                var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

                // 展现策略
                rightCheck.editView('1292734', function(res) {
                    if (!res.errno) {
                        if (res.data.edit) {
                            $('.lemmaWgt-lemmaTitle .add-subLemma').css('display', 'inline-block');
                            $('.top-tool .add-sub-icon').css('display', 'inline-block');
                        }
                    } else {
                        if ('1') {
                            $('.lemmaWgt-lemmaTitle .add-subLemma').css('display', 'inline-block');
                            $('.top-tool .add-sub-icon').css('display', 'inline-block');
                        }
                    }
                });
                require('wiki-lemma:widget/basicElement/addSub/addSub.js')({                    lemmaId: '1292734',                    lemmaTitle:"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212",                    lemmaDesc:null,                    versionId: '425864470',                    subLemmaId: '71418',                    lemmaDesc:"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u5baa\u6cd5\u89c4\u5b9a\u7684\u884c\u653f\u533a\u5212"
});
            }();
!function(){        var $ = require('wiki-common:widget/lib/jquery/jquery');
        var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

        // 展现策略
        rightCheck.editView('1292734', function(res) {
            if (!res.errno) {
                if (res.data.divide) {
                    $('.top-tool .split-icon').css('display', 'block');
                }
            }
        });
    }();
!function(){    var nslog = require('wiki-common:widget/component/nslog/nslog');
	require.async(["wiki-lemma:widget/basicElement/collect/collect"],function(collect){
		collect({
            newLemmaId:"1292734",
			lemmaId:"71418",
			subLemmaId:"71418"
		});
	});
}();
!function(){    require.async(["wiki-lemma:widget/basicElement/topShare/topShare"],function(topShare){
        topShare({
            newLemmaId: '1292734'
        });
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');
    var nsLog = require('wiki-common:widget/component/nslog/nslog');
    var Dialog = require("wiki-common:widget/ui/dialog/dialog");
    var clickstream = require('wiki-lemma:widget/tools/clickstream/clickstream');
    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                clickstream.logViewEl({
                    page: 'lemma',
                    element: 'edit_btn',
                });
                $('.lemmaWgt-lemmaTitle .edit-lemma').css('display', 'inline-block');
                // 编辑和申请本人实名验证保证同一行展示
                if ($('.lemmaWgt-lemmaTitle .personal').length > 0) {
                  if ($('.lemmaWgt-lemmaTitle .edit-lemma').offset().left > $('.lemmaWgt-lemmaTitle .personal').offset().left) {
                    $('.lemmaWgt-lemmaTitle .edit-lemma').before('<br/><br/>');
                  }
                }
            } else {
                nsLog('10003104');
                $('.lemmaWgt-lemmaTitle .lock-lemma').show();
                // 锁定和申请本人实名验证保证同一行展示
                if ($('.lemmaWgt-lemmaTitle .personal').length > 0) {
                  if ($('.lemmaWgt-lemmaTitle .lock-lemma').offset().left > $('.lemmaWgt-lemmaTitle .personal').offset().left) {
                    $('.lemmaWgt-lemmaTitle .lock-lemma').before('<br/><br/>');
                  }
                }
            }
        } else {
            if ('1') {
                clickstream.logViewEl({
                    page: 'lemma',
                    element: 'edit_btn',
                });
                $('.lemmaWgt-lemmaTitle .edit-lemma').css('display', 'inline-block');
                // 编辑和申请本人实名验证保证同一行展示
                if ($('.lemmaWgt-lemmaTitle .personal').length > 0) {
                  if ($('.lemmaWgt-lemmaTitle .edit-lemma').offset().left > $('.lemmaWgt-lemmaTitle .personal').offset().left) {
                    $('.lemmaWgt-lemmaTitle .edit-lemma').before('<br/><br/>');
                  }
                }
            } else {
                nsLog('10003104');
                $('.lemmaWgt-lemmaTitle .lock-lemma').show();
                // 锁定和申请本人实名验证保证同一行展示
                if ($('.lemmaWgt-lemmaTitle .personal').length > 0) {
                  if ($('.lemmaWgt-lemmaTitle .lock-lemma').offset().left > $('.lemmaWgt-lemmaTitle .personal').offset().left) {
                    $('.lemmaWgt-lemmaTitle .lock-lemma').before('<br/><br/>');
                  }
                }
            }
        }
    });

    var canDiscussion = $('.j-discussion-link').length > 0 ? true : false;
    if (canDiscussion) {
        var discussionKey = 'discussion' + 1292734;
        var discussionNum = 0;
        // 锁定跳转
        $('body').on('click', '.lock-lemma', function () {
            var me = $(this);
            var content = '<div style="text-align: left;width: 528px">'
                + '<h2 style="font-size: 20px;color: #333;line-height: 26px;margin-bottom: 20px;">'
                + '词条锁定，暂时无法编辑</h2>'
                + '<p style="font-size: 16px;color: #333;line-height: 26px;">'
                + '亲爱的用户，词条存在争议或词条内容较完善都可能被锁定（'
                + '<a href="/view/10812319.htm" target="_blank">查看详情</a>）。</p>'
                + '<p style="font-size: 16px;color: #333;line-height: 26px;">'
                + '如果你认为锁定词条内容存在问题需要修改，可进行以下操作：</p></div>';
            new Dialog({
                title: '编辑提示',
                content: content,
                btns: [
                    {
                        text: '<span style="font-size: 14px">参与词条讨论，反馈词条问题</span>',
                        key: 'discussion'
                    }
                ],
                onBtnClick: function(btnKey){
                    if (btnKey === 'discussion') {
                        window.location.href = '/planet/talk?lemmaId=1292734&category=1';
                    }
                }
            }).show();
        });
        // 获取讨论数
        $.get('/discussion/api/getdiscussioncount?lemmaId=1292734', function (res) {
            if (res && res.errno === 0 && res.data.discussionCount > 0) {
                var lastNum = parseInt(localStorage.getItem(discussionKey)) || 0;
                discussionNum = res.data.discussionCount;
                var numText = (res.data.discussionCount - lastNum) <= 99 ? (res.data.discussionCount - lastNum) : '99+';
                if (numText > 0 || numText === '99+') {
                    $('.j-discussion-link .num').text(numText).show();
                }

            }
        });
        $('.lemmaWgt-lemmaTitle .j-discussion-link').on('click', function () {
            localStorage.setItem(discussionKey, discussionNum);
            $(this).find('.num').remove();
        });
        // 讨论按钮展现量
        nsLog(90000101, window.location.href, {
            lemmaid: 1292734
        });
    }
    // 他说讨论入口展现打点
    function showTashuoDiscussion() {
        var discussion = $('.j-discussion-link[nslog-type="90000102"]');
        var jVars = $('#J-vars');
        if (discussion.length === 1) {
            var logParam = {
                page: 'lemma',
                element: 'tashuo-issue-list-entrance',
                lemmaId: jVars.attr('data-lemmaid'),
                lemmaTitle: jVars.attr('data-lemmatitle')
            };
            clickstream.logViewEl(logParam);
        }
    }
    
    // 他说讨论入口点击打点
    function clickTashuoDiscussion() {
        var discussion = $('.j-discussion-link[nslog-type="90000102"]');
        var jVars = $('#J-vars');
        if (discussion.length === 1) {
            discussion.on('click', function() {
                var logParam = {
                    page: 'lemma',
                    element: 'tashuo-issue-list-entrance',
                    lemmaId: jVars.attr('data-lemmaid'),
                    lemmaTitle: jVars.attr('data-lemmatitle')
                };
                clickstream.logActClick(logParam);
            })
           
        }
    }
    showTashuoDiscussion();
    clickTashuoDiscussion();
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var nsLog = require('wiki-common:widget/component/nslog/nslog');
    var clickstream = require('wiki-lemma:widget/tools/clickstream/clickstream');
    lemmaId = 1292734;
    lemmaTitle='中华人民共和国行政区划';
    var lemmaDesc = "\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u5baa\u6cd5\u89c4\u5b9a\u7684\u884c\u653f\u533a\u5212";

    var logMap ={
        uploadShow: 10800000,
        uploadClick: 10800001
    };
    nsLog(logMap.uploadShow, window.location.href, {
        lemmaid: lemmaId,
        lemmaTitle: lemmaTitle
    });

    function gotoPage(url, id) {
        var el = document.createElement('a');

        el.setAttribute('href', encodeURI(url));
        el.setAttribute('target', '_blank');
        el.setAttribute('id', id);

        if(!document.getElementById(id)) {
            document.body.appendChild(el);
        }

        el.click();
    }

    $('.J-add-video-link').on('click', function() {
        var videoLocation = '';
        if ($('.J-second-normal').length) {
            videoLocation = 'top-common';
        }
        else if ($('.large-feature').length) {
            videoLocation = 'top-large-feature';
        }
        else if ($('.J-related-video-container').length) {
            videoLocation = 'lemma-video';
        }
        clickstream.logActClick({
            page: 'lemma',
            element: 'video-upload',
            type: 1,
            location: 0,
            lemmaTitle: lemmaTitle,
            lemmaId: lemmaId,
            videoLocation: videoLocation
        });
        nsLog(logMap.uploadClick, window.location.href, {
            lemmaid: lemmaId,
            lemmaTitle: lemmaTitle
        });
        var url = '/second/publish?lemmaId=' + lemmaId + '&from=lemma&lemmaTitle=' + lemmaTitle + '&lemmaDesc=' + lemmaDesc;

        gotoPage(url, 'a_blank_tag')
    })
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var userLogin = require('wiki-common:widget/component/userLogin/userLogin');

    var $loftEditBtn = $('#J-special-edit');
    var lemmaId = 1292734;

    var loftEditUrl = '/editor/load/loftload?lemmaId=' +  lemmaId;

    // 获取 loft 的编辑权限
    function getLoftEditPrivilege() {
        return $.ajax({
            type: 'GET',
            url: '/editor/check/getlofteditprivilege',
            dataType: 'JSON'
        });
    }

    userLogin.checkIfLogin({
        ifMsg: true,
        // 已登录状态
        onLogin: function (res) {
            getLoftEditPrivilege().then(function(res) {
                $loftEditBtn.css(
                    'display',
                    res.data && res.data.length ? 'inline-block' : 'none'
                );
            });
        },
        onUnlogin: function () {
            $loftEditBtn.css('display', 'none');
        }
    });

    $loftEditBtn.on('click', function() {
        userLogin.checkIfLogin({
            ifMsg: true,
            // 已登录状态
            onLogin: function (res) {
                if (res.errno === 0) {
                    window.location.href = loftEditUrl;
                }
            },
            onUnlogin: function () {
                userLogin.showLoginPop();
            }
        });
    });

}();
!function(){    require(["wiki-lemma:widget/lemma_content/mainContent/lemmaTitle/lemmaTitle"],function(lemmaInfo) {
        lemmaInfo.init({
            lemmaTitle: "\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212",
            lemmaDesc: "\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u5baa\u6cd5\u89c4\u5b9a\u7684\u884c\u653f\u533a\u5212"
        });
    });
}();
!function(){    require.async(["wiki-lemma:widget/lemma_content/mainContent/basicInfo/basicInfoTip/basicInfoTip"],function(basicInfoTip){
        new basicInfoTip();
    });
}();
!function(){    require.async(["wiki-lemma:widget/lemma_content/mainContent/basicInfo/basicInfoTip/basicInfoTip"],function(basicInfoTip){
        new basicInfoTip();
    });
}();
!function(){	require('wiki-lemma:widget/lemma_content/mainContent/basicInfo/basicInfo')();
}();
!function(){    require.async(["wiki-lemma:widget/lemma_content/configModule/second/types/common/videoList/videoList"], function(videoList){
        videoList.default.init({
            list: null,
            style: {"viewNum":4,"type":"image-text","videoWidth":182,"videoHeight":102,"margin":15,"containerClassName":"J-related-video-container","lemmaType":"relatedVideo"},
            lemmaInfo: {
                lemmaId: 1292734,
                lemmaTitle: "\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212",
                lemmaDesc: "\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u5baa\u6cd5\u89c4\u5b9a\u7684\u884c\u653f\u533a\u5212"
            },
            isSensitive: false,
            memorial: null,
            showUploadVideoBtn: true
        });
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var nslog = require('wiki-common:widget/component/nslog/nslog');
    nslog(10002701);
    $('.lemmaWgt-lemmaCatalog a').on('click', function () {
           nslog(10002702);
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('1292734', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    require(["wiki-lemma:widget/basicElement/editorialStatement/editorialStatement.es"], function(init) {
        init(1292734);
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var nslog = require('wiki-common:widget/component/nslog/nslog');
    // 展现量
    nslog('10090201');
    require.async(["wiki-lemma:widget/lemma_content/mainContent/personalAuth/goAuth"],function(init){
        init(1292734);
    });
}();
!function(){	require.async(["wiki-common:widget/lib/jquery/jquery","wiki-lemma:widget/lemma_content/mainContent/albumList/albumList","wiki-common:widget/component/nslog/nslog"],function($,AlbumList,nslog){
		var list=new AlbumList({
			newLemmaId:"1292734",
			lemmaTitle:"中华人民共和国行政区划",
			lemmaId:"71418",
			subLemmaId:"71418",
			data:[{"coverpic":"a50f4bfbfbedab641589b799f836afc378311eeb","width":1810,"height":1770,"desc":"\u8bcd\u6761\u56fe\u7247","total":34,"coverurl":"https:\/\/bkimg.cdn.bcebos.com\/pic\/a50f4bfbfbedab641589b799f836afc378311eeb?x-bce-process=image\/resize,m_lfit,w_235,h_235,limit_1\/format,f_auto"},{"coverpic":"71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4","desc":"\u6982\u8ff0\u56fe\u518c","albumTag":"","height":4225,"width":3507,"total":3,"coverurl":"https:\/\/bkimg.cdn.bcebos.com\/pic\/71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4?x-bce-process=image\/resize,m_lfit,w_235,h_235,limit_1\/format,f_auto","toppics":[{"uuid":"33lbkco4h7","src":"b812c8fcc3cec3fd89bec158d588d43f8794271e","desc":"","width":2480,"height":2938},{"uuid":"a376zxb2bk","src":"3b292df5e0fe9925139f80fd3aa85edf8cb17188","desc":"","width":703,"height":463},{"uuid":"l869dbgvz7","src":"71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4","desc":"","width":3507,"height":4225}],"coverPic":{"uuid":"l869dbgvz7","src":"71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4","desc":"","width":3507,"height":4225,"origSrc":"71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4"},"wapPic":{"uuid":"wap429c8","src":"64380cd7912397dda144ae2216c9a5b7d0a20cf429c8","width":4096,"height":2734,"origSrc":"71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4","coverCrop":{"width":180.50541516245,"height":100,"x":0,"y":0,"unit":"%","aspect":1.5,"padWidth":180.50541516245,"padHeight":100,"onlyPad":1},"category":""},"sharePic":{"uuid":"share136c8","src":"caef76094b36acaf2eddadda33929a1001e9390136c8","width":4092,"height":4092,"origSrc":"71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4","coverCrop":{"unit":"%","aspect":1,"x":0,"y":0,"width":100,"height":99.9,"padWidth":120.36144578313,"padHeight":99.9}}}],
			pagetype:""
		});
		!!window.ScriptLazyLoad && window.ScriptLazyLoad.regist({
			dom:$('.album-list'),
			loadFunc:function(){
				list.load();
				nslog(1258);
			},
			distance:500
		});
	});
}();
!function(){		require.async(["wiki-lemma:widget/lemma_content/mainContent/lemmaReference/lemmaReference","wiki-lemma:widget/lemma_content/mainContent/lemmaReference/lemmaReferenceTip/lemmaReferenceTip"],function(Reference,ReferenceTip){
			new Reference({
				subLemmaId:"71418"
			});
			new ReferenceTip({
				subLemmaId:"1292734",
				lemmaTitle:"中华人民共和国行政区划",
				reference:[{"type":"1","uuid":"gntizsnpby","title":"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u4e8c\u3007\u4e00\u4e5d\u5e74\u884c\u653f\u533a\u5212\u7edf\u8ba1\u8868","url":"\/reference\/1292734\/f02cnrjpBEiXp4rI-0C_P3LFVmRYJnLArPPYEDTJhwoFimI4J8FkwhiOC_pxSKqBNakMR82qvELFdqXcyAlvshllPNJh4hJo","site":"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u6c11\u653f\u90e8","publishDate":"2019-12-31","refDate":"2019-12-31","index":1},{"type":"1","uuid":"gntikvqb5o","title":"\u4e2d\u56fd\u7684\u884c\u653f\u533a\u5212\u2014\u2014\u53bf\u7ea7\u4ee5\u4e0b\u57fa\u5c42\u884c\u653f\u5355\u4f4d","url":"\/reference\/1292734\/38b7UYu602bBo3niYDp-YfAe7dwFVJPq1ixyIXfm_1XyTFqjIMFbHqec8pTytPVSmOvIG_qi2KLAMjbly6D6ZKMrZhs6KCJtFvMBzdK0RD9SQw","site":"\u4e2d\u592e\u653f\u5e9c\u95e8\u6237\u7f51\u7ad9","publishDate":"2009\u5e7404\u670817\u65e5","refDate":"2013-12-04","index":2},{"type":"1","uuid":"gntikvqb79","title":"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212\uff081953\u5e74\uff09","url":"\/reference\/1292734\/59faIP6vaPfhQ_wV9TGplUUh-6mXUcxY89REqWLka8oOKCRYhf5yQBxHvfOA6z0uhZM50m3HYJFk3-e3MhSU_HQ0tuKzl6nhgBZ6PP49sP6Z","site":"\u4e2d\u56fd\u653f\u5e9c\u7f51","publishDate":"2007-03-23","refDate":"2018-12-07","index":3},{"type":"1","uuid":"gntj7rxuzt","title":"\u5173\u4e8e\u8bbe\u7acb\u6d77\u5357\u7701\u7684\u51b3\u5b9a","url":"\/reference\/1292734\/cee6zj1hphdM6drbM1jsh5wXv76ZCAoMqRr0SLfaeZC1d4d1sbDB-zsT2XE83hxm7jSd6vkojy96jf4oxbJo9WrRMWZsZu7o1Xhh3Vlu6AqR","site":"\u4e2d\u592e\u653f\u5e9c\u95e8\u6237\u7f51\u7ad9","publishDate":"2008-04-10","refDate":"2021-02-06","index":4},{"type":"1","uuid":"gntikpyyei","title":"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212","url":"\/reference\/1292734\/c2823wXoI39A1Qz1Eamwh5apjRa-iggzRwOCJIBcjGlwlclamyHf1IDUhvIS0KIMxVvfNYKi2sw_4mCaKDEU1e084Yqjg1zvMQf8HmrhNhGuGJjozw","site":"\u4e2d\u56fd\u653f\u5e9c\u7f51","publishDate":"2005-06-15","refDate":"2020-09-26","index":5},{"type":"1","uuid":"gntikpyyf4","title":"\u56fd\u52a1\u9662\u5173\u4e8e\u884c\u653f\u533a\u5212\u7ba1\u7406\u7684\u89c4\u5b9a","url":"\/reference\/1292734\/c44dh-tS100Pnk51xRz6sh2TwqUpc9FYt6u4kVCcjfYiVEynqQkMTBQj4XRsE4xijgRV2zdJ8m3U3I5wpPsIhFlKrLbzlRA7W4NOe_edqI6zyg","site":"\u4e2d\u592e\u653f\u5e9c\u95e8\u6237\u7f51\u7ad9","publishDate":"2009\u5e7403\u670830","refDate":"2013-12-05","index":6},{"type":"1","uuid":"sBMMa9WCRuCn","publishDate":"","refDate":"2021-06-30","site":"\u4e2d\u56fd\u653f\u5e9c\u7f51","title":"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212","url":"\/reference\/1292734\/3484RwZbnUxfAgn_o2N8JNVAjt-OTpyhseIsEbS5YekHU0PXb3wtG704L5UdjUrvq7b_VlqdCgcVXBjkjMgIjTwhh9wGu-XFBgREppQDjr4","index":7},{"type":"1","uuid":"sQrxgFKO32Vg","publishDate":"","refDate":"2021-12-02","site":"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u4e2d\u592e\u4eba\u6c11\u653f\u5e9c","title":"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212\uff081997\u5e74\uff09","url":"\/reference\/1292734\/6cfcnAG-K9zOl6tLvymthE3rysJ8Fgi2614WyBKi64em5J6a5ZwkLWd92AzE-PX7bd_3_iGpEnEB2pT-FmmSsdT1LREXMJfIFc77Tlzm26Lc","index":8},{"type":"1","uuid":"sS73jCefxnYI","publishDate":"","refDate":"2021-12-20","site":"\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a","title":"\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a\u6982\u51b5","url":"\/reference\/1292734\/f804kTZh_tJvgv_oiIq0oNpmJLzpTUsAMJBa7knxO0ouc3WyQkKck21Uwj5v7VNkZTaRD91K__F_22z_2EcBK4J2gX7LLPDYuImLg0duMzd6BQsyqHR_dUencITLPuJXSDu2D4x1BhQr2K5pXbm4wQ0zUQ","index":9},{"labelName":"\u7f51\u7edc\u8d44\u6599","type":"1","publishDate":"","refDate":"2022-02-22","site":"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u6c11\u653f\u90e8","title":"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212\u7edf\u8ba1\u8868","url":"\/reference\/1292734\/4644RM3c4-e-XJ83HkRJ3TSHkXRRtTs46cUKHzW_kwbUDv2tbVrKkxRpTV3e5GMaI_uKvzekWHSnc7qcXi0sGXJUF1yONFXz","uuid":"sY98uBg8diHX","index":10},{"labelName":"\u7f51\u7edc\u8d44\u6599","type":"1","publishDate":"","refDate":"2022-02-22","site":"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u6c11\u653f\u90e8","title":"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212\u7edf\u8ba1\u8868","url":"\/reference\/1292734\/f04d6hWVYFOJGkEeiMsZeRnnOZi2wypD3A9z3Ksaj8IC0Hj3-28-KoBCHfgBZPVUtcWRW7XYlZnjiKB0Efub1Xmhgu9eT3Dt","uuid":"sY98JsbTeiXT","index":11},{"type":"1","uuid":"sZutPWEvcxGZ","publishDate":"","refDate":"2022-03-08","site":"\u5c71\u4e1c\u7701\u4eba\u6c11\u653f\u5e9c","title":"\u5c71\u4e1c\u7701\u4eba\u6c11\u653f\u5e9c \u5c71\u4e1c\u7701\u884c\u653f\u533a\u5212","url":"\/reference\/1292734\/c30c4m5HBZdqVj5DU52mTuREKg0GbKq_CtQ5-ftqG6xG5lv__nKGyL8CepaHW5JGmr8p-FN62C9yn_2W61TE3Wn_KuBRdW5eRn11RuMpow","index":12}]
			});
		});
	}();
!function(){        require('wiki-lemma:widget/lemma_content/configModule/zhixin/zhixin')(
            1292734,
            '中华人民共和国行政区划'
        );
    }();
!function(){    require.async(["wiki-lemma:widget/lemma_content/mainContent/lemmaStatistics/lemmaStatistics"],function(init){
        init({
            newLemmaIdEnc:"5274c62619baecfb8b4e839e",
            lemmaId: 1292734,
        });
    });
}();
!function(){	require.async(["wiki-lemma:widget/lemma_content/mainContent/sideCatalog/sideCatalog"],function(SideCatalog){
		new SideCatalog({
			isMemorial: null,
			catalog: [{"title":"\u5177\u4f53\u533a\u5212","charnum":3255,"screennum":4,"level":1,"index":1,"modules":[],"length":8,"height":28,"top":0,"bottom":28},{"title":"\u534e\u5317\u5730\u533a","charnum":436,"screennum":0,"level":2,"index":"1_1","modules":[],"length":8,"height":21,"top":28,"bottom":49},{"title":"\u4e1c\u5317\u5730\u533a","charnum":302,"screennum":0,"level":2,"index":"1_2","modules":[],"length":8,"height":21,"top":49,"bottom":70},{"title":"\u534e\u4e1c\u5730\u533a","charnum":602,"screennum":0,"level":2,"index":"1_3","modules":[],"length":8,"height":21,"top":70,"bottom":91},{"title":"\u534e\u4e2d\u5730\u533a","charnum":307,"screennum":0,"level":2,"index":"1_4","modules":[],"length":8,"height":21,"top":91,"bottom":112},{"title":"\u534e\u5357\u5730\u533a","charnum":281,"screennum":0,"level":2,"index":"1_5","modules":[],"length":8,"height":21,"top":112,"bottom":133},{"title":"\u897f\u5357\u5730\u533a","charnum":489,"screennum":0,"level":2,"index":"1_6","modules":[],"length":8,"height":21,"top":133,"bottom":154},{"title":"\u897f\u5317\u5730\u533a","charnum":473,"screennum":0,"level":2,"index":"1_7","modules":[],"length":8,"height":21,"top":154,"bottom":175},{"title":"\u6e2f\u6fb3\u53f0\u5730\u533a","charnum":332,"screennum":0,"level":2,"index":"1_8","modules":[],"length":10,"height":21,"top":175,"bottom":196},{"title":"\u533a\u5212\u4f53\u5236","charnum":1418,"screennum":1,"level":1,"index":2,"modules":[],"length":8,"height":28,"top":196,"bottom":224},{"title":"\u7701\u7ea7\u884c\u653f\u533a","charnum":340,"screennum":0,"level":2,"index":"2_1","modules":[],"length":10,"height":21,"top":224,"bottom":245},{"title":"\u5730\u7ea7\u884c\u653f\u533a","charnum":324,"screennum":0,"level":2,"index":"2_2","modules":[],"length":10,"height":21,"top":245,"bottom":266},{"title":"\u53bf\u7ea7\u884c\u653f\u533a","charnum":360,"screennum":0,"level":2,"index":"2_3","modules":[],"length":10,"height":21,"top":266,"bottom":287},{"title":"\u4e61\u7ea7\u884c\u653f\u533a","charnum":374,"screennum":0,"level":2,"index":"2_4","modules":[],"length":10,"height":21,"top":287,"bottom":308},{"title":"\u533a\u5212\u6cbf\u9769","charnum":1629,"screennum":2,"level":1,"index":3,"modules":[],"length":8,"height":28,"top":308,"bottom":336},{"title":"\u7ba1\u7406\u89c4\u5b9a","charnum":661,"screennum":0,"level":1,"index":4,"modules":[],"length":8,"height":28,"top":336,"bottom":364}]
		});
	});
}();
!function(){        require.async(["wiki-lemma:widget/promotion/fengchao/fengchao.es","wiki-lemma:widget/promotion/unionAd/unionAd"], function (init, unionAd) {
            init({
                newLemmaId: "1292734",
                lemmaTitle: "中华人民共和国行政区划",
                encodeLemmaTitle: "%D6%D0%BB%AA%C8%CB%C3%F1%B9%B2%BA%CD%B9%FA%D0%D0%D5%FE%C7%F8%BB%AE",
                adManager: {"wapBaiduYouxuan":0,"pcFengchaoGuess":0,"pcWapDireactAd":0}
            }, {
                errFn: unionAd,
                dom: $('#side_box_unionAd')
            });
        });
    }();
!function(){    require.async(['wiki-lemma:widget/promotion/bottomRecommend/bottomRecommend.es'], function (App) {
        new App({
            lemmaInfo: {"newLemmaId":1292734,"lemmaId":71418,"subLemmaId":71418,"lemmaTitle":"\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212","versionId":425864470,"isPolysemant":false,"isEditable":true,"isOrgLemma":false,"isPerview":false},
            isShowAd: false
        });
    });
}();
!function(){        require.async(['wiki-lemma:widget/promotion/guessLike/guessLike'], function (app) {
            app.init({
                lemmaTitle: '中华人民共和国行政区划',
                lemmaId: '1292734',
                adManager: {"wapBaiduYouxuan":0,"pcFengchaoGuess":0,"pcWapDireactAd":0},
                eid: null
            });
        });
    }();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var Dialog = require("wiki-common:widget/ui/dialog/dialog");
    var userLogin = require('wiki-common:widget/component/userLogin/userLogin');
    var unameFiller = require('wiki-common:widget/component/unameFiller/unameFiller');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');
    var checkUgc = require('wiki-lemma:widget/tools/rightCheck/checkUgc');
    var nsLog = require('wiki-common:widget/component/nslog/nslog');
    var clickstream = require('wiki-lemma:widget/tools/clickstream/clickstream');

            var isEnterprise = false;
        var enterpriseOwnerUserId = 0;
    
    var userId = 0;
    var editUrl = '/editor/load/editload?lemmaTitle=' + encodeURIComponent('中华人民共和国行政区划') + '&lemmaId=' + '1292734';
    var pgcUrl = '/enterprise/editpgc?lemmaId=1292734';

    userLogin.regist({
        onLogin: function(user) {
            userId = user ? user.uid : 0;
        }
    });

    function showChoseEditDialog(pgcCallback, ugcCallback) {
        new Dialog({
            title: '编辑提示',
            subMsg: '<p>您已开通企业百科服务，推荐您直接编辑“官方资料”，官方资料仅限企业百科绑定的百科账号修改，其他用户账号不可修改。</p><p>如果您想修改其他网友编辑的普通词条内容，请注意遵守百科百科编辑规则。<p>',
            btns: [{
            key: 'pgc',
            text: '编辑官方资料'
            }, {
            style: 'white',
            text: '修改普通词条',
            key: 'ugc'
            }],
            onBtnClick: function(btnKey){
                if (btnKey === 'pgc') {
                    pgcCallback && pgcCallback();
                } else if (btnKey === 'ugc') {
                    ugcCallback && ugcCallback();
                }
            }
        }).show();
    }

    function checkUserLegal(res) {
        var legal = false;
        switch (res.errno) {
            case 100001:
                nsLog('10003106');
                userLogin.showLoginPop();
                break;
            case 100006:
                unameFiller.show();
                break;
            default:
                legal = true;
        }
        return legal;
    }

    $(document.body).on('click', '.j-edit-link', function () {
        nsLog('10003100');
        var dl = $(this).attr('data-edit-dl');
        if (dl) {
            var url = editUrl + '&ci=' + dl;
        } else {
            var url = editUrl;
        }

        rightCheck.preeditCheck(
            {
                lemmaId: '1292734',
                lemmaTitle: '中华人民共和国行政区划',
                lemmaDesc: '中华人民共和国宪法规定的行政区划',
                versionId: '425864470',
                action: '',
                ci: dl
            },
            function (res) {
                if (!checkUserLegal(res)) {
                    return;
                }
                if (isEnterprise && enterpriseOwnerUserId === userId) {
                    showChoseEditDialog(
                        function () {
                            location.href = pgcUrl;
                        },
                        function () {
                            checkUgc(res, '1292734', url);
                        }
                    );
                } else {
                    checkUgc(res, '1292734', url);
                }
            }
        );
    });
}();
!function(){  require.async(["wiki-common:widget/lib/jquery/jquery","wiki-common:widget/component/footer/footer_feedback","wiki-common:widget/tools/clickstream/clickstream"], function($, feedback, clickstream){
    // 新打点sdk
    $('.question').on('click', 'a', function () {
      var nslog = $(this).attr('nslog-type');
      var type = $(this).attr('data-type');
      if (nslog && type) {
        clickstream.logActClick({
          page: 'common',
          element: 'footer-question-' + type,
          nslog: nslog
        });
      }
    });
    feedback({el: '#J-bk-feedback-main',
      proData: {
        "extend_feedback_channel": null
      }
    });
    feedback({el: '#J-bk-feedback-query', config: {
        appid: 215645,
        productLine: 20184,
        needContactWay: true,
        issuePlaceholder: '亲爱的百度百科用户，请在此填写您的质疑内容及原因哦～'
      },
      proData: {
        "kw": $('#J-bk-feedback-query').data('lemma')
      }
    });
  });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery'),
      initSearchbar = require('wiki-common:widget/component/searchbar-n/searchbar');  
    initSearchbar($('.wgt-searchbar-simple'));
  }();
!function(){    require.async(["wiki-lemma:widget/tools/searchHeader/toolButtons-n/toolButtons"],function(init){
        init({
            lemmaId:"71418",
            subLemmaId:"71418",
            newLemmaId:"1292734"
        });
    });
}();
!function(){    require('wiki-lemma:widget/tools/searchHeader/toolButtons-n/userInfo')();
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery'),
      animation = require('wiki-common:widget/util/animation'),
      nslog = require('wiki-common:widget/component/nslog/nslog'),
      initSearchbar = require('wiki-common:widget/component/searchbar/searchbar');
    var isFadeIn = false,
        isFadeOut = false;
    var clickstream = require('wiki-lemma:widget/tools/clickstream/clickstream');
    var fadeInAni, fadeOutAni;
    $(window).on('scroll', function(e) {
        var scrollTop = $(this).scrollTop();
        if (scrollTop > 200 && !isFadeIn && $('.lemmaWgt-searchHeader').css('display') == 'none') {
            fadeOutAni && fadeOutAni.stop();
            fadeInAni = animation({
                duration: 200,
                easing: 'linear',
                onStart: function() {
                    isFadeOut = false;
                    isFadeIn = true;
                    $('.lemmaWgt-searchHeader').css('display', 'block');
                },
                onStep: function(progress) {
                    $('.lemmaWgt-searchHeader').css('opacity', progress)
                },
                onComplete: function(progress) {
                    isFadeIn = false;
                    nslog(10010007);
                    clickstream.logViewEl({
                        page: 'lemma',
                        element: 'topbar_edit'
                    });
                    clickstream.logViewEl({
                        page: 'lemma',
                        element: 'topbar_discussion'
                    });
                }
            });
        } else if (scrollTop <= 200 && !isFadeOut && $('.lemmaWgt-searchHeader').css('display') == 'block') {
            fadeInAni && fadeInAni.stop();
            fadeOutAni = animation({
                duration: 300,
                easing: 'linear',
                onStart: function() {
                    $('.lemmaWgt-searchHeader #suggestion').hide();
                    isFadeIn = false;
                    isFadeOut = true;
                },
                onStep: function(progress) {
                    $('.lemmaWgt-searchHeader').css('opacity', 1 - progress);
                },
                onComplete: function(progress) {
                    isFadeOut = false;
                    $('.lemmaWgt-searchHeader').css('display', 'none');
                }
            });
        }
    });
}();
!function(){    require.async(["wiki-lemma:widget/tools/newSideShare/taskSideShare"],function(taskShare){
        taskShare.init({
            title: '中华人民共和国行政区划',
            desc: "\u884c\u653f\u533a\u5212\u662f\u56fd\u5bb6\u4e3a\u4fbf\u4e8e\u884c\u653f\u7ba1\u7406\u800c\u5206\u7ea7\u5212\u5206\u7684\u533a\u57df\u3002\u56e0\u6b64\uff0c\u884c\u653f\u533a\u5212\u4ea6\u79f0\u884c\u653f\u533a\u57df\u3002\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u7684\u884c\u653f\u533a\u5212\u7531\u7701\u7ea7\u884c\u653f\u533a\u3001\u5730\u7ea7\u884c\u653f\u533a\u3001\u53bf\u7ea7\u884c\u653f\u533a\u3001\u4e61\u7ea7\u884c\u653f\u533a\u7ec4\u6210\u3002\u5177\u4f53\u60c5\u51b5\u5982\u4e0b\uff1a\u7701\u7ea7\u884c\u653f\u533a\uff1a23\u4e2a\u7701\u30015\u4e2a\u81ea\u6cbb\u533a\u30014\u4e2a\u76f4\u8f96\u5e02\u30012\u4e2a\u7279\u522b\u884c\u653f\u533a\uff0c\u5408\u8ba134\u4e2a\u7701\u7ea7\u884c\u653f\u533a\u3002\u5730\u7ea7\u884c\u653f\u533a\uff1a293\u4e2a\u5730\u7ea7\u5e02\u30017\u4e2a\u5730\u533a\u300130\u4e2a\u81ea\u6cbb\u5dde\u30013\u4e2a\u76df\uff0c\u5408\u8ba1333\u4e2a\u5730\u7ea7\u533a\u5212\u3002\u53bf\u7ea7\u884c\u653f\u533a\uff1a977\u4e2a\u5e02\u8f96\u533a\u30011303\u4e2a\u53bf\u3001393\u4e2a\u53bf\u7ea7\u5e02\u3001117\u4e2a\u81ea\u6cbb\u53bf\u300149\u4e2a\u65d7\u30013\u4e2a\u81ea\u6cbb\u65d7\u30011\u4e2a\u7279\u533a\u30011\u4e2a\u6797\u533a\uff0c\u5408\u8ba12844\u4e2a\u3002\u4e61\u7ea7\u884c\u653f\u533a\uff1a8562\u4e2a\u8857\u9053\u300120988\u4e2a\u9547\u30018102\u4e2a\u4e61\u3001966\u4e2a\u6c11\u65cf\u4e61\u3001153\u4e2a\u82cf\u6728\u30011\u4e2a\u6c11\u65cf\u82cf\u6728\u30012\u4e2a\u53bf\u8f96\u533a\uff0c\u5408\u8ba138774\u4e2a\u3002",
            pic: 'https:\/\/bkimg.cdn.bcebos.com\/pic\/71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4?x-bce-process=image\/resize,m_lfit,w_268,limit_1\/format,f_auto',
            url: '',
            qqPic: 'https:\/\/bkimg.cdn.bcebos.com\/pic\/71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4?x-bce-process=image\/resize,m_fill,w_3507,h_3507,align_0,limit_0\/format,f_auto',
            newLemmaId: '1292734',
            lemmaTitle: '中华人民共和国行政区划'
        });
    });
}();
!function(){    require.async(['wiki-common:widget/lib/jquery/jquery','wiki-lemma:widget/feature/Audio/core/index.es'], function($, CORE) {
        CORE({
            lemmaTitle: "\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212",
            lemmaId: 1292734,
            pinyin: null,
            summaryPic: "https:\/\/bkimg.cdn.bcebos.com\/pic\/71cf3bc79f3df8dcd100e0b3825a658b4710b91282f4?x-bce-process=image\/resize,m_lfit,w_268,limit_1\/format,f_auto",
            catalog: [{"title":"\u5177\u4f53\u533a\u5212","charnum":3255,"screennum":4,"level":1,"index":1,"modules":[],"length":8,"height":28,"top":0,"bottom":28},{"title":"\u534e\u5317\u5730\u533a","charnum":436,"screennum":0,"level":2,"index":"1_1","modules":[],"length":8,"height":21,"top":28,"bottom":49},{"title":"\u4e1c\u5317\u5730\u533a","charnum":302,"screennum":0,"level":2,"index":"1_2","modules":[],"length":8,"height":21,"top":49,"bottom":70},{"title":"\u534e\u4e1c\u5730\u533a","charnum":602,"screennum":0,"level":2,"index":"1_3","modules":[],"length":8,"height":21,"top":70,"bottom":91},{"title":"\u534e\u4e2d\u5730\u533a","charnum":307,"screennum":0,"level":2,"index":"1_4","modules":[],"length":8,"height":21,"top":91,"bottom":112},{"title":"\u534e\u5357\u5730\u533a","charnum":281,"screennum":0,"level":2,"index":"1_5","modules":[],"length":8,"height":21,"top":112,"bottom":133},{"title":"\u897f\u5357\u5730\u533a","charnum":489,"screennum":0,"level":2,"index":"1_6","modules":[],"length":8,"height":21,"top":133,"bottom":154},{"title":"\u897f\u5317\u5730\u533a","charnum":473,"screennum":0,"level":2,"index":"1_7","modules":[],"length":8,"height":21,"top":154,"bottom":175},{"title":"\u6e2f\u6fb3\u53f0\u5730\u533a","charnum":332,"screennum":0,"level":2,"index":"1_8","modules":[],"length":10,"height":21,"top":175,"bottom":196},{"title":"\u533a\u5212\u4f53\u5236","charnum":1418,"screennum":1,"level":1,"index":2,"modules":[],"length":8,"height":28,"top":196,"bottom":224},{"title":"\u7701\u7ea7\u884c\u653f\u533a","charnum":340,"screennum":0,"level":2,"index":"2_1","modules":[],"length":10,"height":21,"top":224,"bottom":245},{"title":"\u5730\u7ea7\u884c\u653f\u533a","charnum":324,"screennum":0,"level":2,"index":"2_2","modules":[],"length":10,"height":21,"top":245,"bottom":266},{"title":"\u53bf\u7ea7\u884c\u653f\u533a","charnum":360,"screennum":0,"level":2,"index":"2_3","modules":[],"length":10,"height":21,"top":266,"bottom":287},{"title":"\u4e61\u7ea7\u884c\u653f\u533a","charnum":374,"screennum":0,"level":2,"index":"2_4","modules":[],"length":10,"height":21,"top":287,"bottom":308},{"title":"\u533a\u5212\u6cbf\u9769","charnum":1629,"screennum":2,"level":1,"index":3,"modules":[],"length":8,"height":28,"top":308,"bottom":336},{"title":"\u7ba1\u7406\u89c4\u5b9a","charnum":661,"screennum":0,"level":1,"index":4,"modules":[],"length":8,"height":28,"top":336,"bottom":364}],
            modulesData: {"card":["\u4e2d\u6587\u540d,\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212\u3002\u9002\u7528\u56fd\u5bb6,\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u3002\u7701\u7ea7\u884c\u653f\u533a,\u7701\u3001\u81ea\u6cbb\u533a\u3001\u76f4\u8f96\u5e02\u3001\u7279\u522b\u884c\u653f\u533a \u3002\u5730\u7ea7\u884c\u653f\u533a,\u5730\u7ea7\u5e02\u3001\u5730\u533a\u3001\u81ea\u6cbb\u5dde\u3001\u76df\u3002\u53bf\u7ea7\u884c\u653f\u533a,\u5e02\u8f96\u533a\u3001\u53bf\u7ea7\u5e02\u3001\u53bf\u3001\u81ea\u6cbb\u53bf\u3001\u65d7\u3001\u81ea\u6cbb\u65d7\u3001\u7279\u533a\u3001\u6797\u533a\u3002\u4e61\u7ea7\u884c\u653f\u533a,\u8857\u9053\u3001\u9547\u3001\u4e61\u3001\u6c11\u65cf\u4e61\u3001\u82cf\u6728\u3001\u6c11\u65cf\u82cf\u6728\u3001\u53bf\u8f96\u533a\u3002"],"modules":[],"specialTopic":[],"timeLine":[],"tashuo":[]}
        });
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var nslog = require("wiki-common:widget/component/nslog/nslog");
    var testElem = require('wiki-common:widget/component/testElem/testElem');
    var cmsModuleLoader = require('wiki-common:widget/component/cmsModuleLoader/cmsModuleLoader');
    var clickstream = require('wiki-lemma:widget/tools/clickstream/clickstream');
    var urlExt = require('wiki-common:widget/util/url'); 
    function requireAsync() {
        require.async(['wiki-lemma:widget/tools/announcement/announcement']);
    }

    cmsModuleLoader('/api/wikiui/getlemmaconfig', [{
        name: 'announcement',
        script: 'wiki-lemma:widget/tools/announcement/announcement.js'
    }]);

    require.async(["wiki-lemma:widget/tools/lazyLoad/lazyLoad"], function(LazyLoad) {
        new LazyLoad();
    });

    require.async(['wiki-common:widget/component/nslog/nslog','wiki-common:widget/lib/jquery/jquery','wiki-common:widget/component/superLogger/superLogger.es'], function(nslog, $, superLogger) {
        nslog().setGlobal({
            lemmaId: "71418",
            newLemmaId: "1292734",
            subLemmaId: "71418",
            lemmaTitle: "中华人民共和国行政区划"
        });
        function isFun(obj) {
            return Object.prototype.toString.call(obj) === '[object Function]';
        }
        // 设置全局参数
        if (clickstream.setLogGlobalParam && isFun(clickstream.setLogGlobalParam)) {
            clickstream.setLogGlobalParam({
                lemmaId: "71418",
                newLemmaId: "1292734",
                subLemmaId: "71418",
                lemmaTitle: "中华人民共和国行政区划"
            });
        }
        // 词条页 pv
        nslog(9322);
        superLogger.sendPv('lemma_pc', {
            lemmaTitle: "中华人民共和国行政区划",
            lemmaId: "1292734"
        });
        // 新打点sdk
        clickstream.logViewPage({
            page: 'lemma',
            lemmaTitle: "中华人民共和国行政区划",
            lemmaId: "1292734",
            nslog: 9322,
            lemmaFrom: urlExt.getQuery('lemmaFrom', window.location.href) || '',
            fromLemmaId: urlExt.getQuery('lemmaId', window.location.href) || '',
            fromLemmaTitle: decodeURIComponent(urlExt.getQuery('lemmaTitle', window.location.href) || '')
        });

        // 词条页时长
        var startTime = Date.now();
        document.addEventListener('visibilitychange', function () {
            if (document.visibilityState === 'hidden') {
                superLogger.sendState('lemma_pc_duration', Date.now() - startTime, {
                    lemmaTitle: "中华人民共和国行政区划",
                    lemmaId: "1292734",
                    lemmaFrom: urlExt.getQuery('lemmaFrom', window.location.href) || ''
                });
            } else {
                startTime = Date.now();
            }
        });

        $(window).on('beforeunload', function () {
            // 超过一秒再打点，避免某些情况 visibilitychange 和 unload 同时触发
            // 重复打点
            if (Date.now() - startTime > 1000) {
                superLogger.sendState('lemma_pc_duration', Date.now() - startTime, {
                    lemmaTitle: "中华人民共和国行政区划",
                    lemmaId: "1292734",
                    lemmaFrom: urlExt.getQuery('lemmaFrom', window.location.href) || ''
                });
            }
        });

        // 链接点击 pv
        var lemmaPageRegExp = new RegExp(/\/subview\/\d+|\/view\/\d+|\/item\//i);
        $('body').on('mousedown', 'a', function() {
            var href = $(this).attr('href');
            if (href && href.indexOf('/') >= 0 && href.indexOf('#') !== 0) {
                // 链接点击 pv
                nslog(10000001);
                superLogger.sendClk('lemma_link');
                if (lemmaPageRegExp.test(href)) {
                    // 词条页链接点击 pv
                    nslog(10000002, window.location.href, {
                        targetTitle: $(this).text()
                    });
                }
            }
        });

        /****** 词条页站内流转需求统计 start ******/
        (function () {
            // 各种统计配置
            var circulationLinkCfg = {
                innerLink: [ // 内链
                    '.para',
                    '.lemmaWgt-baseInfo-simple-largeMovie',
                    '.lemmaWgt-baseInfo-simple-largeStar',
                    '.basic-info .basicInfo-block',
                    '.lemma-summary',
                    '.lemmaWgt-lemmaSummary',
                    '.view-tip-panel',
                    '.horizontal-module',
                    '.lemmaWgt-roleIntroduction',
                    '.dramaSeries .dramaSerialList',
                    '.module-music',
                    '.table-view',
                    '[log-set-param="table_view"]',
                    '.list-module',
                    '.cell-module',
                    '.baseBox .dl-baseinfo', // 配置后台字段
                    '.pvBtn-box .leadPVBtnWrapper',
                    '.drama-actor',
                    '#staffList',
                    '.starMovieAndTvplay',
                    '.main_tab:not(.main_tab-defaultTab)' // 除去词条tab外的tab
                ],
                relationTable: '.rs-container-foot', // 关系表
                peopleRelation: '.star-info-block.relations, .lemmaWgt-focusAndRelation', // 人物关系（明星+普通）
                moduleActors: '.featureBaseInfo .actors, .lemmaWgt-majorActors', // 主要演员、嘉宾、主持人
                moduleWorks: '.featureBaseInfo .works, .large-feature .works', // 代表作品
                moduleQuarterly: '.featureBaseInfo .po_quarterly, .mian_quarterly', // 分季介绍
                rankStar: '.rank-list.stars-rank', // 明星榜
                rankDrama: '.drama-rank-list', // 电视剧榜
                specialTopic: '.special-topic', // 专题模块
                modDetailTable: '#modDetailTable', // 关系表出图
                chuizhitu: '.chuizhitu', // 垂直化模块
                polysemantList: '.polysemantList-wrapper' // 义项切换
            };
            /****** 连接统计 ******/
            function clickNslogFn() {
                for (var k in circulationLinkCfg) {
                    if (k === 'innerLink') {
                        // 词条内链到词条页
                        var tempArr = circulationLinkCfg[k];
                        for (var i = 0, l = tempArr.length; i < l; i++) {
                            tempArr[i] += ' a';
                        }
                        var sSelector = tempArr.join(', ');

                        $('body').on('mousedown', sSelector, {key: k},function(e) {
                            var key = e.data.key;
                            var href = $(this).attr('href');
                            var tar = $(this).attr('target') || '';
                            if (href && href.indexOf('/') >= 0 && href.indexOf('#') !== 0
                            && tar === '_blank' && lemmaPageRegExp.test(href)) {
                                // 词条页普通内链点击 pv
                                nslog(10000004, null ,{division: key});
                                // 新打点sdk
                                clickstream.logActClick({
                                    page: 'lemma',
                                    element: 'inlink-click',
                                    ivision: key,
                                    nslog: 10000004,
                                    toLemmaId: $(this).attr('data-lemmaid') || '',
                                    toLemmaTitle: $(this).text() || ''
                                });
                            }
                        });
                    } else {
                        // 模块到词条页链接
                        $(circulationLinkCfg[k]).on('mousedown', 'a', {key: k}, function (e) {
                            var key = e.data.key;
                            var href = $(this).attr('href');
                            if (href && href.indexOf('#') !== 0 && lemmaPageRegExp.test(href)) {
                                // 词条页配置模块链接点击 pv
                                nslog(10000004, null, {division: key});
                                // 新打点sdk
                                clickstream.logActClick({
                                    page: 'lemma',
                                    element: 'inlink-click',
                                    ivision: key,
                                    nslog: 10000004
                                });
                            }
                        });
                    }
                }
            }
            // 发起统计请求
            clickNslogFn();

            /****** 各模块展现量pv ******/
            function checkModuleIsShow() {
                var result = [];
                for (var k in circulationLinkCfg) {
                    if (k !== 'innerLink' && k !== 'relationTable') {
                        !!$(circulationLinkCfg[k]).html() && result.push(k);
                    }
                }
                if (result.length > 0) {
                    nslog(10000005, null, {showModules: result.join(',')});
                    // 新打点sdk
                    clickstream.logViewEl({
                        page: 'lemma',
                        element: 'module',
                        showModules: result.join(','),
                        nslog: 10000005
                    });
                }
            }
            checkModuleIsShow();

        })();
        /****** 词条页站内流转需求统计 end ******/

    });

    // 广告接入 wikiad 统一加载
    // log 词条页广告被拦截情况（此处 log 请求行为）
    nslog(70000101, window.location.href, {
        api: 'lemma-ad',
        action: 'request'
    });
    var tags = {"3":{"tagId":0,"tagName":"\u884c\u653f\u533a\u5212"},"1":{"tagId":0,"tagName":"\u793e\u4f1a"},"2":{"tagId":0,"tagName":"\u653f\u6cbb"},"0":{"tagId":0,"tagName":"\u5730\u70b9"}};
    var tagsArray = [];
    for (var key in tags) {
        tagsArray.push(tags[key].tagName);
    }
    $.ajax({
        type: 'GET',
        url: '/api/wikiad/getsquirrels',
        data: {
            lemmaId: 1292734,
            tags: tagsArray.join()
        },
        cache: false,
        dataType: 'JSON',
        success: function (res) {
            // log 词条页广告被拦截情况（此处 log 请求成功）
            nslog(70000101, window.location.href, {
                api: 'lemma-ad',
                action: 'success'
            });

            if (!res.errno) {
                if (res.data[5]) {
                                        require.async(['wiki-lemma:widget/promotion/rightPreciseAd/rightPreciseAd'], function(rightPreciseAd) {
                        rightPreciseAd(res.data[5]);
                        nslog(10002201, location.href, {
                            adId: res.data[5][0].adId,
                            adTitle: res.data[5][0].name,
                            adPos: 5
                        });
                        // 新打点sdk
                        clickstream.logViewEl({
                            page: 'lemma',
                            element: 'rightPreciseAd',
                            adId: res.data[5][0].adId,
                            adTitle: res.data[5][0].name,
                            adPos: 5,
                            nslog: 10002201
                        });
                    });
                                    } else if (res.data[1]) {
                    // 缅怀类词条屏蔽词条页v百科
                                        require.async(['wiki-lemma:widget/promotion/vbaike/vbaike'], function(vbaike) {
                        vbaike(res.data[1]);
                        for(var i in res.data[1]) {
                            nslog(10002201, location.href, {
                                adId: res.data[1][i].adId,
                                adTitle: res.data[1][i].name,
                                adPos: 1
                            });
                            // 新打点sdk
                            clickstream.logViewEl({
                                page: 'lemma',
                                element: 'vbaike',
                                adId: res.data[1][i].adId,
                                adTitle: res.data[1][i].name,
                                adPos: 1,
                                nslog: 10002201
                            });
                        }
                    });
                                    }
                // 缅怀类词条屏蔽广告
                                if (res.data[9]) {
                    require.async(['wiki-lemma:widget/promotion/rightBigAd/rightBigAd'], function(rightBigAd) {
                        rightBigAd(res.data[9]);
                            nslog(10002201, location.href, {
                                adId: res.data[9][0].adId,
                                adTitle: res.data[9][0].name,
                                adPos: 9
                            });
                            // 新打点sdk
                            clickstream.logViewEl({
                                page: 'lemma',
                                element: 'rightBigAd',
                                adId: res.data[9][0].adId,
                                adTitle: res.data[9][0].name,
                                adPos: 9,
                                nslog: 10002201
                            });
                    });
                } else if(res.data[2]) {
                    // 词条页轮播
                                        require.async(['wiki-lemma:widget/promotion/slide/slide'], function(slide) {
                        slide(res.data[2]);
                        for(var i in res.data[2]) {
                            nslog(10002201, location.href, {
                                adId: res.data[2][i].adId,
                                adTitle: res.data[2][i].name,
                                adPos: 2
                            });
                            // 新打点sdk
                            clickstream.logViewEl({
                                page: 'lemma',
                                element: 'slide',
                                adId: res.data[2][i].adId,
                                adTitle: res.data[2][i].name,
                                adPos: 2,
                                nslog: 10002201
                            });
                        }
                    });
                                    }
                // 词条页右上
                if (res.data[3]) {
                                        require.async(['wiki-lemma:widget/promotion/topAd/topAd'], function(topAd) {
                        topAd(res.data[3]);
                        nslog(10002201, location.href, {
                            adId: res.data[3][0].adId,
                            adTitle: res.data[3][0].name,
                            adPos: 3
                        });
                        // 新打点sdk
                        clickstream.logViewEl({
                            page: 'lemma',
                            element: 'topAd',
                            adId: res.data[3][0].adId,
                            adTitle: res.data[3][0].name,
                            adPos: 3,
                            nslog: 10002201
                        });
                    });
                                    }
                // 词条页悬浮
                if (res.data[4]) {
                                        require.async(['wiki-lemma:widget/promotion/rightAd/rightAd'], function(rightAd) {
                        rightAd(res.data[4]);
                        nslog(10002201, location.href, {
                            adId: res.data[4][0].adId,
                            adTitle: res.data[4][0].name,
                            adPos: 4
                        });
                        // 新打点sdk
                        clickstream.logViewEl({
                            page: 'lemma',
                            element: 'rightAd',
                            adId: res.data[4][0].adId,
                            adTitle: res.data[4][0].name,
                            adPos: 4,
                            nslog: 10002201
                        });
                    });
                                    }
                                if (res.data[15]) {
                    require.async(['wiki-lemma:widget/promotion/banner/banner'], function(banner) {
                        banner(res.data[15], {
                            lemmaTitle: "中华人民共和国行政区划",
                            lemmaId: "1292734"
                        });
                        nslog(10002201, location.href, {
                            adId: res.data[15][0].adId,
                            adTitle: res.data[15][0].name,
                            adPos: 15
                        });
                        // 新打点sdk
                        clickstream.logViewEl({
                            page: 'lemma',
                            element: 'banner',
                            adId: res.data[15][0].adId,
                            adTitle: res.data[15][0].name,
                            adPos: 15,
                            nslog: 10002201
                        });
                    });
                }
                if (res.data[16]) {
                    require.async(['wiki-lemma:widget/promotion/declaration/declaration'], function(declaration) {
                        declaration(res.data[16]);
                        nslog(10002201, location.href, {
                            adId: res.data[16][0].adId,
                            adTitle: res.data[16][0].name,
                            adPos: 16
                        });
                        // 新打点sdk
                        clickstream.logViewEl({
                            page: 'lemma',
                            element: 'declaration',
                            adId: res.data[16][0].adId,
                            adTitle: res.data[16][0].name,
                            adPos: 16,
                            nslog: 10002201
                        });
                    })
                }
                // 导流按钮(缅怀类词条不展现)
                                if (res.data[27]) {
                    require.async(['wiki-lemma:widget/feature/generalAdvert/advertActivity/advertActivity','wiki-lemma:widget/feature/generalAdvert/advertBaseInfo/advertBaseInfo','wiki-lemma:widget/promotion/leadPVBtn/leadPVBtn'], function(advertActivity, advertBaseInfo, leadPVBtn) {
                        if (res.data[27][0].isAdvert === '1') {
                            advertBaseInfo(true);
                            advertActivity(res.data[27], {
                                lemmaId: "1292734",
                                lemmaTitle: "中华人民共和国行政区划"
                            });
                            // 服务导流展现量打点
                            clickstream.logViewEl({
                                page: 'lemma',
                                element: 'service-redirect',
                                lemmaId: "1292734",
                                lemmaTitle: "中华人民共和国行政区划"
                            });
                        } else {
                            advertBaseInfo(false);
                            leadPVBtn(res.data[27], {
                                newLemmaId: "1292734",
                                lemmaTitle: "中华人民共和国行政区划"
                            });
                            nslog(10002201, location.href, {
                                adId: res.data[27][0].adId,
                                adTitle: res.data[27][0].name,
                                adPos: 27
                            });
                            // 新打点sdk
                            clickstream.logViewEl({
                                page: 'lemma',
                                element: 'leadPVBtn',
                                adId: res.data[27][0].adId,
                                adTitle: res.data[27][0].name,
                                adPos: 27,
                                nslog: 10002201
                            });
                        }
                    })
                }
                            } else {
                return;
            }

            setTimeout(function () {
                var elemArr = {};
                res.data[1] && res.data[1].length > 0 && (elemArr['lemma-vbaike-ad'] = $('.lemmaWgt-promotion-vbaike .promotion_viewport a:eq(0) img').get(0));
                res.data[2] && res.data[2].length > 0 && (elemArr['lemma-slide-ad'] = $('.lemmaWgt-promotion-slide .promotion_viewport a:eq(0) img').get(0));
                res.data[3] && res.data[3].length > 0 && (elemArr['lemma-navbar-ad'] = {
                    node: $('.header [nslog-type="10002202"]').get(0),
                    validations: {
                        'noBackgroundImage': function() {
                            return $('.header [nslog-type="10002202"]').css('background-image').indexOf(res.data[3][0].picUrl) < 0
                        }
                    }
                });
                res.data[4] && res.data[4].length > 0 && (elemArr['lemma-side-ad'] = {
                    node: $('.right-ad img').get(0),
                    validations: {
                        'noBackgroundImage': function() {
                            return $('.right-ad img').attr('src').indexOf(res.data[4][0].picUrl) < 0
                        }
                    }
                });
                res.data[15] && res.data[15].length > 0 && (elemArr['lemma-configModule-banner'] = $('.configModuleBanner').get(0));
                res.data[16] && res.data[16].length > 0 && (elemArr['lemma-configModule-declaration'] = $('.lemmaWgt-declaration').get(0));

                testElem.log(elemArr, 70000102);
                // 广告点击 新打点sdk
                $('.wiki-lemma').on('click', 'a[nslog-type="10002202"]', function () {
                    var params = JSON.parse($(this).attr('nslog-params' || {}));
                    var element = $(this).attr('ad-type') || 'promote';
                    clickstream.logActClick($.extend({
                        page: 'lemma',
                        element: element,
                        nslog: 10002202
                    }, params));
                });
            }, 1000);
        },
        error: function () {
            // log 词条页广告被拦截情况（此处 log 请求失败）
            nslog(70000101, window.location.href, {
                api: 'lemma-ad',
                action: 'error'
            });
        }
    });

    // 设置分享内容
    window.BKShare.setCommon({
        bdText: "\u3010\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u884c\u653f\u533a\u5212_\u767e\u5ea6\u767e\u79d1\u3011\u884c\u653f\u533a\u5212\u662f\u56fd\u5bb6\u4e3a\u4fbf\u4e8e\u884c\u653f\u7ba1\u7406\u800c\u5206\u7ea7\u5212\u5206\u7684\u533a\u57df\u3002\u56e0\u6b64\uff0c\u884c\u653f\u533a\u5212\u4ea6\u79f0\u884c\u653f\u533a\u57df\u3002\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u7684\u884c\u653f\u533a\u5212\u7531\u7701\u7ea7\u884c\u653f\u533a\u3001\u5730\u7ea7\u884c\u653f\u533a\u3001\u53bf\u7ea7\u884c\u653f\u533a\u3001\u4e61\u7ea7\u884c\u653f\u533a\u7ec4\u6210\u3002\u5177\u4f53\u60c5\u51b5\u5982\u4e0b\uff1a\u7701\u7ea7\u884c\u653f\u533a\uff1a23\u4e2a\u7701\u30015\u4e2a\u81ea\u6cbb\u533a\u30014\u4e2a\u76f4\u8f96\u5e02\u30012\u4e2a\u7279\u522b\u884c\u653f\u533a\uff0c\u5408\u8ba134\u4e2a\u7701\u7ea7\u884c\u653f\u533a\u3002\u5730\u7ea7\u884c\u653f\u533a\uff1a293\u4e2a\u5730\u7ea7\u5e02\u30017\u4e2a\u5730\u533a\u300130\u4e2a\u81ea\u6cbb\u5dde\u30013\u4e2a\u76df\uff0c\u5408\u8ba1333\u4e2a\u5730\u7ea7\u533a\u5212\u3002\u53bf\u7ea7\u884c\u653f\u533a\uff1a977\u4e2a\u5e02\u8f96\u533a\u30011303\u4e2a\u53bf\u3001393\u4e2a\u53bf\u7ea7\u5e02\u3001117\u4e2a\u81ea\u6cbb\u53bf\u300149\u4e2a\u65d7\u30013\u4e2a\u81ea\u6cbb\u65d7\u30011\u4e2a\u7279\u533a\u30011\u4e2a\u6797\u533a\uff0c\u5408\u8ba12844\u4e2a\u3002\u4e61\u7ea7\u884c\u653f\u533a\uff1a8562\u4e2a\u8857\u9053\u300120988\u4e2a\u9547\u30018102\u4e2a\u4e61\u3001966\u4e2a\u6c11\u65cf\u4e61\u3001153\u4e2a\u82cf\u6728\u30011\u4e2a\u6c11\u65cf\u82cf\u6728\u30012\u4e2a\u53bf\u8f96\u533a\uff0c\u5408\u8ba138774\u4e2a\u3002.....\uff08\u5206\u4eab\u81ea@\u767e\u5ea6\u767e\u79d1\uff09",
        bdDesc: '',
        bdUrl: 'http:\/\/baike.baidu.com\/item\/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92\/1292734',
        bdPic: '',
        onBeforeClick: function (){
            $('.bdshare_dialog_box').hide();
        }
    });

    // 底部投诉带入当前页面 url
    var map = [1, 2, 6, 5];
    $('.wgt-footer-main .suggestion').find('a').each(function(i) {
        $(this).attr('href', 'http://help.baidu.com/newadd?word=%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92' + '&&submit_link=' + encodeURIComponent(window.location.href) + '&prod_id=10&category=' + map[i]);
    });

    // 为超出预设内容的表格添加table-responsive控制
    $('.main-content').find('table').each(function(index) {
        var $that = $(this);
        if ($that.width() > 790) {
            $that.wrap('<div class="table-responsive"></div>');
        }
    });
    if (!$('.reference-title').length) {
        $('.main-content').addClass('main-content-margin');
    }
}();
!function(){    require.async(["wiki-lemma:widget/promotion/empty/empty"], function (init) {
        init();
    });
}();
!function(){      require('wiki-common:widget/component/psLink/psLink');
      var clickstream = require('wiki-common:widget/tools/clickstream/clickstream');
      clickstream.logViewPage({
        page: 'all-pc'
      });
    }();</script>
</html>
'''
xzdm_pattern = r'''data-lemmaid=".*?">(.*?)</a></b><b>（行政代码：(\d+)）</b></div><div class="para" label-module="para">(.*?)</div>'''
xzdm_list = re.findall(xzdm_pattern, get_xzdm)
print(xzdm_list)

# for xzdm in xzdm_list:
#     print({xzdm[0]: xzdm[1:3]})

# print([{xzdm[0]: xzdm[1:3]} for xzdm in xzdm_list])

print([xzdm for xzdm in xzdm_list])