#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'luyangong'
SITENAME = 'BEGIN NOW'
SITEURL = '/blog'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh-Hans-CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('博客园', 'https://www.cnblogs.com/lyg-blog/'),
    ('Github', 'https://github.com/luyangong'),
    ('Pelican', 'http://getpelican.com/'),
    # ('Python.org', 'http://python.org/'),
    # ('Jinja2', 'http://jinja.pocoo.org/'),
    # ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    # ('You can add links in your config file', '#'),
    #       ('Another social link', '#'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
OUTPUT_PATH = "docs"
