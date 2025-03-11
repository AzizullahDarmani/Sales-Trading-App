from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import PaymentForm
from User.models import User
from Products.models import Product
from .models import Sale
from django.conf import settings
import stripe




import uuid 
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Sale
from Products.models import Product
from User.models import User
from .forms import PaymentForm

def sales_view(request, product_id):
    if request.session.get("user_role") != "customer":
        messages.error(request, "Only customers can buy products.")
        return redirect("product_list")

    product = get_object_or_404(Product, id=product_id)
    sale = None  

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            customer = get_object_or_404(User, id=request.session.get("user_id"))

            unique_transaction_id = str(uuid.uuid4())[:12] 

            sale = Sale.objects.create(
                customer=customer,
                product=product,
                payment_status=True,
                transaction_id=unique_transaction_id 
            )

            messages.success(request, f"Payment was successful for {product.name}")
            return redirect('product_list')
    else:
        form = PaymentForm()

    return render(request, 'sales.html', {"product": product, "form": form, "sale": sale})







from django.db.models.signals import post_save
from django.dispatch import receiver
from Trading.models import Transaction
from Sales.models import Sale

@receiver(post_save, sender=Sale)
def create_transaction(sender, instance, created, **kwargs):
    if created:  
        Transaction.objects.create(
            transaction_id=instance.transaction_id, 
            product=instance,
            customer=instance.customer,
            status="pending"
        )


