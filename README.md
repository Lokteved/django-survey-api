# django-survey-api
### API для создания и прохождения опросов

## Установка:
    - клонировать репозиторий
    - pip install -r requiements.txt
    - python survey_api/manage.py migrate
    - python survey_api/manage.py createsuperuser
    - python survey_api/manage.py runserver

## Эндпоинты:
    - 'surveys'
        Список все доступных опросов
    - 'surveys/<id>'
        Просмотр выбранного опроса
    - 'surveys/<id>/respond'
        Прохождение выбранного опроса, если в теле запроса нет id респондента, новый id сгенерируется автоматически
    - 'responses/<user_id>'
        Просмотр ответов на опросы выбранного пользователя
