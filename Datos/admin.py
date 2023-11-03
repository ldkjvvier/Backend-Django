from django.contrib import admin
from Datos.models import Producto
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'precio', 'stock','reorder')


class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('id','fechaInicio', 'fechaTermino', 'nombre','responsable','prioridad')

    
admin.site.register(Producto, ProductoAdmin)
