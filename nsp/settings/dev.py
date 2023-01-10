from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-m!3hmhj*5itrj-sdup)#v3o6@gdy@gqkd&n!8ktmfr#m8pdxx("

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# настоящий почтовый сервер для прода
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
