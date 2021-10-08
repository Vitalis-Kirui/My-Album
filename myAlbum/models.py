from django.db import models

# Create your models here.

#Location class model
class Location(models.Model):
    location_name = models.CharField(max_length=50)

    def __str__(self):
        return self.location_name

    class Meta:
        ordering = ['location_name']

#Category class model
class Category(models.Model):
    category_name = models.CharField(max_length=25)

    def __str__(self):
        return self.category_name