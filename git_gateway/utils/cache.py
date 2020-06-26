from flask_caching import Cache
from os import environ

flask_cache = Cache(config={
    'CACHE_REDIS_URL': environ.get('CACHE_REDIS_URL'),
    'CACHE_TYPE': environ.get('CACHE_TYPE')
})
