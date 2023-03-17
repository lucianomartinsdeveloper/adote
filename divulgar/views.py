from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import render, get_object_or_404, redirect

from adotar.models import PedidoAdocao
from .forms import PetForm
from .models import Raca, Tag, Pet


def index(request):
    template_name = 'divulgar/index.html'
    pets = Pet.objects.all()
    context = {
        'pets': pets
    }
    return render(request, template_name, context)


@login_required
def novo_pet(request):
    template_name = 'divulgar/novo_pet.html'
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.usuario = request.user
            pet.save()
            return redirect('/')
    else:
        form = PetForm()
    racas = Raca.objects.all()
    tags = Tag.objects.all()
    context = {
        'racas': racas,
        'tags': tags,
        'form': form.as_p()
    }
    return render(request, template_name, context)


@login_required
def atualizar_pet(request, pk):
    template_name = 'divulgar/novo_pet.html'
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.usuario = request.user
            pet.save()
            return redirect('/')
    else:
        form = PetForm(instance=pet)
    racas = Raca.objects.all()
    tags = Tag.objects.all()
    context = {
        'racas': racas,
        'tags': tags,
        'form': form.as_p()
    }
    return render(request, template_name, context)


@login_required
def remover_pet(request, id):
    pet = Pet.objects.get(id=id)
    if pet.usuario != request.user:
        messages.add_message(request, constants.ERROR, 'Esse pet não é seu!')
        return redirect('divulgar/seus_pets')

    pet.delete()
    messages.add_message(request, constants.SUCCESS, 'Removido com sucesso.')
    return redirect('divulgar/seus_pets')


def new(request):
    template_name = 'home.html'
    return render(request, template_name)

@login_required
def ver_pet(request, id):
    template_name = 'divulgar/ver_pet.html'
    if request.method == "GET":
        pet = Pet.objects.get(id=id)
        context = {
            'pet': pet
        }
        return render(request, template_name, context)

@login_required
def ver_pedido_adocao(request):
    template_name = 'divulgar/ver_pedido_adocao.html'
    if request.method == "GET":
        pedidos = PedidoAdocao.objects.filter(usuario=request.user).filter(status="AG")
        context = {
            'pedidos': pedidos
        }
        return render(request, template_name, context)
