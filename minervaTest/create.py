from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.shortcuts import *
from minervaTest.models import *


def index(request):
    error = ""
    productList = Products.objects.all()

    return render(request, 'create/create.html',  {
    'page_active': 1,
    'error' : error,
    'productList': productList,
    })

def create(request):
    error = ""
    productList = Products.objects.all()

    proList = request.POST.getlist("pro_list[]")
    quanList = request.POST.getlist("quan_list[]")
    lastname = request.POST.get("lastname")
    firstname = request.POST.get("firstname")
    postcode = request.POST.get("postcode")
    city = request.POST.get("city")
    country = request.POST.get("country")
    state = request.POST.get("state")
    segment = request.POST.get("segment")
    ship = request.POST.get("ship")
    orderDate = datetime.now()
    shipDate = datetime.now()

    if ship == 2:
        shipDate = orderDate + timedelta(days=1)
    elif ship == 3:
        shipDate = orderDate + timedelta(days=3)
    elif ship == 4:
        shipDate = orderDate + timedelta(days=5)

    products = {}
    for index, item in enumerate(proList):
        if str(item) in products:
            products[item] = int(products[item]) + int(quanList[index])
        else:
            products[item] = quanList[index]


    lastId = Customers.objects.raw('SELECT * FROM `customers` ORDER BY CAST(SUBSTRING(cusId,3,5) as SIGNED) DESC LIMIT 1')
    if sum(1 for lastId in lastId) == 0 :
        lastId = '10000'
    else:
        lastId = str(int(lastId[0].cusid[3:]) + 1)
    newCusId = (lastname[:1] + firstname[:1]).upper() + '-' + lastId
    name = lastname + ' ' + firstname
    newCus = Customers.objects.create(cusid=newCusId, name=name, segment=segment,postcode=postcode,state=state,city=city,country=country)

    for product,quantity in products.items():
        lastOrderId = Orders.objects.raw('SELECT * FROM `orders` ORDER BY CAST(SUBSTRING(orderId,8,6) as SIGNED) DESC LIMIT 1')
        if sum(1 for lastOrderId in lastOrderId) == 0 :
            lastOrderId = '100001'
        else:
            lastOrderId = str(int(lastOrderId[0].orderid[8:]) + 1)
        orderId = state[:2].upper() + '-' + str(orderDate.year) + '-' + lastOrderId
        productId = Products.objects.get(id=product)
        newOrder = Orders.objects.create(orderid=orderId, orderdate=orderDate.strftime('%Y-%m-%d'), \
                    shipdate=shipDate.strftime('%Y-%m-%d'),shipid=ship,cusid=newCus,productid=productId,quantity=quantity )
    error = 'SUCCESS !'

    return render(request, 'create/create.html',  {
    'page_active': 1,
    'error': error,
    'productList': productList,
    })
