# -*- coding: utf-8 -*-

import os
import pytz


### Core Settings

ABSOLUTE_URL_OVERIDES = []
ADMINS = [('Kevin', 'ikerol@163.com')]
ALLOWED_HOSTS = []
ALLOWED_INCLUDE_ROOTS = []
CACHES = {
    'default': {
        'BACKEND': '',
        'LOCATION': '/var/tmp/django_cache',
        'TIMEOUT': 300,
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
        'TIME_ZONE': 'Asia/Shanghai',
    }
}
DATE_FORMAT = 'N j, Y' # (e.g. Feb 4, 2016)
DATETIME_FORMAT = 'N j, Y, P' # (e.g. Feb 4, 2016, 5 p.m.)

# Basic config

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SECRET_KEY = 'change-secret-key-when-deploy-django'
DEBUG = True

# General project information
# These are available in the template as SITE_INFO.<title>
SITE_VARIABLES = {
    'site_name': 'Kerolgao.com',
    'site_descript': 'Personal website powered by Python',
}

# Local settings

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True


### Auth

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


### Media and Templates

MEDIA_ROOT = os.path.join(BASE_DIR, 'media-root')
MEDIA_URL = '/_sources/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


### Static Files

# collect all static files together
STATIC_ROOT = os.path.join(BASE_DIR, 'static-root')
# either you like, for example: kerolgao.com/static/
STATIC_URL = '/_static/'

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'home/static'),
]


### Other settings

# URLs, WSGI, middleware, etc.

ROOT_URLCONF = 'kgdotcom.urls'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

WSGI_APPLICATION = 'kgdotcom.wsgi.application'

# Applications

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'home',

]

