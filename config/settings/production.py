from .base import *
import environ


# Инициализация django-environ
env = environ.Env()
env.read_env('.env')

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
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
STATIC_ROOT = BASE_DIR / "staticfiles"