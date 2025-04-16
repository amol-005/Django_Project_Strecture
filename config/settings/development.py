from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#Use development "Hosts" here
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

#Use development "database" here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

USERNAME = 'amol@2025'
PASSWORD = 'Amol@2025'