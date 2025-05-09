from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitsListAPIView, HabitRetreiveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitsUserListAPIView, PublicAPIView, NiceHabitAPIView, HabitRewardAPIView, \
    StartHabitUpdateAPIView

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


    # paths tpo activate and deactivate habit reward and nice habits

    # path("nice_habit_status/<int:pk>/", NiceHabitAPIView.as_view(), name="nice_habit-status"),
    # path("reward_habit_status/<int:pk>/", HabitRewardAPIView.as_view(), name="reward_habit-status"),
    #
    # path("habit_started/<int:pk>/", StartHabitUpdateAPIView.as_view(), name="habit-started"),



]
