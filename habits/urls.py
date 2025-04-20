from django.urls import path





from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitsListAPIView, HabitRetreiveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitsUserListAPIView, PublicAPIView, NiceHabitCreateAPIView, NiceHabitsListAPIView, \
    NiceHabitRetreiveAPIView, NiceHabitUpdateAPIView, NiceHabitDestroyAPIView

app_name = HabitsConfig.name



urlpatterns = [
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("habits/", HabitsListAPIView.as_view(), name="habits-list"),
    path("user/habits/", HabitsUserListAPIView.as_view(), name="habits-user-list"),

    path("habit/<int:pk>/", HabitRetreiveAPIView.as_view(), name="habit-detail"),
    path(
        "habit/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit-update"
    ),
    path(
        "habit/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit-delete"
    ),
    path("public/<int:pk>/", PublicAPIView.as_view(), name="public-habit"),

    # paths for CRUD nive_habit
    path("nice_habit/create/", NiceHabitCreateAPIView.as_view(), name="nice-habit-create"),
    path("nice_habits/", NiceHabitsListAPIView.as_view(), name="nice-habits-list"),

    path("nice_habit/<int:pk>/", NiceHabitRetreiveAPIView.as_view(), name="nice-habit-detail"),
    path(
        "nice_habit/update/<int:pk>/", NiceHabitUpdateAPIView.as_view(), name="nice-habit-update"
    ),
    path(
        "nice_habit/delete/<int:pk>/", NiceHabitDestroyAPIView.as_view(), name="nice-habit-delete"
    ),
]
