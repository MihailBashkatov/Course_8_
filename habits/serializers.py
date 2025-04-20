from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Serializer for the model Habit."""

    class Meta:
        model = Habit
        fields = '__all__'
