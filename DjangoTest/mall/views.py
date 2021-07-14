from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Comment
from user.models import User, Order
# Create your views here.

def home(request) : 
    products = Product.objects.all
    return render(request, 'home.html', {'products': products})

# 상품 등록 
def create(request) : 
    if request.method == "POST" :
        new_product = Product()
        new_product.product_name = request.POST['product_name']
        new_product.product_info = request.POST['product_info']
        new_product.product_img = request.FILES.get('product_img')
        # new_product.product_orderd = user
        new_product.save()
        return redirect('home')
    else : 
        return render(request, 'create.html')

def detail(request, id):
    product = get_object_or_404(Product, id = id)
    return render(request, 'detail.html', {'product' : product})

def update(request):
    return render(request, 'update.html')

def delete(request, id) : 
    delete_product = Product.objects.get(id = id)
    delete_product.delete()
    return redirect('home')

# 주문하기 버튼 누르면 이 함수가 실행 . 
def order(request, id) : 
    # 해당 product 객체를 가져온다.
    product = get_object_or_404(Product, id = id)
    # 새로운 order 
    new_order = Order()
    # 현재 user 정보 가져오기 
    user_id = request.user.id
    user = User.objects.get(id = user_id)
    # 새로운 order 채우기 
    new_order.order_user = user
    new_order.order_product = product
    # 상품 객체 저장 
    new_order.save() 
    return redirect('home')

def order_list(request) : 
    # Order 객체 전부 가져오기 
    list = Order.objects.all()
    # 이 유저에 해당하는 객체만 list 에 저장. 
    list = list.filter(order_user = request.user.id)
    # 모든 상품 객체 가져오기 
    products = Product.objects.all()
    # for 문을 돌면서 이 유저가 가지고 있는 상품만 return 
    for user_product in list : 
        for product in products : 
            if user_product == product : 
                print(product.product_name)
    # product_list = list.filter(order_product = request.user.id)
    return render(request, 'order_list.html')