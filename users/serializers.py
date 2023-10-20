from rest_framework import serializers
from users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('email', 'phone', 'first_name', 'last_name',)
