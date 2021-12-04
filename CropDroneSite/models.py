from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GPSData(models.Model):
    # user_name = models.CharField(max_length=100)
    X_Coords = models.DecimalField(max_digits=9, decimal_places=6)
    Y_Coords = models.DecimalField(max_digits=9, decimal_places=6)
    img = models.ImageField(upload_to = 'DB Pictures') #!This needs work, check django doc to work with API model
    desc = models.TextField(null = True), 


