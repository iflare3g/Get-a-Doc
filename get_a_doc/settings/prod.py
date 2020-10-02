from .base import * # noqa

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresq',
        'NAME': '',
        'PORT': 5432,
        'HOST': '127.0.0.1',
        'PASSWORD': '',
        'USER': '',
    }
}

ALLOWED_HOST = ['your_domains']
