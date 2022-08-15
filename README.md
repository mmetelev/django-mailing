# Сервис уведомлений

### Тестовое задание компании Фабрика решений

[Ссылка на задание](https://www.craft.do/s/n6OVYFVUpq0o6L)

## Дополнительные задания

1. Swagger UI `docs/`
2. Docker развертывание

## Инструкция по развертыванию

1. Клонируйте проект из репозитория.
2. Создайте контейнер

~~~
    docker-compose build
~~~

3. Запустите контейнер.

~~~
    docker-compose up
~~~

4. Создайте суперпользователя.

~~~
    docker exec -it container_id python manage.py createsuperuser
~~~

Сервис доступен по ссылке `http://localhost:8000/` \
Узнать имя контейнера можно командой

~~~
    docker ps
~~~
