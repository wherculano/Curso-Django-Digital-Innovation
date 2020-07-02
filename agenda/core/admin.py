from django.contrib import admin
from core.models import Evento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    '''Campos que irão aparecer na pagina do django-admin'''
    list_display = ('id','titulo','data_evento','data_criacao')
    list_filter = ('usuario', 'data_evento')

admin.site.register(Evento, EventoAdmin) # registrando o modelo Evento que foi criado no models.py
