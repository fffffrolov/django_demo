from app.settings.env import env

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'
SITE_ID = 1

MAP_WIDGETS = {
    'GooglePointFieldWidget': (
        ('zoom', 15),
        ('markerFitZoom', 12),
    ),
    'GOOGLE_MAP_API_KEY': env('GOOGLE_MAP_API_KEY', default='', cast=str),
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 600
