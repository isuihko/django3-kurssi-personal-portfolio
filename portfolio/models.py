from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images') # folder name
    url = models.URLField(blank=True) # blank means that we can add anything

    def __str__(self): # determines how default name is shown
        return self.title
