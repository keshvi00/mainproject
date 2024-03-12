from django.contrib.auth.backends import ModelBackend
from .models import CustomUserr

class EmployeeIDBackend(ModelBackend):
    def authenticate(self, request, employee_id=None, password=None, **kwargs):
        try:
            user = CustomUserr.objects.get(employee_id=employee_id)
            if user.check_password(password):
                return user
        except CustomUserr.DoesNotExist:
            return None
