from django.contrib import admin

from adotar.models import PedidoAdocao

class PedidoAdocaoAdmin(admin.ModelAdmin):
    list_display = [
        'pet',
        'usuario',
        'data',
        'status'
    ]

admin.site.register(PedidoAdocao, PedidoAdocaoAdmin)
