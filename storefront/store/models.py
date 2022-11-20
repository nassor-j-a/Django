from django.db import models

# Create your models here.
class Product(models.Model):
    # setting your own primary key || Django automatically creates one for you
    # sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # unique set to true eradicates duplication of emails
    email = models.EmailField(unique=True)
    phone = models.IntegerField(max_length=255)
    birth_date = models.DateField(null=True)