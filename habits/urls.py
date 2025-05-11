from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitsListAPIView, HabitRetreiveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitsUserListAPIView, PublicAPIView

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

]
