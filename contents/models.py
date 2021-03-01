from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    Services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='content_imgs')
    series = models.CharField(max_length=100, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    tags = models.ManyToManyField(Tag)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title