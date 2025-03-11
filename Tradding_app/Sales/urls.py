from django.urls import path
from .views import sales_view

urlpatterns = [
    path('sales/<int:product_id>/', sales_view, name = 'sales_view' ),
]