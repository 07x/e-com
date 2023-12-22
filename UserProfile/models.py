from django.db import models
from django.conf import settings
from django.dispatch import receiver

from django.db import models
from django.conf import settings

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,default=None,null=True,blank=True)
    last_name = models.CharField(max_length=100,default=None,null=True,blank=True)
    email = models.EmailField(max_length=100,default=None,null=True,blank=True,unique=True)

    def __str__(self):
        return str(self.first_name)
    


class Address(models.Model):
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,default='')
    home_address = models.CharField(max_length=200)
    bus_stop = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return str(self.home_address)







