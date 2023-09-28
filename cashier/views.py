from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import models
from .models import Product , Transaction , TransactionItem
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

class createTransaction(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def post(self, request):
        cashier_id = request.data.get('cashier')
        items_data = request.data.get('items')
        
        if not items_data:
            return Response({'error': 'No items provided in the request.'}, status=status.HTTP_400_BAD_REQUEST)

        cashier = None  # Initialize cashier as None

        if cashier_id is not None:
            try:
                cashier = get_user_model().objects.get(pk=int(cashier_id))
            except (ValueError, get_user_model().DoesNotExist):
                return Response({'error': 'Invalid cashier ID or cashier does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # Create a transaction with the correct cashier (or None) and number of items
        transaction = Transaction.objects.create(number_of_items=len(items_data), cashier=cashier)

        # Create TransactionItem instances for each item in items_data
        for item_data in items_data:
            item_id = item_data.get('item')
            qty = item_data.get('qty')

            try:
                # Retrieve the product based on item_id
                product = Product.objects.get(pk=item_id)
            except Product.DoesNotExist:
                return Response({'error': f'Product with ID {item_id} does not exist.'}, status=status.HTTP_404_NOT_FOUND)

            TransactionItem.objects.create(transaction=transaction, item=product, qty=qty)

        # Query all transactions and serialize them
        transactions = Transaction.objects.all()
        transactionItem_serializer = TransactionItemSerializer(transactions, many=True)
        
        return Response(transactionItem_serializer.data, status=status.HTTP_201_CREATED)


# class TransactionList(generics.ListAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer

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

