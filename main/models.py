from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Vendor Model
class Vendor(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE) 
    address = models.TextField(null=True)

    def __str__(self):
        return self.user.username

# ProductCategory Model
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Product Categories"
    
# Product Model
class Product(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title
        