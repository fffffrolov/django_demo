# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

from app.settings.env import env

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}
