from rest_framework.serializers import ValidationError
from datetime import time


class ExecutionTimeValidator:

    def __call__(self, value):
        if value > time(minute=2):
            raise ValidationError("This field cannot be greater than 120 seconds")


class PeriodValidator:

    def __call__(self, value):
        if value > 7:
            raise ValidationError("This field cannot be more than 7 days old")
