from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

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
    permission_classes = [IsAuthenticated, ]  # an access for all users
    pagination_class = MyPagination



    def get(self, request, **kwargs):
        """ Adding logic for pagination"""
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
        """ Adding logic for pagination"""
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


#
#
class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]  # an access only for user


#
#
# class SubscribeAPIView(APIView):
#     serializer_class = SubscriptionSerializer
#     queryset = Subscription.objects.all()
#
#     def post(self, request):
#         user = request.user
#         course_id = request.data.get("course")
#         course = get_object_or_404(Course, id=course_id)
#
#         subscription, created = Subscription.objects.get_or_create(
#             user=user, course=course
#         )
#
#         if subscription.subscription == False:
#             subscription.subscription = True
#             subscription.save()
#             message = "Subscription Added"
#
#         elif subscription.subscription == True:
#             subscription.subscription = False
#             subscription.save()
#             message = "Subscription Deleted"
#
#         return Response({"message": {message}}, status=status.HTTP_201_CREATED)
#
#     def get(self, request):
#         user = request.user
#         subscriptions = Subscription.objects.filter(user=user)
#         serializer = SubscriptionSerializer(subscriptions, many=True)
#         return Response(serializer.data)
