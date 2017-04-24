from django.db import models

# Create your models here

class Treasure(models.Model):

    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    img_url = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):

        return self.name