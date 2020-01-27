---
title: "贯穿大学生涯的Python和爬虫"
date: 2017-09-10
draft: false
tags:
- Python
- webscraping
---

记录了Python学习的历程和用爬虫解决实际问题的经历.

<!--more-->

## 大二下
《计算物理》、实验报告和实习

一开始犯了从头来的老毛病，要一个个装package，装到对编译依赖比较多的scipy系列时终于放弃，选择anaconda

Language syntax的确做到了一下午无痛入门，看的是*ScipyLectures*.

大二下同时找到了实习，老板也让先学好Python，于是买来的计算物理书没怎么看，但每次编程作业都做的非常好，由于教授和助教都是刚把语言从C&Fortran换到Python，所以我才有机会频频和老师“交流经验”。

与此同时没有忘记**从头学**的想法，找来（现在看来）大名鼎鼎的*Learn Python the Hard Way*学习，可惜时间不够，全书52个exercise只学了30+（最近还又看了最后几个exercise，依然觉得很有收获），不过倒是把初学编程最容易弄不清的如*IDE和Terminal有什么区别，程序如何运行*等问题搞明白了些。

为了准备实习、搞清楚`numpy`、`pandas`，正好学期末的*物理实验*和*数学物理方法*课程都有论文，就搞了个用Python对热波传播的数据进行分析处理的小项目。现在回头看当时的报告，居然包含了极端值、空值检查，插值法填补，时间序列去趋势，FFT降噪，感觉当时自己挺nb的，哈哈。


暑假开始实习，工作环境直接就是Ubuntu+VNC，一个小三百万行的HD5放在那里等我搞。这期间没专门参考什么书，就是需要做什么查什么文档。编程能力倒不是实习的主要目的，然而由于天天写、花式写，倒也是对统计数据分析熟悉了不少。

## 大三上
大三上一直在用C++肝数据结构，此部分非本文重点。

此外，考了一个新出炉的Python二级考试，虽然通过这种考试非常随意而无聊，但借此机会把python官方文档又自习看了看，总结了总结。

## 大三下
这段时间主要是找实习过程中的进步。暂略（今天主要写爬虫啦）。

## 大三暑期实习
这段时间Python水平仍是飞速进步，暂略。

## 流水的网站，铁打的爬虫
不得不说爬虫上手的简单、设计领域的广泛和细节处理的复杂性，就像是**设计精巧的闯关游戏**，带领你从新手村一路打怪练级；同时随着等级提高，它又能帮你解决更多实实在在的问题。感谢它！

提到爬虫就不得不提到可爱的**教务处**，围绕着个人信息、查成绩、选课，产生了无数需求……

### 爬虫101 - 规则网址图片下载
某哥们暗恋同选修课的一姑娘，知道院系却不知道其他信息，就去教务网一张张照片翻，我虽然想说服他去搭讪，但我更关系他哪来的照片。终于知道原来所有学生的入学照片按照学号存在一个固定的网址下，而且没有任何权限限制。

我首先想到的是迅雷的批量下载功能，但还是决定使用Python，感谢`requests`给出这么简介优雅的HTTP request解决方案，如果google教程时看到的是直接调用urllib的那种代码，我的爬虫之旅说不定就被扼杀在摇篮里了。

由于程序逻辑简单，又是内网速度很快，没几分钟全校的（带着姓名和学号的）照片就都躺在硬盘里了（我已严格遵守法律关于交流学习资源的相关规定在下载24h内删除）。这种快速实现的成就感是无以复加的。

### 初识POST METHOD - 校园网自动登录
搞完上一个，就想到了校园网登录，每次手动开实在麻烦，想写一个脚本自己用（顺便装逼）。

登录就不仅仅是在`requests.get(url)`这么简单了，需要向服务器额外发送表单数据，这个时候学会了用chrome F12看request和response的内容。

登录脚本很快就写好了，但发现手动运行python和手动开网页区别不大，于是又结合快速启动工具写了windows上的bat，发现windows可以说是很恶心了。最后发现真正的需求是wifi出现问题、电脑移动位置后，自动重连，这需要和系统交互，google一搜全是windows api开发，果断放弃。

### 漂亮的肥皂 - HTML解析
> 战争、色情、欲望是推动科技发展的源动力；成就感（窥探欲）和数据分析（科学装逼）是推动爬虫的源动力

