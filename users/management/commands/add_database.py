from django.core.management import BaseCommand

from habits.models import Habit
from users.models import User
from users.utils import create_user


class Command(BaseCommand):
    help = "Add test habits to the database"

    def handle(self, *args, **kwargs):
        # Delete Data from database
        User.objects.all().delete()
        Habit.objects.all().delete()


        create_user()  # Creating users in database

        user_1 = User.objects.get(email="user1@user.com")
        user_2 = User.objects.get(email="user2@user.com")
        user_3 = User.objects.get(email="user3@user.com")




        habit_run, _ = Habit.objects.get_or_create(
            habit_name="Running", habit_user=user_1, habit_place='street', habit_action="Run", habit_time_duration=2
        )
        habit_jump, _ = Habit.objects.get_or_create(
            habit_name="Jumping", habit_user=user_1, habit_place='street', habit_action="Jump", habit_time_duration=2
        )
        habit_swim, _ = Habit.objects.get_or_create(
            habit_name="Swimming", habit_user=user_2, habit_place='pool', habit_action="Swim", habit_time_duration=2
        )

        habit_sleep, _ = Habit.objects.get_or_create(
            habit_name="Sleeping", habit_user=user_2, habit_place='home', habit_action="Sleep", habit_is_public=True, habit_time_duration=2
        )

        habit_read, _ = Habit.objects.get_or_create(
            habit_name="Reading", habit_user=user_2, habit_place='home', habit_action="Read", habit_time_duration=2
        )
        habit_study, _ = Habit.objects.get_or_create(
            habit_name="Studying", habit_user=user_3, habit_place='School', habit_action="Study", habit_time_duration=2
        )





        self.stdout.write(
            self.style.SUCCESS(f"Successfully added 3 test Users and 5 test habits")
        ),
