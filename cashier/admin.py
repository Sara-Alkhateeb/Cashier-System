from django.contrib import admin
from .models import CustomUser, Product, Transaction, Item

admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(Item)

