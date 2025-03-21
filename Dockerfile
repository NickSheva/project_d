FROM python:3.10-slim

WORKDIR /django_app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .
# Копируем скрипт для запуска
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Указываем entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Команда для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]