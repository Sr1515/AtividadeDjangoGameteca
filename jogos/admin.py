from django.contrib import admin
from . import models


class JogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lancamento')
    list_editable = ('lancamento',)


admin.site.register(models.Jogo, JogoAdmin)
admin.site.register(models.Plataforma)
admin.site.register(models.Genero)
admin.site.register(models.Desenvolvedor)
