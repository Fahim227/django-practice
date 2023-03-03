from celery import shared_task
from time import sleep


@shared_task
def notify_customer():
    print("notify_customer started")
    # print(message)
    sleep(10)
    print("notify_customer ends After 10 seconds !!!!!! ")
    return "returned from notify_customer"