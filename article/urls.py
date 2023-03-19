from django.urls import path
from . import views
app_name= 'article'
urlpatterns = [
    path('', views.homeview, name='home'),
    path('<int:pk>/details', views.detailview, name='detail'),
    path('list', views.articlelist, name='list'),
    path('add-article', views.addarticle, name='add'),
    path('<int:pk>/update-article', views.updatearticle, name='update'),
    path('<int:pk>/delete-article', views.deletearticle, name='delete'),
    path('add-comment', views.addcomment, name='add-comment'),
    path('<int:pk>/remove-comment', views.removecomment, name='remove-comment'),
    path('update-comment', views.updatecomment, name='update-comment'),
]
