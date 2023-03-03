from celery import shared_task
from time import sleep


@shared_task
def notify_customer(message):
    print("notify_customer started")
    # print(message)
    sleep(secs=10)
    print("notify_customer ends After 10 seconds !!!!!! ")