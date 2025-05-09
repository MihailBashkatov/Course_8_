from rest_framework import serializers

from habits.models import Habit
from habits.validators import (HabitPeriodValidator, NiceHabitRelatedValidator,
                               NiceNotRewardNotRelatedHabitValidator,
                               RewardOrHabitRelatedValidator,
                               TimeDurationValidator)


class HabitSerializer(serializers.ModelSerializer):
    """Serializer for the model Habit."""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            TimeDurationValidator(field=["habit_time_duration"]),
            RewardOrHabitRelatedValidator(field=["related_habit", "habit_reward"]),
            NiceHabitRelatedValidator(field=["related_habit"]),
            NiceNotRewardNotRelatedHabitValidator(field=["is_nice_habit"]),
            HabitPeriodValidator(field=["habit_period"]),
        ]
