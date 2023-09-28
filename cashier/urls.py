from django.contrib import admin
from django.urls import path
from .views import ProductListCreateView, ProductDetailView, TransactionList , createTransetion , FilteredTransactionListView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('transactions/report/', TransactionList.as_view(), name='create_transaction'),
    path('transactions/create/', createTransetion.as_view(), name='transactions_report'),
     path('transactions/filtered/', FilteredTransactionListView.as_view(), name='filtered-transaction-list'),
   
]