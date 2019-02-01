from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import *
from minervaTest.models import *

def product_create(request):
    cat = request.POST.get("cat","")
    name = request.POST.get("name","")
    price = request.POST.get("price","")
    discount = request.POST.get("discount","")
    cat = Subcategories.objects.get(id=cat)

    lastId = Products.objects.raw('SELECT * FROM `products` ORDER BY CAST(SUBSTRING(productId,9,8) as SIGNED) DESC LIMIT 1')
    lastId = str(int(lastId[0].productid[7:]) + 1)
    proId = (cat.catid.name[:3] +'-'+ cat.name[:2]).upper() + '-' + lastId
    new = Products.objects.create(productid=proId, name=name, catid=cat, price=price, discount=discount)
    new.save()
    return HttpResponse("Created")


def product_delete(request):
    proId = request.POST.get("pro_id","")
    product = Products.objects.get(id=proId)
    product = product.delete()
    return HttpResponse("Deleted")

def product_read(request):
  
  subCatList = Subcategories.objects.all()
  proList = Products.objects.all()

  return render(request, 'product/view.html', { 
  	'page_active': 4,
    'subCatList': subCatList,
    'proList': proList,
    })