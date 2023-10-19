from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if (data.get('pleasant_habit', None) and data.get('binding_habit', None)) is not None:
            raise serializers.ValidationError(
                "only one of the fields 'pleasant_habit' or 'attachment_habit' can be used")
        return data

    class Meta:
        model = Habit
        fields = ('place', 'time', 'action', 'pleasant_habit', 'binding_habit', 'period', 'reward', 'execution_time',
                  'is_publish')
