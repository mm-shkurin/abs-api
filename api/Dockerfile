# Используем официальный образ Python
FROM python:3.11-slim

# Установка рабочей директории
WORKDIR /api

# Копируем файлы зависимостей и устанавливаем
COPY requirements.txt /api/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /api/

EXPOSE 8000

# Указываем команду для запуска приложения
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "setting.wsgi:application"]