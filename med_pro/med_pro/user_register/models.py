from django.db import models

# Create your models here.

class Register(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, primary_key=True)
    store_name= models.CharField(max_length=250)
    address = models.TextField(max_length=1000)
    gst_no = models.CharField(max_length= 50)
    telephone = models.CharField(max_length=25, unique=True)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=85)
    password = models.CharField(max_length=4)

    def __str__(self):
        return self.email
