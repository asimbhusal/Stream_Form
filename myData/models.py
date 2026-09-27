from django.db import models

class Stream(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image=models.ImageField(default='fallback.png', blank=True, null=True)

def __str__(self):
    return self.name
