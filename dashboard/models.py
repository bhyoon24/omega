from django.db import models

# Create your models here.
class omegadbconn(models.Model):
    CUSTOM_CODE = models.CharField(max_length=20)
    CUSTOM_NAME = models.CharField(max_length=100)
    VAT_RATE = models.DecimalField(max_digits=5, decimal_places=2)
