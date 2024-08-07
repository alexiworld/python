from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField() # unrestricted in length text
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # what to do with the post if the user is deleted

    # after creating this file run
    #   python3 manage.py makemigrations
    #   python3 manage.py sqlmigrate blog 0001
    # make sure 0001 is the number received in the first step
    #   python3 manage.py migrate

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})