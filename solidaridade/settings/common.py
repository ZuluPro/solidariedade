"""
Common settings for solidariedade project.
"""
from django.utils.translation import ugettext_lazy as _
from .env import CONFIG

DEBUG = CONFIG.getboolean('DEFAULT', 'debug')
TEMPLATE_DEBUG = CONFIG.getboolean('DEFAULT', 'template_debug')
ALLOWED_HOSTS = CONFIG.get('DEFAULT', 'allowed_hosts').split(',')
SERVER_URL = CONFIG.get('DEFAULT', 'server_url')
SITE_ID = CONFIG.getint('DEFAULT', 'site_id')
SECRET_KEY = CONFIG.get('DEFAULT', 'secret_key')
ROOT_URLCONF = CONFIG.get('DEFAULT', 'root_urlconf')
WSGI_APPLICATION = CONFIG.get('DEFAULT', 'wsgi_application')
# i18n
LANGUAGE_CODE = CONFIG.get('DEFAULT', 'language_code')
TIME_ZONE = CONFIG.get('DEFAULT', 'time_zone')
USE_I18N = CONFIG.getboolean('DEFAULT', 'use_i18n')
USE_L10N = CONFIG.getboolean('DEFAULT', 'use_l10n')
USE_TZ = CONFIG.getboolean('DEFAULT', 'use_tz')
# Extra files (CSS, JavaScript, Images)
STATIC_ROOT = CONFIG.get('DEFAULT', 'static_root')
STATIC_URL = CONFIG.get('DEFAULT', 'static_url')
STATICFILES_DIRS = list(filter(bool, CONFIG.get('DEFAULT', 'staticfiles_dirs').split(',')))
MEDIA_ROOT = CONFIG.get('DEFAULT', 'media_root')
MEDIA_URL = CONFIG.get('DEFAULT', 'media_url')
# STATICFILES_STORAGE = 'lor.storage.LorStorage'
TEST_RUNNER = CONFIG.get('DEFAULT', 'test_runner')

# Application definition
INSTALLED_APPS = (
    'core',
    'showcase',
    'contact',
    'donation',
    'blog',
    'tagging',
    'django_comments',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'tinymce',
    'zinnia',
    'zinnia_tinymce',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': CONFIG.get('DEFAULT', 'default_db_engine'),
        'NAME': CONFIG.get('DEFAULT', 'default_db_name'),
        'USER': CONFIG.get('DEFAULT', 'default_db_user'),
        'PASSWORD': CONFIG.get('DEFAULT', 'default_db_password'),
        'HOST': CONFIG.get('DEFAULT', 'default_db_host'),
        'PORT': CONFIG.get('DEFAULT', 'default_db_port'),
    }
}

# Internationalization
LANGUAGE_CODE = 'fr-fr'
LANGUAGES = [
    ('fr', _('French')),
    ('pt', _('Portuguese')),
    ('es', _('Spanish')),
    ('en', _('English')),
]

CONTACT_EMAIL = 'contact@solidariedade-france-portugal.org'
EMAIL_BACKEND = CONFIG.get('DEFAULT', 'email_backend')
EMAIL_HOST = CONFIG.get('DEFAULT', 'email_host')
EMAIL_PORT = CONFIG.get('DEFAULT', 'email_port')
EMAIL_HOST_USER = CONFIG.get('DEFAULT', 'email_host_user')
EMAIL_HOST_PASSWORD = CONFIG.get('DEFAULT', 'email_host_password')
EMAIL_USE_TLS = CONFIG.getboolean('DEFAULT', 'email_use_tls')
EMAIL_USE_SSL = CONFIG.getboolean('DEFAULT', 'email_use_ssl')


DBBACKUP_STORAGE_OPTIONS = {
    'location': CONFIG.get('DEFAULT', 'backup_dir')
}
