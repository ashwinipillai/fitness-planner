"""iproxy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin

from django.urls import path

from .views import *

from user import views

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', views.LoginAPIView.as_view(), name='login'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api/exercise/', ExerciseListView.as_view(), name='exercise-list'),
    path('api/exercise/<int:pk>/', ExerciseDetailView.as_view(), name='exercise-detail'),

    path('api/workout_plan_exercise/', WorkoutPlanExerciseListView.as_view(), name='workout-plan-exercise-list'),
    path('api/workout_plan_exercise/<int:pk>/', WorkoutPlanExerciseDetailView.as_view(),
         name='workout-plan-exercise-detail'),

    path('api/workout_plan/', WorkoutPlanListView.as_view(), name='workout-plan-list'),
    path('api/workout_plan/<int:pk>/', WorkoutPlanDetailView.as_view(), name='workout-plan-detail'),

    path('api/weight_tracking/', WeightTrackingListView.as_view(), name='weight-tracking-list'),
    path('api/weight_tracking/<int:pk>/', WeightTrackingDetailView.as_view(), name='weight-tracking-detail'),

    path('api/fitness_goal/', FitnessGoalListView.as_view(), name='fitness-goal-list'),
    path('api/fitness_goal/<int:pk>/', FitnessGoalDetailView.as_view(), name='fitness-goal-detail'),

    path('api/user_fitness_details/<int:pk>/', UserDetailAPIView.as_view(), name='user_fitness'),

    path('api/create_user/', UserListView.as_view(), name="create-user")
]
