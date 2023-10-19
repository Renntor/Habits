from habits.models import Habit
from rest_framework import viewsets

from habits.pagination import MyPagination
from habits.serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = HabitSerializer
    pagination_class = MyPagination


