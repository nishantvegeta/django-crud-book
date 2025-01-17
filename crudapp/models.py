from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.title + ' ' + self.author

class School(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=25)

    def __str__(self):
        return self.name
