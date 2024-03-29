from datetime import datetime

from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect

from adotar.models import PedidoAdocao
from divulgar.models import Pet, Raca


def listar_pets(request):
    template_name = 'divulgar/listar_pets.html'
    if request.method == "GET":
        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')
        pets = Pet.objects.filter(status="P")
        racas = Raca.objects.all()
        if cidade:
            pets = pets.filter(cidade__icontains=cidade)
        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)
            raca_filter = Raca.objects.get(id=raca_filter)

        context = {
            'pets': pets,
            'racas': racas,
            'cidade': cidade,
            'raca_filter': raca_filter
        }
        return render(request, template_name, context)


def pedido_adocao(request, id_pet):
    pet = Pet.objects.filter(id=id_pet).filter(status="P")
    if not pet.exists():
        messages.add_message(request, constants.ERROR,
                             'Esse pet já foi adotado :)'
                             )
    else:
        pedido = PedidoAdocao(
            pet=pet.first(),
            usuario=request.user,
            data=datetime.now()
        )
        pedido.save()
        messages.add_message(request, constants.SUCCESS,
                             'Pedido de adoção realizado, você receberá um e-mail caso ele seja aprovado.'
                             )
    return redirect('/adotar')
