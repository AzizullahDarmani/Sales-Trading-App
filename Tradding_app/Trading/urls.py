from django.urls import path
from .views import order_list, transaction_detail
from .views import customer_transactions


urlpatterns = [
    path('orders/', order_list, name = 'order_list'),
    path('transaction/<str:transaction_id>/', transaction_detail, name='transaction_detail'),
    path('transactions/', customer_transactions, name='customer_transactions'),

]