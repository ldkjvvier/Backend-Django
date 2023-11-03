from django.urls import path
from . import views



urlpatterns = [path('', views.Productos),
               path('UserRegistros/', views.UserRegistrationForm),
               path('proyectos/', views.listadoProyecto),
               path('agregarProyecto/', views.agregarProyecto)]