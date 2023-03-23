from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def notify_customer():
    print("notify_customer started")
    # print(message)
    sleep(10)
    print("notify_customer ends After 10 seconds !!!!!! ")
    return "returned from notify_customer"

@shared_task
def send_email_to_notify(to,sub="testSubject",body="testBody"):
    EMAIL_HOST_USER = 'rashidurrahman2001@gmail.com'
    EMAIL_HOST_PASSWORD = 'vmlseultjxoulbbz'
    response  = {}
    res = send_mail(sub,body,EMAIL_HOST_USER,[to],auth_password=EMAIL_HOST_PASSWORD) # "iqsiydcrndnvumjd"
    if res == 1:
        response['isSuccess'] = True
        response['message'] = "Please Check Your Mail inbox for link"
    else:
        response['isSuccess'] = False
        response['message'] = "Failed! Please Try Again"
    print(response)
    # return HttpResponse(json.dumps(response))