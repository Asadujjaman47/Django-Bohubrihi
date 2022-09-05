from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [
    # path('', views.index, name='index'),  --> function base view path
    # --> class base view path
    path('', views.IndexView.as_view(), name='index'),
    path('musician_details/<pk>/', views.MusicianDetail.as_view(),
         name='musician_details'),
    path('add_musician/', views.AddMusician.as_view(), name='add_musician'),

]
