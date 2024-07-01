from django.db import models

class Car(models.Model):
    name = models.CharField(max_length = 255)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    yearMfct = models.IntegerField()
    trimlevel = models.CharField(max_length=255)
    locallyAvailable = models.BooleanField(default=False)
    # image = models.ImageField(
    #     upload_to='path/to/upload/directory/', blank=True, null=True)
    fueltype = models.CharField(max_length=255, blank=True, null=True)
    drivetype = models.CharField(max_length=255, blank=True, null=True)
    transmission = models.CharField(max_length=255, blank=True, null=True)
    enginesize = models.CharField(max_length=255, blank=True, null=True)
    currentlocation = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.make} - {self.model}"


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_images')
    image = models.ImageField(upload_to='car_images/',blank=True,null=True)
