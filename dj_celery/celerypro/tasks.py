from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task

from time import sleep

@shared_task
def sleep_well(duration):
    print("sleeping for {} seconds".format(duration))
    sleep(duration)
    print("sleeped for {} seconds".format(duration))

@shared_task 
def test_periodic_task():
    print("hello hello")

@shared_task 
def send_notification():
     print("Here Im")
     # Another trick


