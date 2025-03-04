from django import forms
from .models import Sale

class PaymentForm(forms.ModelForm):
    card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder':'Card Number'}))
    expiray_date = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'MM/YY'}))
    cvv = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'placeholder': 'CVV'}))

    class Meta:
        model = Sale
        fields = []