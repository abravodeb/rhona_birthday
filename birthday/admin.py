from django.contrib import admin
from .models import Mensaje, Cumple
# Register your models here.

# Personalizacion del Panel de administracion
class MensajeAdmin(admin.ModelAdmin):
    search_fields = ['msg']
    list_fields = ['msg']
    filter_fields = ['msg']

admin.site.register(Mensaje,MensajeAdmin)


class CumpleAdmin(admin.ModelAdmin):
    search_fields = ['nombre','cumple','mail']
    list_filter = ['cumple']
    list_display = ['nombre','cumple','mail']


admin.site.register(Cumple,CumpleAdmin)