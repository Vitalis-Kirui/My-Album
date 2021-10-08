from django.db import models

# Create your models here.

#Location class model
class Location(models.Model):
    """
    Location class for creating our location instances
    """
    location_name = models.CharField(max_length=50)

    def __str__(self):
        return self.location_name

    class Meta:
        ordering = ['location_name']

#Category class model
class Category(models.Model):
    """
    Category class for creating our categories instances
    """
    category_name = models.CharField(max_length=25)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete() 

#Image class model
class Image(models.Model):
    """
    Image class for creating our image instances
    """
    image = models.ImageField(upload_to = 'images/')
    image_name =models.CharField(max_length=100)
    image_details =models.TextField()
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image_location = models.ForeignKey(Location ,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name