#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Iván Hernández Cazorla"
SITENAME = "Taller de transferencia digital y conocimiento libre para investigadores"
SITEURL = "https://taller-iatext.ivanhercaz.com"

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
                    ("Módulos", "modulos.html"),
                    ("Cronograma", "cronograma.html"))

MENUITEMS_NAVBAR_FEATURED = (("Contactar",
                              "https://ivanhercaz.com/p/contactar.html",
                              "is-primary"),
                             ("GitHub",
                              "https://github.com/ivanhercaz/taller-iatext-transferencia-digital-wikimedia",
                              "is-warning"))

FOOTER = ("Este sitio web funciona gracias a <a href='https://getpelican.com'>Pelican</a>, "
          "un gestor de contenido desarrollado en <a href='https://python.org'>Python</a> y "
          "utiliza la plantilla <a href='https://github.com/ivanhercaz/buruma'>Buruma</a>.")

LICENSE = True
LICENSE_NOTICE = ("<p><a rel='license' href='https://creativecommons.org/licenses/by-sa/4.0/'>"
                  "<img alt='Licencia Creative Commons' style='border-width: 0'"
                  "src='https://i.creativecommons.org/l/by-sa/4.0/88x31.png' /></a><br />Esta "
                  "obra está bajo una licencia <a rel='license' class='license-text'"
                  "href='https://creativecommons.org/licenses/by-sa/4.0'>Creative Commons "
                  "Atribución-CompartirIgual 4.0 Internacional</a>.")

ABOUT_EXTRACT = ("Taller de introducción al conocimiento libre y enlazado a partir del uso de"
                 " los proyectos Wikimedia, de herramientas como Scholia y Source MetaData, y de"
                 " identificadores como ORCID.<br>El principal objetivo es que los investigadores del"
                 " Instituto Universitario de Análisis y Aplicaciones Textuales tengan nociones"
                 " sobre conocimiento libre y las licencias Creative Commons compatibles, los"
                 " proyectos Wikimedia y herramientas como Scholia y Source MetaData, así como "
                 " buenas prácticas para mantener actualizado el identificador ORCID.")


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

# Matomo
MATOMO = """<!-- Matomo -->
<script type="text/javascript">
  var _paq = window._paq || [];
  /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//stats.ivanhercaz.com/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '3']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
<noscript><p><img src="//stats.ivanhercaz.com/matomo.php?idsite=3&amp;rec=1" style="border:0;" alt="" /></p></noscript>
<!-- End Matomo Code -->"""
