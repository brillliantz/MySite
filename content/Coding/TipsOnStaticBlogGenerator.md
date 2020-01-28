---
title: "静态博客搭建指南"
date: 2020-01-27
url: "/what/a/url"
---

使用博客生成器有内容-样式分离、便于版本管理、定制程度高等一系列优点。折腾过两个不同的框架后总结一些经验要点。本文关注high-level的一些要点，不涉及具体技术细节。

<!--more-->

## 静态博客框架的选择

### 自己搭建博客相比使用Medium等现有平台有何好处
无论自己搭建还是使用其他平台，它们背后的工作原理都是类似的。一个博客网页=纯粹的内容+内容所套的样式（字体、字体大小、行间距、背景颜色等）。除非是微信公众号文章这种需要样式精准结合内容以增强表达效果，内容和样式分离是比较方便的。这样一方面在输出内容时可以专心于想法本身，另一方面样式由于是独立的所以可以方便地更换。

如果使用博客平台，比如新浪博客，我们的内容实际上是保存在平台那里，样式也只能在对方提供的选项中选择。如果自己搭建就方便得多，内容自己写自己版本管理（Git），样式随便魔改，放博客的网站服务器如果倒了，就换一家放就行，非常方便。

### 静态 v.s. 动态
静态指的是所有网页都已经提前制作好，网页行为不会因为用户行为而改变（比如无法输入任何日期查询当日天气），微信公众号文章就可以理解为典型的静态网页。动态网页则是有后端程序/数据库等能进行更复杂的互动。对于输出内容的博客来讲，静态足以，而且方便搭建维护。

### 静态博客框架选择

刚玩博客的时候，想着自己只会Python所以选的时候只看基于Python的。后来发现，其实自己只是作为用户，除了各种configuration，主要修改的也就是HTML模板和CSS，语言parse和render的部分其实很少有魔改的需求。而且，现在对新语言心态开放多了，就当开开眼界换换思路，无何不可。

因此，选择模板只需要
- 颜值高：千篇一律的文字载体我选好看的；
- 足够灵活：可以自定义；
- 用的人多：Bug少教程多；

_注：选框架的网站是[StaticGen](https://www.staticgen.com/)，可以根据最近30天/7天Github stars数目排序筛选活跃项目。曾经用的Pelican，现在转到Hugo_

## 配置要点

即使是开箱即用的强大博客框架（如[Hugo](https://gohugo.io/)框架+[Ananke](https://themes.gohugo.io/gohugo-theme-ananke/)主题），也有很多需要配置的地方，本文简单记录。

### 主要考虑的需求
- 读者友好性：网页加载速度快，字体样式好看，文章分类、目录结构清晰；
- 互动性：最好支持评论，至少有个联系方式；
- 可维护性：模板/主题可扩展性强好修改，文章永久链接可自定义这样换平台后还是同样的链接，部署简单方便CI这样以后只需要关心内容输出。

### 对于Hugo来说我做了如下事情
1. Table of Contents 自动显示；
2. 开启`disqus`评论系统；
3. 文章预览显示长度，如何分割预览区（比如Hugo使用`<!--more-->`分割）；
4. 如何覆盖主题的template和默认配置（类似于PYTHONPATH的优先级列表）；
5. 每篇文章的永久链接：文件名/标题不易改变但文件夹结构很可能以后变化；
6. 静态页面输出目录和自动部署脚本，部分框架如我用的Hugo官方就有[tutorial](https://gohugo.io/hosting-and-deployment/hosting-on-github/)，部分CI服务商对Github Pages提供了额外的便利，如[Travis CI](https://docs.travis-ci.com/user/deployment/pages/)；
7. 如果有googleapis，cloudfare等依赖，为加速国内访问需要替换掉被墙；
8. 使用兼容中文字体的font-family声明；  
    ```
    * {
    font-family: Helvetica, Tahoma, Arial, STXihei, "华文细黑", "Microsoft YaHei", "微软雅黑", SimSun, "宋体", Heiti, "黑体", sans-serif !important;
    }
    ```
9. 选好看、成熟的主题（Hugo[官方默认主题](https://themes.gohugo.io/gohugo-theme-ananke/)就很强，宣称"The last theme you'll  ever need"），如果主题作者对框架的使用很烂，你在改的时候也会很痛苦。
10. 考虑加速访问：使用[Chrome Dev Panel分析访问速度瓶颈](https://developers.google.com/web/tools/chrome-devtools/network/resource-loading)，使用本地CDN、SVG图片等优化访问速度（如[css.loli.net](https://css.loli.net/)）.

