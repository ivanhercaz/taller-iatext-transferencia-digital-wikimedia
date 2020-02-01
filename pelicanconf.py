#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Iván Hernández Cazorla"
SITENAME = "Taller de transferencia digital y conocimiento libre para investigadores"
SITEURL = ""

PATH = "taller"
OUTPUT_PATH = "sitio"

ARTICLE_URL = "{date:%Y}/{slug}.html"
ARTICLE_SAVE_AS = "{date:%Y}/{slug}.html"
ARTICLE_PATHS = ["blog"]
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
PAGE_PATHS = ["."]

TIMEZONE = "Atlantic/Canary"

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "es"

THEME = "buruma"
THEME_LOGO = False

JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"]
}

# Buruma customization

MENUITEMS_NAVBAR = (("Inicio", SITEURL),
                    ("Introducción", "introduccion.html"),
                    ("Módulos", "modulos.html"))

FOOTER = ("Este sitio web funciona gracias a <a href='https://getpelican.com'>Pelican</a>, "
          "un gestor de contenido desarrollado en <a href='https://python.org'>Python</a> y "
          "utiliza la plantilla <a href='https://github.com/ivanhercaz/buruma'>Buruma</a>.")

PLUGIN_PATHS = ["plugins"]

PLUGINS = ["i18n_subsites"]

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
# RELATIVE_URLS = True

