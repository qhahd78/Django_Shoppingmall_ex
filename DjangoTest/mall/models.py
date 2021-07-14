from django.db import models

# Create your models here.

class Product(models.Model) : 
    product_name = models.CharField(max_length=50)
    product_info = models.TextField()
    product_img = models.ImageField(upload_to = "mall/", null=True)

    def __str__(self) : 
        return self.product_name

class Comment(models.Model) : 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    writer = models.ForeignKey('user.User',on_delete=models.CASCADE)
    date = models.DateTimeField()
    content = models.TextField()

    def __str__(self) : 
        return self.content    