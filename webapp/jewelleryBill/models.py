from django.db import models

# Create your models here.
class CustomersInfo(models.Model):
    name = models.CharField(max_length = 30)
    phoneNumber = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)

class BillForm(models.Model):
    itemName = models.CharField(max_length = 30)
    itemType = models.CharField(max_length = 30)
    Rate = models.DecimalField(decimal_places=5,max_digits=9)
    grossWeight = models.DecimalField(decimal_places=3,max_digits=6)
    netWeight = models.DecimalField(decimal_places=3,max_digits=6)
    making = models.DecimalField(decimal_places=0,max_digits=5)
    otherCharges = models.CharField(max_length = 30)
    otherChargesAmount = models.DecimalField(decimal_places=0,max_digits=5)
    discount = models.DecimalField(decimal_places=0,max_digits=5)
     
    



