# from Django_Shoppingmall_ex.DjangoTest.mall.models import Product
from django.db import models
from django.contrib.auth.models import AbstractUser
from mall.models import Product
# Create your models here.

class User(AbstractUser) : 
    university = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to="user/", null=True)

# order (주문내역 모델) 은 user 와 product 를 외래키로 갖습니다.
# (어떤 유저가 어떤 상품을 주문했는지 객체로 생성. ex) 하유민-청소기, 하유민-책 이런식으로 생깁니다.)
# 내 주문내역만 확인하는 부분은 views 에서 처리하도록 했으니 views 참고 필요
class Order(models.Model) :
    order_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self) : 
        return self.order_product.product_name