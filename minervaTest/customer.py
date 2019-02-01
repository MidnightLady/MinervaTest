from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import *
from minervaTest.models import *

def index(request):
    cusList = Customers.objects.all()

    return render(request, 'customer/view.html',  {
    'page_active': 3,
    'cusList': cusList,
    })





