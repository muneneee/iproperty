from django.db import models
from cloudinary.models import CloudinaryField


class Property(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=40)
    description = models.TextField()
    location = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=12, decimal_places=2)


    def __str__(self):
        return f'{self.title}'