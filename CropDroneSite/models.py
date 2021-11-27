from django.db import models

# Create your models here.

class GPSData:
    X_Coords: models.BigIntegerField()
    Y_Coords: models.BigIntegerField()
    img: models.ImageField() #!This needs work, check django doc to work with API model
    desc: models.TextField()
    