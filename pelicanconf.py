#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Iván Hernández Cazorla"
SITENAME = "Taller de transferencia digital y conocimiento libre para investigadores"
SITEURL = ""

PATH = "contenido"
OUTPUT_PATH = "taller"

TIMEZONE = "Atlantic/Canary"

DEFAULT_LANG = "es"

THEME = "/home/ivanhercaz/Apps/buruma"
THEME_LOGO = False

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}

PLUGIN_PATHS = ['/home/ivanhercaz/Apps/pelican-plugins']

PLUGINS = ['i18n_subsites']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Pelican", "http://getpelican.com/"),
         ("Python.org", "http://python.org/"),
         ("Jinja2", "http://jinja.pocoo.org/"),
         ("You can modify those links in your config file", "#"),)

# Social widget
SOCIAL = (("You can add links in your config file", "#"),
          ("Another social link", "#"),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
