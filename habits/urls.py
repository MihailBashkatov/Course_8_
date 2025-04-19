from django.urls import path





from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitsListAPIView, HabitRetreiveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = HabitsConfig.name



urlpatterns = [
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("habits/", HabitsListAPIView.as_view(), name="habits-list"),
    path("habit/<int:pk>/", HabitRetreiveAPIView.as_view(), name="habit-detail"),
    path(
        "habit/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit-update"
    ),
    path(
        "habit/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit-delete"
    ),
    # path("subscription/", SubscribeAPIView.as_view(), name="subscription"),
]
