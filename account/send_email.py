from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'РСК', # title
        f'http://localhost:8000/account/activate/{code}', # body
        'kasimmashrapov@gamil.com', # from
        [email] # to
    )

def send_email_about_shop(email):
    send_mail(
        'RSK', # title

        f'Была создана заявка на создание организции. Пожалуйста проверьте заявку. http://34.89.184.22/admin/', # body
        'kasimmashrapov@gamil.com', # from
        [email] # to
    )

def send_reset_password_code(email, code):
    send_mail(
        'РСК', # title
        f'Привет чтобы бросить пароль тебе нужно знать этот код = {code}', # body
        'kasimmashrapov@gmail.com', # from
        [email] # to
    )