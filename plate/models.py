from django.db import models

# Create your models here.
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Plate(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    tags = models.ManyToManyField("plate.Tag")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plate:detail", args=[self.pk])


class PlateImage(models.Model):
    image = models.ImageField(blank=True, upload_to="plate/%Y/%m/%d")
    plate = models.ForeignKey(Plate, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.plate.name, self.image.name)
