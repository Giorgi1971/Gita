from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pics')
    follow = models.ManyToManyField(User, related_name='follow', blank=True, null=True)
    followed = models.ManyToManyField(User, related_name='followed', blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username