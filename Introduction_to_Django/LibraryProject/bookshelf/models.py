from django.db import models

#Models
class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()