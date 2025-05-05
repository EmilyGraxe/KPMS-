from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class UserIDAuthBackend(BaseBackend):
    def authenticate(self, request, user_id=None, password=None, ):
        try:
            user = CustomUser.objects.get(user_id=user_id)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None