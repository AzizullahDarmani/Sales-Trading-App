from django.db import models
from User.models import User  # Import your custom User model
from Sales.models import Sale

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    transfer_id = models.CharField(null=True, max_length=36, unique=True)  # Store Sale's transaction_id
    product = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions", null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction {self.transfer_id} - {self.status}"






