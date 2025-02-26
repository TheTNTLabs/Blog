from pelican import __version__
PELICAN_VERSION = __version__

AUTHOR = 'TheTNTLabs Gaming'
SITENAME = 'TheTNTLabs Blog'
SITEURL = 'https://blog.thetntlabs.us.to'
PARENTNAME = 'TheTNTLabs'
PARENTURL = 'https://www.thetntlabs.us.to/'
PARENTIMG = 'https://design.thetntlabs.us.to/ttl/img/logo-32x32.png'
PARENTIMGALT = 'TheTNTLabs Logo'
MAINNAV = (
    ('Blog', '/', '_self', True),
    ('Chat', 'https://thetntlabs.zulipchat.com/', '_blank', False),
    ('Source', 'https://codeberg.org/TheTNTLabs', '_blank', False),
    ('Status', 'https://status.thetntlabs.us.to/', '_self', False)
  )
BLOGNAV = (
    ('Archives', '/archives', 'archive'),
    ('Authors', '/authors', 'author'),
    ('Categories', '/categories', 'categor'),
    ('Tags', '/tags', 'tag')
  )

PATH = 'content/'
OUTPUT_PATH = 'static-deployment/'
THEME = 'themes/thetntlabs/'
STATIC_PATHS = [
    'root/_headers',
  ]
EXTRA_PATH_METADATA = {
    'root/_headers': {'path': '_headers'},
  }

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
TIMEZONE = 'Etc/UTC'

DEFAULT_PAGINATION = 12
PAGINATION_PATTERNS = (
  (1, '{base_name}/', '{save_as}'),
  (2, '{base_name}/-/{number}', '{base_name}/-/{number}.html'),
)

DELETE_OUTPUT_DIRECTORY = True

ARTICLE_SAVE_AS = 'article/{slug}.html'
ARTICLE_URL = 'article/{slug}'

ARTICLE_LANG_SAVE_AS = 'article/{slug}-{lang}.html'
ARTICLE_LANG_URL = 'article/{slug}-{lang}'

YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'
YEAR_ARCHIVE_URL = 'archive/{date:%Y}/'

MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/{date:%m}.html'
MONTH_ARCHIVE_URL = 'archive/{date:%Y}/{date:%m}'

AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'

CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'

TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
