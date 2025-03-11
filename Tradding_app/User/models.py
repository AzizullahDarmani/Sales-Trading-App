
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    CUSTOMER = 'customer'
    PRODUCT_OWNER = 'product_owner'
    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (PRODUCT_OWNER, 'Product Owner'),
    ]

    full_name = models.CharField(max_length=400)
    username = models.CharField(max_length=300)
    email = models.EmailField()
    password = models.CharField(max_length=128, null=True)  # Stores hashed password
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CUSTOMER)

    def __str__(self):
        return self.username
