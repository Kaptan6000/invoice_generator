from django.db import models
import uuid
# Create your models here.
class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True,default=0)
    invoice_date = models.DateField()
    seller_name = models.CharField(max_length=50)
    seller_address = models.CharField(max_length=150, default="")
    seller_phone = models.CharField(max_length=50, default="")
    buyer_name = models.CharField(max_length=50)
    buyer_address = models.CharField(max_length=150, default="")
    buyer_phone = models.CharField(max_length=50, default="")
    totalproducts = models.IntegerField(default=1)
   
class Items(models.Model):
    items_id = models.AutoField
    items = models.CharField(max_length=200)  
    price = models.CharField(max_length=200)
    total = models.CharField(max_length=10)  