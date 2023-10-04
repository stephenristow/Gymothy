from django.urls import path

from . import views

app_name = "exercise_logs"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:workout_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    #path("<int:workout_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:workout_id>/set/", views.addset, name="set"),
]