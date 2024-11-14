from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date = models.DateField()