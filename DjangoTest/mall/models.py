from django.db import models

# Create your models here.

class Product(models.Model) : 
    product_name = models.CharField(max_length=50)
    product_info = models.TextField()
    product_img = models.ImageField(upload_to = "mall/", null=True)