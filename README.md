# django-celery
Integrating celery with django 
hello
Steps to get started

Step one :
git clone https://github.com/kusalkumar/django-celery.git

Follow the tutorials to learn more

Step two :
virtualenv env

Now install all the dependencies

pip install -r requirements.txt

3 Step three : Change directory to dj_delery
cd django-celery/dj_celery/

4 Step four : configure your db and redis configuration in settings.py
vim dj_celery/settings.py

Step five : Now you can run the server, celry and celery beat
py manage.py runserver
celery -A dj_celery worker -l INFO
celery -A dj_celery beat -l INFO
