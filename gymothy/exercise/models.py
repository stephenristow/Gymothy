from django.db import models
from exercise_logs.models import Workout
from django.contrib.auth.models import User
from django.urls import reverse

from django.utils.text import slugify

class Tag(models.Model):
    title = models.CharField(max_length=75, verbose_name='Tag')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural='Tags'
    
    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_text = models.CharField(max_length=200)
    exercise_date = models.DateTimeField("date of exercise", auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='tags')

    #weights, sets & reps
    weight_num = models.IntegerField(default=0)
    weight_type = models.CharField(default="lb",max_length=200)
    set_num = models.IntegerField(default=1)
    rep_num = models.IntegerField(default=10)
    
    def __str__(self):
        return self.exercise_text

