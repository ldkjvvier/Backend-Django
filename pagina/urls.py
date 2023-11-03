from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('juguetes/', views.juguetes),
    path('tecnologia/', views.tecnologia),
    path('ropa/', views.ropa)
]