体育锻炼打卡查询网站外观简陋，信息丰富，最重要密码=用户名=学号，这让我无法控制自己的麒麟臂。不过话说，最初的想法是用来随时用学号/姓名互查以及查身高体重，结果现在一年多那个存好的excel也没开过2次。

当时的我，还不会正则表达式，没有萌生对目标字符串一个个匹配的智障想法，而是发现BeautifulSoup这个包，正好那时对ipython notebook也比较熟了，就在ipynb里研究html解析，也开始熟悉`div`, `span`, `tr`等tag

随着程序逻辑变复杂，我的代码也变得有点脏了，当时就是凭着感觉走嘛，而且从PyCharm换了WingIDE，没有代码风格提示，就是凭着感觉写。

### 再复杂一点 - 成绩查询 和 逸夫楼自习教室课表
我喜欢在考完试后最短的时间内知道成绩，趁着考试的感觉还在尽快自我伤害，于是在考试周我会每几个小时点进教务系统查一次成绩，久而久之我可以闭眼操作了 --- 那为什么不写个爬虫呢？

这不仅涉及登录，还要保存cookie，页面跳转、解析、再跳转、再解析，最后把数据放在`DataFrame`里print出来，收获：
- 这让我写了一个类出来，因为相关函数很多，而且还要保存`requests.Session`
- 要处理各种编码问题，`unicode`, `utf-8`, `gbk`, `ascii`傻傻分不清楚

至于逸夫楼自习教室课表，则有个小故事。某日在逸夫楼自习，一妹子问如何下掌上南大，因为逸夫楼教室门上没有贴课表，她总是需要中途换教室。我凭记忆找了下那个网站，没有找到，实在**没有办法**，**迫不得已**加了她微信，说回去找找发给她。结果回去也没找到，那...**干脆自己写一个**！

法律判决中听说过“激情杀人”，那我就算是“激情写码”，从10点回去写到2点，没考虑什么代码风格，直接在ipynb里边试边写，其中涉及了
- 对所有院系、专业的课表遍历（所以得先搞出来院系代码）
- 筛选地点出含“逸”的课
- 整理放到dataframe里再按教室号group

最后搞出来个csv，又用excel搞搞数据透视表什么的，生成了一份颜值略高的PDF，牛逼哄哄起名为《南京大学 16-17第一学期 逸夫楼自习指南》

### 来吧验证码！ - GRE抢座
除了查成绩，我还要查GRE考位，想报个好点的考场，尽管ETS网页设计没毛病，但一次次用鼠标点实在太恶心了，果断爬之。

这次就恶心了：
- 网页上没有验证码图片网址，需要先访问一个**神秘链接**，从response中拿到**神秘图片地址**，从而获得验证码
- 得从图片url转成image object再弹出来，让我输入
- 登录账号时提交的form中有个叫`csrf_token`的神奇东西，找了一个多小时，才发现隐藏在网页源代码的一个角落，还要用regex取出来

最后把这个和之前的校园网登录脚本放在一个windows脚本中，用不同的参数来区分运行哪个，终于在我不懈查找下，抢到了考位。

### 搞个Amazon的服务器吧 - 7*24服务端抢课

大三下到了，能否把学分修够，影响大四能否自由实习，不得不抢一波课了。也是在这个过程中，终于感觉用到了一点智商。

首先把之前写的gre查询的类简单修改，就可以用来抢课了，发现自己抽象的还不错（其实应该是继承之类的，当时很菜）

#### 控制变量法实验
用浏览器提交选课正常，但用爬虫就不行。于是打开隐身窗口，浏览器做一步，代码调试一步，终于发现：不可以直接提交选课，需要先访问一次选课列表的界面--一句GET搞定。教务处隐藏的小心机哈哈哈哈哈

#### URL找规律
当时不会看`onClick=blabla`，也不会看JavaScript函数，只知道点提交，看request form，但通识课全部选满无法提交，就无法知道表单内容。于是我开始根据其他类型课程推测：

之前通修课补选的时候，发现**查看列表**的URL和**选课**的URL很像：  
`/courseList.do?method=commonCourseRenewList&courseKind=15`  
`/courseList.do?method=submitCommonRenew&classId=74391&courseKind=15`
但是照搬并没有用，忽然想起，有些选课是用GET，有些是用POST，说明部分API已经修改了。

于是考虑和通识课同一时代的公选课。对比公选课**查看**和**提交选课**的链接：
`/courseList.do?method=publicRenewCourseList&campus=%E4%BB%99%E6%9E%97%E6%A0%A1%E5%8C%BA`
`/courseList.do?method=submitPublicRenew&classId=75533&campus=%E4%BB%99%E6%9E%97%E6%A0%A1%E5%8C%BA`

