"""
Django settings for Helpdesk project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eui!+=^m*cq+e)=@4386rpu!77+10iic*zp*gi-kc=buhr9%of'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mongoengine.django.mongo_auth',
    'django.contrib.humanize',
    'HelpdekApp',
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
]

ROOT_URLCONF = 'Helpdesk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Helpdesk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)
AUTH_USER_MODEL = 'mongo_auth.MongoUser'
MONGOENGINE_USER_DOCUMENT = 'HelpdekApp.models.CustomUser'
#MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'
SESSION_ENGINE = 'mongoengine.django.sessions'

import mongoengine
DBNAME = 'HelpDeskDB'

AUTHENTICATION_BACKENDS = (
	'mongoengine.django.auth.MongoEngineBackend',
)

_MONGODB_USER = 'admin'
_MONGODB_PASSWD = 'admin'
_MONGODB_HOST = 'localhost'
_MONGODB_NAME = DBNAME
_MONGODB_DATABASE_HOST = \
	'mongodb://%s:%s@%s/%s' \
	% (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)
#, host=_MONGODB_DATABASE_HOST
mongoengine.connect(_MONGODB_NAME)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'aacs3173@gmail.com'
EMAIL_HOST_PASSWORD = 'password3173 '
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
PROJECT_DIR = os.path.dirname(__file__)
STATIC_ROOT = os.path.join(PROJECT_DIR, '/')
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'static'),)

MEDIA_ROOT = os.path.join(BASE_DIR, 'Helpdesk/media')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)
