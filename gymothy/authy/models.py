from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	height = models.IntegerField(default=170, null=True, blank=True)
	weight = models.IntegerField(default=62, null=True, blank=True)
	url = models.CharField(max_length=80, null=True, blank=True)
	created = models.DateField(auto_now_add=True)
	picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True, verbose_name='Picture')
		

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)