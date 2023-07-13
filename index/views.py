from django.shortcuts import render
from django.conf import settings
import os

def home(request):
    path = os.path.join(settings.BASE_DIR, 'README.md')

    with open(path, 'r') as arq:
        content = arq.read()

    contexto = {'content':content}
    return render(request, 'index.html', contexto)