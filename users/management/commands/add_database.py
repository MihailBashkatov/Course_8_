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
            habit_name="Running",
            habit_user=user_1,
            habit_place="street",
            habit_action="Run",
            habit_date="2025-05-14 22:00",
            habit_time_duration=100,
            is_nice_habit=True,
        )
        habit_jump, _ = Habit.objects.get_or_create(
            habit_name="Jumping",
            habit_user=user_1,
            habit_place="street",
            habit_action="Jump",
            habit_date="2025-05-11 20:00",
            habit_time_duration=58,
            habit_period=2,
        )
        habit_swim, _ = Habit.objects.get_or_create(
            habit_name="Swimming",
            habit_user=user_2,
            habit_place="pool",
            habit_action="Swim",
            habit_date="2025-05-11 01:00",
            habit_time_duration=70,
            habit_period=5,
        )

        habit_sleep, _ = Habit.objects.get_or_create(
            habit_name="Sleeping",
            habit_user=user_2,
            habit_place="home",
            habit_action="Sleep",
            habit_date="2025-05-15 06:00",
            habit_is_public=True,
            habit_time_duration=120,
            habit_period=3,
        )

        habit_read, _ = Habit.objects.get_or_create(
            habit_name="Reading",
            habit_user=user_2,
            habit_place="home",
            habit_action="Read",
            habit_date="2025-05-12 07:00",
            habit_time_duration=30,
            habit_period=7,
            habit_reward="Go sleep",
        )
        habit_study, _ = Habit.objects.get_or_create(
            habit_name="Studying",
            habit_user=user_3,
            habit_place="School",
            habit_action="Study",
            habit_date="2025-05-11 15:00",
            habit_time_duration=100,
            habit_reward="Apple juice",
        )
        habit_music, _ = Habit.objects.get_or_create(
            habit_name="Listening music",
            habit_user=user_3,
            habit_place="home",
            habit_action="Sleep",
            habit_date="2025-05-15 06:00",
            habit_is_public=True,
            habit_time_duration=120,
            is_nice_habit=True,
        )

        # Creating related habit running for the initial habit Jumping
        habit_running = Habit.objects.get(habit_name="Running")
        habit_jumping = Habit.objects.get(habit_name="Jumping")
        habit_jumping.related_habit = habit_running
        habit_jumping.save()

        self.stdout.write(
            self.style.SUCCESS(f"Successfully added 3 test Users and 7 test habits")
        ),
