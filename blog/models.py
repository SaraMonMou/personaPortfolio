from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    imageSec = models.ImageField(upload_to='portfolio/images/', blank=True)


    def __str__(self):
        return self.title