"""
Django settings for the backend project.

This file contains the settings for the project and is generated using
Django 5.1.1. The settings are configured to use PostgreSQL as the database,
and it reads sensitive configurations like the database credentials from a
secrets.json file.

For more information, see:
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see:
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import json
import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the secrets from the secrets.json file located in the backend directory (inside BASE_DIR)
with open(os.path.join(BASE_DIR, 'backend', 'secrets.json')) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """
    Get a secret from the secrets.json file or raise an error if the secret
    is not found.
    
    Args:
        setting (str): The setting key to retrieve from the secrets.json file.
        secrets (dict): The loaded secrets from the secrets.json file.
    
    Returns:
        The value of the requested secret.

    Raises:
        ImproperlyConfigured: If the requested secret is not found in the secrets.json file.
    """
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f'Set the {setting} environment variable'
        raise ImproperlyConfigured(error_msg)

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-key'

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
    'api',  # Your app
    'corsheaders',  # To allow Cross-Origin Resource Sharing (CORS)
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Middleware to handle CORS
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Can be used to define additional template directories
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

WSGI_APPLICATION = 'backend.wsgi.application'

# Database configuration for PostgreSQL using secrets from secrets.json
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret('database_name'),  # Database name
        'USER': get_secret('database_user'),  # Database user
        'PASSWORD': get_secret('database_pwd'),  # Database password
        'HOST': get_secret('database_host'),  # Database host, typically 'localhost'
        'PORT': get_secret('database_port'),  # Database port, typically 5432
    }
}

# Password validation settings for production environments
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

# Auth User Model
AUTH_USER_MODEL = 'api.CustomUser'

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Defines where static files are stored
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'build', 'static'),
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS policy for allowing all origins (for development)
CORS_ALLOW_ALL_ORIGINS = True  # Consider restricting this for production environments
