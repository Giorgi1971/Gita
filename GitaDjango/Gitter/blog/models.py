from statistics import mode
from django.db import models
from django.utils import timezone
from django.urls import reverse
from account.models import Author

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=any)
    title = models.CharField(max_length=124)
    text = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self) -> str:
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=any)
    author = models.ForeignKey(Author, on_delete=any)
    text = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.text

    # def get_absolute_url(self):
    #     return reverse('post_list')