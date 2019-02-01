from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import *
from minervaTest.models import *

def cat_create(request):
    catId = request.POST.get("cat_main","")
    catName = request.POST.get("cat_name","")
    cat = Categories.objects.get(id=catId)
    new = Subcategories.objects.create(name=catName, catid=cat)
    new.save()
    return HttpResponse("Created")


def cat_delete(request):
    catId = request.POST.get("cat_id","")
    cat = Subcategories.objects.get(id=catId)
    cat = cat.delete()
    return HttpResponse("Deleted")
 

def cat_read(request):
  subCatList = Subcategories.objects.all()
  catList = Categories.objects.all()

  return render(request, 'category/view.html', { 
  	'page_active': 5,
    'subCatList': subCatList,
    'catList': catList })