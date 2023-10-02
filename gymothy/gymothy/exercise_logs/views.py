from django.http import HttpResponse

from .models import Exercise, Workout

def index(request):
    latest_workout_list = Workout.objects.order_by("-workout_date")[:5]
    output = ", ".join([q.workout_text for q in latest_workout_list])
    return HttpResponse(output)

def detail(request, workout_id):
    return HttpResponse("You're looking at workout %s." % workout_id)


# def results(request, workout_id):
#     response = "You're looking at the results of workout %s."
#     return HttpResponse(response % workout_id)


def addset(request, exercise_id):
    return HttpResponse("You're adding a set onto exercise %s." % exercise_id)