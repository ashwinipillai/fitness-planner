from rest_framework import serializers
from .models import WorkoutPlanExercise, WorkoutPlan, Exercise, WeightTracking


class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlanExercise
        fields = '__all__'


class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class WeightTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightTracking
        fields = '__all__'
