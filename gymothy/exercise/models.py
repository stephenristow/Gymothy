from django.db import models
from exercise_logs.models import Workout
from django.contrib.auth.models import User

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_text = models.CharField(max_length=200)
    exercise_date = models.DateTimeField("date of exercise", auto_now_add=True)

    #weights, sets & reps
    weight_num = models.IntegerField(default=0)
    weight_type = models.CharField(default="lb",max_length=200)
    set_num = models.IntegerField(default=1)
    rep_num = models.IntegerField(default=10)
    
    def __str__(self):
        return self.exercise_text

