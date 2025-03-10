from config.settings.base import *
import environ

env = environ.Env()
env.read_env(".env")
# Режим отладки
SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG")

# Разрешенные хосты
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Настройки базы данных для разработки
DATABASES = {
    "default": {
        "ENGINE": env("DB_ENGINE"),
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

# Настройки для отправки email (например, вывод в консоль)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
