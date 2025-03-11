


import uuid
from django.db import models
from User.models import User
from Products.models import Product

class Sale(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, limit_choices_to={'role': 'customer'})
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)  # False = Pending, True = Paid
    transaction_id = models.CharField(max_length=36, unique=True, default=uuid.uuid4)  # Auto-generate unique ID
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.product.name}"
