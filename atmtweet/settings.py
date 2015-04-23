# -*- coding: utf-8 -*-

import os
import platform
#PAOLO - see: https://docs.djangoproject.com/en/1.4/topics/i18n/translation/#how-django-discovers-language-preference
ugettext = lambda s: s

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = PROJECT_PATH

RUNNING_MACHINE_NAME = platform.node().upper()
IS_DEVELOPMENT_MACHINE = RUNNING_MACHINE_NAME in ['DELLY','DAVIDEPC']

DEBUG = IS_DEVELOPMENT_MACHINE #or RUNNING_MACHINE_NAME in ['WEB371.WEBFACTION.COM']
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
#MNT_PATH = PROJECT_PATH.replace('/var/www/','/mnt/webdata/')
MNT_PATH = PROJECT_PATH

print u'Project: "{}"'.format(PROJECT_PATH)
print u'Running on: "{}"'.format(RUNNING_MACHINE_NAME)
print u'With mnt: "{}"'.format(MNT_PATH)
print u'Development machine: "{}"'.format('yes' if IS_DEVELOPMENT_MACHINE else 'no')
print u'Debug: "{}"'.format('yes' if DEBUG else 'no')

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP, \
  FORCE_SCRIPT_NAME

#PAOLO - following lines are to "mount" project under a subpath of the domain (ie: "example.com/project/")
#WARN!!! The same subpath must be correctly setup in configuring the HTTP front server!!!
if IS_DEVELOPMENT_MACHINE:
  FORCE_SCRIPT_NAME = ''
else:
  FORCE_SCRIPT_NAME = ''

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'efb=#^xp)a81b0pyo$mhn&$)s^+gmnf8apcs#yt6tqd3nnx4yj'

# Sistemare in produzione!!!
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'rest_framework.filters',
    'rest_framework_swagger',
    'tweet',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'atmtweet.urls'

WSGI_APPLICATION = 'atmtweet.wsgi.application'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
     ('Paolo', 'prove_django@oicom.com'),
     ('Davide', 'davide.nuccio@gmail.com'),
)

MANAGERS = ADMINS

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#PAOLO - Usa i parametri corretti a seconda dell'host su cui sta girando
if IS_DEVELOPMENT_MACHINE:
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3_test'),
    }
  }
else:
  DATABASES = {
      'default': {
#           'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
          'ENGINE': 'django.contrib.gis.db.backends.postgis',
          'NAME': 'django_atmtweet',                      # Or path to database file if using sqlite3.
          'USER': 'django',                      # Not used with sqlite3.
          'PASSWORD': 'djangopass',                  # Not used with sqlite3.
          'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
          'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
      }
  }


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'Europe/Rome'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'it-it'

#PAOLO - Make only these languages available
LANGUAGES = (
    ('it', ugettext('Italian')),
)

#PAOLO - Change it from the default (0=Sunday)
FIRST_DAY_OF_WEEK = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

#PAOLO - Usa i parametri corretti a seconda dell'host su cui sta girando
if IS_DEVELOPMENT_MACHINE:
  MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
else:
  MEDIA_ROOT = os.path.abspath(os.path.join(MNT_PATH, '..', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#PAOLO - Usa i parametri corretti a seconda dell'host su cui sta girando
MEDIA_URL = '{}/media/'.format(FORCE_SCRIPT_NAME)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#PAOLO - Usa i parametri corretti a seconda dell'host su cui sta girando
if IS_DEVELOPMENT_MACHINE:
  STATIC_ROOT = ''
else:
  STATIC_ROOT = os.path.abspath(os.path.join(MNT_PATH, '..', 'static'))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#PAOLO - Usa i parametri corretti a seconda dell'host su cui sta girando
STATIC_URL = '{}/static/'.format(FORCE_SCRIPT_NAME)

STATICFILES_DIRS = (
#     os.path.abspath(os.path.join(BASE_DIR, "../../static/")),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    #PAOLO - Following is to have the "request" object inside templates,
    #see: http://stackoverflow.com/questions/2882490/get-the-current-url-within-a-django-template
    'django.core.context_processors.request',
)


#PAOLO - Define a suitable value for From field (it will be used for exceptions EMails)
SERVER_EMAIL = 'AMAT ATM-Tweet errors <info@amat-mi.it>'

#PAOLO - First line will print EMails to console, second line is for the default "real" SMTP backend
#PAOLO - NOOO!!! Let it always print to console, until we have a SMTP server available!!!
if IS_DEVELOPMENT_MACHINE or True:
  EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
  #PAOLO - This is for sending through local MTA
  #EMAIL_HOST = 'localhost'
  #EMAIL_PORT = 25  
  #PAOLO - This is for sending through Kolst mailserver
  EMAIL_USE_TLS = True
  EMAIL_HOST = 'xxxxxxxxxx'
  EMAIL_PORT = 25
  EMAIL_HOST_USER = 'xxx@xxx.xxx'
  EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxx'
  

REST_FRAMEWORK = {
    'PAGINATE_BY': 9,                 # Default to 10
    'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100,             # Maximum limit allowed when using `?page_size=xxx`.
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PAGINATION_SERIALIZER_CLASS': 'tweet.pagination.CustomPaginationSerializer',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}
