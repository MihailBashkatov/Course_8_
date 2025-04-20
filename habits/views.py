from django.http import HttpResponseForbidden
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from habits.models import Habit, NiceHabit
from habits.paginators import MyPagination
from habits.permissions import IsOwner, IsOwnerNiceHabit
from habits.serializers import HabitSerializer, NiceHabitSerializer


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
            "You do not have permission to change a status of public availavility"
        )























class NiceHabitCreateAPIView(generics.CreateAPIView):
    """View to create a NiceHabit"""

    serializer_class = NiceHabitSerializer
    permission_classes = [IsOwnerNiceHabit, IsAuthenticated]

    def perform_create(self, serializer):
        """Adding logic to get user, who is creating a NiceHabit"""
        serializer.save(nice_habit_user=self.request.user)


class NiceHabitsListAPIView(generics.ListAPIView):
    """View to create a list of public NiceHabits"""

    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    permission_classes = [
        IsAuthenticated,
    ]  # an access for all users
    pagination_class = MyPagination

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = NiceHabit.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = NiceHabitSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)





class NiceHabitRetreiveAPIView(generics.RetrieveAPIView):
    """View to get a particular NiceHabit for the user"""

    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerNiceHabit]  # an access only for user


#
#
class NiceHabitUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular NiceHabit for the user"""

    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerNiceHabit]  # an access only for user


class NiceHabitDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular NiceHabit for the user"""

    queryset = NiceHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerNiceHabit]  # an access only for user





# class PublicAPIView(APIView):
#     serializer_class = NiceHabitSerializer
#     queryset = NiceHabit.objects.all()
#
#     def post(self, request, pk):
#         """View to make the NiceHabit publicly available or unavailable only for the user of the habbit."""
#
#         message = ""
#         if NiceHabit.objects.filter(
#             pk=pk, nice_habit_user=self.request.user
#         ).exists():  # In case if NiceHabit belongs to particular user
#
#             NiceHabit = get_object_or_404(
#                 NiceHabit, id=pk
#             )  # get a particular NiceHabit via request

        #     if NiceHabit.NiceHabit_is_public:
        #         NiceHabit.NiceHabit_is_public = False
        #         NiceHabit.save()
        #         message = "NiceHabit is deleted"
        #
        #     elif not NiceHabit.NiceHabit_is_public:
        #         NiceHabit.NiceHabit_is_public = True
        #         NiceHabit.save()
        #         message = "NiceHabit is added "
        #
        #     return Response({"message": {message}}, status=status.HTTP_201_CREATED)
        # return HttpResponseForbidden(
        #     "You do not have permission to change a status of nice habit"
        # )