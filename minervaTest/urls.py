"""minervaTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from minervaTest import create, category, customer, order, product

urlpatterns = [
	path('', create.index, name='create'),
	path('create_order', create.index, name='create'),
	path('customer_list', customer.index, name='customer'),
	path('product_list', product.product_read, name='product'),
	path('order_list', order.index, name='order'),

	path('category_list', category.cat_read, name='category_list'),
    path('category_delete', category.cat_delete, name='category_delete'),
    path('category_create', category.cat_create, name='category_create'),

    path('product_list', product.product_read, name='product_list'),
    path('product_delete', product.product_delete, name='product_delete'),
    path('product_create', product.product_create, name='product_create'),

    path('create_order/create', create.create, name='create_order'),


]
