from rest_framework.serializers import ValidationError
from datetime import time


class TimeValidator:
    def __call__(self, value):
        if value > time(minute=2):
            raise ValidationError("This field cannot be greater than 120 seconds")
        else:
            return True