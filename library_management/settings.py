
# library_management/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use the MySQL backend
        'NAME': 'library_db',  # Name of the MySQL database you created
        'USER': 'NamuJagtap',  # Your MySQL username
        'PASSWORD': 'Namu@8955',  # Your MySQL password
        'HOST': 'localhost',  # Localhost or the IP address of your MySQL server
        'PORT': '3306',  # Default MySQL port
    }
}
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library',
    'rest_framework_jwt',# Ensure your 'library' app is listed here
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can specify custom template directories here if you wish
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session Middleware first
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication Middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Message Middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Optionally, you can add token expiration time
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': 'your_secret_key_here',  # Ensure you change this to a secure key
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
ROOT_URLCONF = 'library_management.urls'

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
# settings.py

SECRET_KEY = '123456789'
DEBUG = True
# settings.py

import os
from pathlib import Path

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Other settings...
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
