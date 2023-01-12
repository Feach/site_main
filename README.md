site_main

Описание проекта:

Блог шеф-повара с рецептами

Инструменты разработки

Стек:
python==3.11
asgiref==3.6.0
Django==4.1.5
django-ckeditor==6.5.1
django-js-asset==2.0.0
django-mptt==0.14.0
django_debug_toolbar==3.8.1
Pillow==9.4.0
sqlparse==0.4.3
sqlite3
Разработка

1) Прочитать все

2) Клонировать репозиторий

git clone https://github.com/Feach/site_main
3) Создать виртуальное окружение

cd mysite

python -m venv venv
4) Активировать виртуальное окружение

Linux
source venv/bin/activate

Windows
./venv/Scripts/activate
5) Устанавливить зависимости:

pip install -r req.txt
6) Выполнить команду для выполнения миграций

python manage.py migrate
8) Создать суперпользователя

python manage.py createsuperuser    "admin" занят))
9) Запустить сервер

python manage.py runserver
10) Ссылки

Сайт http://127.0.0.1:8000/

Админ панель http://127.0.0.1:8000/admin
