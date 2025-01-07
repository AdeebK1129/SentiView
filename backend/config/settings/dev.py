import environ

from .base import *

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(str(BASE_DIR / ".env"))

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = ["*"]

THIRD_PARTY_APP = [
    "django_extensions",
]  # third party apps goes here

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APP

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PWD"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    }
}


