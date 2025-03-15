from .base import BASE_DIR, environ, os  # Явный импорт BASE_DIR


env = environ.Env()
env.read_env(".env")

SECRET_KEY = env("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

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

# Настройки статических файлов
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
