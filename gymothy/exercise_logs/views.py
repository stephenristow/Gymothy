from typing import Any

from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
#from django.views import generic
from django.template import loader

#Users
from django.contrib.auth.models import User

#Forms and Models
from .forms import WorkoutForm#, ExerciseForm
from exercise.forms import ExerciseForm
from .models import Workout, Stream
from exercise.models import Exercise

@login_required
def index(request):
    user = request.user
    workouts = Stream.objects.filter(user=user)

    group_ids = []

    for workout in workouts:
        group_ids.append(workout.workout_id)
    
    workout_items = Workout.objects.filter(id__in=group_ids).all().order_by('-workout_date')

    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = user
            workout.save()
            return HttpResponseRedirect(reverse("exercise_logs:detail", args=(workout.id,)))
    else:
        form = WorkoutForm()


    template = loader.get_template("exercise_logs/index.html")

    context = {
        'form': form,
        'workout_items': workout_items,
        
    }
    return HttpResponse(template.render(context, request))

@login_required
def my_workouts(request):
    user = request.user
    workouts = Stream.objects.filter(user=user)

    group_ids = []

    for workout in workouts:
        group_ids.append(workout.workout_id)
    
    workout_items = Workout.objects.filter(id__in=workouts).all().order_by('-workout_date')

    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = user
            workout.save()
            return HttpResponseRedirect(reverse("exercise_logs:detail", args=(workout.id,)))
    else:
        form = WorkoutForm()


    template = loader.get_template("exercise_logs/index.html")

    context = {
        'form': form,
        'workout_items': workout_items,
        
    }
    return HttpResponse(template.render(context, request))

# class IndexView(generic.ListView):
#     template_name = "exercise_logs/index.html"
#     context_object_name = "latest_workout_list"

#     def get_queryset(self):
#         #Return workest in order by workout_date
#         return Workout.objects.order_by("-workout_date")

@login_required
def WorkoutDetails(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    user = request.user
    exercises = Exercise.objects.filter(workout=workout).order_by('exercise_date')

    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.workout = workout
            exercise.user = user
            exercise.save()
            return HttpResponseRedirect(reverse("exercise_logs:detail", args=(workout.id,)))
    else:
        form = ExerciseForm()


    template = loader.get_template("exercise_logs/detail.html")

    context = {
        'workout': workout,
        'form': form,
        'exercises': exercises,
        
    }
    return HttpResponse(template.render(context, request))


# class ExerciseView(generic.DetailView):
#     model = Exercise
#     template_name = "exercise_logs/exercise.html"

@login_required
def new_workout(request):
    user = request.user
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = user
            workout.save()
            return HttpResponseRedirect(reverse("exercise_logs:detail", args=(workout.id,)))
    else:
        form = WorkoutForm()

    template = loader.get_template("exercise_logs/new_workout.html")

    context = {
        'form': form,
        
    }
    return HttpResponse(template.render(context, request))

#render(request, "exercise_logs/new_workout.html", {"workout": workout})

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


