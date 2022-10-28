from .models import SUser

def authenticate(username=None, password=None):
    try:
        user = SUser.objects.get(username=username)
    except SUser.DoesNotExist:
        try:
            user = SUser.objects.get(email=username)
        except SUser.DoesNotExist:
            return None
    if user.check_password(password):
        return user
    else:
        return None

def get_user(user_id):
    try:
        return SUser.objects.get(pk=user_id)
    except SUser.DoesNotExist:
        return None