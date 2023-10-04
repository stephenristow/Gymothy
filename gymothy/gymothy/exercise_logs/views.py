from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Exercise, Workout

def index(request):
    latest_workout_list = Workout.objects.order_by("-workout_date")[:5]
    context = {"latest_workout_list": latest_workout_list}
    #output = ", ".join([e.workout_text for e in latest_workout_list])
    return render(request, "exercise_logs/index.html", context)

def detail(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    return render(request, "exercise_logs/detail.html", {"workout": workout})


# def results(request, workout_id):
#     response = "You're looking at the results of workout %s."
#     return HttpResponse(response % workout_id)


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