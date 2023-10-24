from django.urls import path

from . import views

app_name = "exercise_logs"
urlpatterns = [
    # ex: /exercise_logs/
    path("", views.index, name="index"),# ex: /exercise_logs/5/
    # /my_workouts/
    path("my_workouts", views.my_workouts, name="my_workouts"),
    # ex: /exercise_logs/5/
    path("<int:workout_id>/", views.WorkoutDetails, name="detail"),
    # ex: /exercise_logs/5/results/
    #path("<int:pk>/exercise/", views.ExerciseView.as_view(), name="exercise"),
    # ex: /exercise_logs/5/vote/
    #path("<int:workout_id>/set/", views.addset, name="set"),
    path("new_workout", views.new_workout, name="new_workout"),
]