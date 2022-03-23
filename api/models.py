from ast import mod
from os import link
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ["created"]
    

    def likes(self):
        return self.likes
    
    def __str__(self):
        return self.title