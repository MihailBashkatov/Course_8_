from rest_framework import serializers

from habits.models import Habit, NiceHabit


class NiceHabitSerializer(serializers.ModelSerializer):
    """Serializer for the model NiceHabit."""


    class Meta:
        model = NiceHabit
        fields = "__all__"


class HabitSerializer(serializers.ModelSerializer):
    """Serializer for the model Habit."""
    nice_habit = NiceHabitSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = '__all__'
