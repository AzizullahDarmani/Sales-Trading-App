
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Sales.models import Sale 

def order_list(request):
    user_role = request.session.get("user_role") 
    user_id = request.session.get("user_id") 

    orders = Sale.objects.none()  

    if user_role == "customer":
        orders = Sale.objects.filter(customer_id=user_id, payment_status=True)
    elif user_role == "product_owner":
        orders = Sale.objects.filter(payment_status=True)

    return render(request, "order_list.html", {"orders": orders})





from .forms import TransactionForm
from .models import Transaction


def transaction_detail(request, transaction_id):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.save()
            return redirect('order_list')
    else:
        form = TransactionForm
    return render(request, "transaction_detail.html", {"form":form})






def customer_transactions(request):
    transactions = Transaction.objects.all()  

    if not transactions:
        message = "Soon your transaction process will be shared."
    else:
        message = None 

    return render(request, 'transactions.html', {'transactions': transactions, 'message': message})




