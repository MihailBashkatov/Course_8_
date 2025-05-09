import datetime

from django.http import HttpResponseForbidden
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from habits.models import Habit
from habits.paginators import MyPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer




class HabitCreateAPIView(generics.CreateAPIView):
    """View to create a habit"""

    serializer_class = HabitSerializer
    permission_classes = [IsOwner, IsAuthenticated]

    def perform_create(self, serializer):
        """Adding logic to get user, who is creating a habit"""
        serializer.save(habit_user=self.request.user)


class HabitsListAPIView(generics.ListAPIView):
    """View to create a list of public habits"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(habit_is_public=True)
    permission_classes = [
        IsAuthenticated,
    ]  # an access for all users
    pagination_class = MyPagination

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = Habit.objects.filter(habit_is_public=True)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = HabitSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class HabitsUserListAPIView(generics.ListAPIView):
    """View to create a list of habits for particular user"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
    pagination_class = MyPagination

    def get_queryset(self):

        return Habit.objects.filter(habit_user=self.request.user)

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = Habit.objects.filter(habit_user=self.request.user)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = HabitSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class HabitRetreiveAPIView(generics.RetrieveAPIView):
    """View to get a particular habit for the user"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]  # an access only for user


#
#
class HabitUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular habit for the user"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]  # an access only for user


class HabitDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular habit for the user"""

    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]  # an access only for user


