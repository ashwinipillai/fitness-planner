from rest_framework import generics
from .models import WorkoutPlanExercise, WorkoutPlan, Exercise, WeightTracking
from .serializers import WorkoutPlanSerializer, ExerciseSerializer, \
    WorkoutPlanExerciseSerializer, WeightTrackingSerializer


# Create your views here.
class WorkoutPlanListView(generics.ListCreateAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer


class WorkoutPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer


class ExerciseListView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer



class WorkoutPlanExerciseListView(generics.ListCreateAPIView):
    queryset = WorkoutPlanExercise.objects.all()
    serializer_class = WorkoutPlanExerciseSerializer


class WorkoutPlanExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanExerciseSerializer


class WeightTrackingListView(generics.ListCreateAPIView):
    queryset = WeightTracking.objects.all()
    serializer_class = WeightTrackingSerializer


class WeightTrackingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeightTracking.objects.all()
    serializer_class = WeightTrackingSerializer
