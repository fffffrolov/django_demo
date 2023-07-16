from app.settings.env import env, BASE_PATH

DEFAULT_STATIC_ROOT = (BASE_PATH.parent / 'static').resolve()
STATIC_URL = 'static/'
STATIC_ROOT = env('STATIC_ROOT', cast=str, default=str(DEFAULT_STATIC_ROOT))
STATICFILES_DIRS = [
    BASE_PATH / 'static_src',
]
