from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-inmemory-example-secret-key"
DEBUG = True
ALLOWED_HOSTS = ["*"]

# 🚫 No contrib apps that need DB. Only our API app.
INSTALLED_APPS = [
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    # CSRF is fine to keep; our API views use @csrf_exempt anyway.
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "inmemory_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                # no auth/messages context processors
            ],
        },
    },
]

WSGI_APPLICATION = "inmemory_project.wsgi.application"

# ⚠️ Dummy DB backend – never actually used.
# Django requires DATABASES to exist, but this won't create sqlite
# or any tables, and we never call ORM.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.dummy",
        "NAME": "dummy",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
