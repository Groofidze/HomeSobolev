from HomeSobolev.settings import BASE_DIR

# Режим разработки
DEBUG = True

# Подключенные хосты
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Статические файлы
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static"
]



