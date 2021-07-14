"""shoppingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mall import views as M 
from user import views as U

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', M.home, name="home"),
    path('mall/create', M.create, name="create"),
    path('mall/detail/<str:id>', M.detail, name="detail"),
    path('mall/update', M.update, name="update"),
    path('mall/delete/<str:id>', M.delete, name="delete"),
    path('mall/order/<str:id>', M.order, name="order"),
    path('mall/order_list', M.order_list, name="order_list"),
    path('user/user_login', U.user_login, name="user_login"),
    path("user/user_signup", U.user_signup, name="user_signup"),
    path("user/user_logout", U.user_logout, name="user_logout"),
    path("user/mypage", U.mypage, name="mypage"),
] + static (settings.MEDIA_URL, document_root  = settings.MEDIA_ROOT)
