from rest_framework import serializers
from .models import Product, Transaction , Item

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class TransactionItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    qty = serializers.IntegerField()

class TransactionSerializer(serializers.ModelSerializer):
    items = TransactionItemSerializer(many=True)

    class Meta:
        model = Transaction
        fields = '__all__'

