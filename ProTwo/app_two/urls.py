from django.conf.urls import url, include
from django.urls import include, path
from app_two import views

urlpatterns = [
    path('',views.index,name='index'),
    path('users/',views.users,name='users'),
    path('form/',views.form,name='form'),
    path('help/',views.help,name='help'),


]
