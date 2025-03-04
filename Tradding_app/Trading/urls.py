from django.urls import path
from .views import order_list, transaction_detail



urlpatterns = [
    path('orders/', order_list, name = 'order_list'),
    path('transaction/<str:transaction_id>/', transaction_detail, name='transaction_detail'),


]