import tempfile

SECRET_KEY = 'fake-key'
SCANCODEIO_WORKSPACE_LOCATION = tempfile.mkdtemp()
INSTALLED_APPS = ["scanpipe"]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
