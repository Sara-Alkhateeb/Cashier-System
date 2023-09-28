from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    last_login = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )

    def __str__(self):
        return self.username
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.CharField(max_length=255)

class Item(models.Model):
    name = models.CharField(max_length=100)
    qty = models.PositiveIntegerField(default=0) 

class Transaction(models.Model):
    cashier = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    number_of_items = models.PositiveIntegerField()
    items = models.ManyToManyField(Item, through='TransactionItem')
    transaction_time = models.DateTimeField(auto_now_add=True)

class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0) 


    
