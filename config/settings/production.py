from .base import * 
import dj_database_url

env = environ.Env()
env.read_env(".env")

DATABASE_URL = env.str("DATABASE_URL", default=None)

if DATABASE_URL:
    DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("DB_NAME"),
            "USER": env("DB_USER"),
            "PASSWORD": env("DB_PASSWORD"),
            "HOST": env("DB_HOST"),
            "PORT": env("DB_PORT"),
        }
    }

SECRET_KEY = env("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")


# Настройки статических файлов
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

