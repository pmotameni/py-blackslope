from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    release_date = models.DateField(null=True)
