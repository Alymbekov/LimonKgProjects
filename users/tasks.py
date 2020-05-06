from limon_project.celery import app
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
User = get_user_model()


@app.task
def conf_emil(email):
    send_mail(
        'Hello from Limon.KG',
        'Confirm your login http://127.0.0.1:8000/users/login/',
        'nursultankaragulov0220@gmail.com',
        [email],
        fail_silently=False,
    )
    
# @app.task
# def spam_email():
#     for users in User.objects.all():
#         send_mail(
#             'Hello user from Bishkek',
#             'You subcribe on spam sms',
#             'nusultankaragulov0220@gmail.com',
#             [users.email],
#             fail_silently=False,
#         )

@app.task
def plus(a, b):
    return a + b

@app.task(bind=True, default_retry_delay=5 * 60)
def my_task_retry(self, a, b):
    try:
        return a + b
    except Exception as exc:
        raise self.retry(exc=exc, contdown=50)