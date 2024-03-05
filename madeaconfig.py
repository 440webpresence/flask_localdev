import datetime 

{
    'DEBUG': True,
    'TESTING': False,
    'PROPAGATE_EXCEPTIONS': None,
    'SECRET_KEY': 'your_long_random_secret_key_here',
    'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31),
    'USE_X_SENDFILE': False,
    'SERVER_NAME': 'localhost:5000',
    'APPLICATION_ROOT': '/',
    'SESSION_COOKIE_NAME': 'session',
    'SESSION_COOKIE_DOMAIN': None,
    'SESSION_COOKIE_PATH': '/',
    'SESSION_COOKIE_HTTPONLY': False,
    'SESSION_COOKIE_SECURE': True,  # Ensure cookies are sent over HTTPS only
    'SESSION_COOKIE_SAMESITE': 'Lax',  # Set to 'Lax', 'Strict', or None
    'SESSION_REFRESH_EACH_REQUEST': True,
    'MAX_CONTENT_LENGTH': None,
    'SEND_FILE_MAX_AGE_DEFAULT': None,
    'TRAP_BAD_REQUEST_ERRORS': None,
    'TRAP_HTTP_EXCEPTIONS': False,
    'EXPLAIN_TEMPLATE_LOADING': True,
    'PREFERRED_URL_SCHEME': 'https',  # Ensure URLs generated are HTTPS
    'TEMPLATES_AUTO_RELOAD': False,
    'MAX_COOKIE_SIZE': 4404
}

