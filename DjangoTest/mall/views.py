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

# 상품 상세 
def detail(request, id):
    product = get_object_or_404(Product, id = id)
    return render(request, 'detail.html', {'product' : product})

# 상품 수정
def update(request, id):
    if request.method == "POST" : 
        update_product = Product.objects.get(id = id)
        update_product.product_name = request.POST["product_name"]
        update_product.product_info = request.POST["product_info"]
        update_product.product_img = request.FILES.get('product_img')
        update_product.save()
        return redirect('detail', update_product.id)
    else : 
        product = Product.objects.get(id = id )
        return render(request, 'update.html', {'product' : product})

# 상품 삭제 
def delete(request, id) : 
    delete_product = Product.objects.get(id = id)
    delete_product.delete()
    return redirect('home')

# 주문 목록에 넣기 
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
    # order 객체 저장 
    new_order.save() 
    return redirect('home')

# 내 주문 내역 
def order_list(request) : 
    # Order 객체 전부 가져오기 
    list = Order.objects.all()
    # product 객체 전부 가져오기
    products = Product.objects.all()
    # 이 유저에 해당하는 객체만 list 에 저장. 
    list = list.filter(order_user = request.user.id)
    # for 문을 돌면서 이 유저가 가지고 있는 상품 result 에 저장 후 return
    result = []

    for i in list : 
        for j in products : 
            # 상품명으로 비교
            if str(i) == str(j) : 
                result.append(j)
                
    return render(request, 'order_list.html', {'result':result})