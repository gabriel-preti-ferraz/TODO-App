from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import logout
from django.urls import reverse
import re

def register(request):
    if 'register' in request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_check = User.objects.filter(username=username)
        email_check = User.objects.filter(email=email)

        if user_check.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existente.')
            return redirect(reverse('register'))
        
        if email_check.exists():
            messages.add_message(request, constants.ERROR, 'E-mail já registrado.')
            return redirect(reverse('register'))

        """if not (re.search('[A-Z]', password) and re.search('[a-z]', password)):
            messages.add_message(request, constants.ERROR, 'Sua senha deve conter no mínimo uma letra maiúscula e uma minúscula.')
            return redirect(reverse('register'))

        if len(password) < 8:
            messages.add_message(request, constants.ERROR, 'A senha deve conter no mínimo 8 caracteres.')
            return redirect(reverse('register'))"""

        if ' ' in username:
            messages.add_message(request, constants.ERROR, 'O nome de usuário não pode conter espaço.')
            return redirect(reverse('register'))
        
        if len(username) < 4:
            messages.add_message(request, constants.ERROR, 'O nome de usuário deve conter no mínimo 4 caracteres.')

        User.objects.create_user(username=username, email=email, password=password)
        messages.add_message(request, constants.SUCCESS, 'Usuário registrado com sucesso!')
        return redirect(reverse('login'))

    return render(request, 'register.html')

def login(request):
    if 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if not username or not password:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos.')
            return redirect(reverse('login'))
        
        auth.login(request, user)

        return redirect('index.html')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')