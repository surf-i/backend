from django.contrib.auth.models import User

def get_user_by_username(username):
    user = User.objects.get(username=username)
    return user

def get_user_by_email(email):
    user = User.objects.get(email=email)
    return user