import tempfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'fake-key'
SCANCODEIO_WORKSPACE_LOCATION = tempfile.mkdtemp()
INSTALLED_APPS = ["scanpipe"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
