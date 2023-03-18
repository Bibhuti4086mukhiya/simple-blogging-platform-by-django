from django.urls import path
from . import views
app_name= 'article'
urlpatterns = [
    path('', views.homeview, name='home'),
    path('<int:pk>/details', views.detailview, name='detail'),
]
