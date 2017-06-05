#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'BN Liu'
SITENAME = u'BrZ site'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%b.%d, %Y (%Z)'

THEME = './theme/elegant-1.3/'
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

# use folder name as category
USE_FOLDER_AS_CATEGORY = True
# use filename as slug
FILENAME_METADATA = '(?P<slug>.*)'

#----------------------------------------------------------------------
# show and store directories setting:
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL

PAGE_URL = 'page_{slug}.html'
PAGE_SAVE_AS = PAGE_URL

# category index ("articles in xxx category" page)
CATEGORY_URL = '_categories/{slug}_index.html'
# CATEGORY_URL = 'category_{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL

TAG_URL = '_tags/{slug}_index.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tags.html'

AUTHOR_URL = '_authors/{slug}_index.html'
AUTHOR_SAVE_AS = AUTHOR_URL
#----------------------------------------------------------------------

#---------------------------------------------------------------------
# ipynb plugin
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins/',]
#----------------------------------------------------------------------

PLUGINS = ['ipynb.markup', 'render_math', 'sitemap','random_article', 'tag_cloud', 'extract_toc', 'tipue_search']
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
# personal URLs
GITHUB_URL = 'https://github.com/brillliantz'
TWITTER_URL = 'http://twitter.com'
FACEBOOK_URL = 'http://www.facebook.com'
LINKEDIN_URL = 'https://www.linkedin.com/in/bingnliu/en'

#----------------------------------------------------------------------
# Below are settings only for the Elegent theme

# About Me section on homepage
LANDING_PAGE_ABOUT = {'title': "I'm a junior in physics, focusing on quant trading.",
                      'details': "Always seeking the infinite beauty of the world in my finite existence."}

# PROJECTS section on homepage
PROJECTS = [
    {'name': 'Citi Financial Innovation Application Competation',
     'url': 'http://www.citigroup.com/china/csts/EducationProgram/AboutEducation_CFC.html',
     'description': 'Leader. Lead the team to design a robo-advisor platform, allocating among major assets.',},
    {'name': 'Quantitative Analyst Intern @Wizardquant',
     'url': 'http://www.wizardquant.com/en/html/aboutus.html',
     'description': 'Research on statistical modeling.',}
]


# Here are the variables that you should set in your configuration to get the most out of Elegant
#MARKDOWN = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
#STATIC_PATHS = ['theme/images', 'images']

#----------------------------------------------------------------------

