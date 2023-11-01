from django.db import models

from exercise.models import Exercise
from django.contrib.auth.models import User

from django.urls import reverse

from django.utils.text import slugify

class Tag(models.Model):
    title = models.CharField(max_length=75, verbose_name='Tag')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural='Tags'
    
    #def get_absolute_url(self):
    #    return reverse('tags', args=[self.slug])
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    

class Set(models.Model):
    #Foreign Keys
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #Tags
    tags = models.ManyToManyField(Tag, related_name='tags')

    #Weight, Weight Type, Reps
    weight_num = models.IntegerField(default=0)
    weight_type = models.CharField(default="lb",max_length=200)
    rep_num = models.IntegerField(default=10)