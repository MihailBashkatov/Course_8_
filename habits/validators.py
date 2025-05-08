from rest_framework.serializers import ValidationError


class TimeDurationValidator:
    """
    Adding validator to check if time duration for habit more than 2 mins"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_duration = value.get("habit_time_duration")
        if time_duration:
            if time_duration > 2:
                raise ValidationError("Time duration shall not be more then 2 mins")


class RewardOrHabitRelatedValidator:
    """
    Adding validator to check if Related habit does not appear together with Reward"""

    requires_context = True

    def __init__(self, field):
        self.field = field

    def __call__(self, value, serializer):

        if serializer.instance.related_habit and value.get("habit_reward"):
            raise ValidationError(
                f"You can choose either Reward or Related Habit, but not both at once. Currently you have Related Habit: {serializer.instance.related_habit}"
            )
        if serializer.instance.habit_reward and value.get("related_habit"):
            raise ValidationError(
                f"You can choose either Reward or Related Habit, but not both at once. Currently you have Reward: {serializer.instance.habit_reward}"
            )


class NiceHabitRelatedValidator:
    """
    Adding validator to check if Related habit is Nice Habit"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get("related_habit") and not value.get("related_habit").is_nice_habit:

            raise ValidationError(
                f"You can choose Related Habit only if it is Nice Habit. Currently {value.get('related_habit').habit_name} is not Nice Habit"
            )


class NiceNotRewardNotRelatedHabitValidator:
    """
    Adding validator to check if Nice habit can't have Related Habit or Reward"""

    requires_context = True

    def __init__(self, field):
        self.field = field

    def __call__(self, value, serializer):

        if value.get("is_nice_habit") and (
            serializer.instance.habit_reward or serializer.instance.related_habit
        ):

            raise ValidationError(
                "You can't have Nice Habit if Related habit or Reward is in place."
            )
