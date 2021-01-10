from django.db import models

# Create your models here.
class DetailsModal(models.Model):
    full_name = models.CharField(max_length=100)
    eAdress = models.EmailField(unique=True)
    Subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)