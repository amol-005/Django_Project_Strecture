from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


#Use Production "Hosts" here
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

#Use Production "database" here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}