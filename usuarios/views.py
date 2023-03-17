from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import render, redirect


def cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(
                confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Campos não podem ficar em branco. Reveja!')
            return render(request, 'usuarios/cadastro.html')
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senhas não coincidem.')
            return render(request, 'usuarios/cadastro.html')
        try:
            User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, f'Usuário..: {nome.upper()} cadastrado com sucesso!')
            return render(request, 'usuarios/cadastro.html')
        except Exception:
            messages.add_message(request, constants.ERROR, 'Sua mensagem aqui.')
            return render(request, 'usuarios/cadastro.html')


def logar(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome, password=senha)
        if user is not None:
            login(request, user)
            return redirect('novo_pet')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return render(request, 'usuarios/login.html')


def sair(request):
    logout(request)
    return redirect('/usuarios/login')


def novo_pet(request):
    return None