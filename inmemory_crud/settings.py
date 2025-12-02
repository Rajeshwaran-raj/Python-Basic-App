
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY="dummy"
DEBUG=True
ALLOWED_HOSTS=[]

INSTALLED_APPS=[
    "django.contrib.staticfiles",
    "api",
]

MIDDLEWARE=[
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF="inmemory_crud.urls"

DATABASES={
    "default":{
        "ENGINE":"django.db.backends.sqlite3",
        "NAME":":memory:",
    }
}

LANGUAGE_CODE="en-us"
TIME_ZONE="UTC"
USE_I18N=True
USE_TZ=True
STATIC_URL="static/"
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
