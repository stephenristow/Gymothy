import datetime

#from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# from django.db.models.signals import post_save

# # USER

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     height = models.IntegerField(default=170, null=True, blank=True)
#     weight = models.IntegerField(default=62, null=True, blank=True)
#     url = models.CharField(max_length=50, null=True, blank=True)
#     created = models.DateField(auto_now_add=True)
#     picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True, verbose_name='Picture')


# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# post_save.connect(create_user_profile, sender=User)
# post_save.connect(save_user_profile, sender=User)

# WORKOUT

class Workout(models.Model):
    workout_text = models.CharField(max_length=200)
    workout_date = models.DateTimeField("date of workout", auto_now_add=True)
    def __str__(self):
        return self.workout_text
    
    def was_done_recently(self):
        return self.workout_date >= timezone.now() - datetime.timedelta(days=1)


