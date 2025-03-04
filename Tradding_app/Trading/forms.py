# from django import forms
# from .models import Transaction

# class TransactionForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields = ["status"]
#         widgets = {
#             "status": forms.Select(
#                 attrs={"class": "form-control"}
#             )
#         }



from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transfer_id','product', 'customer', 'status']



