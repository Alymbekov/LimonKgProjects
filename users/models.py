from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse



class Profile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='profiles')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', default='media/default_av.jpg')

    def __str__(self):
        return self.user.username
    
    @property
    def get_absolute_avatar_url(self):
        return f'{self.avatar.url}'
    


class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.profiles.pk})
    

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profiles.save()
    

    # def save(self, *args, **kwargs):
    #     self.user.
    #     return super().save(args, kwargs)