class PublicAPIView(APIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def post(self, request, pk):
        """View to make the habit publicly available or unavailable only for the user of the habbit."""

        message = ""
        if Habit.objects.filter(
            pk=pk, habit_user=self.request.user
        ).exists():  # In case if habit belongs to particular user

            habit = get_object_or_404(
                Habit, id=pk
            )  # get a particular habit via request

            if habit.habit_is_public:
                habit.habit_is_public = False
                habit.save()
                message = "Habit is not public anymore"

            elif not habit.habit_is_public:
                habit.habit_is_public = True
                habit.save()
                message = "Habit is publicly available now"

            return Response({"message": {message}}, status=status.HTTP_201_CREATED)
        return HttpResponseForbidden(
            "You do not have permission to change a status of public availability"
        )


class NiceHabitAPIView(APIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def post(self, request, pk):
        """View to make the NiceHabit publicly available or unavailable only for the user of the habbit."""

        message = ""
        if Habit.objects.filter(
            pk=pk, habit_user=self.request.user
        ).exists():  # In case if NiceHabit belongs to particular user

            habit = get_object_or_404(
                Habit, id=pk
            )  # get a particular NiceHabit via request

            if habit.is_nice_habit:
                habit.is_nice_habit = False
                habit.save()
                message = "Nice Habit is deleted"

            elif (
                not habit.is_nice_habit
                and not habit.is_habit_reward
                and habit.nice_habit_name
            ):
                habit.is_nice_habit = True
                habit.save()
                message = "Nice Habit is added"

            elif (
                not habit.is_nice_habit
                and not habit.is_habit_reward
                and not habit.nice_habit_name
            ):
                return HttpResponseForbidden(
                    "Not possible to activate Nice Habit, because no Nice Habit name"
                )

            elif not habit.is_nice_habit and habit.is_habit_reward:
                return HttpResponseForbidden(
                    "Not possible to activate Nice Habit, because reward is granted"
                )

            return Response({"message": {message}}, status=status.HTTP_201_CREATED)
        return HttpResponseForbidden(
            "You do not have permission to change a status of nice habit"
        )


class HabitRewardAPIView(APIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def post(self, request, pk):
        """View to make the Habit Reward  available or unavailable only for the user of the habbit."""

        message = ""
        if Habit.objects.filter(
            pk=pk, habit_user=self.request.user
        ).exists():  # In case if Habit belongs to particular user

            habit = get_object_or_404(
                Habit, id=pk
            )  # get a particular Habit via request

            if habit.is_habit_reward:
                habit.is_habit_reward = False
                habit.save()
                message = "Reward is deleted"

            elif (
                not habit.is_habit_reward
                and not habit.is_nice_habit
                and habit.habit_reward
            ):
                habit.is_habit_reward = True
                habit.save()
                message = "Reward is added"

            elif (
                not habit.is_nice_habit
                and not habit.is_habit_reward
                and not habit.habit_reward
            ):
                return HttpResponseForbidden(
                    "Not possible to activate Reward Habit, because no Reward Habit name"
                )

            elif not habit.is_habit_reward and habit.is_nice_habit:
                return HttpResponseForbidden(
                    "Not possible to add a reward, because nice habit is activated"
                )

            return Response({"message": {message}}, status=status.HTTP_201_CREATED)
        return HttpResponseForbidden(
            "You do not have permission to change a status of habit reward"
        )



class StartHabitAPIView(APIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # print(serializer_class)

    def post(self, request, pk):
        """View to make the Habit Reward  available or unavailable only for the user of the habbit."""

        message = ""
        if Habit.objects.filter(
                pk=pk, habit_user=self.request.user
        ).exists():  # In case if Habit belongs to particular user

            habit = get_object_or_404(
                Habit, id=pk
            )  # get a particular Habit via request

            if not habit.is_habit_started:
                habit.is_habit_started = True
                habit_started = datetime.datetime.now().strftime("%H:%M:%S") # gets current time
                habit.habit_time_start = habit_started
                habit.save()
                message = f"Habit {habit.habit_name} is started"

            else:
                message = f"Habit {habit.habit_name} is ongoing"

            return Response({"message": {message}}, status=status.HTTP_201_CREATED)
        return HttpResponseForbidden(
            "You do not have permission to change a status of habit reward"
        )

class StartHabitUpdateAPIView(generics.UpdateAPIView):
        """View to update a particular habit for the user"""

        serializer_class = HabitSerializer
        queryset = Habit.objects.all()
        permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
        #
        def patch(self, request, pk=None, *args, **kwargs):
            if Habit.objects.filter(
                    pk=pk, habit_user=self.request.user
            ).exists():  # In case if Habit belongs to particular user

                habit = get_object_or_404(
                    Habit, id=pk
                )  # get a particular Habit via request

                if not habit.is_habit_started:
                    habit.is_habit_started = True

                    # Initializing a date and time
                    date_and_time = datetime.datetime.now()

                    print("Original time:")
                    print(f'AAA{type(date_and_time)}')

                    # Calling the timedelta() function
                    time_change = datetime.timedelta(minutes=75)
                    print(type(time_change))
                    new_time = date_and_time + time_change

                    # Printing the new datetime object
                    print("changed time:")
                    print(type(new_time))

                    habit_started = datetime.datetime.now() # gets current time
                    habit.date_and_time = habit_started
                    habit.save()

                else:
                    message = f"Habit {habit.habit_name} is ongoing"
                    return Response({"message": {message}}, status=status.HTTP_201_CREATED)
            return self.partial_update(request,  *args, **kwargs)

        # def post(self, request, pk):
        #     """View to make the Habit Reward  available or unavailable only for the user of the habbit."""
        #
        #     message = ""
        #     if Habit.objects.filter(
        #             pk=pk, habit_user=self.request.user
        #     ).exists():  # In case if Habit belongs to particular user
        #
        #         habit = get_object_or_404(
        #             Habit, id=pk
        #         )  # get a particular Habit via request
        #
        #         if not habit.is_habit_started:
        #             habit.is_habit_started = True
        #             habit_started = datetime.datetime.now().strftime("%H:%M:%S")  # gets current time
        #             habit.habit_time_start = habit_started
        #             habit.save()
        #             message = f"Habit {habit.habit_name} is started"
        #
        #         else:
        #             message = f"Habit {habit.habit_name} is ongoing"
        #
        #         return Response({"message": {message}}, status=status.HTTP_201_CREATED)
        #     return HttpResponseForbidden(
        #         "You do not have permission to change a status of habit reward"
        #     )
