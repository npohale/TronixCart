from decimal import Clamped
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product (models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    product_desc=models.CharField(max_length=350)
    poduct_pub_date=models.DateField()
    

    

    
