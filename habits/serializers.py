from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    def validate(self, data):
        print(self)
        print(data)


    class Meta:
        model = Habit
        fields = ('place', 'time', 'action', 'pleasant_habit', 'binding_habit', 'period', 'reward', 'execution_time',
                  'is_publish')
