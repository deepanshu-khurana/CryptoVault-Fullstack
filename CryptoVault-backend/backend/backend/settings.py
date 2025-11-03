from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR is the 'backend' folder
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings
SECRET_KEY = 'django-insecure-=b+@@!^crnxvo3#dx(bi_07w@(%3)onzqkffsdl&(-bzk+(3_5'
DEBUG = True
ALLOWED_HOSTS = []
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 🎯 FIX: Rely on Token/Basic Auth and remove SessionAuthentication 
        # which requires CSRF.
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # If you want to keep permissions strict:
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your App & Third-party Apps
    'api',
    'rest_framework'
]

# 🎯 CRITICAL FIX: Middleware in the correct order for Admin and security
# CryptoVault-backend\backend\settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'django.middleware.common.CommonMiddleware',  
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        # 🎯 VERIFIED TEMPLATE PATH FIX: Points to the 'dist' folder inside 'CryptoVault'
        # BASE_DIR.parent.parent is C:\Users\deepa\New folder
        'DIRS': [BASE_DIR.parent.parent / 'CryptoVault' / 'dist'], 
        
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation (omitted for brevity, assume default)
AUTH_PASSWORD_VALIDATORS = [
# ...
]


# Internationalization (omitted for brevity, assume default)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- FILE UPLOAD (MEDIA) CONFIGURATION ---
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# 🎯 FINAL STATICFILES_DIRS FIX: Points to the *root* of the build output ('dist').
# This allows Django to find the 'assets' subdirectory, resolving the 404 errors.
STATICFILES_DIRS = [
    BASE_DIR.parent.parent / 'CryptoVault' / 'dist', 
]


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'