#!/usr/bin/env python
from djeasytests.testsetup import TestSetup, default_settings


default_settings.update(dict(
    ROOT_URLCONF='unit_tests.urls',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'ikari',
        'unit_tests'
    ],
    MIDDLEWARE_CLASSES=[
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'ikari.middleware.DomainsMiddleware',
    ],
    PASSWORD_HASHERS=(
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ),
    IKARI_MASTER_DOMAIN='ikari.local',
    IKARI_ACCOUNT_URL='ikari.urls.private',
    IKARI_USERSITE_URLCONF='ikari.urls.sites',
))

unittests = TestSetup(appname='unit_tests',
                      default_settings=default_settings)

if __name__ == '__main__':
    unittests.run('tests')
