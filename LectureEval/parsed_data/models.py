from django.db import models

# Create your models here.

class SearchData(models.Model):
    title = models.TextField()
    link = models.URLField()
    