from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver # Use to capturing reciever information. 
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.TextChoices):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True, 
        blank=True
    )
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User) # Whenever a user is saved, it is created in the UserProfile table
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
