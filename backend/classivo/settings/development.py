from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Print emails to console instead of sending them
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'