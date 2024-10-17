# from flask import Flask
# from flask_caching import Cache
#
# app = Flask(__name__)
#
# # Configure Flask-Caching
# app.config['CACHE_TYPE'] = 'redis'
# app.config['CACHE_REDIS_HOST'] = 'localhost'
# app.config['CACHE_REDIS_PORT'] = 6379
# app.config['CACHE_REDIS_DB'] = 0
# app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'
#
# cache = Cache(app)
#
#
# @app.route('/')
# @cache.cached(timeout=60)  # Cache timeout in seconds
# def index():
#     return "Hello, World!"
#
# #  opchcannlly
# @app.route('/clear-cache')
# def clear_cache():
#     cache.clear()
#     return "Cache cleared!"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
#
