from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if the user will be deleted then all his post althou will be deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self): # this method means after created a new post we will be redirect to 'post-detail'
    	return reverse('post-detail', kwargs={'pk': self.pk})




    
