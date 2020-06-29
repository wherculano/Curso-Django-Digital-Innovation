from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100) # max 100 caracteres
    descricao = models.TextField(blank=True, null=True) # Pode ser 'branco' e/ou 'nulo'
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) # preenche o registro com a hora atual
    # pegar a tabela de usuarios do Django para usa-los como usuarios da agenda.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # no on_delete, ao deletar o usuario, seus eventos tbm serão


    class Meta:
        '''Exigindo que minha tabela se chame "evento" na criação do BD'''
        db_table = 'evento'
    
    def __str__(self):
        return self.titulo # no django-admin irá mostrar o titulo do envendo ao inves de Evento.object

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%y às %H:%M')
