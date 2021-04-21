# django-celery
Integrating celery with django 

Steps to get started

1 Step one :
```
git clone https://github.com/kusalkumar/django-celery.git
```

Follow the tutorials to learn more

2 Step two :
```
virtualenv env
```

Now install all the dependencies
```
pip install -r requirements.txt
```

3 Step three : Change directory to dj_delery
```
cd django-celery/dj_celery/
```

4 Step four : configure your db and redis configuration in settings.py
```
vim dj_celery/settings.py
```

5 Step five : Now you can run the server, celry and celery beat and flower (to monitor celery tasks)
```
python manage.py runserver
celery -A dj_celery worker -l INFO -E
celery -A dj_celery beat -l INFO
celery -A dj_celery flower --port=5555 
```

6 Step six

Configure async and periodic async task in admin portal

![image](https://user-images.githubusercontent.com/17420868/115117203-09f9d200-9fbb-11eb-9562-29a97f59c006.png)

7.Step six:

We can see celery tasks status:
![image](https://user-images.githubusercontent.com/17420868/115500680-6c8af080-a28f-11eb-81e7-34fa015a8170.png)




