from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import models
from .models import Product , Transaction , TransactionItem, Item
from .serializers import TransactionSerializer, TransactionItemSerializer , ProductSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

class createTransetion(APIView):
   def post(self, request):
        items_data = request.data.get('items')
        if not items_data:
            return Response({'error': 'No items provided in the request.'}, status=status.HTTP_400_BAD_REQUEST)

        items = []
        total_items = 0  # Initialize the total_items count

        for item_data in items_data:
            item_serializer = TransactionItemSerializer(data=item_data)
            if item_serializer.is_valid():
                item = Item.objects.create(**item_serializer.validated_data)
                items.append(item)
                total_items += item.qty  # Increment the total_items count
            else:
                return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create the Transaction instance with the total_items count
        transaction = Transaction.objects.create(number_of_items=total_items)
        for item in items:
            TransactionItem.objects.create(transaction=transaction, item=item.id, quantity=item.qty)

        return Response({'transaction_id': transaction.id}, status=status.HTTP_201_CREATED)

class TransactionList(generics.ListCreateAPIView):
   queryset = Transaction.objects.all()
   serializer_class = TransactionSerializer



