from os import getenv
from datetime import datetime


AUTHOR = 'Marek Sierociński'
SITENAME = "Marek's Blog"
SITESUBTITLE = "Moje małe Kaer Morhen"
SITEURL = getenv("SITEURL", "")
COPYRIGHT_YEAR = datetime.now().year
HEADER_COVER = "theme/images/kaer-morhen.jpg"
SHOW_CREDITS = True

PATH = "content"
THEME = 'theme'
THEME_STATIC_DIR = 'theme'
TAGS_URL = 'tags.html'
CATEGORIES_URL = 'categories.html'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'
LOCALE = 'pl_PL.UTF-8'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True
