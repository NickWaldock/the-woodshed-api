from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    headline = models.CharField(max_length=80)
    instrument = models.CharField(max_length=50)
    location = models.CharField(max_length=80)
    email = models.EmailField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../woodshed_media/profile-default_iqrrx0.png'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
