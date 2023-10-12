import datetime

from django.db import models
from django.utils import timezone


class Workout(models.Model):
    workout_text = models.CharField(max_length=200)
    workout_date = models.DateTimeField("date of workout", auto_now_add=True)
    def __str__(self):
        return self.workout_text
    
    def was_done_recently(self):
        return self.workout_date >= timezone.now() - datetime.timedelta(days=1)


# class Set(models.Model):
#     exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
#     weight_num = models.IntegerField(default=0)
#     weight_type = models.CharField(max_length=200)
#     set_num = models.IntegerField(default=1)
#     rep_num = models.IntegerField(default=10)