然后对应通识课**查看**的连接：  
`http://219.219.120.48/jiaowu/student/elective/courseList.do?method=discussRenewCourseList&campus=%E4%BB%99%E6%9E%97%E6%A0%A1%E5%8C%BA`
做相应修改得到：  
`http://219.219.120.48/jiaowu/student/elective/courseList.do?method=submitDiscussRenew&classId=75302&campus=%E4%BB%99%E6%9E%97%E6%A0%A1%E5%8C%BA`
直接复制到地址栏测试，提示“课程已满”，完美！

不知道是不是所有人都有这种感觉，当凭自己的idea成功解决一个难题的时候，**高举双手，闭上双眼，嘴里嘟囔着：我TM简直是个天才！**


#### 上服务器
由于我的笔记本需要经常开关移动，没法持续选课，于是想到了之前申请的Amazon AWS 弹性计算服务器。来吧Ubuntu，好久不见！

在服务器上运行程序，又经历了这样的过程：
1. 直接运行，后来发现这样我就没法干别的了
2. 于是使用`screen`命令来在SSH下开多个terminal，方便切换，让程序后台运行，但看程序运行记录又很不方便
3. 于是搞log，并用`>`进行output redirection，这样就可以
4. 随时ssh过去查看log. 但人总会更懒，甚至不向按`shift+G`翻到最后看最新log，
5. 于是使用`stdbuf -oL`来设置只输出一行，或者用`-tail`来看整个log的最后几行。但总不能一直看着它
5. 于是搞个异常处理，自动重启，`Supervisor`开机自启什么的

战果是辉煌的，想要的选修课**全部**抢到，甚至多出来了几门。

### 有了服务器人就会变贪 - 定制新闻推送和天气预报

申请微信企业号，配合服务器端爬虫，实现教务网新闻的自动爬取整理推送和与用户指令交互。

这个比较长，设计微信开发、flask web server、nginx转发。下次更新。

### 决战新版教务系统

教务处加了验证码，选课API也变了一些，再考虑到之前的代码风格好垃圾，决定重构之前的抢课类。这次代码要robust一点，增强成功率（不好意思说最后是手选的，尴尬）

由于这次是提前准备，选课入口没有开，大部分API都是根据上学期的推测，写了不少`if`判断，越写越乱，于是干脆自己总结个API的思维导图。一开始还是用看request的老方法，搞着搞着发现了`onClick`函数里其实写了提交方法，搞着搞着又发现原来代码都已经在JavaScript函数里了，顺手看了一点点js的syntax，终于可以直接从源代码提取API了。

细看源代码，又突然发现，原来入口不是没开，只是被**注释**掉了，哈哈哈哈哈哈哈哈哈哈哈哈！冷静，其实还是不能选课，因为后台是有时间过滤的，但至少能直接看到具体的API了。

总结好API，又按照一些开源项目里学来的优雅做法，写了**基类**和继承，这样以后爬别的也能用。除此之外，为了优雅地处理**优先级**问题（优先选A课，然后选B,C,D，如果某门课已经选中，就继续刷优先级比它高的课，而低的不再管），翻了Python自带的`PriorityQueue`和`heapq`，发现都不行，于是自己写了一个**优先队列**，而且用到了generator的`yield`和`send`，再次感觉自己碉堡了，哈哈。

最后就是找课程代码，由于看不到任何课程，没法从选课页面找，我就翻遍教务系统各个页面的html寻找突破口，终于在成绩单页面找到了——只要上过这门课，就会同时记录下当时的课程后台编号，这样只要找个上过想选的课的人就行了。

问题基本解决，然而由于各种原因，找不到。那程序就没法提前部署，于是我又开始写监控提醒，这次连`winsound`库都用上了（用于在windows上用播放声音），还操起GoldWave亲自剪了个充满激情的铃声用于提醒。

好了！我看了数据结构、写优雅代码、翻html源码，最后程序却出了意料之外的bug，我们用浏览器手动刷新抢的课。。。不过这个过程很有收获！代码以后还能复用！

### 辣鸡ETS毁我青春 - 托福抢座记
托福考试注册网站，不仅登录方式诡异、表单难以获取、错误提示多样、而且速度非常不稳定！无论多优美的idea，写到最后都是满屏的corner case和异常处理。

下次单独写好了。