
# Medidas por defecto para resizing y todo eso
DEFAULT_WIDTH = 150
DEFAULT_HEIGHT = 150
DEFAULT_QUALITY = 60

MAX_WIDTH = 3000
MAX_HEIGHT = 3000

# Imágenes par mostrar en caso de error
IMAGE_400 = './static/400.jpg'
IMAGE_401 = './static/401.jpg'
IMAGE_404 = './static/404.jpg'
IMAGE_500 = './static/500.jpg'


# Auth
AUTH_BACKEND = 'auth.none'
AUTH_BACKEND_HOST = None

# Cosas para Flask
SENTRY_DSN = None  # noqa
REDIS_URL = 'redis://localhost:6379/0'

# Source & Cache paths
IMAGES_SOURCE_DIR = '/tmp'
IMAGES_CACHE_DIR = '/tmp'
