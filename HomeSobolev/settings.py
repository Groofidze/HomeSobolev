from .secret import *
from pathlib import Path

# Путь проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Режим разработки
DEBUG = True

# Подключенные хосты
ALLOWED_HOSTS = ["*"]

# Активные приложения
INSTALLED_APPS = [
    # Начальные
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # Приложение проекта
    "books",
]

# Прослойка
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Основной роут
ROOT_URLCONF = "HomeSobolev.urls"

# пути HTML страниц, контекстных процессоров
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Запуск wsgi
WSGI_APPLICATION = "HomeSobolev.wsgi.application"

# Базы данных
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": NAME_BD,
        "USER": USER_BD,
        "PASSWORD": PASSWORD_BD,
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# Валидатор паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Локализация
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Статические файлы
STATIC_URL = "/static/"
STATIC_ROOT = [BASE_DIR / "collect_static"]

# Медиа файлы
MEDIA_URL = "/media/"

# PrimaryKey
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
