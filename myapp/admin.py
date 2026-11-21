from django.contrib import admin
from .models import Programa

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'estado', 'facultad')
    search_fields = ('codigo', 'nombre', 'facultad')
    list_filter = ('estado', 'facultad')