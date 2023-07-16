from app.settings.env import env

ALLOWED_HOSTS = ['*']

ABSOLUTE_HOST = env('ABSOLUTE_HOST', cast=str, default='http://localhost:8000')
