from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='HomeView'), 
    path('logout/signin/', views.LogoutView, name='Logout'), 
    path('user/', views.UserView, name= 'UserView'),
    path('signin/', views.SignIn, name='SignIn'), 
    path('about/', views.about_Us, name='about_us'), 
]