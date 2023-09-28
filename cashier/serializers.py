from rest_framework import serializers
from .models import Product, Transaction , TransactionItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class TransactionItemSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # qty = serializers.IntegerField()

    class Meta:
        model = TransactionItem
        fields = ['item' , 'qty']

class TransactionSerializer(serializers.ModelSerializer):
    items = TransactionItemSerializer(source="transactionitem_set", many=True)

    class Meta:
        model = Transaction
        fields = '__all__'

