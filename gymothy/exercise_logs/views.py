from typing import Any
from django.db.models.query import QuerySet
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.template import loader

from .forms import WorkoutForm#, ExerciseForm
from exercise.forms import ExerciseForm
from .models import Workout
from exercise.models import Exercise

class IndexView(generic.ListView):
    template_name = "exercise_logs/index.html"
    context_object_name = "latest_workout_list"

    def get_queryset(self):
        #Return workest in order by workout_date
        return Workout.objects.order_by("-workout_date")

def WorkoutDetails(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    user = request.user
    exercises = Exercise.objects.filter(workout=workout).order_by('exercise_date')

    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.workout = workout
            exercises.user = user
            exercise.save()
            return redirect("exercise_logs/{{workout_id}}.html")
    else:
        form = ExerciseForm()


    template = loader.get_template("exercise_logs/detail.html")

    context = {
        'workout': workout,
    }
    return HttpResponse(template.render(context, request))


# class ExerciseView(generic.DetailView):
#     model = Exercise
#     template_name = "exercise_logs/exercise.html"


def new_workout(request):
    if request.method == "POST":
        workout = WorkoutForm(request.POST)
        if workout.is_valid():
            workout.save()
            return redirect("exercise_logs")
    else:
        workout = WorkoutForm()
    return render(request, "exercise_logs/new_workout.html", {"workout": workout})

# def add_exercise(request, workout_id):
#     exercise = get_object_or_404(Exercise, fk=workout_id)
#     if request.method == "POST":
#         exercise = ExerciseForm(request.POST)
#         if exercise.is_valid():
#             exercise.save()
#             return redirect("exercise_logs/{{workout_id}}.html")
#     else:
#         exercise = ExerciseForm()
#     return render(request, "exercise_logs/{{workout_id}}.html", {"exercise": exercise})

# def addset(request, workout_id):
#     workout = get_object_or_404(Workout, pk=workout_id)
#     try:
#         selected_exercise = workout.exercise_set.get(pk=request.POST["exercise"])
#     except (KeyError, Exercise.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "exercise_logs/detail.html",
#             {
#                 "Workout": workout,
#                 "error_message": "You didn't select an exercise.",
#             },
#         )
#     else:
#         selected_exercise.set_num += 1
#         selected_exercise.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("exercise_logs:detail", args=(workout.id,)))
#     #return HttpResponse("You're adding a set onto exercise %s." % exercise_id)


