from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'account'
urlpatterns = [
    path('', views.loginview, name='login'),
    path('register', views.registerview, name='register'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    
]
