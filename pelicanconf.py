from pelican import __version__
PELICAN_VERSION = __version__

AUTHOR = 'TheTNTLabs Gaming'
SITENAME = 'TheTNTLabs Blog'
SITEDESC = 'Gaming, with a bang!'
SITEURL = 'https://blog.thetntlabs.us.to'
PARENTNAME = 'TheTNTLabs'
PARENTURL = 'https://www.thetntlabs.us.to/'
PARENTIMG = 'https://design.thetntlabs.us.to/ttl/img/logo-32x32.png'
PARENTIMGALT = 'TheTNTLabs Logo'
COLORMODE = 'dark'
MAINNAV = (
    ('Blog', '/', '_self', True),
    ('Chat', 'https://thetntlabs.zulipchat.com/', '_blank', False),
    ('Source', 'https://codeberg.org/TheTNTLabs', '_blank', False),
    ('Status', 'https://status.thetntlabs.us.to/', '_self', False),
  )
BLOGNAV = (
    ('Archives', '/archives', 'archive'),
    ('Authors', '/authors', 'author'),
    ('Categories', '/categories', 'categor'),
    ('Tags', '/tags', 'tag'),
  )
FOOTER = (
    ('body', 'Copyright © TheTNTLabs Gaming. <a target="_blank" href="https://codeberg.org/TheTNTLabs/Blog/src/branch/main/LICENSE.md">LICENSE (Blog)</a> <a target="_blank" href="https://codeberg.org/TheTNTLabs/Design/src/branch/main/LICENSE.md">LICENSE (Design)</a>'),
    ('body', 'Powered by <a target="_blank" href="https://getpelican.com/">Pelican</a>'),
)

DELETE_OUTPUT_DIRECTORY = True

PATH = 'content/'
OUTPUT_PATH = 'static-deployment/'
THEME = 'themes/thetntlabs/'

ARTICLE_PATHS = [
    'articles/',
  ]
STATIC_PATHS = [
    'configs/_headers',
    'configs/_redirects',
  ]
EXTRA_PATH_METADATA = {
    'configs/_headers': {'path': '_headers'},
    'configs/_redirects': {'path': '_redirects'},
  }

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
TIMEZONE = 'Etc/UTC'

DEFAULT_PAGINATION = 12
PAGINATION_PATTERNS = (
  (1, '{base_name}/', '{save_as}'),
  (2, '{base_name}/{number}', '{base_name}/{number}.html'),
)

ARTICLE_SAVE_AS = 'article/{slug}.html'
ARTICLE_URL = 'article/{slug}'

ARTICLE_LANG_SAVE_AS = 'article/{slug}-{lang}.html'
ARTICLE_LANG_URL = 'article/{slug}-{lang}'

PAGE_SAVE_AS = 'page/{slug}.html'
PAGE_URL = 'page/{slug}'

AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'

CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'

TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_URL = 'tag/{slug}/'

AUTHOR_FEED_RSS = None
