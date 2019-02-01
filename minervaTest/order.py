from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import *
from minervaTest.models import *

def index(request):
    orderList = Orders.objects.all()

    return render(request, 'order/view.html',  {
    'page_active': 2,
    'orderList': orderList,
    })





