---
title: "博客注意事项"
date: 2020-01-27
draft: false
---

即使是开箱即用的博客框架，也有很多需要配置的地方，本文简单记录。


<!--more-->

1. Table of Contents 自动显示；
2. 开启`disqus`评论系统；
3. 文章预览显示长度，如何分割预览区（比如Hugo使用`<!--more-->`分割）；
4. 如何覆盖主题的template和默认配置（类似于PYTHONPATH的优先级列表）；
5. 每篇文章的永久链接：文件名/标题不易改变但文件夹结构很可能以后变化；
6. 静态页面输出目录和自动部署脚本；
7. 如果有googleapis，cloudfare等依赖，为加速国内访问需要替换掉被墙；
8. 使用兼容中文字体的font-family声明；  
    ```
    * {
    font-family: Helvetica, Tahoma, Arial, STXihei, "华文细黑", "Microsoft YaHei", "微软雅黑", SimSun, "宋体", Heiti, "黑体", sans-serif !important;
    }
    ```