import os

import dj_database_url

SECRET_KEY = "loadtest"
DEBUG = False
ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = "project.urls"
INSTALLED_APPS = []
MIDDLEWARE = []
DATABASES = {"default": dj_database_url.parse(os.environ["DATABASE_URL"], conn_max_age=60)}
CACHES = {"default": {"BACKEND": "django.core.cache.backends.redis.RedisCache", "LOCATION": os.environ["REDIS_URL"]}}
