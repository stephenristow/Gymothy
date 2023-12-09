from django.db import models

from exercise.models import Exercise
from django.contrib.auth.models import User
    

class Set(models.Model):
    #Foreign Keys
    exercise = models.ForeignKey(Exercise, related_name='exercises', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #DateTime for ordering
    set_time = models.DateTimeField("date of set", auto_now_add=True)

    #Weight, Weight Type, Reps
    weight_num = models.IntegerField(default=0)
    weight_type = models.CharField(default="lb",max_length=200)
    rep_num = models.IntegerField(default=10)