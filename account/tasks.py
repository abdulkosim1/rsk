from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_activation_code(email, code):
    send_mail(
        'RSK', # title
        f'https://petshackaton.ru/account/activate/{code}/', # body
        'kasimmashrapov@gmail.com', # from
        [email] # to
    )
