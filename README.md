first install requirements:
pip install -r requirements.txt

If you want to use PostgreSQL instead of sqlite3, make blank database with your own username and password.
then uncomment and change database connection settings at
./Portfolio/settings.py

for more information :
https://www.guru99.com/postgresql-create-database.html
https://djangocentral.com/using-postgresql-with-django/

then :
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver