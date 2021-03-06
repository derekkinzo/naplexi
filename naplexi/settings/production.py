from .base import *
import os
import dj_database_url

# import django_heroku

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['naplexi.herokuapp.com',  'www.naplexi.com']

# # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')


DATABASES['default'] = dj_database_url.config(conn_max_age=600)


# #Run this only on production (Heroku), otherwise travis tests fail with sqlite3 SCHEMA issue
# This line is causing heroku deployment to fail
# django_heroku.settings(locals())