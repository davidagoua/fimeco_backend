from .settings import *



ALLOWED_HOSTS = ['192.168.1.3','localhost','127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_PASSWORD'),
        'PORT': env('DB_PORT')
    }
}
