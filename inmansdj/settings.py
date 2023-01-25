import django_heroku # add in the beginning
from pathlib import Path
import os
import environ


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

#SECRET_KEY = 'django-insecure-r*7!z5*e)e($a=9eddvn1m1&mru^d$4yej!a3z3f159s7438r4'
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS=["http://10.0.2.2", "http://127.0.0.1","http://localhost", 'https://instatogether.com', "https://127.0.0.1","https://localhost" ]
ALLOWED_HOSTS = ['http://127.0.0.1', "http://10.0.2.2", 'http://localhost', 'https://inmansdj.herokuapp.com', 'http://192.168.1.154', 'https://thinkfollow.com' ]
#ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS=ALLOWED_HOSTS

# Application definition

INSTALLED_APPS = [
    'api',
    'channels',
    'daphne',
    'rest_framework', 
    'rest_framework.authtoken',
    'django_filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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




ROOT_URLCONF = 'inmansdj.urls'

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

#WSGI_APPLICATION = 'inmansdj.wsgi.application'
ASGI_APPLICATION = 'inmansdj.asgi.application'



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default1': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3')
        }
    },
    'default2': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inmans',
        'USER': 'cappittall',  #capital
        'PASSWORD': 'Aura533422',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_inmansdj',
        'USER':'rootadmin',
        'PASSWORD':'prjvpc930ghuj',
        'HOST':'localhost',
        'PORT':'',
    },

}

CHANNEL_LAYERS = {
    'default': {
     #'BACKEND': 'channels_redis.core.RedisChannelLayer', 
     #'CONFIG': {
          #"hosts": [(os.environ.get('REDIS_HOST', 'localhost'),6379)],
     #     "host":"ec2-44-209-239-126.compute-1.amazonaws.com:6379"
     #    }, 
     "BACKEND": "channels.layers.InMemoryChannelLayer"
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-En' #tr-TR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'),
}

ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

if ENVIRONMENT == 'production':
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') 

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
# Bu ayar konsolda email i yazdırmak için
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" 
EMAIL_FROM = "EarnTogether"

MEDIA_URL = '/media/'
MEDIA_ROOT = 'uploads'

""" REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER': 'api.serializers.ChangePasswordSerializer'
}  """

SITE_ID = 1

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'netartyazilim@gmail.com'
EMAIL_HOST_PASSWORD = 'upwghkvfessvbyvd'




django_heroku.settings(locals())
