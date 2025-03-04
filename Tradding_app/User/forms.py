# from django import forms
# from .models import User

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['full_name', 'username', 'email', 'role']



from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Secure input field
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email','password', 'role']
    

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=[('customer', 'Customer'), ('product_owner', 'Product Owner')])


