AUTHOR = 'TheTNTLabs'
SITENAME = 'TheTNTLabs Blog'
SITEURL = 'https://blog.thetntlabs.us.to'

PATH = 'content/'
OUTPUT_PATH = 'static-deployment/'
THEME = 'themes/thetntlabs/'
THEME_STATIC_DIR = ''

DEFAULT_LANG = 'en-us'
TIMEZONE = 'Etc/UTC'

MENUITEMS = (('Home', 'https://www.thetntlabs.us.to/'),
             ('Archives', '/archives.html'),
             ('Authors', '/authors.html'),
             ('Categories', '/categories.html'),
             ('Feed', '/feeds/all.atom.xml'))

DEFAULT_PAGINATION = 10

DELETE_OUTPUT_DIRECTORY = True
