from django.db import models

from users.models import User

# class NiceHabit(models.Model):
#     nice_habit_name = models.CharField(
#         max_length=300,
#         verbose_name="Nice Habit name",
#     )
#
#     nice_habit_user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="nice_habit_user"
#     )
#
#
#     is_nice_habit = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.nice_habit_name
#
#     class Meta:
#         verbose_name = "Nice Habit"
#         verbose_name_plural = "Nice Habits"

# Create Model Mailing
class Habit(models.Model):

    habit_name = models.CharField(
        max_length=300,
        verbose_name="Habit name",
    )

    habit_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="habit_user"
    )

    habit_place = models.TextField(verbose_name="Place to have a habit")

    habit_time_start = models.TimeField(
        auto_now=True, verbose_name="Timeset for a habit"
    )

    habit_action = models.TextField(verbose_name="Action for a habit")

    habit_time_duration = models.PositiveSmallIntegerField(
        verbose_name="Time duration for a habit"
    )

    habit_is_public = models.BooleanField(default=False)

    is_nice_habit = models.BooleanField(default=False)


    habit_period = models.PositiveSmallIntegerField(
        verbose_name="Period for a habit (in days)", default=1
    )

    nice_habit_name = models.CharField(
        max_length=300,
        verbose_name="Habit name",
        default='Draft',
        blank=True
    )

    is_habit_reward = models.BooleanField(default=False)

    habit_reward = models.TextField(
        verbose_name="Reward for a habit",
        default='Tea',
        blank=True
    )

    def __str__(self):
        return self.habit_name

    class Meta:
        verbose_name = "Habit"
        verbose_name_plural = "Habits"
