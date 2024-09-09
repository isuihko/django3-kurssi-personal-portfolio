from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self): # determines how default name is shown
        return f'{self.title} ({self.date})'