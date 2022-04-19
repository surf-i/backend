from django.contrib.auth.models import User

def get_user_by_username(username):
    user = User.objects.get(username=username)
    return user