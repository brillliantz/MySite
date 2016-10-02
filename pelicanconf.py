#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'BN Liu'
SITENAME = u'BrZ site'
SITEURL = '.'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

THEME = './theme/xycoding-gum/'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('QuantStart', 'http://www.quantstart.com'),
         ('Quantopian', 'http://www.quantopian.com/'),
         )

# Social widget
SOCIAL = (('LinkedIn', 'http://www.linkedin.com/in/bingnliu/en'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#---------------------------------------------------------------------
# ipynb plugin
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins/',]
PLUGINS = ['ipynb.markup', 'render_math', 'sitemap', 'random_article']
# sitemap plugin options:
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.3,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
# random_article plugin options:
RANDOM = 'random.html'

#--------------------------------------------------------------------
# comment system
#DISQUS_SITENAME =

#--------------------------------------------------------------------
# personal URLs
GITHUB_URL = 'https://github.com/brillliantz'
TWITTER_URL = 'http://twitter.com'
FACEBOOK_URL = 'http://www.facebook.com'
LINKEDIN_URL = 'https://www.linkedin.com/in/bingnliu/en'
