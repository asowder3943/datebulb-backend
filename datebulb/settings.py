import dj_database_url
from pathlib import Path
import os
import django_heroku
from dotenv import load_dotenv

# In production the environment variables are preset in heroku
if not os.getenv('PROD'):
    # During development the environment variables are loaded via dotenv .env file
    load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("DJANGO_SECRET")

"""
!!!!!!!!!!!
FIX DEBUG SWITCH AND HOSTING BEFORE DEPLOYMENT ON DEC 1
!!!!!!!!!!!
"""
DEBUG = True
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    # Datebulb Apps
    'idea_manager',
    'journal_manager',
    'event_manager',
    'profile_manager',

    # Django Contrib
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Authentication Apps
    'allauth',
    'allauth.account',
    'dj_rest_auth.registration',

    # REST Framework
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'drf_multiple_model'
]

# Default middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'datebulb.urls'

# Template settings required for admin dashboard
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

# Runs with django webserver in development 'runserver'
# Runs with Gunicorn in production
WSGI_APPLICATION = 'datebulb.wsgi.application'

# In production a default DB is set up with sqlite config (this is overwritten later)
if os.getenv('PROD'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            # There is a separate database for running tests on production server
            'TEST': {
                # Name of the testing database is stored in environment variable on heroku
                'NAME': 'd9bmr3u3t3atuu',
            }
        }
    }
# Dutring development local database credentials are retrieved from environment variables retrieved from the .env files loaded with dotenv
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DB_NAME'),
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': os.getenv('DB_IP'),
                'port': int(os.getenv('DB_PORT')),
                'username': os.getenv('DB_USER'),
                'password': os.getenv('DB_PASS'),
                'authSource': os.getenv('DB_AUTH'),
                'authMechanism': 'SCRAM-SHA-1'
            }
        }
    }

# Overwrite heroku default sqlite config with AWS postgres instance credentials
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Using default password validations
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

# Language Locale and time settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


"""
!!!!!!!!!!!
SWITCH TO NGINX STATIC FILE SERVING BEFORE DEPLOYENT ON DEC 1
!!!!!!!!!!!
"""
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# using default model auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# rest framework return preferences
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# single domain display at the moment, using default site id
SITE_ID = 1

# default email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# load heroku settings required in production
django_heroku.settings(locals())
