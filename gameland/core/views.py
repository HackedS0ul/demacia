from django.shortcuts import render
from .models import Character


def home(request):
    return render(request, "index.html")


def select_char(request):
    
    char = Character.objects.all()
    context = {
        'obj': char,
    }
    return render(request, 'character.html', context)