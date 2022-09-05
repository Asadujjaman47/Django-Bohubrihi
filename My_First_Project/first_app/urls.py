from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [
    # path('', views.index, name='index'),  --> function base view path
    path('', views.IndexView.as_view(), name='index'), # --> class base view path

]
