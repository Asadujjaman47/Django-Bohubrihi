from operator import concat
from django.conf.urls import url
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.contact, name='contact')

]
