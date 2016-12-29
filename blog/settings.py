"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from decouple import config, Csv
from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)


ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'admin_tools_zinnia',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sitemaps',
    'django_comments',
    'django_xmlrpc',
    'mptt',
    'tagging',
    'zinnia',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.contrib.messages.context_processors.messages',
                'zinnia.context_processors.version',
            ],
            'loaders': [
                'app_namespace.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]


ZINNIA_ENTRY_CONTENT_TEMPLATES = [
    ('zinnia/_short_entry_detail.html', 'Short entry template'),
]


ZINNIA_ENTRY_DETAIL_TEMPLATES = [
    ('zinnia/fullwidth_entry_detail.html', 'Fullwidth template'),
]


WSGI_APPLICATION = 'blog.wsgi.application'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'comparison': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'comparison',
        'TIMEOUT': None,
    }
}


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'HOST': config('DB_HOST', default='localhost'),
    #     'USER': config('DB_USER', default=''),
    #     'PASSWORD': config('DB_PASSWORD', default=''),
    #     'NAME': config('DB_NAME', default=''),
    #     'PORT': config('DB_PORT', default='5432', cast=int),
    # }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


ZINNIA_SPAM_CHECKER_BACKENDS = (
    'zinnia.spam_checker.backends.long_enough',
)


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = config('STATIC_URL', default='')
# in dev environment we may not have STATIC_ROOT defined
try:
    STATIC_ROOT = config('STATIC_ROOT', default='')
except ImportError:
    pass


MEDIA_URL = config('MEDIA_URL', default='')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
# MEDIA_ROOT = config('MEDIA_ROOT', default='')

# email settings
ADMIN_EMAIL = config('ADMIN_EMAIL')
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_USE_SSL = config('EMAIL_USE_SSL', default=True, cast=bool)

# admins
ADMINS = (('Admin', ADMIN_EMAIL),)
MANAGERS = (('Manager', ADMIN_EMAIL),)

SITE_ID = 1

ZINNIA_PING_EXTERNAL_URLS = False
ZINNIA_SAVE_PING_DIRECTORIES = False

ZINNIA_MARKUP_LANGUAGE = 'textile'

XMLRPC_METHODS = ZINNIA_XMLRPC_METHODS
