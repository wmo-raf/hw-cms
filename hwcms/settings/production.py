from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', cast=None, default=[])

MIDDLEWARE = [
    'wagtailcache.cache.UpdateCacheMiddleware',
    *MIDDLEWARE,
    'wagtailcache.cache.FetchFromCacheMiddleware'
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache'),
        'KEY_PREFIX': 'hw_cms_default',
        'TIMEOUT': 14400,  # 4 hours (in seconds)
    },
    'pagecache': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': env('MEMCACHED_URI', default=""),
        'KEY_PREFIX': 'hw_cms_pagecache',
        'TIMEOUT': 14400,  # 4 hours (in seconds)
    },
}

MANIFEST_LOADER = {
    'cache': True,
    # recommended True for production, requires a server restart to pick up new values from the manifest.
}

WAGTAIL_CACHE_BACKEND = "pagecache"

# Enable caching in production
WAGTAIL_CACHE = env("WAGTAIL_CACHE", True)

FILE_UPLOAD_TEMP_DIR = os.path.join(BASE_DIR, 'tmp')

CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', cast=None, default=[])
