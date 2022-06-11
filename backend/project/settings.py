"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
# Standard Library
import os
from datetime import timedelta
from pathlib import Path

# Django
from django.utils.translation import gettext_lazy as _

# 3rd-party
from corsheaders.defaults import default_headers

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nyqa6gebz7n%hy$h*%^9^5zy9efk$&j9-)96%c185#(d82=h@4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ALLOWED_ORIGINS = [
    'vps-9ee2e9ea.vps.ovh.net'
]
CORS_ALLOW_HEADERS = default_headers + ('cache-control',)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'channels',
    'backend.settings.apps.SettingsConfig',
    'backend.handlers.apps.HandlersConfig',
    'backend.accounts.apps.AccountsConfig',
    'backend.notify.apps.NotifyConfig',
    'backend.chat.apps.ChatConfig',
    'corsheaders',
    'rosetta',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'push_notifications',
    'import_export',
]

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'backend.accounts.serializers.UserSerializer',
}

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.project.urls'

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
                'backend.settings.context_processors.settings_processor',
            ],
        },
    },
]

LOGGING = {
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(process)d %(filename)s %(lineno)d %(message)s',
        },
    },
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'debug.log'),
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'email_backend': 'django.core.mail.backends.smtp.EmailBackend',
        },
        'file-info': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'info.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

WSGI_APPLICATION = 'backend.project.wsgi.application'
ASGI_APPLICATION = 'backend.project.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pl-pl'
TIME_ZONE = 'Europe/Warsaw'

gettext = lambda s: s  # noqa: E731
LANGUAGES = [
    ('pl', gettext('Polish')),
    ('en', gettext('English')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

ROSETTA_LANGUAGES = [
    ('pl', _('Polski')),
]


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# REST_USE_JWT = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(days=60),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=90),
#     'ROTATE_REFRESH_TOKENS': True,
# }

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'apps_static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/uploads/')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.CustomUser'

DEFAULT_FROM_EMAIL = 'uwm.kropka.masters@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'uwm.kropka.masters@gmail.com'
EMAIL_HOST_PASSWORD = 'costam123'

FCM_API_KEY = 'AAAAD9bfjIY:APA91bGH8OpKBJNrym_NuxjOdW_RWJPpIfWls8ldTUvqkfG6AHfGE3GCnaONL8Tr' \
              'WTTd3qqCAkE2wWRsSgICH8pTdUUlW9x3NjPZ8ZyQtcRsdqm_MFxvag6QKixF0iXjG4EAdoskJmxr'

PUSH_NOTIFICATIONS_SETTINGS = {
    'FCM_API_KEY': FCM_API_KEY,
    'GCM_API_KEY': '',
}

LOGIN_REDIRECT_URL = '/'

try:
    # Project
    from backend.project.settings_local import *  # noqa: F403, F401
except ImportError:
    pass

# Needs to be after
try:
    # Project
    from backend.project.settings_sentry import *  # noqa: F403, F401
except ImportError:
    pass
