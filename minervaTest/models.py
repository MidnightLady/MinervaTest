# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Customers(models.Model):
    cusid = models.CharField(db_column='cusId', max_length=255)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    segment = models.IntegerField()
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Orders(models.Model):
    orderid = models.CharField(db_column='orderId', max_length=255)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='orderDate', blank=True, null=True)  # Field name made lowercase.
    shipdate = models.DateTimeField(db_column='shipDate', blank=True, null=True)  # Field name made lowercase.
    shipid = models.IntegerField(db_column='shipId')  # Field name made lowercase.
    cusid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='cusId')  # Field name made lowercase.
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='productId')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orders'


class Products(models.Model):
    productid = models.CharField(db_column='productId', unique=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    catid = models.ForeignKey('Subcategories', models.DO_NOTHING, db_column='catId')  # Field name made lowercase.
    price = models.FloatField()
    discount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Subcategories(models.Model):
    name = models.CharField(max_length=255)
    catid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='catId')  # Field name made lowercase.
    desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subCategories'
