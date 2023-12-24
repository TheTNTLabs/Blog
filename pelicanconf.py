AUTHOR = 'TheTNTLabs'
SITENAME = 'TheTNTLabs Blog'
SITEURL = 'https://blog.thetntlabs.us.to'

PATH = 'content/'
OUTPUT_PATH = 'static-deployment/'
THEME = 'themes/thetntlabs/'
THEME_STATIC_DIR = ''

DEFAULT_LANG = 'en-us'
TIMEZONE = 'Etc/UTC'

MENUITEMS = (('Home', 'https://www.thetntlabs.us.to/', '_blank'),
             ('Archives', '/archives/', '_self'),
             ('Feed', '/feeds/all.atom.xml', '_self'))

DEFAULT_PAGINATION = 10

DELETE_OUTPUT_DIRECTORY = True

ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'

AUTHOR_SAVE_AS = 'author/{slug}.html'
AUTHOR_URL = 'author/{slug}/'

CATEGORY_SAVE_AS = 'category/{slug}.html'
CATEGORY_URL = 'category/{slug}/'

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}/'
