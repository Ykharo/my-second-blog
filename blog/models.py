from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author =models.ForeignKey('auth.User')
    title = models.CharField(max_length =200)
    text = models.TextField()
    created_date = models.DateTimeField( default=timezone.now())
    pubished_date = models.DateField(blank=True,null=True)
    
    def publish(self):
        self.pubished_date = timezone.now()
        self.save()
        
    def __srt__(self):
        return self.title