from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', default='media/default_av.jpg')


class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True)


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
    

    # def save(self, *args, **kwargs):
    #     self.user.
    #     return super().save(args, kwargs)



