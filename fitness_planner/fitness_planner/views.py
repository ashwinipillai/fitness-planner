from django.http import  JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .models import WorkoutPlanExercise, WorkoutPlan, Exercise, WeightTracking, FitnessGoal
from .serializers import WorkoutPlanSerializer, ExerciseSerializer, \
    WorkoutPlanExerciseSerializer, WeightTrackingSerializer, UserSerializer, FitnessGoalSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create your views here.
class WorkoutPlanListView(generics.ListCreateAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]


class WorkoutPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]


class ExerciseListView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]


class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]


class WorkoutPlanExerciseListView(generics.ListCreateAPIView):
    queryset = WorkoutPlanExercise.objects.all()
    serializer_class = WorkoutPlanExerciseSerializer
    permission_classes = [IsAuthenticated]


class WorkoutPlanExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanExerciseSerializer
    permission_classes = [IsAuthenticated]


class WeightTrackingListView(generics.ListCreateAPIView):
    queryset = WeightTracking.objects.all()
    serializer_class = WeightTrackingSerializer
    permission_classes = [IsAuthenticated]


class WeightTrackingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeightTracking.objects.all()
    serializer_class = WeightTrackingSerializer
    permission_classes = [IsAuthenticated]


class FitnessGoalListView(generics.ListCreateAPIView):
    queryset = FitnessGoal.objects.all()
    serializer_class = FitnessGoalSerializer
    permission_classes = [IsAuthenticated]


class FitnessGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FitnessGoal.objects.all()
    serializer_class = FitnessGoalSerializer
    permission_classes = [IsAuthenticated]


class UserDetailAPIView(APIView):

    def get(self, request, pk):
        weight_trackings = WeightTracking.objects.filter(user_id=pk)
        fitness_goals = FitnessGoal.objects.filter(user_id=pk)

        weight_tracking_serializer = WeightTrackingSerializer(weight_trackings, many=True)
        fitness_goal_serializer = FitnessGoalSerializer(fitness_goals, many=True)

        user_details = {
            'weight_tracking': weight_tracking_serializer.data,
            'fitness_goals': fitness_goal_serializer.data,
            # Add other related data here
        }

        return JsonResponse(user_details)
