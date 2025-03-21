#!/bin/bash

# Выходим из скрипта, если любая команда завершится ошибкой
set -e

# Применяем миграции базы данных
echo "Applying database migrations..."
python manage.py migrate --noinput

# Собираем статические файлы
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Запускаем сервер (или другую команду, переданную в docker-compose)
echo "Starting server..."
exec "$@"