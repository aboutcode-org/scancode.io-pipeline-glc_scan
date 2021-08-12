#!/usr/bin/env python
# https://docs.djangoproject.com/en/3.2/topics/testing/advanced/#using-the-django-test-runner-to-test-reusable-applications

import os

import django
from django.core.management import call_command

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    call_command("test", interactive=False)
