from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login_page, name="login"),
    path('category', views.category, name="category"),
    path('category/<str:name>', views.categoryView, name="category_products"),
    path('category/<str:cname>/<str:pname>', views.product_details, name="product_details"),
]