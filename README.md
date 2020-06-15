Hi. This is very basic personal portfolio project to understand how django works.
First install requirements:

pip install -r requirements.txt

If you want to use PostgreSQL instead of sqlite3, make blank database with your own username and password.
then uncomment and change database connection settings at

./Portfolio/settings.py

for more information :
https://www.guru99.com/postgresql-create-database.html

https://djangocentral.com/using-postgresql-with-django/

then :
1. py manage.py makemigrations
2. py manage.py migrate
3. py manage.py createsuperuser
4. py manage.py runserver
