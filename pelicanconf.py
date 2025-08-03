from os import getenv
from datetime import datetime

# Site settings
AUTHOR = 'Marek Sierociński'
SITENAME = "Marek's Blog"
SITESUBTITLE = "Moje małe Kaer Morhen"
SITEURL = getenv("SITEURL", "")
TIMEZONE = 'Europe/Warsaw'
DEFAULT_LANG = 'pl'
LOCALE = 'pl_PL.UTF-8'

# Header settings
HEADER_COVER = "theme/images/kaer-morhen.jpg"

# Footer settings
COPYRIGHT_YEAR = datetime.now().year
SHOW_CREDITS = True

# Other settings
GITHUB_URL = "https://github.com/marverix"

# Theme
THEME = 'theme'
THEME_STATIC_DIR = 'theme'

# Content settings
PATH = "content"

ARCHIVES_SAVE_AS = ARCHIVES_URL = 'archives.html'
AUTHORS_SAVE_AS = AUTHORS_URL = 'authors.html'
CATEGORIES_SAVE_AS = CATEGORIES_URL = 'categories.html'
TAGS_SAVE_AS = TAGS_URL = 'tags.html'

ARTICLE_PATHS = ['posts']
ARTICLE_SAVE_AS = 'post/{date:%Y}/{slug}.html'
ARTICLE_URL = 'post/{date:%Y}/{slug}.html'

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
MENUITEMS = (
    ("Strona główna", "/"),
    ("Kategorie", f"/{CATEGORIES_URL}"),
)

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
