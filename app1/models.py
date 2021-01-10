from django.db import models

# Create your models here.
class StudentModal(models.Model):
      s_f_name=models.CharField(max_length=30)
      s_l_name=models.CharField(max_length=30)
      email=models.EmailField(unique=True)
      mobile_no=models.IntegerField(unique=True)
      password=models.CharField(max_length=8)
      con_password=models.CharField(max_length=8)
