from split_settings.tools import include

from app.settings.env import env

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG', cast=bool, default=False)
ENVIRONMENT = env('ENVIRONMENT', cast=str, default='local')

include(
    'api.py',
    'auth.py',
    'common.py',
    'db.py',
    'healthchecks.py',
    'http.py',
    'i18n.py',
    'installed_apps.py',
    'media.py',
    'middleware.py',
    'static.py',
    'storage.py',
    'timezone.py',
)
