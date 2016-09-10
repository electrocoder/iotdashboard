# -*- coding: utf-8 -*-
"""
Settings for iotdashboard project.
Django 1.9.7.
Python 2.7.12

https://iothook.com/
"""

import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (
    (u'iot', 'info@iothook.com'),
)

SECRET_KEY = '9#rxdk3_%-sufmh$#!b+iqpm0!ztfv+)08g-%g@#)flx*p$o(('

WEBSITE_NAME = "Iotdashboard"

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'markup_deprecated',
    # 'syntax_colorize',
    'chartit',
    'panels',
    'devices',
    'channels',
    'elements',
    'datas',
    'drawcharts',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'iotdashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'iotdashboard.wsgi.application'

HEROKU = False # if heroku server HEROKU = True,  else HEROKU = False for local server
IHOOK_WEB_SITE = True # if ihook.xyz domain IHOOK_WEB_SITE = True, else IHOOK_WEB_SITE = False for local server

DEBUG = False

if HEROKU:
    import dj_database_url

    DATABASES = {}
    DATABASES['default'] = dj_database_url.config()
    DATABASES['default']['CONN_MAX_AGE'] = 500

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    MEDIA_ROOT = os.path.join(BASE_DIR, 'iotdashboard_media')
    STATIC_ROOT = os.path.join(BASE_DIR, "iotdashboard_static")
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'iotdashboard_db.sqlite3'),
        }
    }

    MEDIA_ROOT = os.path.join(BASE_DIR, '../iotdashboard_media/')
    STATIC_ROOT = os.path.join(BASE_DIR, "../iotdashboard_static/")

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

_ = lambda s: s

LANGUAGES = [
  ('tr', _('Turkish')),
  ('en', _('English')),
]

LOCALE_PATHS = (
                os.path.join(BASE_DIR, 'locale'),
)

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
                    BASE_DIR + '/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

LOGIN_URL          = '/admin/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
#     'PAGINATE_BY': 10
# }
