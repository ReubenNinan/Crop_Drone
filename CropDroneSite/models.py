from django.db import models

# Create your models here.

class GPSData(models.Model):
    X_Coords = models.BigIntegerField()
    Y_Coords = models.BigIntegerField()
    img = models.ImageField(upload_to = 'DB Pictures') #!This needs work, check django doc to work with API model
    desc = models.TextField()
    