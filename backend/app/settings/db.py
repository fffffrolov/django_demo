# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

from app.settings.env import env

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}
