
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Sales.models import Sale  # Ensure this import is correct

def order_list(request):
    user_role = request.session.get("user_role")  # Fetch user role from session
    user_id = request.session.get("user_id")  # Fetch user ID from session

    orders = Sale.objects.none()  # Default to an empty queryset

    if user_role == "customer":
        orders = Sale.objects.filter(customer_id=user_id, payment_status=True)
    elif user_role == "product_owner":
        orders = Sale.objects.filter(payment_status=True)

    return render(request, "order_list.html", {"orders": orders})




# works
# from django.shortcuts import render, get_object_or_404, redirect
# from Sales.models import Sale  # Ensure the correct Order model import
# from .models import Transaction

# def transaction_detail(request, order_id):
#     order = get_object_or_404(Sale, id=order_id)
#     transaction, created = Transaction.objects.get_or_create(order=order)

#     if request.user == order.product.name and request.method == "POST":
#         new_status = request.POST.get("status")
#         if new_status in ['pending', 'processing', 'completed']:
#             transaction.status = new_status
#             transaction.save()

#     return render(request, "transaction_list.html", {"order": order, "transaction": transaction})




# # today
# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponseForbidden
# from .models import Transaction
# from .forms import TransactionForm

# def transaction_detail(request, transaction_id):
#     transaction = get_object_or_404(Transaction, id=transaction_id)

#     # Only allow product owners to update transactions
#     # if request.user.role == "product_owner":
#     if request.user == "product_owner":
#         if request.method == "POST":
#             form = TransactionForm(request.POST, instance=transaction)
#             if form.is_valid():
#                 form.save()
#                 return redirect("transaction_detail", transaction_id=transaction.id)
#         else:
#             form = TransactionForm(instance=transaction)
#     else:
#         form = None  # Customers won't see the form

#     return render(request, "transaction_detail.html", {"transaction": transaction, "form": form})


from .forms import TransactionForm
from .models import Transaction

# works great 
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







# def transaction_detail(request, transaction_id):
#     transaction = get_object_or_404(Transaction, transaction_id=transaction_id)  # Query by transaction_id

#     if request.method == 'POST':
#         form = TransactionForm(request.POST, instance=transaction)
#         if form.is_valid():
#             form.save()
#             return redirect('order_list')

#     else:
#         form = TransactionForm(instance=transaction)

#     return render(request, "transaction_detail.html", {"form": form})

