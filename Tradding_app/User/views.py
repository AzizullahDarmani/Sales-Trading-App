from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

from .models import User



def HomeView(request):
    return render(request, 'home.html')


def LogoutView(request):
    request.session.flush()  
    return redirect('SignIn')




def UserView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password']) 
            user.save()
            request.session['user_id'] = user.id  
            return redirect('SignIn')
    else:
        form = UserForm()
    return render(request, 'user.html', {'form': form})






def SignIn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            try:
                user = User.objects.get(email=email, role=role)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    request.session['user_role'] = user.role  # Store role in session
                    return redirect('product_list')
                else:
                    form.add_error('password', 'Invalid password')
            except User.DoesNotExist:
                form.add_error('email', 'User with this email and role does not exist')

    else:
        form = LoginForm()
    
    return render(request, 'Sign_in.html', {'form': form})






def about_Us(request):
    return render(request, 'about.html')