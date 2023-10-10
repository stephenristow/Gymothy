from typing import Any
from django.db.models.query import QuerySet
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from .forms import PostWorkout, PostExercise
from .models import Exercise, Workout

class IndexView(generic.ListView):
    template_name = "exercise_logs/index.html"
    context_object_name = "latest_workout_list"

    def get_queryset(self):
        #Return workest in order by workout_date
        return Workout.objects.order_by("-workout_date")

class DetailView(generic.DetailView):
    model = Workout
    template_name = "exercise_logs/detail.html"


class ExerciseView(generic.DetailView):
    model = Exercise
    template_name = "exercise_logs/exercise.html"


def new_workout(request):
    if request.method == "POST":
        workout = PostWorkout(request.POST)
        if workout.is_valid():
            workout.save()
            return redirect("exercise_logs")
    else:
        workout = PostWorkout()
    return render(request, "exercise_logs/new_workout.html", {"workout": workout})

# def add_exercise(request, workout_id):
#     exercise = get_object_or_404(Exercise, fk=workout_id)
#     if request.method == "POST":
#         exercise = PostExercise(request.POST)
#         if exercise.is_valid():
#             exercise.save()
#             return redirect("exercise_logs/{{workout_id}}.html")
#     else:
#         exercise = PostExercise()
#     return render(request, "exercise_logs/{{workout_id}}.html", {"exercise": exercise})

def addset(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    try:
        selected_exercise = workout.exercise_set.get(pk=request.POST["exercise"])
    except (KeyError, Exercise.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "exercise_logs/detail.html",
            {
                "Workout": workout,
                "error_message": "You didn't select an exercise.",
            },
        )
    else:
        selected_exercise.set_num += 1
        selected_exercise.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("exercise_logs:detail", args=(workout.id,)))
    #return HttpResponse("You're adding a set onto exercise %s." % exercise_id)


