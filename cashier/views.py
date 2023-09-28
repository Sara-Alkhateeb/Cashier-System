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
            TransactionItem.objects.create(transaction=transaction, item=item, quantity=item.qty)

        transactions = Item.objects.all()
        transactionItem_serializer = TransactionItemSerializer(Item, many=True)
    

        return Response("Transaction added!!", status=status.HTTP_201_CREATED)

class TransactionList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class FilteredTransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()

        cashier_id = self.request.query_params.get('cashier_id')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        # Apply filters based on query parameters
        if cashier_id:
            queryset = queryset.filter(cashier_id=cashier_id)
        if start_date and end_date:
            queryset = queryset.filter(
                Q(transaction_time__gte=start_date) &
                Q(transaction_time__lte=end_date)
            )

        return queryset

