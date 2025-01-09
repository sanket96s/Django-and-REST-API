from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_created=True)
    
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    
class Order(models.Model):
    customer_name = models.CharField(max_length=50)
    order_date = models.DateField()
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    product = models.CharField(max_length=50)
    quantity = models.IntegerField()
    