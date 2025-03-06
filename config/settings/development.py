from config.settings.base import BASE_DIR  # Явный импорт BASE_DIR

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Указывает на использование SQLite
        "NAME": BASE_DIR / "db.sqlite3",  # Путь к файлу базы данных
    }
}

# Дополнительные настройки для development
