from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50, null = True,)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=True)
    date= models.DateField()
    isActive = models.BooleanField()