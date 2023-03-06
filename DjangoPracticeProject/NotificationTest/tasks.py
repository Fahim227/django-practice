from celery import shared_task
from time import sleep


@shared_task
def notify_customer():
    print("notify_customer started")
    # print(message)
    sleep(10)
    print("notify_customer ends After 10 seconds !!!!!! ")
    return "returned from notify_customer"

@shared_task
def send_email(from_send,to,subject="Test"):
    print("send_email started")
    print(from_send,to,subject)
    # sleep(10)
    print("send_email ends After 10 seconds !!!!!! ")
    return "returned from send_email"