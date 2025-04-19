# Привычка:



# Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
# Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
# Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
# Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
from django.db import models

from users.models import User


# Create Model Mailing
class Habit(models.Model):

    habit_name =  models.CharField(
        max_length=300,
        verbose_name="Habit name",
    )

    habit_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="habit_user"
    )

    habit_place = models.TextField(verbose_name="Place to have a habit")

    habit_time_start = models.TimeField(auto_now=True, verbose_name="Timeset for a habit")

    habit_action= models.TextField(verbose_name="Action for a habit")

    habit_time_duration = models.PositiveSmallIntegerField(verbose_name="Timme duration for a habit")

    habit_is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.habit_name

    class Meta:
        verbose_name = "Habit"
        verbose_name_plural = "Habits"
