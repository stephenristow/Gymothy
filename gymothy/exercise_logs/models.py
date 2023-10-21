import datetime

#from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import uuid


from django.db.models.signals import post_save

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
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    workout_text = models.CharField(max_length=200)
    workout_date = models.DateTimeField("date of workout", default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.first().pk)

    def get_absolute_url(self):
        return reverse("exercise_logs:detail", kwargs={"workout_id": self.id})
    

    def __str__(self):
        return self.workout_text
    
    def was_done_recently(self):
        return self.workout_date >= timezone.now() - datetime.timedelta(days=1)


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

class Stream(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def add_workout(sender, instance, *args, **kwargs):
        workout = instance
        user = workout.user
        followers = Follow.objects.all().filter(following=user)
        for follower in followers:
            stream = Stream(workout=workout, user=follower.follower, date=workout.workout_date, following=user)
            stream.save()

post_save.connect(Stream.add_workout, sender=Workout)