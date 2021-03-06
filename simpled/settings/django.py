import environ
import django_heroku

from . import configuration
from .utils import config_media_storage

# Build paths inside the project like this: BASE_DIR('subdir').
BASE_DIR = environ.Path(__file__) - 3

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = configuration.env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = configuration.env.bool('DEBUG', default=False)

ALLOWED_HOSTS = configuration.env.list('ALLOWED_HOSTS')


# Application definition

AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_yasg',
    'cloudinary',
    'channels',

    'users',
    'courses',
    'chats'
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

ROOT_URLCONF = 'simpled.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR('templates')]
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

WSGI_APPLICATION = 'simpled.wsgi.application'
ASGI_APPLICATION = 'simpled.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {'default': configuration.env.db('DATABASE_URL')}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

PUBLIC_DIR = BASE_DIR.path('public/')
STATIC_ROOT = PUBLIC_DIR('static')
STATIC_URL = configuration.env.str('STATIC_URL', default='/static/')
MEDIA_ROOT = PUBLIC_DIR('media')
MEDIA_URL = configuration.env.str('MEDIA_URL', default='/media/')

# Media storage configuration

config_media_storage()


# Configure Heroku

django_heroku.settings(locals(), databases=False, secret_key=False, allowed_hosts=False)

# Email configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587
EMAIL_HOST_USER = configuration.env.str('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = configuration.env.str('EMAIL_HOST_PASSWORD')

