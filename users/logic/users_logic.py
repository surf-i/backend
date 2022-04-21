from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
def get_user_by_username(username):
    user = User.objects.get(username=username)
    return user

def get_user_by_email(email):
    user = User.objects.get(email=email)
    return user

def get_user_by_token(token):
   user = Token.objects.get(key=token).user
   return user